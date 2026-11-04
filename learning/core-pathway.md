---
id: CORE-PATH-001
title: Cave diving learning pathway
type: learning_path
topic: mixed
status: draft
version: 0.5.0
knowledge_ids:
  - GAS-004
  - GAS-005
  - GAS-006
  - GAS-007
  - GAS-008
  - GAS-009
  - GAS-010
  - GAS-011
  - PHY-001
  - EMR-002
  - PLN-003
  - NAV-004
  - EMR-001
  - ENV-001
  - ENV-002
  - EQP-001
  - EQP-002
  - FND-001
  - FND-002
  - GAS-003
  - GAS-001
  - GAS-002
  - NAV-003
  - NAV-001
  - NAV-002
  - DEC-001
  - PLN-002
  - PLN-001
  - RES-001
---

# Cave diving learning pathway

Start here for the course. Eight modules combine lessons, 43 core questions and 20 optional practice questions. The revised questions belong to this sequence alongside the other authored questions. All learning material remains draft; this is a concept-level learning pathway, not a complete qualification syllabus.

The course order is recorded in [curriculum-manifest.json](../curriculum-manifest.json). The catalog indexes content; this pathway determines the default teaching sequence.

## Lesson cycle

1. Read the module's lessons and every question's linked knowledge entries. Introduce unfamiliar terms using the [glossary](../GLOSSARY.md), including prerequisites from other topics. Keep canonical English terms in Swedish teaching.
2. Teach the relevant concept briefly using a worked example different from the assessment. If the explanation reveals a pending answer, use a different checked exercise labeled **AI-generated practice** and revisit the authored item later.
3. Present one core question at a time, showing only its ID, Question and Choices. Keep titles and teaching notes private until feedback.
4. After the response, explain the reasoning and the relevant alternatives. Use an authored Follow-up discussion when present, asking it separately before consulting Tutor guidance. Where no authored follow-up exists, invite a brief explanation of the deciding fact without claiming it is an authored exercise.
5. Use the module's practice questions to revisit uncertainty or deepen understanding. Check all their prerequisites first. Practice questions are part of the same course; completing core questions does not automatically start a second question sequence.
6. Summarize what was understood and what needs another example, then move to the next module. Follow the learner's request to pause, skip or select a topic.

For numerical work, distinguish method, units and arithmetic. Before shared-demand exercises, teach combined normalized L/min × ambient/reference pressure ratio × minutes = reference litres. Add delay segments with their own pressure, duration and demand; a rate already combined for two divers is not doubled again. These are classroom calculations, not operational dive plans.

When a learner continues, use the last completed question and any outstanding follow-up from the current conversation. Continue with the next unanswered core question in that module; avoid restarting completed questions merely because they also appear in a topic index. Ask for the last question ID only when progress is unavailable. Keep recognition, explained reasoning and unresolved concepts distinct without imposing passing scores or claiming persistent tracking.

## Module 1: Foundations and conditions

Lessons: [FND-001](../knowledge/foundations/competence-boundaries.md), [FND-002](../knowledge/foundations/environment-change.md), [GAS-002](../knowledge/gas/reserves-and-team-demand.md), [EMR-001](../knowledge/emergencies/stress-and-capacity.md).

Use GAS-002 here only for the principle that conditions can require earlier termination. Defer its numerical matching example to Module 4.

Core sequence: [FND-Q001](../questions/foundations/competence-boundaries.md) → [FND-Q002](../questions/foundations/environment-change.md).

Optional practice: [FND-Q003](../questions/foundations/flow-return-asymmetry.md), [FND-Q004](../questions/foundations/passage-configuration.md).

## Module 2: Position control and equipment

Lessons: [EQP-001](../knowledge/equipment/buoyancy-trim-propulsion.md), [EQP-002](../knowledge/equipment/functional-redundancy.md), [RES-001](../knowledge/resources/checklists-devices-logs.md), [PLN-002](../knowledge/planning/communication-and-workload.md), [PLN-001](../knowledge/planning/limits-and-briefing.md).

Core sequence: [EQP-Q001](../questions/equipment/buoyancy-trim-propulsion.md) → [EQP-Q002](../questions/equipment/functional-redundancy.md).

Optional practice: [EQP-Q003](../questions/equipment/battery-failure-analysis.md), [EQP-Q004](../questions/equipment/backup-duration.md), [EQP-Q005](../questions/equipment/stationary-task-silt.md), [EQP-Q006](../questions/equipment/primary-light-loss.md).

## Module 3: Guidelines and route decisions

Lessons: [NAV-004](../knowledge/navigation/line-hazards.md), [NAV-001](../knowledge/navigation/guideline-continuity.md), [NAV-002](../knowledge/navigation/markers-and-evidence.md), [NAV-003](../knowledge/navigation/connections-and-decisions.md), [ENV-002](../knowledge/environment/survey-and-conservation.md), [FND-002](../knowledge/foundations/environment-change.md).

Core sequence: [NAV-Q001](../questions/navigation/continuity.md) → [NAV-Q002](../questions/navigation/markers-and-evidence.md) → [NAV-Q003](../questions/navigation/connections-and-decisions.md) → [NAV-Q009](../questions/navigation/line-hazards.md)

Optional practice: [NAV-Q004](../questions/navigation/parallel-team-lines.md), [NAV-Q005](../questions/navigation/connection-direction.md), [NAV-Q006](../questions/navigation/unfamiliar-cookie.md), [NAV-Q007](../questions/navigation/map-line-disagreement.md), [NAV-Q008](../questions/navigation/nearby-line-end.md).

## Module 4: Gas quantities and demand

Lessons: [GAS-004](../knowledge/gas/cylinder-size-and-gas-quantity.md), [GAS-005](../knowledge/gas/bar-and-reference-litres.md), [GAS-006](../knowledge/gas/sixths-and-thirds.md), [GAS-007](../knowledge/gas/turn-pressure-and-rounding.md), [GAS-008](../knowledge/gas/matching-equal-configurations.md), [GAS-009](../knowledge/gas/matching-different-starting-pressures.md), [GAS-010](../knowledge/gas/matching-different-cylinder-sizes.md), [GAS-011](../knowledge/gas/matching-mixed-capacities-and-pressures.md), [GAS-001](../knowledge/gas/pressure-and-consumption.md), [GAS-002](../knowledge/gas/reserves-and-team-demand.md), [GAS-003](../knowledge/gas/oxygen-and-gas-identity.md), [RES-001](../knowledge/resources/checklists-devices-logs.md).

Core sequence: [GAS-Q010](../questions/gas/identify-twinset-inventory.md) → [GAS-Q011](../questions/gas/separate-cylinder-readings.md) → [GAS-Q012](../questions/gas/used-and-remaining-quantity.md) → [GAS-Q013](../questions/gas/convert-quantity-to-pressure.md) → [GAS-Q014](../questions/gas/sixths-allocation.md) → [GAS-Q015](../questions/gas/compare-sixths-and-thirds.md) → [GAS-Q016](../questions/gas/round-retained-pressure.md) → [GAS-Q017](../questions/gas/insufficient-starting-inventory.md) → [GAS-Q018](../questions/gas/equal-team-matching.md) → [GAS-Q019](../questions/gas/additional-demand-check.md) → [GAS-Q020](../questions/gas/unequal-pressure-matching.md) → [GAS-Q021](../questions/gas/common-allowance-rounding.md) → [GAS-Q022](../questions/gas/unequal-capacity-matching.md) → [GAS-Q023](../questions/gas/unequal-capacity-rounded-threshold.md) → [GAS-Q024](../questions/gas/mixed-capacity-pressure-matching.md) → [GAS-Q025](../questions/gas/mixed-smaller-donor.md) → [GAS-Q026](../questions/gas/cumulative-matching-worksheet.md) → [GAS-Q027](../questions/gas/cumulative-insufficient-donor.md) → [GAS-Q001](../questions/gas/pressure-and-consumption.md) → [GAS-Q004](../questions/gas/pressure-rate-comparison.md) → [GAS-Q002](../questions/gas/reserves-and-team-demand.md) → [GAS-Q006](../questions/gas/exit-delay-demand.md) → [GAS-Q003](../questions/gas/oxygen-and-gas-identity.md) → [GAS-Q008](../questions/gas/oxygen-pressure-change.md).

Optional practice: [GAS-Q005](../questions/gas/available-gas-comparison.md), [GAS-Q007](../questions/gas/allocation-versus-failure.md), [GAS-Q009](../questions/gas/gas-identity-mismatch.md).

### Gas calculation teaching block

Use [the eight-stage gas pathway](gas-calculations.md) for GAS-Q010 through GAS-Q027 before the existing consumption and exposure questions. Teach only the current stage, including its guided exercise, before its independent questions. Do not teach all matching examples upfront. The manifest records stage membership; this core sequence records each question exactly once.

These questions use open numerical responses: present ID, Question and Response format, withholding answers and tutor notes. Ask the calculation and follow-up separately. Allow several sessions and resume at the pending question or follow-up. Use the stage's stated readiness evidence to resolve conceptual gaps before adding complexity, without assigning certification scores.

## Module 5: Team plans and communication

Lessons: [PLN-003](../knowledge/planning/readiness-and-preparedness.md), [PLN-001](../knowledge/planning/limits-and-briefing.md), [PLN-002](../knowledge/planning/communication-and-workload.md), [GAS-002](../knowledge/gas/reserves-and-team-demand.md), [EMR-001](../knowledge/emergencies/stress-and-capacity.md), [EQP-001](../knowledge/equipment/buoyancy-trim-propulsion.md).

Core sequence: [PLN-Q001](../questions/planning/limits-and-briefing.md) → [PLN-Q002](../questions/planning/communication-and-workload.md) → [PLN-Q003](../questions/planning/first-limit.md) → [PLN-Q006](../questions/planning/readiness-and-preparedness.md)

Optional practice: [PLN-Q004](../questions/planning/briefing-signal-disagreement.md), [PLN-Q005](../questions/planning/task-priority.md).

## Module 6: Physiology and emergency capacity

Lessons: [PHY-001](../knowledge/physiology/breathing-and-workload.md), [EMR-002](../knowledge/emergencies/distinguish-events.md), [DEC-001](../knowledge/physiology/models-and-risk.md), [EMR-001](../knowledge/emergencies/stress-and-capacity.md), [GAS-002](../knowledge/gas/reserves-and-team-demand.md), [FND-001](../knowledge/foundations/competence-boundaries.md).

Core sequence: [DEC-Q001](../questions/physiology/models-and-risk.md) → [EMR-Q001](../questions/emergencies/stress-and-capacity.md) → [EMR-Q004](../questions/emergencies/distinguish-events.md) → [PHY-Q001](../questions/physiology/breathing-and-workload.md)

Optional practice: [EMR-Q002](../questions/emergencies/compound-demand.md), [EMR-Q003](../questions/emergencies/unpracticed-configuration.md).

## Module 7: Incident learning and conservation

Lessons: [ENV-001](../knowledge/environment/incident-learning.md), [ENV-002](../knowledge/environment/survey-and-conservation.md).

Core sequence: [ENV-Q001](../questions/environment/incident-learning.md) → [ENV-Q002](../questions/environment/survey-and-conservation.md).

Optional practice: [ENV-Q003](../questions/environment/permission-scope.md).

## Module 8: Documentation and debriefing

Lessons: [RES-001](../knowledge/resources/checklists-devices-logs.md), [NAV-001](../knowledge/navigation/guideline-continuity.md), [EQP-001](../knowledge/equipment/buoyancy-trim-propulsion.md).

Core sequence: [RES-Q001](../questions/resources/checklists-devices-logs.md).

Optional practice: [RES-Q002](../questions/resources/log-evidence-limits.md).

## Course debrief

Revisit uncertain concepts using a materially different checked example. Ask which assumptions changed the learner's reasoning and what needs practical work with an instructor. Record question wording concerns separately from the learner's understanding.

The [project appendix](../questions/interoperability/evidence-and-review-status.md) concerns AI-provider evaluation and is available for contributors separately from the diving course.

## Integrated classroom review
Use a fictional, non-site-specific case after Module 8. Give the learner a team description, conceptual route, stated gas assumptions, equipment dependencies and surface-access constraints. Ask them to identify missing information before making a decision.

Change one condition at a time: a light fails; a return takes longer; a teammate misses a signal; or an apparent line connection is not followable. Ask which assumption changed, which lesson applies and what requires practical training. Do not invent operational gas thresholds or local procedures.

Keep recognition, explanation, numerical reasoning and demonstrated practical skills distinct. Revisit a misunderstood concept with a different example, rather than treating repeated correct letters as mastery.
