<module>

<moduleIdentity>

Foundational engineering judgment for GHCP.

Responsibilities:

- engineering quality
- maintainability
- modularity
- security fundamentals
- testing fundamentals
- anti-pattern detection

</moduleIdentity>

<engineeringJudgment>

- Prefer simple, maintainable solutions.
- Prefer composition over inheritance.
- Keep boundaries explicit and modules loosely coupled.
- Prefer explicit behavior over hidden magic.
- Isolate side effects.
- Fail fast on invalid configurations.
- Validate assumptions early.
- Keep changes small and reversible.
- Use deterministic behavior.
- Judge tradeoffs intentionally.

</engineeringJudgment>

<qualityAndSafety>

- Use explicit typing where supported.
- Prefer static validation over runtime surprises.
- Use linting and tests consistently.
- Mock only external boundaries.
- Handle errors explicitly and transparently.
- Validate inputs and protect sensitive data.
- Use structured diagnostics.

</qualityAndSafety>

<antiPatterns>

- overengineering
- unnecessary abstractions
- hidden side effects
- excessive dependencies
- tightly coupled modules
- premature optimization
- monolithic implementations
- nondeterministic behavior
- undocumented tradeoffs

</antiPatterns>

</module>
