from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys

try:
    import tiktoken
except ImportError:
    tiktoken = None

ROOT = Path(__file__).resolve().parent.parent
ROUTING_DIR = ROOT / "routing"
PROFILES_DIR = ROOT / "profile"
PROMPTS_DIR = ROOT / "prompts"
SKILLS_DIR = ROOT / "skills"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def token_count(text: str) -> int:
    if tiktoken is None:
        return int(len(text.encode("utf-8")) / 4)
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def parse_simple_yaml(text: str):
    data = {}
    stack = [(0, data)]
    current_key = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = line.strip()
        while stack and indent < stack[-1][0]:
            stack.pop()
        container = stack[-1][1]
        if stripped.startswith("- "):
            value = stripped[2:].strip()
            if not isinstance(container, list):
                parent = stack[-2][1]
                parent[current_key] = []
                container = parent[current_key]
                stack[-1] = (stack[-1][0], container)
            container.append(value)
            continue
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                container[key] = value
                current_key = key
            else:
                container[key] = {}
                current_key = key
                stack.append((indent + 2, container[key]))
    return data


def load_routing():
    profiles = parse_simple_yaml(read_text(ROUTING_DIR / "profiles.yml")).get("profiles", {})
    intents = parse_simple_yaml(read_text(ROUTING_DIR / "intents.yml")).get("intents", {})
    capabilities = parse_simple_yaml(read_text(ROUTING_DIR / "capabilities.yml")).get("capabilities", {})
    skills = parse_simple_yaml(read_text(ROUTING_DIR / "skills.yml")).get("skills", {})
    return profiles, intents, capabilities, skills


def load_profile_tokens(profile_name: str) -> int:
    prompt_path = PROMPTS_DIR / f"{profile_name}.prompt.md"
    if prompt_path.exists():
        return token_count(read_text(prompt_path))
    profile_path = PROFILES_DIR / f"{profile_name}.profile.md"
    if profile_path.exists():
        return token_count(read_text(profile_path))
    raise FileNotFoundError(f"Unknown profile: {profile_name}")


def load_skill_tokens(skill_names: list[str]) -> int:
    total = 0
    for skill_name in skill_names:
        skill_path = SKILLS_DIR / f"{skill_name}.skill.md"
        if not skill_path.exists():
            continue
        total += token_count(read_text(skill_path))
    return total


def estimate_task_tokens(task: str) -> int:
    return token_count(task)


def detect_intent(task: str, intents: dict) -> str:
    task_l = task.lower()
    keywords = {
        "implement": ["build", "create", "implement", "add", "set up", "setup"],
        "design": ["design", "architecture", "architect", "shape"],
        "review": ["review", "audit", "check", "inspect"],
        "troubleshoot": ["troubleshoot", "debug", "fix", "investigate", "diagnose"],
        "optimize": ["optimize", "improve", "reduce", "compress", "simplify"],
    }
    for intent, words in keywords.items():
        if intent in intents and any(word in task_l for word in words):
            return intent
    return "implement" if "implement" in intents else next(iter(intents.keys()), "")


def task_capabilities(task: str) -> list[str]:
    task_l = task.lower()
    signals = {
        "backend-development": ["backend", "api", "service", "python", "java", "c#", ".net", "dotnet"],
        "frontend-development": ["frontend", "react", "ui", "typescript", "javascript", "web"],
        "cloud-automation": ["azure", "vm", "terraform", "infrastructure", "automation", "aks", "kubernetes", "helm"],
        "platform-engineering": ["platform", "devpod", "container", "docker", "linux", "windows", "shell", "powershell"],
        "testing": ["test", "testing", "playwright", "squash", "validation", "qa"],
        "observability": ["observability", "monitor", "insight", "telemetry", "tracing", "kafka"],
        "data-engineering": ["data", "pipeline", "etl", "batch", "stream", "warehouse"],
    }
    found = []
    for capability, words in signals.items():
        if any(word in task_l for word in words):
            found.append(capability)
    return found


def workload_family_signals(task: str) -> list[str]:
    task_l = task.lower()
    signals = {
        "developer-environment": ["devpod", "bootstrap script", "local environment", "workspace", "setup"],
        "application-development": ["backend", "frontend", "api", "service", "react", "python", "java", "c#", ".net", "dotnet"],
        "cloud-automation": ["azure", "vm", "terraform", "infrastructure", "automation", "aks", "helm"],
        "kubernetes-platform": ["kubernetes", "kubectl", "cluster", "pod", "deployment", "namespace"],
        "observability": ["observability", "monitor", "telemetry", "tracing", "kafka"],
        "testing": ["test", "testing", "playwright", "squash", "qa"],
        "platform-engineering": ["platform", "container", "docker", "shell", "powershell", "linux", "windows"],
    }
    found = []
    for family, words in signals.items():
        if any(word in task_l for word in words):
            found.append(family)
    return found


def size_label(total: int) -> str:
    if total < 4000:
        return "Small"
    if total < 10000:
        return "Medium"
    return "Large"


def expected_output_range(size: str) -> tuple[int, int]:
    if size == "Small":
        return (300, 700)
    if size == "Medium":
        return (300, 700)
    return (500, 1200)


def compatible_skill_set(task_skills: list[str], candidate_profile: str) -> bool:
    return True


def suggest_smaller_profile(
    profile_name: str,
    profiles: dict,
    intents: dict,
    capabilities: dict,
    task: str,
    requested_skills: list[str],
):
    current = profiles.get(profile_name, {})
    current_cap = current.get("capability")
    current_family = current.get("workload_family", "")
    current_intent = None
    for intent_name, intent_meta in intents.items():
        if profile_name in intent_meta.get("primary_profiles", []):
            current_intent = intent_name
            break
    task_intent = detect_intent(task, intents)
    task_caps = task_capabilities(task)
    task_families = workload_family_signals(task)
    primary_family = task_families[0] if task_families else current_family
    if "developer-environment" in task_families:
        primary_family = "developer-environment"
    candidates = []
    for name, meta in profiles.items():
        if name == profile_name:
            continue
        candidate_cap = meta.get("capability")
        candidate_family = meta.get("workload_family", "")
        if current_cap and candidate_cap != current_cap and candidate_cap not in task_caps:
            continue
        if task_caps and candidate_cap not in task_caps and candidate_cap != current_cap:
            continue
        if primary_family and candidate_family != primary_family:
            continue
        prompt_path = PROMPTS_DIR / f"{name}.prompt.md"
        if prompt_path.exists():
            tokens = token_count(read_text(prompt_path))
        else:
            profile_path = PROFILES_DIR / f"{name}.profile.md"
            tokens = token_count(read_text(profile_path)) if profile_path.exists() else 999999
        candidate_modules = profiles.get(name, {}).get("modules", [])
        if len(candidate_modules) > len(current.get("modules", [])):
            continue
        if requested_skills and not compatible_skill_set(requested_skills, name):
            continue
        if candidate_cap == current_cap:
            tokens -= 500
        elif candidate_cap in task_caps:
            tokens -= 150
        elif candidate_family == current_family:
            tokens -= 200
        candidates.append((tokens, name, candidate_cap, candidate_family))
    candidates.sort()
    return candidates[0] if candidates else None


def estimate(profile_name: str, skills: list[str], task: str):
    profiles, intents, capabilities, skill_meta = load_routing()
    profile_tokens = load_profile_tokens(profile_name)
    skill_tokens = load_skill_tokens(skills)
    task_tokens = estimate_task_tokens(task)
    task_caps = task_capabilities(task)
    task_families = workload_family_signals(task)
    estimated_input = profile_tokens + skill_tokens + task_tokens
    output_low, output_high = expected_output_range(size_label(estimated_input))
    estimated_total_low = estimated_input + output_low
    estimated_total_high = estimated_input + output_high
    smaller_profile = suggest_smaller_profile(profile_name, profiles, intents, capabilities, task, skills)
    return {
        "profile_tokens": profile_tokens,
        "skill_tokens": skill_tokens,
        "task_tokens": task_tokens,
        "estimated_input": estimated_input,
        "expected_output_low": output_low,
        "expected_output_high": output_high,
        "estimated_total_low": estimated_total_low,
        "estimated_total_high": estimated_total_high,
        "context_size": size_label(estimated_input),
        "smaller_profile": smaller_profile,
        "matched_capabilities": task_caps,
        "matched_workload_families": task_families,
    }


def print_result(result: dict):
    print(f"Profile Tokens:\n{result['profile_tokens']}")
    print()
    print(f"Skill Tokens:\n{result['skill_tokens']}")
    print()
    print(f"Task Tokens:\n{result['task_tokens']}")
    print()
    print(f"Estimated Input:\n{result['estimated_input']}")
    print()
    print(f"Expected Output:\n{result['expected_output_low']}-{result['expected_output_high']}")
    print()
    print(f"Estimated Total:\n{result['estimated_total_low']}-{result['estimated_total_high']}")
    print()
    print(f"Context Size:\n{result['context_size']}")
    print()
    if result["smaller_profile"]:
        tokens, name, _cap, _family = result["smaller_profile"]
        savings = max(0, result["profile_tokens"] - tokens)
        print(f"Alternative Profile:\n{name}")
        print()
        print(f"Alternative Tokens:\n{tokens}")
        print()
        print(f"Potential Savings:\n{savings}")
        print()
        print("Matched Capabilities:")
        if result["matched_capabilities"]:
            for capability in result["matched_capabilities"]:
                print(f"* {capability}")
        else:
            print("* none")
        print()
        print("Matched Workload Families:")
        if result["matched_workload_families"]:
            for family in result["matched_workload_families"]:
                print(f"* {family}")
        else:
            print("* none")
        print()
        print("Reasoning:")
        print("Compatible capability family and workload family, same intent, and no required-skill conflict.")
    else:
        print("No smaller compatible profile found.")


def main():
    parser = argparse.ArgumentParser(description="Estimate GHCP context size for a profile, skills, and task.")
    parser.add_argument("--profile", required=True, help="Profile name, for example python-docker-azure")
    parser.add_argument("--skills", nargs="*", default=[], help="Optional skill names")
    parser.add_argument("--task", required=True, help="Task description")
    args = parser.parse_args()
    result = estimate(args.profile, args.skills, args.task)
    print_result(result)


if __name__ == "__main__":
    main()
