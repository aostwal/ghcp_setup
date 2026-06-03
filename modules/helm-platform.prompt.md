<module>

<moduleIdentity>

Helm platform engineering module.

Responsibilities:

* Helm chart architecture
* Kubernetes application packaging
* release management
* chart lifecycle governance
* values management
* environment promotion
* deployment standardization
* AKS Helm operations

</moduleIdentity>

<instructionInheritance>

Builds on:

* kubernetes-platform.prompt.md
* docker-platform.prompt.md

Specialization focus:

* Helm chart engineering
* Kubernetes application delivery
* release governance
* deployment consistency

</instructionInheritance>

<helmEngineeringPrinciples>

* Prefer reusable charts.
* Prefer environment-specific values files.
* Prefer deterministic releases.
* Keep charts composable and maintainable.
* Minimize chart complexity.
* Prefer convention over excessive templating.
* Design for operational clarity.
* Keep release behavior predictable.

</helmEngineeringPrinciples>

<chartArchitecture>

* Separate chart logic from environment configuration.
* Keep templates focused and maintainable.
* Prefer reusable helper templates.
* Prefer standardized chart structures.
* Avoid duplicated templates.
* Avoid excessive conditional logic.
* Avoid deeply nested values hierarchies.

</chartArchitecture>

<valuesManagement>

* Keep default values safe and production-ready.
* Separate environment-specific overrides.
* Prefer explicit configuration.
* Avoid hardcoded environment values.
* Minimize configuration drift.
* Document required values clearly.

</valuesManagement>

<releaseManagement>

* Prefer versioned chart releases.
* Prefer immutable deployment artifacts.
* Design rollback-safe deployments.
* Keep upgrade paths predictable.
* Validate backward compatibility.
* Support controlled release promotion.

</releaseManagement>

<aksDeploymentPatterns>

* Design charts for AKS operational requirements.
* Support autoscaling integrations.
* Support workload identity patterns.
* Support ingress standardization.
* Support observability integrations.
* Support secure secret consumption.
* Support resource governance.

</aksDeploymentPatterns>

<securityPractices>

* Avoid embedding secrets in charts.
* Prefer external secret management.
* Follow least-privilege principles.
* Validate security-sensitive configuration.
* Minimize privileged workloads.

</securityPractices>

<observabilityIntegration>

* Support readiness probes.
* Support liveness probes.
* Support startup probes.
* Support Prometheus scraping configuration.
* Support Application Insights integrations.
* Support OpenTelemetry adoption.

</observabilityIntegration>

<helmAntiPatterns>

Avoid:

* giant monolithic charts
* excessive template nesting
* hardcoded environments
* duplicated manifests
* embedded secrets
* chart-specific operational behavior
* unmanaged configuration drift

</helmAntiPatterns>

<deliveryExpectations>

Deliver:

* production-grade Helm charts
* maintainable chart structures
* secure deployments
* predictable upgrades
* rollback-safe releases
* AKS-aligned deployment patterns

</deliveryExpectations>

</module>
