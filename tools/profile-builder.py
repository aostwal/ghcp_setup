from pathlib import Path
from datetime import datetime
import re
import hashlib

ROOT = Path(__file__).resolve().parent.parent

PROMPTS_DIR = ROOT / "prompts"
PROFILES_SOURCE_DIR = ROOT / "profiles" / "source"
PROFILES_GENERATED_DIR = ROOT / "profiles" / "generated"

COPILOT_INSTRUCTIONS = (
    ROOT / ".github" / "copilot-instructions.md"
)

PROMPT_PATTERN = re.compile(
    r"-\s+prompts\/([a-zA-Z0-9\-_\.]+)"
)

SECTION_PATTERN = re.compile(
    r"<([a-zA-Z0-9\-_]+)>"
)


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_prompt_paths(profile_content: str):
    matches = PROMPT_PATTERN.findall(profile_content)

    ordered_unique = []

    for match in matches:
        path = PROMPTS_DIR / match

        if path not in ordered_unique:
            ordered_unique.append(path)

    return ordered_unique


def validate_file_exists(path: Path):

    if not path.exists():
        raise FileNotFoundError(
            f"Missing required file:\n{path}"
        )


def validate_prompt_exists(prompt_paths):

    missing = [
        p for p in prompt_paths
        if not p.exists()
    ]

    if missing:
        raise FileNotFoundError(
            "Missing prompt files:\n" +
            "\n".join(str(m) for m in missing)
        )


def extract_sections(content: str):

    return SECTION_PATTERN.findall(content)


def detect_duplicate_sections(prompt_contents):

    seen = {}
    duplicates = []

    for prompt_name, content in prompt_contents:

        sections = extract_sections(content)

        for section in sections:

            if section in seen:
                duplicates.append(
                    (
                        section,
                        seen[section],
                        prompt_name
                    )
                )

            else:
                seen[section] = prompt_name

    return duplicates


def generate_checksum(content: str):

    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()[:12]


def build_profile(profile_path: Path):

    validate_file_exists(COPILOT_INSTRUCTIONS)

    profile_content = read_file(profile_path)

    prompt_paths = extract_prompt_paths(profile_content)

    validate_prompt_exists(prompt_paths)

    prompt_contents = []

    for prompt_path in prompt_paths:

        prompt_contents.append(
            (
                prompt_path.name,
                read_file(prompt_path)
            )
        )

    duplicates = detect_duplicate_sections(
        prompt_contents
    )

    if duplicates:

        print("\n[WARNING] Duplicate XML sections detected:\n")

        for section, first, second in duplicates:

            print(
                f"  Section <{section}> "
                f"exists in both "
                f"{first} and {second}"
            )

        print()

    assembled_sections = []

    assembled_sections.append(
        f"<!-- GENERATED PROFILE: {profile_path.name} -->"
    )

    assembled_sections.append(
        "<!-- DO NOT EDIT GENERATED FILE DIRECTLY -->"
    )

    assembled_sections.append(
        "<!-- EDIT SOURCE PROFILE IN /profiles/source -->"
    )

    assembled_sections.append(
        f"<!-- GENERATED AT: "
        f"{datetime.utcnow().isoformat()}Z -->"
    )

    assembled_sections.append(
        "\n<!-- ================================================= -->"
    )

    assembled_sections.append(
        "<!-- BEGIN GLOBAL GOVERNANCE -->"
    )

    assembled_sections.append(
        "<!-- ================================================= -->\n"
    )

    governance_content = read_file(
        COPILOT_INSTRUCTIONS
    )

    assembled_sections.append(
        governance_content
    )

    assembled_sections.append(
        "\n<!-- ================================================= -->"
    )

    assembled_sections.append(
        "<!-- END GLOBAL GOVERNANCE -->"
    )

    assembled_sections.append(
        "<!-- ================================================= -->\n"
    )

    assembled_sections.append(
        "\n<!-- ================================================= -->"
    )

    assembled_sections.append(
        "<!-- BEGIN PROFILE ORCHESTRATION -->"
    )

    assembled_sections.append(
        "<!-- ================================================= -->\n"
    )

    assembled_sections.append(profile_content)

    assembled_sections.append(
        "\n<!-- ================================================= -->"
    )

    assembled_sections.append(
        "<!-- END PROFILE ORCHESTRATION -->"
    )

    assembled_sections.append(
        "<!-- ================================================= -->\n"
    )

    for prompt_path, (_, prompt_content) in zip(
        prompt_paths,
        prompt_contents
    ):

        assembled_sections.append(
            "\n<!-- ================================================= -->"
        )

        assembled_sections.append(
            f"<!-- BEGIN PROMPT: {prompt_path.name} -->"
        )

        assembled_sections.append(
            "<!-- ================================================= -->\n"
        )

        assembled_sections.append(
            prompt_content
        )

        assembled_sections.append(
            "\n<!-- ================================================= -->"
        )

        assembled_sections.append(
            f"<!-- END PROMPT: {prompt_path.name} -->"
        )

        assembled_sections.append(
            "<!-- ================================================= -->\n"
        )

    final_content = "\n".join(
        assembled_sections
    )

    checksum = generate_checksum(
        final_content
    )

    final_content += (
        f"\n<!-- PROFILE CHECKSUM: {checksum} -->\n"
    )

    output_name = profile_path.name.replace(
        ".profile.md",
        ".generated.md"
    )

    output_path = (
        PROFILES_GENERATED_DIR / output_name
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path.write_text(
        final_content,
        encoding="utf-8"
    )

    size_kb = round(
        len(final_content.encode("utf-8")) / 1024,
        2
    )

    print(
        f"[OK] Generated: {output_path.name} "
        f"({size_kb} KB)"
    )


def build_all_profiles():

    profiles = sorted(
        PROFILES_SOURCE_DIR.glob(
            "*.profile.md"
        )
    )

    if not profiles:

        print(
            "[INFO] No source profiles found."
        )

        return

    print(
        f"[INFO] Building {len(profiles)} profiles...\n"
    )

    for profile in profiles:

        build_profile(profile)

    print(
        "\n[INFO] Profile generation complete."
    )


if __name__ == "__main__":

    build_all_profiles()
