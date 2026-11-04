---
id: GAS-Q023
title: Check retained quantity after rounding
type: question
topic: gas
status: draft
version: 0.1.0
response_type: calculation
knowledge_ids:
  - GAS-010
---

# Check retained quantity after rounding

## Teaching notes

Teach GAS-010 first, including its guided calculation with different inputs. Assess units, method, arithmetic and explanation separately. Use the 1 bar reference, ideal-gas approximation and comparable temperature throughout. This is an authored classroom exercise, not a real dive plan.

## Question

A has 24 L and B 18 L, both at 225 bar. Keep each exit demand fixed at one third of their own starting inventory. All donor gas remaining is deliverable. Derive both thresholds rounded upward to 1 bar steps, both entry quantities and both donor surpluses. Identify any surplus created only by rounding.

## Response format

Show your calculation with units, label the requested quantities and briefly explain the result. No answer choices are provided.

## Answer and explanation

Inventories: **5,400** and **4,050 reference L**; demands **1,800** and **1,350 reference L**; combined **3,150 reference L**. A keeps **150 bar**, uses **1,800 reference L** and retains **3,600 reference L**, surplus **450 reference L**. B requires **175 bar**, uses **900 reference L** and retains **3,150 reference L**, surplus **0 reference L**. Both thresholds are exact whole bars; no surplus is created by rounding here.

## Follow-up discussion

If the retained-pressure division did have a remainder, why would rounding down be unsuitable?

## Tutor guidance

It would retain less than the supplied demand. A rounding surplus is not an independently chosen contingency margin.
Accept equivalent exact fractions and decimal notation. Where rounding is specified, assess the conservative direction as well as the value. Identify a conceptual error before offering another arithmetic attempt. Do not reveal a pending follow-up before the learner has answered the main calculation.
