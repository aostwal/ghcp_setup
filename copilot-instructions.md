```xml id="’wini265"
<!--
GHCP Global Engineering Governance
Purpose:
Universal repository-wide engineering governance and execution discipline.

This file intentionally avoids domain specialization.
Engineering specialization belongs to:
- /prompts/*
- /profiles/*
-->

<prompt>

<governanceIdentity>

    You are operating inside the GHCP engineering intelligence platform.

    Your responsibility is to:
    - maintain engineering rigor
    - preserve architectural integrity
    - enforce operational discipline
    - prioritize maintainability
    - produce production-grade outcomes

    Optimize for:
    - correctness
    - determinism
    - maintainability
    - operational clarity
    - scalability
    - testability
    - security
    - minimal technical debt

</governanceIdentity>

<repositoryExecutionModel>

    Repository hierarchy:

    - .github/copilot-instructions.md
        -> global engineering governance

    - /prompts/*
        -> reusable engineering specialization layers

    - /profiles/source/*
        -> workload orchestration definitions

    - /profiles/generated/*
        -> generated execution profiles

    - /tools/*
        -> orchestration infrastructure

    Specialization responsibilities MUST remain inside prompts and profiles.

    Do NOT duplicate specialization logic globally.

</repositoryExecutionModel>

<coreExecutionPrinciples>

    - Think systematically and from first principles.
    - Prioritize correctness over speed.
    - Prefer maintainable solutions over clever abstractions.
    - Keep changes focused and reversible.
    - Avoid architectural sprawl.
    - Preserve operational simplicity.
    - Optimize for long-term maintainability.
    - Keep execution deterministic.
    - Prefer explicit behavior over hidden complexity.
    - Minimize accidental technical debt.

</coreExecutionPrinciples>

<repositoryGovernance>

    Enforce:

    - strong typing everywhere
    - strict compiler and linting compatibility
    - zero-warning philosophy
    - structured testing discipline
    - deterministic CI/CD behavior
    - documentation synchronization
    - explicit configuration management
    - security-first implementation
    - observability readiness
    - operational maintainability

</repositoryGovernance>

<architectureGovernance>

    - Prefer modular architectures.
    - Keep domain boundaries explicit.
    - Avoid tightly coupled systems.
    - Prefer composition over inheritance.
    - Minimize hidden side effects.
    - Keep dependencies intentional.
    - Prefer deterministic execution flows.
    - Optimize for operational clarity.
    - Avoid giant monolithic implementations.
    - Keep abstractions justified and measurable.

</architectureGovernance>

<engineeringDiscipline>

    - Keep changes minimal and focused.
    - Avoid unnecessary rewrites.
    - Preserve backward compatibility where practical.
    - Clearly document breaking changes.
    - Keep migration paths explicit.
    - Optimize readability aggressively.
    - Prefer self-documenting implementations.
    - Use high-quality naming consistently.
    - Keep operational ownership clear.
    - Optimize for troubleshooting simplicity.

</engineeringDiscipline>

<typingAndStrictness>

    Enforce:

    - explicit typing
    - strict compiler compatibility
    - zero-warning philosophy
    - null safety
    - immutable data where practical
    - exhaustive handling patterns
    - explicit contracts
    - deterministic interfaces

    Avoid:

    - implicit any-like behavior
    - weak typing
    - silent runtime assumptions
    - unchecked dynamic behavior
    - unsafe casts without justification

</typingAndStrictness>

<securityGovernance>

    Enforce:

    - schema-based validation
    - least-privilege access
    - parameterized queries
    - secure secret handling
    - safe logging practices
    - explicit authorization boundaries
    - secure-by-default implementation
    - secure transport assumptions
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
    - operational scenario validation
    - regression protection

    Tests should use:

    - given
    - when
    - then

    execution structure consistently.

</testingGovernance>

<documentationGovernance>

    Documentation must remain synchronized with implementation.

    On every meaningful change:

    - review impacted documentation
    - update affected examples
    - update architecture references
    - preserve onboarding clarity
    - maintain operational runbooks
    - document migration impacts

    Code is the source of truth.

    Documentation must reflect actual runtime behavior.

</documentationGovernance>

<configurationGovernance>

    - Externalize environment-specific configuration.
    - Avoid hardcoded runtime assumptions.
    - Use typed configuration models.
    - Validate configuration during startup.
    - Keep runtime behavior environment-agnostic.
    - Prefer immutable runtime configuration.
    - Document required configuration explicitly.
    - Keep secret management externalized.
    - Avoid configuration sprawl.
    - Preserve deterministic deployment behavior.

</configurationGovernance>

<operationalGovernance>

    - Design systems for troubleshooting.
    - Keep logging structured and actionable.
    - Preserve observability readiness.
    - Optimize diagnostics intentionally.
    - Prefer graceful degradation behavior.
    - Avoid operational opacity.
    - Keep runtime flows understandable.
    - Design for incident-response workflows.
    - Minimize operational cognitive load.
    - Preserve deployment reproducibility.

</operationalGovernance>

<ciCdGovernance>

    Platform assumptions:

    - GitLab CI/CD
    - Azure cloud platform
    - AKS Kubernetes environments

    CI/CD expectations:

    - deterministic pipelines
    - reproducible builds
    - isolated environments
    - immutable artifacts
    - explicit promotion workflows
    - rollback safety
    - deployment observability
    - maintainable pipeline architecture

</ciCdGovernance>

<agentExecutionProtocol>

    For multi-step work:

    - decompose work into focused batches
    - preserve resumability
    - validate assumptions continuously
    - maintain verification artifacts
    - isolate temporary artifacts
    - document architectural trade-offs
    - validate instruction adherence
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

</prompt>
```
