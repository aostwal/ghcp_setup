```python id="’wini237"
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

PROMPTS_DIR = ROOT / "prompts"
PROFILES_SOURCE_DIR = ROOT / "profiles" / "source"
PROFILES_GENERATED_DIR = ROOT / "profiles" / "generated"

PROMPT_PATTERN = re.compile(
    r"-\s+prompts\/([a-zA-Z0-9\-_\.]+)"
)

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def extract_prompt_paths(profile_content: str):
    matches = PROMPT_PATTERN.findall(profile_content)
    return [PROMPTS_DIR / match for match in matches]

def validate_prompt_exists(prompt_paths):
    missing = [p for p in prompt_paths if not p.exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing prompt files:\n" +
            "\n".join(str(m) for m in missing)
        )

def build_profile(profile_path: Path):

    profile_content = read_file(profile_path)

    prompt_paths = extract_prompt_paths(profile_content)

    validate_prompt_exists(prompt_paths)

    assembled_sections = []

    assembled_sections.append(
        f"<!-- GENERATED PROFILE: {profile_path.name} -->\n"
    )

    assembled_sections.append(
        "<!-- DO NOT EDIT GENERATED FILE DIRECTLY -->\n"
    )

    assembled_sections.append(profile_content)

    for prompt_path in prompt_paths:

        assembled_sections.append(
            f"\n<!-- BEGIN PROMPT: {prompt_path.name} -->\n"
        )

        assembled_sections.append(
            read_file(prompt_path)
        )

        assembled_sections.append(
            f"\n<!-- END PROMPT: {prompt_path.name} -->\n"
        )

    output_name = profile_path.name.replace(
        ".profile.md",
        ".generated.md"
    )

    output_path = PROFILES_GENERATED_DIR / output_name

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path.write_text(
        "\n".join(assembled_sections),
        encoding="utf-8"
    )

    print(f"Generated: {output_path}")

def build_all_profiles():

    profiles = PROFILES_SOURCE_DIR.glob("*.profile.md")

    for profile in profiles:
        build_profile(profile)

if __name__ == "__main__":
    build_all_profiles()
```
