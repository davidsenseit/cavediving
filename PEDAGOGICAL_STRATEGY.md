# Pedagogical Strategy

This document guides the development and delivery of the cave-diving learning course. It defines educational quality expectations, not a fixed lesson template or a technical architecture.

## Purpose and boundaries

Help learners understand concepts, apply them to new situations, explain decisions and retain knowledge. The course supports preparation and review; it does not certify practical competence or authorize dives. In-water skills and emergency procedures require supervised training and assessment.

Use the canonical terminology in `GLOSSARY.md` regardless of the learner's language. Preserve `draft` and `verified` content statuses. Newly authored or substantively revised content starts as `draft`.

## Five teaching principles

1. **Progressive understanding (scaffolding).** Introduce prerequisites and vocabulary before assessment. Move from a clear explanation and guided example to independent work. Increase complexity only when the learner demonstrates the relevant prerequisite.
2. **Active application (scenario-based learning).** Prefer realistic, original decisions, calculations, error diagnosis and explanations over recall alone. State all assumptions and constraints needed for an unambiguous answer. Adapt the exercise format to the topic rather than imposing one pattern on every lesson.
3. **Accurate, explanatory feedback.** Explain why an answer works or fails, including relevant alternatives and consequences. Distinguish conceptual misunderstanding, arithmetic error, unit error, unsupported assumption and ambiguous question. Never label a defensible answer wrong merely because it differs from a preferred wording.
4. **Understanding over scores (mastery-based learning).** Evaluate whether the learner can independently apply and explain a concept in a new example. Revisit unresolved misconceptions before adding dependent complexity. Do not treat a quiz score as proof of practical readiness; safety-critical misunderstandings must be addressed explicitly.
5. **Retrieval and retention.** Ask the learner to recall and apply earlier material after some intervening study. Revisit weak concepts with varied questions, rather than simply repeating identical items. Timed spaced repetition is an optional later enhancement, not a requirement for the initial course.

## Authoring and assessment quality

For each lesson or exercise, contributors should be able to identify the learning objective, necessary prerequisites, expected reasoning and evidence of understanding. These may live in existing lesson/question formats; no new mandatory schema is required.

Before adding or changing an assessment, check that:

- The question has enough information to support the intended answer, with units and assumptions stated.
- The answer and explanation are consistent with the accessible, applicable knowledge and the question's stated model.
- Distractors are plausible but not misleadingly correct; if multiple answers are defensible, revise the question.
- The feedback teaches the underlying principle and identifies the learner's actual error.
- Numerical results and boundary cases are checked independently, with calculation tests where practical.
- Safety-critical examples clearly distinguish classroom simplifications from operational planning.

For gas management, keep gas inventory, planned allocation, team matching and scenario-specific emergency exit demand as distinct checks. A correct arithmetic result is not by itself proof of adequate emergency reserves. For navigation and emergency topics, use clear route and equipment assumptions; avoid invented site-specific procedures.

## Delivery and progression

Use the existing `learning/core-pathway.md`, `curriculum-manifest.json`, `catalog.md` and `AGENTS.md` as the operational course structure. Teach one assessment at a time, withhold its answer until an attempt, and provide focused feedback afterward. Respect topic selection and the learner's pace. Revisit concepts when reasoning reveals a gap; avoid unnecessary repetition when understanding is demonstrated.

The same principles apply to AI-assisted and non-AI delivery. Deterministic checks are preferred for arithmetic and other objectively testable outcomes. AI-generated practice must be identified as such and checked for ambiguity before use.

## Implementation priorities

1. Apply the authoring and feedback checks to existing questions, beginning with safety-critical and calculation-heavy material.
2. Use Gas Management as the first reference implementation for progressive teaching and independently verified calculations; use visual route decisions for Navigation.
3. Add lightweight tracking of unresolved concepts only when the course interface needs it.
4. Consider automated adaptation and scheduled spaced repetition after the basic learning experience has been evaluated.

Keep implementation details in issues and feature-specific documents. Revise this strategy only when the underlying educational principles change.
