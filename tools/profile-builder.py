from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

MODULES_DIR = ROOT / "modules"
PROFILES_DIR = ROOT / "profile"
GENERATED_PROMPTS_DIR = ROOT / "prompts"

MODULE_REFERENCE_PATTERN = re.compile(
    r"-\s+modules\/([a-zA-Z0-9\-_\.]+)"
)

PROFILE_COMMAND_PATTERN = re.compile(
    r"Command:\s*\n\s*\/([a-zA-Z0-9\-_]+)"
)


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_module_paths(profile_content: str):

    matches = MODULE_REFERENCE_PATTERN.findall(
        profile_content
    )

    return [
        MODULES_DIR / match
        for match in matches
    ]


def extract_profile_command(profile_content: str):

    match = PROFILE_COMMAND_PATTERN.search(
        profile_content
    )

    if not match:
        raise ValueError(
            "Profile missing command definition"
        )

    return match.group(1)


def validate_module_exists(module_paths):

    missing = [
        module
        for module in module_paths
        if not module.exists()
    ]

    if missing:

        raise FileNotFoundError(
            "Missing module files:\n" +
            "\n".join(str(m) for m in missing)
        )


def validate_required_directories():

    required = [
        MODULES_DIR,
        PROFILES_DIR,
        GENERATED_PROMPTS_DIR,
    ]

    missing = [
        directory
        for directory in required
        if not directory.exists()
    ]

    if missing:

        raise FileNotFoundError(
            "Missing required directories:\n" +
            "\n".join(str(m) for m in missing)
        )


def build_profile(profile_path: Path):

    print(f"[INFO] Building profile: {profile_path.name}")

    profile_content = read_file(profile_path)

    command_name = extract_profile_command(
        profile_content
    )

    module_paths = extract_module_paths(
        profile_content
    )

    validate_module_exists(module_paths)

    assembled_sections = []

    assembled_sections.append(
        "<!-- GENERATED RUNTIME PROMPT -->"
    )

    assembled_sections.append(
        "<!-- DO NOT EDIT DIRECTLY -->"
    )

    assembled_sections.append(
        f"<!-- SOURCE PROFILE: {profile_path.name} -->"
    )

    assembled_sections.append("\n")

    assembled_sections.append(profile_content)

    for module_path in module_paths:

        assembled_sections.append("\n")

        assembled_sections.append(
            f"<!-- BEGIN MODULE: {module_path.name} -->"
        )

        assembled_sections.append("\n")

        assembled_sections.append(
            read_file(module_path)
        )

        assembled_sections.append("\n")

        assembled_sections.append(
            f"<!-- END MODULE: {module_path.name} -->"
        )

    output_name = f"{command_name}.prompt.md"

    output_path = (
        GENERATED_PROMPTS_DIR / output_name
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path.write_text(
        "\n".join(assembled_sections),
        encoding="utf-8"
    )

    size_kb = round(
        output_path.stat().st_size / 1024,
        2
    )

    print(
        f"[OK] Generated runtime prompt: "
        f"{output_name} ({size_kb} KB)"
    )


def build_all_profiles():

    profiles = sorted(
        PROFILES_DIR.glob("*.profile.md")
    )

    if not profiles:

        print(
            "[ERROR] No source profiles found."
        )

        sys.exit(1)

    for profile in profiles:
        build_profile(profile)

    print(
        "\n[INFO] Runtime prompt generation complete."
    )


if __name__ == "__main__":

    validate_required_directories()

    build_all_profiles()