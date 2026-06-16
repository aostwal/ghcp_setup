<!--
GHCP Global Engineering Governance
Purpose:
Global repository-wide governance and execution discipline.

This file intentionally avoids deep domain specialization.
Reusable engineering expertise belongs inside:
- /modules/*
- /profiles/*

Runtime execution artifacts belong inside:
- /prompts/*
-->

<governance>

<governanceIdentity>

    You are operating inside the GHCP engineering intelligence platform.

    Your responsibilities:

    - preserve architectural integrity
    - maintain engineering rigor
    - prioritize maintainability
    - enforce operational discipline
    - minimize technical debt
    - produce production-grade outcomes

    Optimize for:

    - correctness
    - determinism
    - maintainability
    - scalability
    - operational clarity
    - testability
    - security
    - reproducibility

</governanceIdentity>

<contextBudgetGovernance>

Prefer minimum required cognition.

Avoid unnecessary specialization activation.

Prefer focused implementation plans.

Avoid giant response payloads.

Escalate complexity progressively.

Prefer bounded execution context.

</contextBudgetGovernance>

<repositoryArchitecture>

    Repository hierarchy:

    - .github/copilot-instructions.md
        -> global governance

    - .github/modules/*
        -> reusable engineering intelligence

    - .github/profiles/*
        -> orchestration definitions

    - .github/prompts/*
        -> generated runtime prompts

    - .github/tools/*
        -> orchestration tooling

    - .github/hooks/*
        -> validation and governance hooks

    - .github/skills/*
        -> operational accelerators

    Architecture rules:

    - modules define reusable expertise
    - profiles define orchestration
    - prompts are generated runtime artifacts
    - governance remains globally reusable
    - avoid duplicated specialization logic
    - preserve deterministic composition

</repositoryArchitecture>

<repositoryModificationRules>

Never edit generated prompts directly.

Modify:

- modules/\*
- profile/\*
- tools/\*
- hooks/\*

Then regenerate:

- prompts/\*

Preserve source-of-truth ownership.

Generated artifacts are disposable.

</repositoryModificationRules>

<coreExecutionPrinciples>

    - Think systematically and from first principles.
    - Prioritize correctness over speed.
    - Prefer maintainable systems over clever abstractions.
    - Keep changes focused and reversible.
    - Preserve operational simplicity.
    - Optimize for long-term maintainability.
    - Keep runtime behavior deterministic.
    - Prefer explicit behavior over hidden complexity.
    - Minimize accidental technical debt.
    - Prefer composable architectures.

</coreExecutionPrinciples>
<intentSpecificationGovernance>

For medium and large initiatives:

1. Define objective.
2. Define constraints.
3. Define success criteria.
4. Define acceptance criteria.
5. Define implementation phases.

Prefer specification-driven execution.

Avoid implementation before intent is clear.

Use:

- templates/intent-spec.md
- templates/adr.md
- templates/implementation-plan.md

for complex work.

</intentSpecificationGovernance>
<engineeringGovernance>

    Enforce:

    - strong typing everywhere
    - strict compiler compatibility
    - zero-warning philosophy
    - schema-based validation
    - structured testing discipline
    - deterministic CI/CD behavior
    - explicit configuration management
    - documentation synchronization
    - observability readiness
    - operational maintainability

</engineeringGovernance>

<architectureGovernance>

    - Prefer modular architectures.
    - Keep domain boundaries explicit.
    - Prefer composition over inheritance.
    - Avoid tightly coupled systems.
    - Keep dependencies intentional.
    - Avoid giant monolithic implementations.
    - Minimize hidden side effects.
    - Keep abstractions measurable and justified.
    - Prefer deterministic execution flows.
    - Preserve operational clarity.

</architectureGovernance>

<securityGovernance>

    Enforce:

    - schema-based validation
    - least-privilege access
    - secure secret handling
    - parameterized queries
    - safe logging practices
    - explicit authorization boundaries
    - secure-by-default implementation
    - sanitized external inputs
    - operational auditability

    Avoid:

    - hardcoded credentials
    - insecure defaults
    - wildcard production permissions
    - unvalidated inputs
    - secret leakage
    - verbose production error exposure

</securityGovernance>

<testingGovernance>

    Enforce:

    - mandatory automated tests
    - BDD-style test naming
    - deterministic test behavior
    - isolated test execution
    - reproducible test environments
    - explicit edge-case validation
    - CI-enforced verification
    - meaningful assertions
    - regression protection

    Test execution structure:

    - given
    - when
    - then

</testingGovernance>

<documentationGovernance>

    Documentation must remain synchronized with implementation.

    On meaningful changes:

    - review impacted documentation
    - update affected examples
    - update architecture references
    - preserve onboarding clarity
    - maintain operational runbooks
    - document migration impacts

    Code remains the source of truth.

</documentationGovernance>

<platformContext>

    Platform assumptions:

    - GitLab CI/CD
    - Azure cloud platform
    - AKS Kubernetes environments
    - enterprise operational tooling

</platformContext>

<agentExecutionProtocol>

    For multi-step work:

    - decompose work into focused batches
    - preserve resumability
    - validate assumptions continuously
    - maintain verification artifacts
    - isolate temporary artifacts
    - document architectural tradeoffs
    - verify instruction adherence
    - verify tests before completion
    - verify documentation synchronization
    - preserve repository consistency

</agentExecutionProtocol>

<verificationProtocol>

    Before completion:

    - verify architectural consistency
    - verify strict typing compliance
    - verify testing expectations
    - verify security expectations
    - verify documentation synchronization
    - verify operational maintainability
    - verify configuration correctness
    - verify CI/CD compatibility
    - verify minimal diff scope
    - verify repository convention adherence

</verificationProtocol>

<fiftyMistakesRule>

    Before finalizing work:

    - aggressively search for mistakes
    - validate assumptions
    - identify hidden edge cases
    - inspect security implications
    - inspect operational risks
    - inspect maintainability concerns
    - inspect testing gaps
    - inspect runtime assumptions
    - inspect documentation drift
    - inspect deployment risks

    Scale verification depth proportionally to change complexity.

</fiftyMistakesRule>

<antiPatterns>

    Avoid:

    - giant monolithic implementations
    - weak typing
    - hidden runtime behavior
    - overengineered abstractions
    - tightly coupled systems
    - operationally opaque architectures
    - duplicated business logic
    - configuration chaos
    - non-deterministic execution
    - architecture without ownership

</antiPatterns>

<deliveryExpectations>

    Deliver:

    - production-grade implementations
    - maintainable architectures
    - operationally reliable systems
    - strongly typed code
    - deterministic behavior
    - secure implementations
    - reproducible delivery workflows
    - maintainable CI/CD systems
    - observable runtime behavior
    - low operational overhead

</deliveryExpectations>

</governance>
