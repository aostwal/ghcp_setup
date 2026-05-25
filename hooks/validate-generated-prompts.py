from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

PROMPTS_DIR = ROOT / "prompts"

PROFILES_DIR = ROOT / "profiles"

MODULES_DIR = ROOT / "modules"

MAX_PROMPT_SIZE_KB = 180

REQUIRED_GOVERNANCE_MARKERS = [
    "BEGIN GLOBAL GOVERNANCE",
    "END GLOBAL GOVERNANCE",
]

FORBIDDEN_MODULE_PATTERNS = [
    r"modules\/.*\.module\.md"
]

PROMPT_EXTENSION = ".prompt.md"

PROFILE_EXTENSION = ".profile.md"


def calculate_size_kb(path: Path):

    return round(
        path.stat().st_size / 1024,
        2
    )


def read_file(path: Path):

    return path.read_text(
        encoding="utf-8"
    )


def fail(message):

    print(f"[FAIL] {message}")
    sys.exit(1)


def warn(message):

    print(f"[WARN] {message}")


def info(message):

    print(f"[INFO] {message}")


def validate_prompt_size(prompt_path):

    size = calculate_size_kb(prompt_path)

    if size > MAX_PROMPT_SIZE_KB:

        fail(
            f"{prompt_path.name} "
            f"is too large: {size} KB"
        )

    info(
        f"{prompt_path.name} size OK "
        f"({size} KB)"
    )


def validate_governance(prompt_path):

    content = read_file(prompt_path)

    for marker in REQUIRED_GOVERNANCE_MARKERS:

        if marker not in content:

            fail(
                f"{prompt_path.name} "
                f"missing governance marker: "
                f"{marker}"
            )

    info(
        f"{prompt_path.name} governance OK"
    )


def validate_no_module_leakage(prompt_path):

    content = read_file(prompt_path)

    for pattern in FORBIDDEN_MODULE_PATTERNS:

        if re.search(pattern, content):

            warn(
                f"{prompt_path.name} "
                f"still references module paths"
            )


def validate_checksum(prompt_path):

    content = read_file(prompt_path)

    if "PROFILE CHECKSUM:" not in content:

        warn(
            f"{prompt_path.name} "
            f"missing checksum"
        )


def validate_duplicate_sections(prompt_path):

    content = read_file(prompt_path)

    sections = re.findall(
        r"<([a-zA-Z0-9\-_]+)>",
        content
    )

    duplicates = set([
        x for x in sections
        if sections.count(x) > 1
    ])

    if duplicates:

        warn(
            f"{prompt_path.name} "
            f"duplicate XML sections: "
            f"{sorted(duplicates)}"
        )


def validate_prompt(prompt_path):

    print(
        f"\n[VALIDATING] "
        f"{prompt_path.name}"
    )

    validate_prompt_size(
        prompt_path
    )

    validate_governance(
        prompt_path
    )

    validate_no_module_leakage(
        prompt_path
    )

    validate_checksum(
        prompt_path
    )

    validate_duplicate_sections(
        prompt_path
    )


def validate_runtime_prompts():

    prompts = sorted(
        PROMPTS_DIR.glob(
            f"*{PROMPT_EXTENSION}"
        )
    )

    if not prompts:

        fail(
            "No runtime prompts found"
        )

    info(
        f"Found {len(prompts)} runtime prompts"
    )

    for prompt in prompts:

        validate_prompt(prompt)


if __name__ == "__main__":

    validate_runtime_prompts()

    print(
        "\n[SUCCESS] "
        "All generated prompts validated."
    )