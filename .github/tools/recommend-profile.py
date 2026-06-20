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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def estimate_tokens(text: str) -> int:
    return int(len(text.encode("utf-8")) / 4)


def accurate_tokens(text: str) -> int:
    if tiktoken is None:
        return estimate_tokens(text)
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
    intents = parse_simple_yaml(read_text(ROUTING_DIR / "intents.yml")).get("intents", {})
    capabilities = parse_simple_yaml(read_text(ROUTING_DIR / "capabilities.yml")).get("capabilities", {})
    profiles = parse_simple_yaml(read_text(ROUTING_DIR / "profiles.yml")).get("profiles", {})
    skills = parse_simple_yaml(read_text(ROUTING_DIR / "skills.yml")).get("skills", {})
    return intents, capabilities, profiles, skills


def load_profile_stats():
    stats = {}
    for path in sorted(PROFILES_DIR.glob("*.profile.md")):
        text = read_text(path)
        name = re.search(r"Command:\s*\n\s*/([a-zA-Z0-9\-_]+)", text)
        if not name:
            continue
        modules = re.findall(r"-\s+modules/([a-zA-Z0-9\-_\.]+)", text)
        prompt_path = PROMPTS_DIR / f"{name.group(1)}.prompt.md"
        prompt_tokens = None
        if prompt_path.exists():
            prompt_tokens = accurate_tokens(read_text(prompt_path))
        stats[name.group(1)] = {
            "source_tokens": estimate_tokens(text),
            "runtime_tokens": prompt_tokens or estimate_tokens(text),
            "text": text,
            "modules": modules,
        }
    return stats


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
        if any(word in task_l for word in words) and intent in intents:
            return intent
    return "implement" if "implement" in intents else next(iter(intents.keys()))


def capability_signals(task: str):
    task_l = task.lower()
    signals = {
        "backend-development": ["backend", "api", "service", "python", "java", "c#", ".net", "dotnet"],
        "frontend-development": ["frontend", "react", "ui", "typescript", "javascript", "web"],
        "cloud-automation": ["azure", "vm", "terraform", "infrastructure", "automation", "aks", "kubernetes", "helm"],
        "platform-engineering": ["platform", "container", "docker", "linux", "windows", "shell", "powershell"],
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


def score_profiles(capabilities: list[str], profiles: dict, profile_stats: dict, task: str):
    scored = []
    task_l = task.lower()
    task_tokens = set(re.findall(r"[a-z0-9\.\-\#]+", task_l))
    broad_capabilities = {"platform-engineering"}
    task_families = workload_family_signals(task)
    for profile_name, meta in profiles.items():
        cap = meta.get("capability")
        family = meta.get("workload_family", "")
        ref_count = len(meta.get("modules", []))
        base_tokens = profile_stats.get(profile_name, {}).get("runtime_tokens", 999999)
        source_tokens = profile_stats.get(profile_name, {}).get("source_tokens", 999999)
        profile_blob = " ".join(
            [profile_name, cap or "", " ".join(meta.get("modules", [])), profile_stats.get(profile_name, {}).get("text", "")]
        ).lower()
        keyword_hits = sum(1 for token in task_tokens if token and token in profile_blob)
        score = 0
        matched = cap in capabilities
        if matched:
            score += 1000
        elif not capabilities:
            score += 10

        if cap in broad_capabilities and any(c in capabilities for c in ("backend-development", "frontend-development")):
            score -= 250

        if cap == "backend-development" and any(term in task_l for term in ("python", "backend")):
            score += 125
        if cap == "frontend-development" and "backend-development" in capabilities:
            score -= 75

        if family in task_families:
            score += 250
        elif task_families:
            score -= 200

        capability_rank = capabilities.index(cap) if cap in capabilities else 99
        score += max(0, 50 - capability_rank * 10)
        score += keyword_hits * 2
        score += max(0, 10 - ref_count)
        score += max(0, 12 - (base_tokens / 1000))
        score -= base_tokens / 800
        score -= ref_count
        score -= source_tokens / 8000
        scored.append((score, base_tokens, ref_count, profile_name, cap, family, capability_rank, keyword_hits))
    scored.sort(key=lambda item: (-item[0], item[1], item[2], item[3]))
    return scored


def recommend_skills(task: str, intent: str, skills: dict):
    task_l = task.lower()
    result = []
    for skill_name, meta in skills.items():
        purpose = meta.get("purpose", "")
        uses = " ".join(meta.get("uses", []))
        strong_terms = [
            skill_name.replace("-", " "),
            purpose.lower(),
        ]
        if any(term and term in task_l for term in strong_terms):
            result.append(skill_name)
        elif intent in meta.get("recommended_intents", []):
            if any(word in task_l for word in uses.lower().split()) and len(result) < 3:
                result.append(skill_name)
    return list(dict.fromkeys(result))


def confidence_for(capability_matches: int, profile_tokens: int, skill_count: int) -> str:
    if capability_matches >= 2 and profile_tokens < 8500:
        return "High"
    if capability_matches >= 1:
        return "Medium"
    if skill_count:
        return "Medium"
    return "Low"


def reason_text(task: str, intent: str, capability_matches: list[str], profile_name: str, skills: list[str]):
    parts = []
    if capability_matches:
        parts.append(", ".join(capability_matches))
    if skills:
        parts.append("skills: " + ", ".join(skills))
    if not parts:
        parts.append("matched by closest available capability and smallest suitable profile")
    return "; ".join(parts)


def capability_labels(capability_names: list[str]) -> list[str]:
    labels = []
    for capability in capability_names:
        if capability == "backend-development":
            labels.append("backend-development")
        elif capability == "frontend-development":
            labels.append("frontend-development")
        elif capability == "cloud-automation":
            labels.append("cloud-automation")
        elif capability == "platform-engineering":
            labels.append("developer-environment")
        else:
            labels.append(capability)
    return labels


def workload_family_labels(family_names: list[str]) -> list[str]:
    return list(dict.fromkeys(family_names))


def recommend(task: str):
    intents, capabilities, profiles, skills = load_routing()
    profile_stats = load_profile_stats()
    intent = detect_intent(task, intents)
    caps = capability_signals(task)

    scored = score_profiles(caps, profiles, profile_stats, task)
    chosen = scored[0] if scored else None
    if not chosen:
        return {
            "profile": "",
            "skills": [],
            "tokens": 0,
            "confidence": "Low",
            "reasoning": "No profiles available.",
        }

    _, token_count, _, profile_name, cap, family, cap_rank, keyword_hits = chosen
    runner_up = scored[1] if len(scored) > 1 else None
    runner_up_profile = runner_up[3] if runner_up else ""
    runner_up_tokens = runner_up[1] if runner_up else 0
    recommended_skills = recommend_skills(task, intent, skills)
    confidence = confidence_for(len(caps), token_count, len(recommended_skills))
    return {
        "profile": profile_name,
        "runner_up_profile": runner_up_profile,
        "runner_up_tokens": runner_up_tokens,
        "matched_capabilities": capability_labels(caps),
        "matched_workload_families": workload_family_labels(task_families := workload_family_signals(task)),
        "skills": recommended_skills,
        "tokens": token_count,
        "confidence": confidence,
        "reasoning": reason_text(task, intent, caps, profile_name, recommended_skills),
    }


def print_result(result: dict):
    print("Recommended Profile:")
    print(result["profile"] or "unknown")
    print()
    print(f"Estimated Runtime Tokens:\n{result['tokens']}")
    print()
    print("Runner Up Profile:")
    print(result.get("runner_up_profile") or "none")
    print()
    print(f"Runner Up Tokens:\n{result.get('runner_up_tokens') or 0}")
    print()
    savings = (result.get("runner_up_tokens") or 0) - result["tokens"]
    print(f"Estimated Savings:\n{max(0, savings)}")
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
    print("Recommended Skills:")
    if result["skills"]:
        for skill in result["skills"]:
            print(f"* {skill}")
    else:
        print("* none")
    print()
    print(f"Confidence:\n{result['confidence']}")
    print()
    print("Reasoning:")
    print(result["reasoning"])


def main():
    parser = argparse.ArgumentParser(description="Recommend the smallest suitable GHCP profile for a task.")
    parser.add_argument("task", nargs="+", help="Free-form engineering task description")
    args = parser.parse_args()
    task = " ".join(args.task).strip()
    result = recommend(task)
    print_result(result)


if __name__ == "__main__":
    main()
