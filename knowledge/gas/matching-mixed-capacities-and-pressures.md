---
id: GAS-011
title: Match different capacities and different starting pressures
type: knowledge
topic: gas
status: draft
version: 0.1.0
---

# Match different capacities and different starting pressures

## Prerequisites

GAS-010: fixed demand bounds, both donor directions and conservative rounding.

## Learning objective

Combine capacity and pressure differences, retain the stricter threshold and identify a model with no entry allowance.

## Use a consistent worksheet

For each diver calculate starting inventory Q. Write the two stipulated exit demands and add them to get D. For each potential donor calculate the pressure required to retain D. Compare this with that donor's ordinary entry-fraction threshold and keep the higher retained threshold. Round retained thresholds upward using the stated exercise step. Subtract from the actual start, convert the allowed drop to quantity and check both supplies again.

For these fixed-demand exercises, D is the sum of one third of each diver's starting inventory. The exact threshold is the greater of the ordinary two-thirds pressure and D / water volume. Keep D fixed during this calculation. This is a classroom allocation worksheet, not an operational planning tool; it assumes full deliverability of the listed remaining gas.

## Worked example

A has 24 L at 230 bar; B has 20 L at 210 bar. Inventories are 5,520 and 4,200 reference L. Fixed demands are 1,840 and 1,400 reference L; D = **3,240 reference L**.

| Quantity | A | B |
| --- | --- | --- |
| Ordinary thirds threshold | 153.333… bar | 140 bar |
| Pressure equivalent of D | 135 bar | 162 bar |
| Stricter threshold, rounded up to 1 bar | 154 bar | 162 bar |
| Allowed drop | 76 bar | 48 bar |
| Allowed entry quantity | 1,824 reference L | 960 reference L |
| Retained supply | 3,696 reference L | 3,240 reference L |
| Surplus over D | 456 reference L | 0 reference L |

Although A starts with lower pressure than in some earlier examples, its larger capacity gives the larger inventory here. Inspect quantities rather than ranking gauges or cylinder sizes alone.

## Guided calculation

A has 24 L at 225 bar; B has 18 L at 240 bar. Use the same fixed-demand model and round retention upward in 1 bar steps. Show D, both thresholds, entry quantities and both donor checks.

## Guided answer — reveal after the learner attempts

Inventories = 5,400 and 4,320 reference L; fixed demands = 1,800 and 1,440 reference L; D = **3,240 reference L**. A keeps **150 bar**, allowing 75 bar = 1,800 reference L entry and retaining 3,600 reference L. B needs **180 bar**, allowing 60 bar = 1,080 reference L entry and retaining 3,240 reference L. Surpluses are 360 and 0 reference L.

## When the worksheet rejects entry

If either donor's required retention exceeds their starting inventory, the assumed failure model cannot be covered even before entry. If it equals starting inventory, there is zero entry allowance for that donor. Identify the limitation instead of forcing a positive answer. Reconsider the plan and assumptions within applicable training.

## Explain before moving on

If cylinder access after a failure reduces deliverable supply, which part of the worksheet changes? If return delay increases, which part changes? A numerical threshold cannot establish an exit time or distance.
