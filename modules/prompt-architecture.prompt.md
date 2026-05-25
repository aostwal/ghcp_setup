```xml
<prompt>

<architecturePurpose>

    This prompt defines governance, composition, and scalability rules for the GHCP engineering intelligence platform.

    It standardizes:

    - prompt layering
    - profile composition
    - orchestration boundaries
    - specialization rules
    - maintainability standards
    - prompt architecture consistency

</architecturePurpose>

<coreArchitecturePrinciples>

    - Prompts define reusable engineering intelligence.
    - Profiles define workload orchestration.
    - Profiles must compose prompts intentionally.
    - Avoid giant all-in-one prompts.
    - Keep specialization boundaries explicit.
    - Optimize for maintainability and scalability.
    - Prefer composable intelligence layers.
    - Minimize instruction duplication.
    - Prevent conflicting architectural guidance.
    - Prefer deterministic orchestration behavior.

</coreArchitecturePrinciples>

<promptLayeringRules>

    Prompts must specialize in ONE primary concern.

    Examples:

    - go-platform.prompt.md
        -> Go runtime engineering

    - kubernetes-platform.prompt.md
        -> Kubernetes operational engineering

    - docker-platform.prompt.md
        -> container runtime engineering

    Prompts must NOT:
    - duplicate other prompt responsibilities
    - become generic mega-prompts
    - contain unrelated domain specialization
    - overload multiple engineering concerns

</promptLayeringRules>

<profileCompositionRules>

    Profiles orchestrate prompts for specific engineering workflows.

    Profiles must:
    - define clear workload specialization
    - activate only relevant prompts
    - optimize for one primary engineering workflow
    - maintain clear operational priorities
    - avoid unrelated domain pollution

    Profiles must NOT:
    - activate unnecessary prompts
    - become universal expert modes
    - combine conflicting specializations
    - overload unrelated engineering domains

</profileCompositionRules>

<namingConventions>

    Prompt naming:
    - *.prompt.md

    Profile naming:
    - *.profile.md

    Generated profile naming:
    - *.generated.md

    Naming should prioritize:
    - explicit specialization
    - operational clarity
    - maintainability
    - workload orientation

</namingConventions>

<directoryArchitecture>

    /prompts
        reusable engineering intelligence

    /profiles/source
        workload orchestration definitions

    /profiles/generated
        assembled GHCP-consumable profiles

    /tools
        orchestration and generation tooling

</directoryArchitecture>

<compositionStandards>

    Composition must:

    - maintain deterministic prompt ordering
    - prevent duplicated instructions
    - prevent conflicting guidance
    - maintain specialization clarity
    - optimize token efficiency
    - preserve workload intent
    - support future scalability
    - support maintainable evolution

</compositionStandards>

<specializationBoundaries>

    Each prompt should answer:

    "What engineering specialization does this own?"

    Each profile should answer:

    "What engineering workflow does this optimize for?"

    If unclear:
    architecture boundaries are weak.

</specializationBoundaries>

<antiPatterns>

    Avoid:

    - giant universal prompts
    - overloaded profiles
    - duplicated engineering guidance
    - unclear specialization ownership
    - prompt responsibility overlap
    - random technology grouping
    - conflicting orchestration priorities
    - abstraction-heavy prompt systems
    - architecture without governance

</antiPatterns>

<scalabilityGoals>

    The GHCP architecture must scale through:

    - reusable prompt specialization
    - composable workload profiles
    - deterministic profile generation
    - maintainable orchestration tooling
    - clear architectural governance
    - isolated engineering intelligence layers

</scalabilityGoals>

</prompt>
```
