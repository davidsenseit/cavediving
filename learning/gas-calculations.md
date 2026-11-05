---
id: LEARN-GAS-001
title: Gas calculation learning block
type: learning_path
topic: gas
status: draft
version: 0.1.0
knowledge_ids:
  - GAS-004
  - GAS-005
  - GAS-006
  - GAS-007
  - GAS-008
  - GAS-009
  - GAS-010
  - GAS-011
  - GAS-001
  - GAS-002
---

# Gas calculation learning block

This is the teaching sequence inside Module 4 of the core course. It is not a second quiz queue. Resume using the same question IDs. Plan multiple sessions if needed; do not compress the block into one summary or skip directly to matching.

## Teach one stage at a time

1. Introduce the current stage's terms and objective. Ask for a qualitative prediction before showing arithmetic.
2. Work through the lesson example with units and the reason for each operation.
3. Present the guided calculation without its answer. Let the learner attempt it, offer one hint if requested, then discuss the guided answer.
4. Ask the two independent authored calculations separately. Show only the ID, Question and Response format; hide worked answers, teaching notes and follow-ups until feedback. Accept equivalent decimal notation and appropriately labelled units.
5. Ask the follow-up separately. Distinguish conceptual mistakes, method selection and arithmetic. For a conceptual error, return to the relevant explanation with a different example before attempting the next stage. Progress is conversational, not a certification score.
6. Summarize what the learner can explain and compute. Continue when prerequisites are understood; allow pauses and learner-directed review.

## Learning evidence and feedback

Record evidence by concept, not only whether a numerical answer matches. A learner may be **introduced**, **guided**, **independent**, or **needs review** for each stage. These are study notes, not dive qualifications or a new required storage schema. Ask the learner to predict the direction of change before computing, then explain the result in a changed example before treating the stage as independently understood.

For each calculation, assess four separate dimensions: **model and assumptions**, **method**, **units and arithmetic**, and **interpretation and safety boundary**. Give a targeted correction rather than simply displaying the solution. An answer using a defensible interpretation of an ambiguous prompt must trigger question review, not automatic failure.

Use [the pressure-and-quantity diagram](../assets/gas/pressure-quantity.svg) at Stage 2 to contrast start inventory, gas used and gas remaining. At Stage 6, use the same diagram's idea of **different start pressures but equal pressure drops**: draw two bars or let the learner change the starting pressures, predict both turn readings, then check the common drop. A static or text equivalent must remain available. Visualizations are conceptual and not real-time gas monitoring.

## Stages

| Stage | Lesson | Independent questions | Evidence before continuing |
| --- | --- | --- | --- |
| 1 | [GAS-004](../knowledge/gas/cylinder-size-and-gas-quantity.md) | [GAS-Q010](../questions/gas/identify-twinset-inventory.md), [GAS-Q011](../questions/gas/separate-cylinder-readings.md) | Identify capacity, pressure and reference quantity; count cylinders once. |
| 2 | [GAS-005](../knowledge/gas/bar-and-reference-litres.md) | [GAS-Q012](../questions/gas/used-and-remaining-quantity.md), [GAS-Q013](../questions/gas/convert-quantity-to-pressure.md) | Convert both ways and distinguish used from remaining gas. |
| 3 | [GAS-006](../knowledge/gas/sixths-and-thirds.md) | [GAS-Q014](../questions/gas/sixths-allocation.md), [GAS-Q015](../questions/gas/compare-sixths-and-thirds.md) | Explain stipulated sixths and thirds without choosing privileges. |
| 4 | [GAS-007](../knowledge/gas/turn-pressure-and-rounding.md) | [GAS-Q016](../questions/gas/round-retained-pressure.md), [GAS-Q017](../questions/gas/insufficient-starting-inventory.md) | Derive a retained threshold and round in the conservative direction. |
| 5 | [GAS-008](../knowledge/gas/matching-equal-configurations.md) | [GAS-Q018](../questions/gas/equal-team-matching.md), [GAS-Q019](../questions/gas/additional-demand-check.md) | Explain both donor checks and zero additional margin. |
| 6 | [GAS-009](../knowledge/gas/matching-different-starting-pressures.md) | [GAS-Q020](../questions/gas/unequal-pressure-matching.md), [GAS-Q021](../questions/gas/common-allowance-rounding.md) | Apply a common entry allowance to different actual starts. |
| 7 | [GAS-010](../knowledge/gas/matching-different-cylinder-sizes.md) | [GAS-Q022](../questions/gas/unequal-capacity-matching.md), [GAS-Q023](../questions/gas/unequal-capacity-rounded-threshold.md) | Identify quantity shortage despite equal gauge pressure. |
| 8 | [GAS-011](../knowledge/gas/matching-mixed-capacities-and-pressures.md) | [GAS-Q024](../questions/gas/mixed-capacity-pressure-matching.md), [GAS-Q025](../questions/gas/mixed-smaller-donor.md) | Combine both differences without changing fixed demand bounds. |

## Retrieval checkpoints

After Stage 4, ask a new short conversion or turn-pressure question from Stages 1–2 without showing the formula. After Stage 6, revisit the distinction between a common pressure drop and a common final gauge reading. After Stage 8, use a fresh mixed-capacity example and ask which assumption would have to change before claiming operational adequacy. Vary the numbers and ask for reasoning; do not reuse unanswered authored question inputs.

## Consolidation

After the eight stages, use [GAS-Q026](../questions/gas/cumulative-matching-worksheet.md) and [GAS-Q027](../questions/gas/cumulative-insufficient-donor.md) for a mixed case and a case that does not permit entry. Then return to the core sequence's existing consumption, demand, delay and oxygen questions. Teach GAS-001 before the consumption questions; use GAS-002 to distinguish inventory allocation from actual exit demand. The core pathway and manifest contain all question links and course roles.

## Feedback and remediation

| Observation | Teaching response |
| --- | --- |
| Uses one cylinder capacity for a twinset, or doubles pressure too | Return to GAS-004; draw the two capacities and one shared pressure. |
| Converts remaining gas but labels it used gas | Return to GAS-005; label start, change and remainder before calculating. |
| Treats a one-sixth allowance as one-sixth remaining | Return to GAS-006; partition starting inventory and subtract entry use. |
| Rounds retained pressure downward | Return to GAS-007; reverse-convert and compare with the required quantity. |
| Applies the same turn reading to different starts | Return to GAS-009; subtract the common allowance from each actual start. |
| Compares unequal cylinders using only bar | Return to GAS-010; express both supplies in reference litres. |
| Recalculates a fixed demand from the reduced entry allowance | Restate the exercise's supplied demand bounds; do not substitute a new model mid-solution. |
| Supplies a correct threshold but claims a real dive is safe | Ask which route, demand, access and contingency assumptions remain unestablished. |

For generated remediation, label the exercise AI-generated practice, verify its arithmetic independently and keep it distinct from authored question IDs. Do not use a pending question's numbers as the teaching example.
