---
id: GAS-007
title: Derive a turn pressure and round conservatively
type: knowledge
topic: gas
status: draft
version: 0.1.0
---

# Derive a turn pressure and round conservatively

## Prerequisites

GAS-005 and GAS-006: inverse conversions and allocations.

## Learning objective

Derive the retained-pressure threshold in two ways and explain the direction of conservative rounding.

## Worked allocation route

For 24 L starting at 232 bar with a stipulated thirds ceiling, the exact entry pressure allowance is 232 / 3 = 77.333… bar. In this exercise the agreed entry allowance is rounded down to a multiple of 5 bar: **75 bar**. Subtract that allowance from the actual start: 232 − 75 = **157 bar**. If a turn threshold must also be expressed in 5 bar steps, round the required retained pressure upward to **160 bar**. That gives 72 bar entry use and retains more gas.

Do not replace the actual start with a rounded number and then forget the excess gas. Label what is being rounded: allowable consumption goes down; required retention goes up.

## Worked retained-quantity route

A separate classroom problem specifies that 3,560 reference L must remain in a 20 L configuration starting at 240 bar. Required pressure is 3,560 / 20 = **178 bar**. For the stipulated 5 bar steps, use **180 bar**. The allowed drop is then 240 − 180 = 60 bar, representing 1,200 reference L. Remaining quantity is 20 × 180 = 3,600 reference L, at least the stated requirement.

If the required retained quantity exceeds starting inventory, the model cannot support entry. A negative entry allowance is not permission to change the sign or round the shortage away. Equality permits zero entry use and provides no extra margin in the stated model.

## Guided calculation

A 24 L configuration starts at 230 bar. The task stipulates 3,720 reference L retained. Calculate exact threshold, a threshold rounded upward to 10 bar steps, permitted pressure drop and entry quantity after rounding.

## Guided answer — reveal after the learner attempts

Exact threshold = 3,720 / 24 = **155 bar**; rounded threshold = **160 bar**; drop = 70 bar; entry quantity = 24 × 70 = **1,680 reference L**. Remaining quantity is 3,840 reference L. The 10 bar step is an exercise condition, not a universal gauge-reading rule.

## Explain before moving on

State the difference between a pressure drop, a turn pressure, a time limit and penetration distance. None of the last two can be inferred from a pressure threshold alone.
