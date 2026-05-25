# GHCP Setup

Modular GitHub Copilot Prompt (GHCP) architecture for building reusable, composable, and maintainable engineering cognition systems.

This repository is designed to solve a major scaling problem with large Copilot instruction files:

- duplicated cognition
- giant prompt files
- weak specialization boundaries
- difficult maintainability
- poor runtime composition
- token inefficiency
- conflicting instructions

The architecture separates:

- governance
- specialization
- orchestration
- execution
- validation

into modular reusable layers.

---

# Architecture Overview

```text
.github/
│
├── copilot-instructions.md
│
├── modules/
│   ├── core-engineering.prompt.md
│   ├── workflow-orchestration.prompt.md
│   ├── kubernetes-platform.prompt.md
│   ├── go-platform.prompt.md
│   ├── python-platform.prompt.md
│   ├── docker-platform.prompt.md
│   ├── terraform-devops.prompt.md
│   ├── frontend-platform.prompt.md
│   ├── azure-cloud.prompt.md
│   ├── azure-observability.prompt.md
│   ├── gitlab-ci.prompt.md
│   └── execution-runtime.prompt.md
│
├── profile/
│   ├── aks-observability-engineer.profile.md
│   ├── kubectl-plugin-architect.profile.md
│   ├── terraform-aks-platform.profile.md
│   ├── frontend-azure-platform.profile.md
│   └── python-docker-azure.profile.md
│
├── prompts/
│   ├── aks-observability-engineer.prompt.md
│   ├── kubectl-plugin-architect.prompt.md
│   ├── terraform-aks-platform.prompt.md
│   ├── frontend-azure-platform.prompt.md
│   └── python-docker-azure.prompt.md
│
├── hooks/
│   └── validate-generated-prompts.py
│
├── tools/
│   └── profile-builder.py
│
└── skills/
```

---

# Core Architecture Principles

## 1. Modules = Reusable Cognition

Modules contain reusable engineering expertise.

Examples:

- Kubernetes cognition
- Terraform cognition
- Azure governance cognition
- frontend architecture cognition
- Docker runtime cognition
- workflow orchestration cognition

Modules should:

- be reusable
- avoid orchestration logic
- avoid profile-specific instructions
- avoid runtime activation behavior
- remain domain focused

Modules should NOT:

- behave like personas
- duplicate governance
- own orchestration
- contain unrelated expertise

---

## 2. Profiles = Orchestration Layers

Profiles assemble cognition modules.

Profiles define:

- mission
- execution mode
- module composition
- runtime activation guidance
- output expectations

Profiles should remain lightweight.

Profiles should NOT duplicate module cognition.

Correct responsibility:

```text
modules = expertise
profiles = orchestration
```

---

## 3. Generated Prompts = Runtime Artifacts

Generated prompts are final runtime-ready prompts consumed by GitHub Copilot Chat.

These files are automatically generated from:

- profile definitions
- module composition

Generated prompts should NEVER be manually edited.

---

# Prompt Build Flow

```text
modules
    ↓
profiles
    ↓
profile-builder.py
    ↓
generated runtime prompts
    ↓
GitHub Copilot Chat
```

---

# How To Generate Prompts

## Step 1

Place reusable cognition modules under:

```text
modules/
```

Example:

```text
modules/kubernetes-platform.prompt.md
```

---

## Step 2

Create orchestration profiles under:

```text
profile/
```

Example:

```text
profile/kubectl-plugin-architect.profile.md
```

Profile example:

```xml
<moduleComposition>

    Compose modules:

    - prompts/core-engineering.prompt.md
    - prompts/kubernetes-platform.prompt.md
    - prompts/go-platform.prompt.md

</moduleComposition>
```

Important:

Profiles reference generated runtime prompt names because GHCP only exposes prompts directly under the prompts folder.

---

## Step 3

Run the builder:

```bash
python tools/profile-builder.py
```

The builder will:

- read profiles
- resolve module references
- compose runtime prompts
- generate final prompts under prompts/

---

# Generated Prompt Behavior

Generated prompts:

- are runtime artifacts
- are consumed directly by GHCP chat
- should remain flattened
- should not contain recursive references
- should not be manually modified

Example generated output:

```text
prompts/kubectl-plugin-architect.prompt.md
```

Available inside Copilot Chat as:

```text
/kubectl-plugin-architect
```

---

# Profile Builder

Main compiler:

```text
tools/profile-builder.py
```

Responsibilities:

- discover profiles
- resolve module references
- validate dependencies
- generate runtime prompts
- prevent missing references
- create deterministic outputs

---

# Validation Hooks

Validation hooks help prevent:

- broken module references
- missing prompt files
- stale generated prompts
- invalid composition
- duplicated references
- recursive prompt inclusion

Recommended hook location:

```text
hooks/validate-generated-prompts.py
```

Recommended validations:

- ensure all referenced prompts exist
- ensure generated prompts are current
- ensure no recursive references exist
- ensure prompts folder contains generated runtime artifacts only
- ensure profiles do not duplicate module cognition excessively

---

# Recommended Hook Workflow

## Before Commit

Run:

```bash
python hooks/validate-generated-prompts.py
```

Then:

```bash
python tools/profile-builder.py
```

Then commit.

---

# Recommended Development Workflow

## Adding New Expertise

Add a reusable module:

```text
modules/new-domain.prompt.md
```

---

## Adding New Runtime Persona

Add a profile:

```text
profile/new-runtime.profile.md
```

Then regenerate prompts.

---

## Regenerate Runtime Prompts

```bash
python tools/profile-builder.py
```

---

# Why This Architecture Scales Better

Traditional GHCP setups usually become:

- giant instruction dumps
- duplicated cognition systems
- impossible to maintain
- conflicting instruction layers
- weak specialization boundaries

This architecture instead provides:

- reusable cognition modules
- lightweight orchestration
- deterministic runtime generation
- maintainable specialization boundaries
- scalable profile composition
- lower runtime token waste
- cleaner runtime signal quality

---

# Current Recommended Conventions

## Modules

```text
modules/*.prompt.md
```

## Profiles

```text
profile/*.profile.md
```

## Runtime Generated Prompts

```text
prompts/*.prompt.md
```

---

# Important Design Rules

## DO

- keep modules reusable
- keep profiles lightweight
- inject execution cognition selectively
- compose specialization intentionally
- validate generated prompts continuously
- regenerate runtime prompts after profile changes

---

## DO NOT

- manually edit generated prompts
- duplicate cognition across profiles
- create giant megaprofiles
- place orchestration logic inside modules
- mix unrelated expertise domains together
- create recursive prompt references

---

# Future Enhancements

Potential future improvements:

- automated validation hooks
- profile dependency graphs
- prompt token analysis
- runtime prompt diff validation
- skill integration
- GHCP agent integration
- prompt caching strategies
- runtime composition testing

---

# Recommended Usage Pattern

Use generated prompts directly in GitHub Copilot Chat:

```text
/kubectl-plugin-architect
/terraform-aks-platform
/aks-observability-engineer
/frontend-azure-platform
/python-docker-azure
```

These prompts dynamically inherit reusable cognition through profile composition.

---

# Repository Goal

The goal of this repository is NOT to build:

- giant prompts
- persona sprawl
- instruction duplication

The goal is to build:

- modular cognition
- reusable engineering expertise
- scalable orchestration
- maintainable runtime composition
- production-grade Copilot engineering systems
