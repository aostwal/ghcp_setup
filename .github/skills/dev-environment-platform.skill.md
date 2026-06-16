# Dev Environment Platform Skill

## Purpose

Use this skill when a task needs fast local environment setup, verification, or repair.

## Load When

- A tool, SDK, runtime, shell, or package manager is missing.
- PATH, environment variables, credentials, or local config block progress.
- The task requires confirming versions before implementation.

## Acceleration Pattern

1. Detect the active OS, shell, workspace, and available package managers.
2. Prefer existing installed tools before adding new dependencies.
3. Verify with direct commands such as `--version`, `where`, `Get-Command`, or `which`.
4. Keep fixes user-scoped unless system scope is explicitly required.
5. Record exact commands and final verification output.

## Guardrails

- Do not introduce project-specific architecture here.
- Do not duplicate language, cloud, or CI module guidance.
- Avoid global installs unless they are required for the current task.
- Prefer reversible environment changes.

## Credit Strategy

Load only for environment repair or setup work. Keep runtime profiles lean by leaving platform troubleshooting out of default module composition.
