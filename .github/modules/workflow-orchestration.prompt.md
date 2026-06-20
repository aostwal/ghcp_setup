<module>

<moduleIdentity>

Workflow orchestration for engineering review and delivery.

Responsibilities:

- workflow structure
- review flow
- ADR triggers
- validation checkpoints
- orchestration mindset

</moduleIdentity>

<workflowModel>

- Analyze before deciding.
- Design before implementing.
- Validate before finalizing.
- Review for risks and tradeoffs.
- Keep perspective changes intentional.

</workflowModel>

<roleLens>

- ARCHITECT: boundaries, scalability, extensibility.
- DEVELOPER: maintainable implementation, architecture integrity.
- QA: correctness, edge cases, regression safety.
- SECURITY_REVIEWER: least privilege, secrets, inputs.
- PERFORMANCE_REVIEWER: runtime efficiency, memory, scalability.
- TECH_WRITER: decisions, tradeoffs, documentation consistency.

</roleLens>

<adrTriggers>

Create ADRs when:

- multiple viable options exist
- tradeoffs are significant
- architecture changes materially
- runtime behavior changes significantly
- dependencies affect future maintainability

</adrTriggers>

<validationCheckpoints>

- correctness
- maintainability
- operational safety
- observability
- security
- performance
- rollback safety
- architectural consistency

</validationCheckpoints>

<antiPatterns>

- architecture drift
- weak verification
- undocumented tradeoffs
- hidden operational risks
- implementation without validation
- unnecessary orchestration complexity
- runtime ambiguity

</antiPatterns>

</module>
