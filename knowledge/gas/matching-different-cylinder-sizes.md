---
id: GAS-010
title: Match different capacities at equal starting pressure
type: knowledge
topic: gas
status: draft
version: 0.1.0
---

# Match different capacities at equal starting pressure

## Prerequisites

GAS-009, GAS-005 and GAS-007: compare quantities before thresholds.

## Learning objective

Expose a shortage hidden by equal gauge readings and derive the retained threshold for the smaller donor.

## Declare the fixed-demand model

Each ordinary exit demand is stipulated as one third of that diver's own starting inventory. Keep those demand bounds fixed when adjusting entry allowances. This is the limited allocation model introduced in GAS-008 and used in GAS-002. It differs from GAS-009's common-demand comparison. All remaining donor gas is assumed accessible and deliverable; actual demand, cylinder-access restrictions and additional margins are not established.

## Worked example

A has 24 L and B has 18 L, both at 240 bar. Starting inventories are 5,760 and 4,320 reference L. Stipulated individual exit demands are 1,920 and 1,440 reference L. Combined demand is **3,360 reference L**.

At an unadjusted 160 bar turn, A retains 3,840 reference L and B retains 2,880 reference L. If A loses gas, B is **480 reference L short**. A has 0 reference L shortage at that threshold. Equal pressure has hidden unequal quantity.

A's ordinary thirds threshold of 160 bar already retains enough for the fixed combined demand. B needs 3,360 / 18 = 186.666… bar retained. This exercise rounds required retention upward in 1 bar steps: **187 bar**.

| Quantity | A | B |
| --- | --- | --- |
| Threshold | 160 bar | 187 bar |
| Allowed pressure drop | 80 bar | 53 bar |
| Allowed entry quantity | 1,920 reference L | 954 reference L |
| Retained donor quantity | 3,840 reference L | 3,366 reference L |
| Surplus over fixed combined demand | 480 reference L | 6 reference L |

The 6 reference L is only a rounding surplus, not an independently chosen emergency margin. The team turns at the first applicable limit. Different thresholds are not predictions of when either gauge reaches them.

## Guided calculation

A has 24 L and B 20 L, both at 210 bar. Use each diver's own starting third as a fixed exit-demand bound. Calculate combined demand, the shortage for B at unadjusted thirds, and both thresholds. Round required retained pressures upward to 1 bar.

## Guided answer — reveal after the learner attempts

Inventories: 5,040 and 4,200 reference L. Fixed demands: 1,680 and 1,400 reference L; combined **3,080 reference L**. At 140 bar B retains 2,800 reference L, a **280 reference L shortage**. B needs **154 bar**, allowing 56 bar = 1,120 reference L entry use. A remains at **140 bar**, allowing 70 bar = 1,680 reference L entry and retaining 3,360 reference L. A has 0 reference L shortage at the unadjusted threshold. Both donor directions meet the stipulated demand; B has no extra margin.

## Explain before moving on

Why must the fixed demand bounds remain unchanged while solving this particular allocation exercise? What additional work would establish an actual route-dependent demand?
