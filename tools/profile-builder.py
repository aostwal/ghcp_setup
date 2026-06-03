from pathlib import Path
import re
import sys
import argparse

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


def estimate_tokens(content: str) -> int:
    """
    Approximation:
    1 token ~= 4 chars
    """
    return int(len(content) / 4)


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


def print_profile_stats(
    profile_name,
    module_stats,
    total_size_bytes,
    total_tokens
):

    print("\n")
    print("=" * 80)
    print(f"PROFILE: {profile_name}")
    print("=" * 80)

    print(
        f"{'Module':45}"
        f"{'KB':>10}"
        f"{'Tokens':>12}"
    )

    print("-" * 80)

    for stat in sorted(
        module_stats,
        key=lambda x: x["size_bytes"],
        reverse=True
    ):

        print(
            f"{stat['name']:45}"
            f"{stat['size_kb']:>10.2f}"
            f"{stat['tokens']:>12}"
        )

    print("-" * 80)

    print(
        f"{'TOTAL':45}"
        f"{round(total_size_bytes/1024,2):>10.2f}"
        f"{total_tokens:>12}"
    )

    print("\nLargest Contributors:")

    for stat in sorted(
        module_stats,
        key=lambda x: x["size_bytes"],
        reverse=True
    )[:5]:

        print(
            f"  - {stat['name']} "
            f"({stat['size_kb']} KB)"
        )


def build_profile(
    profile_path: Path,
    show_stats: bool = False
):

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

    module_stats = []

    total_tokens = estimate_tokens(
        profile_content
    )

    total_size_bytes = len(
        profile_content.encode("utf-8")
    )

    for module_path in module_paths:

        module_content = read_file(
            module_path
        )

        size_bytes = len(
            module_content.encode("utf-8")
        )

        size_kb = round(
            size_bytes / 1024,
            2
        )

        tokens = estimate_tokens(
            module_content
        )

        module_stats.append(
            {
                "name": module_path.name,
                "size_bytes": size_bytes,
                "size_kb": size_kb,
                "tokens": tokens,
            }
        )

        total_size_bytes += size_bytes
        total_tokens += tokens

        assembled_sections.append("\n")

        assembled_sections.append(
            f"<!-- BEGIN MODULE: {module_path.name} -->"
        )

        assembled_sections.append("\n")

        assembled_sections.append(
            module_content
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

    if show_stats:

        print_profile_stats(
            command_name,
            module_stats,
            total_size_bytes,
            total_tokens
        )

    return {
        "profile": command_name,
        "size_kb": round(
            total_size_bytes / 1024,
            2
        ),
        "tokens": total_tokens,
    }


def build_all_profiles(
    show_stats: bool = False
):

    profiles = sorted(
        PROFILES_DIR.glob("*.profile.md")
    )

    if not profiles:

        print(
            "[ERROR] No source profiles found."
        )

        sys.exit(1)

    summary = []

    for profile in profiles:

        result = build_profile(
            profile,
            show_stats
        )

        summary.append(result)

    print(
        "\n[INFO] Runtime prompt generation complete."
    )

    if show_stats:

        print("\n")
        print("=" * 80)
        print("PROFILE SUMMARY")
        print("=" * 80)

        print(
            f"{'Profile':40}"
            f"{'KB':>10}"
            f"{'Tokens':>12}"
        )

        print("-" * 80)

        for item in sorted(
            summary,
            key=lambda x: x["tokens"],
            reverse=True
        ):

            print(
                f"{item['profile']:40}"
                f"{item['size_kb']:>10.2f}"
                f"{item['tokens']:>12}"
            )


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show profile size and token statistics"
    )

    args = parser.parse_args()

    validate_required_directories()

    build_all_profiles(
        show_stats=args.stats
    )
