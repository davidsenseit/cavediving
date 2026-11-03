---
id: REVIEW-CALC-001
title: Separate arithmetic review
status: draft
version: 0.1.0
---

# Separate arithmetic review

Educational ideal-gas calculations only. Not an operational planning utility, validated turn-pressure prescription or independently approved gas strategy. An AI author checked the arithmetic with two numerical representations; no independent human has approved the assumptions.

## Supplied gas-matching example

The attachment describes two 12 L cylinders and two 11 L cylinders, each at 210 bar. Here water volumes sum to 24 L and 22 L. The simplified calculation uses a 1 bar surface reference, comparable temperature and ideal gas behavior. It ignores real-gas corrections and inaccessible residual gas.

| Quantity | Independently recomputed result |
| --- | --- |
| Larger nominal gas quantity | 24 × 210 = 5040 surface-equivalent L |
| Smaller nominal gas quantity | 22 × 210 = 4620 surface-equivalent L |
| Larger nominal third | 1680 L |
| Smaller nominal third | 1540 L |
| Fixed assumed combined exit demand | 1680 + 1540 = 3220 L |
| Smaller supply after its nominal third | 3080 L |
| Shortfall under this demand assumption | 3220 − 3080 = 140 L |
| Smaller supply less fixed assumed demand | 4620 − 3220 = 1400 L |
| Pressure drop for 1400 L in 22 L | 63.636363… bar |
| Remaining pressure corresponding to 3220 L in 22 L | 146.363636… bar |

The attachment also states 700/11 = 63.3 bar, which is incorrect: it is 63.636363… bar. Its earlier 63.6 is a reasonable one-decimal approximation. Subtracting 63.3 from 210 gives 146.7, not 146.4. The displayed 146.4 is consistent with rounding the unrounded 146.363636… result, despite the conflicting intermediate value. Do not propagate the incorrect intermediate arithmetic.

## Model boundary, separate from arithmetic

3220 L is a stipulated exit demand, not a measurement. Changing the team's turn time changes consumption and normally changes the return demand too. Individual thirds cannot be assumed to occur at the same location or time. One cannot derive a universal team-matching rule from the fixed numbers alone.

A real assessment needs each diver’s consumption assumptions, accessible cylinder gas after the modeled failure, depths and travel times for the return, delays, stress/exertion allowance, gas-sharing feasibility, decompression, residual pressure requirements, flow and uncertainty. Neither total litres nor a turn pressure establishes those conditions. The reserve and route model requires independent expert review.

## Independent numerical checks

`python -m unittest discover -s tests -v` compares exact Fraction results with a separately expressed Decimal calculation and fixed expected fixtures. Additional cases cover cylinder-size effects, zero consumption, invalid/nonfinite inputs, units and partial pressure. Inputs use an explicit 1 bar reference. Tests check educational arithmetic, not fitness for a dive. There is no distance-range estimator, decompression engine, automatic reserve rule or operational planner in this change.
