---
id: GAS-009
title: Match equal capacities with different starting pressures
type: knowledge
topic: gas
status: draft
version: 0.1.0
---

# Match equal capacities with different starting pressures

## Prerequisites

GAS-008 and GAS-007: donor checks and threshold arithmetic.

## Learning objective

Match a stipulated entry allowance to the lower starting pressure when capacities are equal, then subtract it from each actual starting pressure.

## Declare the comparison

For this equal-capacity exercise, both divers' entry use is capped at one third of the lower starting inventory. Each ordinary exit demand is stipulated to equal that common allowance. This keeps the compared quantities equal; it does not infer equal actual demand from cylinder size. Both donor directions must still be checked. Use the same accessible-supply assumptions as GAS-008.

This common-allowance model differs from later cases that explicitly stipulate different fixed exit demands for the two divers. Read the demand assumptions before selecting a calculation.

## Worked example

A and B each have 24 L. A starts at 240 bar; B starts at 210 bar. Their starting quantities are 5,760 and 5,040 reference L. The lower starting pressure gives a 210 / 3 = **70 bar** common entry allowance, representing 1,680 reference L for each diver.

| Quantity | A | B |
| --- | --- | --- |
| Actual starting pressure | 240 bar | 210 bar |
| Allowed entry pressure drop | 70 bar | 70 bar |
| Individual turn pressure | 170 bar | 140 bar |
| Quantity at threshold | 4,080 reference L | 3,360 reference L |

Stipulated combined exit demand is 1,680 + 1,680 = **3,360 reference L**. A can supply it at its threshold with 720 reference L surplus; B has zero surplus. The lower starting supply governs the common allowance, but the individual thresholds differ.

Using each diver's own thirds would allow A a larger entry quantity, changing the assumptions. Giving both divers a 140 bar threshold would allow A an excessive pressure drop within this common-allowance exercise.

## Visual reasoning prompt

Before using the guided numbers, sketch two pressure bars of equal capacity but different starting pressure. Mark the **same allowed drop** on each, then ask whether their final gauge readings should match. They should not: the drops match, but each reading is subtracted from its own start. This can later be made interactive with two starting-pressure controls and an explicitly displayed common allowance; no interactive tool is required to teach the concept.

## Guided calculation

Both configurations are 20 L. A starts at 230 bar and B at 180 bar. Set each stipulated exit demand to one third of the lower starting inventory. Calculate common allowance, thresholds and both retained supplies.

## Guided answer — reveal after the learner attempts

Lower inventory = 3,600 reference L. Common entry allowance = **1,200 reference L = 60 bar**. A turns at **170 bar**, retaining 3,400 reference L. B turns at **120 bar**, retaining 2,400 reference L. Combined demand is 2,400 reference L; surpluses are 1,000 and 0 reference L.

## Explain before moving on

When is an equal pressure-drop allowance also an equal quantity allowance? Why does that statement not transfer unchanged to unequal capacities?
