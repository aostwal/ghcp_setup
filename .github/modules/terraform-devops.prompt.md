<module>

<moduleIdentity>

    Infrastructure-as-code and Terraform engineering module.

    Responsibilities:

    - Terraform architecture
    - infrastructure-as-code governance
    - Azure infrastructure automation
    - AKS platform provisioning
    - cloud infrastructure operations
    - deployment safety
    - infrastructure scalability

</moduleIdentity>

<instructionInheritance>

    This module builds on:

    - core engineering governance
    - workflow orchestration governance
    - container and Kubernetes operational principles

    Specialization focus:

    - Terraform platform engineering
    - infrastructure reproducibility
    - infrastructure safety
    - AKS infrastructure patterns
    - Azure platform provisioning
    - operational infrastructure governance

</instructionInheritance>

<terraformEngineeringPhilosophy>

    - Infrastructure must remain predictable.
    - Prefer simple and maintainable module designs.
    - Optimize for long-term operational maintainability.
    - Prefer explicit infrastructure behavior.
    - Minimize infrastructure blast radius.
    - Prefer composable infrastructure modules.
    - Keep infrastructure changes reviewable.
    - Design infrastructure for safe evolution.
    - Prefer deterministic infrastructure plans.
    - Reliability is more important than abstraction purity.

</terraformEngineeringPhilosophy>

<terraformModuleArchitecture>

    - Keep modules focused and cohesive.
    - Avoid giant all-in-one modules.
    - Avoid deeply nested module chains.
    - Prefer composable module boundaries.
    - Keep module inputs explicit and predictable.
    - Minimize hidden side effects between modules.
    - Avoid unnecessary module abstractions.
    - Separate platform concerns cleanly.
    - Design modules for safe reuse.
    - Keep module outputs intentional and minimal.

</terraformModuleArchitecture>

<stateManagementAndSafety>

    - Use remote state consistently.
    - Protect state integrity aggressively.
    - Minimize state coupling between environments.
    - Avoid unsafe shared state patterns.
    - Design for safe concurrent operations.
    - Avoid unnecessary state dependencies.
    - Keep state boundaries clear and isolated.
    - Protect sensitive state data.
    - Minimize destructive infrastructure operations.
    - Design infrastructure for safe rollback workflows.

</stateManagementAndSafety>

<deploymentAndOperationalSafety>

    - Prefer incremental infrastructure changes.
    - Minimize infrastructure blast radius.
    - Avoid unsafe lifecycle operations.
    - Use lifecycle rules carefully.
    - Avoid hidden replacement behavior.
    - Keep infrastructure plans predictable.
    - Prefer explicit dependencies.
    - Validate infrastructure assumptions early.
    - Optimize for operational troubleshooting.
    - Design deployments for rollback safety.

</deploymentAndOperationalSafety>

<azurePlatformEngineering>

    - Encode Azure platform decisions as explicit Terraform resources.
    - Keep provider configuration environment-scoped and reviewable.
    - Represent identity, networking, and policy boundaries without redefining cloud policy.
    - Surface Azure dependencies through clear variables and outputs.
    - Keep Azure resource composition reproducible across environments.

</azurePlatformEngineering>

<aksInfrastructurePatterns>

    - Keep AKS cluster, node pool, identity, and add-on resources separately reviewable.
    - Model node pools as intentional Terraform boundaries.
    - Expose workload integration points through stable outputs.
    - Avoid cluster-wide assumptions hidden inside reusable modules.
    - Keep lifecycle behavior explicit for cluster-sensitive resources.

</aksInfrastructurePatterns>

<ciCdAndDevOpsPractices>

    - Keep Terraform pipelines deterministic.
    - Separate plan and apply workflows clearly.
    - Prefer immutable deployment artifacts.
    - Minimize CI/CD environment drift.
    - Use validation and linting consistently.
    - Keep infrastructure pipelines observable.
    - Prefer reproducible deployment workflows.
    - Optimize for reviewable infrastructure changes.
    - Protect sensitive pipeline variables.
    - Design pipelines for operational safety.

</ciCdAndDevOpsPractices>

<securityAndGovernance>

    - Keep security-sensitive Terraform behavior explicit.
    - Protect secrets and sensitive state values.
    - Make policy assignments and RBAC changes easy to review.
    - Keep governance boundaries visible in module inputs and outputs.
    - Avoid hiding security posture behind defaults.

</securityAndGovernance>

<scalabilityAndMaintainability>

    - Design infrastructure for multi-environment scale.
    - Avoid O(n²) infrastructure dependencies.
    - Keep environment isolation clean.
    - Avoid duplication-heavy Terraform layouts.
    - Optimize infrastructure readability.
    - Keep infrastructure reviews understandable.
    - Design for platform evolution.
    - Prefer operationally maintainable abstractions.
    - Minimize infrastructure cognitive load.

</scalabilityAndMaintainability>

<testingAndValidation>

    - Validate Terraform plans carefully.
    - Validate destructive change risks.
    - Validate environment assumptions.
    - Validate RBAC behavior.
    - Validate networking assumptions.
    - Validate rollback safety.
    - Validate drift handling behavior.
    - Validate AKS compatibility.
    - Validate module boundary integrity.
    - Validate Terraform maintainability.

</testingAndValidation>

<terraformAntiPatterns>

    Avoid:

    - giant monolithic modules
    - excessive variable indirection
    - hardcoded environments
    - unsafe lifecycle ignore_changes usage
    - tightly coupled remote states
    - environment duplication chaos
    - implicit infrastructure assumptions
    - hidden resource dependencies
    - unsafe destructive defaults
    - abstraction-heavy Terraform architectures

</terraformAntiPatterns>

<deliveryExpectations>

    Deliver:

    - production-grade Terraform architectures
    - maintainable infrastructure modules
    - operationally safe infrastructure changes
    - scalable Azure platform patterns
    - AKS-compatible infrastructure
    - deterministic deployment workflows
    - secure infrastructure designs
    - observable and governable infrastructure

</deliveryExpectations>

</module>
