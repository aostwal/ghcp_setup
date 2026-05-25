from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

MODULES_DIR = ROOT / "modules"
PROFILES_DIR = ROOT / "profile"
PROMPTS_DIR = ROOT / "prompts"

PROMPT_REFERENCE_PATTERN = re.compile(
    r"-\s+prompts\/([a-zA-Z0-9\-_\.]+)"
)

PROFILE_COMMAND_PATTERN = re.compile(
    r"Command:\s*\n\s*\/([a-zA-Z0-9\-_]+)"
)

FAILURES = []
WARNINGS = []


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_required_directories():

    required = [
        MODULES_DIR,
        PROFILES_DIR,
        PROMPTS_DIR,
    ]

    for directory in required:

        if not directory.exists():
            FAILURES.append(
                f"Missing required directory: {directory}"
            )


def validate_profile_references(profile_path: Path):

    content = read_file(profile_path)

    references = PROMPT_REFERENCE_PATTERN.findall(content)

    if not references:
        FAILURES.append(
            f"No prompt references found in profile: {profile_path.name}"
        )

    seen = set()

    for reference in references:

        if reference in seen:
            FAILURES.append(
                f"Duplicate prompt reference '{reference}' in {profile_path.name}"
            )

        seen.add(reference)

        prompt_path = PROMPTS_DIR / reference

        if not prompt_path.exists():
            FAILURES.append(
                f"Missing referenced prompt '{reference}' in {profile_path.name}"
            )


def validate_profile_command(profile_path: Path):

    content = read_file(profile_path)

    match = PROFILE_COMMAND_PATTERN.search(content)

    if not match:
        FAILURES.append(
            f"Missing profile command in: {profile_path.name}"
        )
        return

    command_name = match.group(1)

    expected_prompt = PROMPTS_DIR / f"{command_name}.prompt.md"

    if not expected_prompt.exists():
        FAILURES.append(
            f"Generated runtime prompt missing for command '/{command_name}'"
        )


def validate_generated_prompt(prompt_path: Path):

    content = read_file(prompt_path)

    if "<profile>" not in content:
        WARNINGS.append(
            f"Generated prompt may not contain profile wrapper: {prompt_path.name}"
        )

    if "<!-- GENERATED" not in content:
        WARNINGS.append(
            f"Generated marker missing in: {prompt_path.name}"
        )

    recursive_refs = PROMPT_REFERENCE_PATTERN.findall(content)

    if recursive_refs:
        FAILURES.append(
            f"Recursive prompt references detected in generated prompt: {prompt_path.name}"
        )


def validate_modules():

    modules = list(MODULES_DIR.glob("*.prompt.md"))

    if not modules:
        FAILURES.append("No modules found")

    for module in modules:

        content = read_file(module)

        if "<module>" not in content:
            WARNINGS.append(
                f"Missing <module> wrapper in {module.name}"
            )


def validate_profiles():

    profiles = list(PROFILES_DIR.glob("*.profile.md"))

    if not profiles:
        FAILURES.append("No profiles found")

    for profile in profiles:

        validate_profile_references(profile)
        validate_profile_command(profile)


def validate_generated_prompts():

    generated_prompts = [
        p for p in PROMPTS_DIR.glob("*.prompt.md")
        if p.name != "README.md"
    ]

    if not generated_prompts:
        FAILURES.append("No generated runtime prompts found")

    for prompt in generated_prompts:
        validate_generated_prompt(prompt)


def print_results():

    if WARNINGS:

        print("\nWARNINGS:\n")

        for warning in WARNINGS:
            print(f"[WARNING] {warning}")

    if FAILURES:

        print("\nVALIDATION FAILED:\n")

        for failure in FAILURES:
            print(f"[ERROR] {failure}")

        sys.exit(1)

    print("\nValidation successful.\n")


if __name__ == "__main__":

    validate_required_directories()

    validate_modules()
    validate_profiles()
    validate_generated_prompts()

    print_results()