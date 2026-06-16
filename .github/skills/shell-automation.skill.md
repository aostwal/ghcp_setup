# Shell Automation Skill

## Purpose

Use this skill for focused Bash, POSIX shell, and cross-platform command automation.

## Load When

- The task is best solved with command composition, filesystem checks, or process orchestration.
- A short script can replace repetitive manual terminal work.
- CI or local developer workflows need lightweight shell glue.

## Acceleration Pattern

1. Detect shell assumptions before writing commands.
2. Use strict modes where compatible: `set -euo pipefail`.
3. Quote paths and variables.
4. Prefer `rg`, `find`, `xargs`, and structured tool output over fragile parsing.
5. Add clear exit codes and concise error messages.

## Guardrails

- Do not duplicate platform modules for Linux, PowerShell, Docker, or CI.
- Avoid destructive commands without explicit safeguards.
- Keep scripts small and task-shaped.

## Credit Strategy

Load only when command automation is needed, keeping general profiles free of shell-specific tactics.
