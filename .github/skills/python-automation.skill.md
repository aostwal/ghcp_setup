# Python Automation Skill

## Purpose

Use this skill for small Python scripts, automation tasks, repository maintenance, and repeatable local checks.

## Load When

- A task needs file inspection, report generation, validation, or scripted cleanup.
- Existing shell commands are too brittle or verbose.
- Python is already available or is the requested automation runtime.

## Acceleration Pattern

1. Prefer standard library modules before adding packages.
2. Use `pathlib`, `argparse`, `json`, `csv`, `subprocess`, and structured parsers where appropriate.
3. Make scripts deterministic, idempotent, and safe by default.
4. Print concise status and actionable failures.
5. Add `--dry-run` when the script changes files or external state.

## Guardrails

- Do not repeat full Python platform engineering guidance.
- Do not hide destructive behavior behind default execution.
- Do not generate large framework abstractions for simple maintenance scripts.

## Credit Strategy

Load on demand for automation work instead of embedding scripting tactics into every engineering profile.
