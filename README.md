# GHCP Setup

Modular GitHub Copilot Prompt (GHCP) architecture for building reusable, composable, and maintainable engineering cognition systems.

This repository is designed to solve major scaling problems with large Copilot instruction files:

- duplicated cognition
- giant prompt files
- weak specialization boundaries
- difficult maintainability
- poor runtime composition
- token inefficiency
- conflicting instructions
- orchestration sprawl
- runtime ambiguity

The architecture separates:

- governance
- specialization
- orchestration
- execution
- observability
- runtime cognition
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
│   ├── java-platform.prompt.md
│   ├── dotnet-platform.prompt.md
│   ├── shell-platform.prompt.md
│   ├── powershell-platform.prompt.md
│   ├── docker-platform.prompt.md
│   ├── terraform-devops.prompt.md
│   ├── frontend-platform.prompt.md
│   ├── azure-cloud.prompt.md
│   ├── azure-observability.prompt.md
│   ├── distributed-observability.prompt.md
│   ├── gitlab-ci.prompt.md
│   └── execution-runtime.prompt.md
│
├── profile/
│   ├── aks-observability-engineer.profile.md
│   ├── kubectl-plugin-architect.profile.md
│   ├── terraform-aks-platform.profile.md
│   ├── frontend-azure-platform.profile.md
│   ├── python-docker-azure.profile.md
│   ├── devops-runtime-engineer.profile.md
│   └── distributed-observability-architect.profile.md
│
├── prompts/
│   ├── aks-observability-engineer.prompt.md
│   ├── kubectl-plugin-architect.prompt.md
│   ├── terraform-aks-platform.prompt.md
│   ├── frontend-azure-platform.prompt.md
│   ├── python-docker-azure.prompt.md
│   ├── devops-runtime-engineer.prompt.md
│   └── distributed-observability-architect.prompt.md
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
- distributed observability cognition
- Bash execution cognition
- PowerShell execution cognition
- Java runtime instrumentation cognition
- .NET runtime instrumentation cognition
- workflow orchestration cognition

Modules should:

- be reusable
- avoid orchestration logic
- avoid profile-specific instructions
- avoid runtime activation behavior
- remain domain focused
- define clear cognition boundaries
- specialize deeply in one domain

Modules should NOT:

- behave like personas
- duplicate governance
- own orchestration
- contain unrelated expertise
- collapse multiple runtime concerns together

---

## 2. Profiles = Orchestration Layers

Profiles assemble cognition modules.

Profiles define:

- mission
- execution mode
- module composition
- runtime activation guidance
- output expectations
- orchestration behavior

Profiles should remain lightweight.

Profiles should NOT duplicate module cognition.

Correct responsibility:

```text
modules = expertise
profiles = orchestration
generated prompts = runtime artifacts
```

---

## 3. Generated Prompts = Runtime Artifacts

Generated prompts are final runtime-ready prompts consumed by GitHub Copilot Chat.

These files are automatically generated from:

- profile definitions
- module composition
- reusable cognition layers

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
flattened runtime prompts
    ↓
GitHub Copilot Chat
```

---

# Why This Architecture Is More Effective

Traditional GHCP repositories eventually become:

- giant instruction dumps
- duplicated expertise layers
- conflicting runtime behaviors
- token-heavy prompts
- noisy cognition activation
- weak specialization boundaries
- impossible-to-maintain prompt systems

This architecture avoids those problems through modular cognition composition.

---

# How This Architecture Saves Tokens

## Traditional Prompt Problem

In most Copilot repositories:

- every persona duplicates infrastructure knowledge
- every prompt duplicates Kubernetes guidance
- every profile duplicates CI/CD behavior
- every runtime repeats execution governance
- observability logic gets repeated everywhere

This creates:

- massive prompt expansion
- unnecessary token usage
- noisy runtime cognition
- conflicting instructions
- weak reasoning quality

---

## Modular Cognition Approach

Instead of duplicating knowledge:

```text
profile
    ↓
references reusable modules
    ↓
builder composes only required cognition
```

This means:

- Kubernetes cognition exists once.
- GitLab CI cognition exists once.
- Bash runtime cognition exists once.
- PowerShell runtime cognition exists once.
- distributed tracing cognition exists once.
- Java instrumentation cognition exists once.
- .NET instrumentation cognition exists once.

This dramatically reduces:

- duplicated runtime instructions
- repeated governance layers
- orchestration conflicts
- unnecessary token expansion

---

# Why Token Reduction Matters

Lower token usage improves:

- runtime reasoning quality
- instruction clarity
- specialization accuracy
- response consistency
- context efficiency
- maintainability
- scalability of cognition systems

Smaller focused cognition layers produce:

- cleaner runtime signal quality
- stronger specialization behavior
- better operational reasoning
- less hallucinated orchestration
- fewer conflicting instructions

---

# Example Cognition Separation

Instead of creating one giant:

```text
enterprise-devops-observability.prompt.md
```

This architecture separates:

| Concern | Module |
|---|---|
| Kubernetes runtime | kubernetes-platform |
| GitLab orchestration | gitlab-ci |
| Bash execution | shell-platform |
| PowerShell execution | powershell-platform |
| Azure governance | azure-cloud |
| distributed tracing | distributed-observability |
| Java instrumentation | java-platform |
| .NET instrumentation | dotnet-platform |
| execution rigor | execution-runtime |

This keeps cognition:

- modular
- composable
- reusable
- maintainable
- operationally deterministic

---

# Distributed Observability Architecture Support

This repository now supports enterprise distributed observability architectures involving:

- React frontends
- Java backends
- .NET backends
- Kafka messaging systems
- Azure Application Insights
- OpenTelemetry
- AKS workloads
- distributed transaction tracing
- async trace propagation
- telemetry governance
- KQL-driven diagnostics

Supported observability concepts include:

- W3C TraceContext
- traceparent propagation
- tracestate propagation
- baggage propagation
- Kafka header propagation
- distributed transaction lineage
- async transaction tracing
- service dependency maps
- Application Insights transaction maps
- telemetry governance standards

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
profile/distributed-observability-architect.profile.md
```

Profile example:

```xml
<moduleComposition>

- modules/core-engineering.prompt.md
- modules/distributed-observability.prompt.md
- modules/java-platform.prompt.md
- modules/dotnet-platform.prompt.md
- modules/azure-observability.prompt.md

</moduleComposition>
```

---

## Step 3

Run the builder:

```bash
python tools/profile-builder.py
```

The builder will:

- read profiles
- resolve module references
- flatten reusable cognition
- generate runtime prompts
- prevent missing references
- produce deterministic runtime artifacts

---

# Validation Hooks

Validation hooks help prevent:

- broken module references
- stale runtime prompts
- recursive prompt inclusion
- duplicated module references
- invalid orchestration
- broken runtime composition
- architecture drift

Main validation hook:

```text
hooks/validate-generated-prompts.py
```

Recommended workflow:

```bash
python tools/profile-builder.py
python hooks/validate-generated-prompts.py
```

---

# Runtime Cognition Separation

This architecture intentionally separates:

| Layer | Responsibility |
|---|---|
| modules | reusable expertise |
| profiles | orchestration |
| prompts | runtime artifacts |
| hooks | architecture validation |
| builder | cognition compilation |

This separation is critical for:

- maintainability
- token efficiency
- runtime correctness
- specialization clarity
- scalable cognition evolution

---

# Recommended Usage Pattern

Use generated prompts directly inside GitHub Copilot Chat:

```text
/kubectl-plugin-architect
/terraform-aks-platform
/aks-observability-engineer
/frontend-azure-platform
/python-docker-azure
/devops-runtime-engineer
/distributed-observability-architect
```

These prompts dynamically inherit reusable cognition through profile composition.

---

# Important Design Rules

## DO

- keep modules reusable
- keep profiles lightweight
- inject execution cognition selectively
- compose specialization intentionally
- validate generated prompts continuously
- regenerate runtime prompts after profile changes
- preserve cognition boundaries
- keep orchestration separated from execution
- keep distributed tracing governance centralized

---

## DO NOT

- manually edit generated prompts
- duplicate cognition across profiles
- create giant megaprofiles
- place orchestration logic inside modules
- mix unrelated expertise domains together
- collapse runtime layers together
- create recursive prompt references
- merge CI orchestration with runtime scripting
- merge distributed tracing with logging-only cognition

---

# Repository Goal

The goal of this repository is NOT to build:

- giant prompts
- persona sprawl
- instruction duplication
- orchestration chaos
- runtime ambiguity

The goal is to build:

- modular cognition
- reusable engineering expertise
- scalable orchestration
- maintainable runtime composition
- deterministic cognition compilation
- enterprise-grade Copilot engineering systems
- operationally scalable AI engineering workflows
