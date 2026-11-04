---
id: GAS-002
title: Compare available gas with the actual demand model
type: knowledge
topic: gas
status: draft
version: 0.4.0
---

# Compare available gas with the actual demand model

## Core idea

The familiar thirds allocation limits entry use to one third, leaving a third for return and a third for contingencies. At the turn, at least two thirds remains under that allocation. It is a ceiling on entry use, not a target to consume and not proof of an adequate emergency reserve. Training restrictions, conditions or the failure model can require an earlier turn.

Match quantities and demands across the team. Equal pressure readings do not mean equal gas quantities when cylinder sizes differ. Evaluate gas actually accessible after the modeled failure against both divers' exit demand, including delay, depth, exertion and decompression. Separate cylinders and access failures can change what a donor can supply. A team turns when its first applicable limit is reached.

## Original example

A fictional exercise stipulates 2,600 surface-equivalent litres accessible to a donor and 2,750 litres of combined exit demand. The modeled shortage is 150 litres. Neither figure establishes an actual turn pressure or validates the assumed demand.

## Worked allocation example: unequal cylinder volumes

This original classroom exercise shows how a stipulated exit requirement becomes a pressure threshold. It is not a validated gas-planning method for an actual dive.

### Inputs and assumptions

Both divers start at 240 bar. Diver A has two 10 L cylinders; diver B has two 12 L cylinders. Use ideal gas at comparable temperature and express gas quantities at a 1 bar reference.

For this exercise only, each diver's exit demand is fixed at one third of their own starting inventory. These are supplied demand bounds, not demands calculated from a real route, exit time or measured breathing rate. The modeled event is complete gas loss by either diver, with the other diver supplying both. All gas listed as remaining in the donor's configuration is assumed accessible and deliverable; cylinder access restrictions are not modeled.

| Quantity | Diver A | Diver B |
| --- | --- | --- |
| Total cylinder water volume | 20 L | 24 L |
| Starting inventory | 20 × 240 = 4,800 reference L | 24 × 240 = 5,760 reference L |
| Nominal one-third entry allowance | 1,600 reference L | 1,920 reference L |
| Stipulated individual exit demand | 1,600 reference L | 1,920 reference L |
| Unadjusted thirds turn threshold | 160 bar | 160 bar |

### Compare both divers' demand with the smaller donor's supply

Combined exit demand is 1,600 + 1,920 = **3,520 reference L**. At an unadjusted 160 bar threshold, A would have 20 × 160 = 3,200 reference L. If B lost all gas then, A would be **320 L short** within the stated model.

To retain 3,520 reference L in A's 20 L configuration:

- Maximum entry use for A: 4,800 − 3,520 = 1,280 reference L.
- Corresponding pressure drop: 1,280 ÷ 20 = 64 bar.
- Adjusted threshold for A: 240 − 64 = **176 bar**.

### Check the reverse failure

B keeps the ordinary thirds threshold of **160 bar** in this example. At that pressure, B retains 24 × 160 = 3,840 reference L. If A lost all gas, that exceeds the stipulated combined demand of 3,520 L by 320 L. A, at 176 bar, retains exactly the stipulated combined demand, with **no additional gas margin within this model**.

The team turns when A reaches 176 bar, B reaches 160 bar, or another applicable limit requires it, whichever happens first. The calculation does not assume that both pressure thresholds occur at the same time. In operational planning, pressure thresholds also need a conservative allowance for reading uncertainty and rounding; never round a donor's required retained pressure downward.

### What this example does not establish

The entry allowance changes, while the stipulated exit-demand bounds remain fixed. This is a limited allocation calculation, not a method for predicting penetration distance or optimizing a turn time. Recalculate actual exit demand for the proposed route and failure; do not infer it from a fraction of starting gas. Unequal breathing rates, stress, delay, current, depth changes, decompression, unusable residual gas and delivery limitations can require more gas or an earlier turn. Applicable training restrictions still govern. Passing these two supply checks does not establish a safe real-world reserve.

See the [separate arithmetic review](../../reviews/2026-11-04-clarity-and-gas.md) for recomputation.


## Check understanding

Why does A need a higher pressure threshold than B in the allocation example? Identify two real-world inputs that its fixed demand bounds do not establish.

## Learning objective
Separate inventory allocation, expected consumption and gas accessible after failure.

## Follow the planning chain
First establish cylinder volumes and actual starting pressures. Next express consumption in comparable units. Describe the return route and the failure being considered, including who supplies whom. Determine what gas remains accessible in that configuration. Compare that supply with the combined exit demand and applicable restrictions.

A reduced entry allowance does not itself prove that an assumed exit demand is realistic. Gas remaining somewhere in the system is not necessarily gas the donor can deliver. A delayed return can change time, effort and depth exposure together.

## Contrast one changed assumption
Keep cylinder inventory unchanged but increase the stipulated exit delay. Required exit gas increases; physical inventory does not. Keep the delay unchanged but make part of the donor's gas inaccessible. Available supply decreases; the original demand does not disappear. State which side of the comparison changed before recalculating.
