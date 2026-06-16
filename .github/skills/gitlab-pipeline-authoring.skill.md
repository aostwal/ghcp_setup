# GitLab Pipeline Authoring Skill

## Purpose

Use this skill to accelerate focused `.gitlab-ci.yml` authoring, review, and repair.

## Load When

- A task changes GitLab CI jobs, stages, rules, variables, includes, or artifacts.
- A pipeline failure points to YAML structure, job dependencies, or runner behavior.
- The work needs concise CI implementation guidance without loading broad DevOps context.

## Acceleration Pattern

1. Identify pipeline intent, trigger model, runner tags, and required artifacts.
2. Keep jobs small, named clearly, and stage-aligned.
3. Prefer `rules` over legacy `only` and `except` for new work.
4. Use caches and artifacts intentionally.
5. Validate YAML shape and dependency flow before finalizing.

## Guardrails

- Do not duplicate the full GitLab CI module.
- Do not encode secrets in pipeline files.
- Avoid broad platform redesign during targeted pipeline edits.

## Credit Strategy

Load only for pipeline authoring or debugging so profiles avoid carrying CI implementation detail by default.
