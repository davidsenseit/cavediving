# Gas calculation learning block

Status: draft.

## Scope

Eight new lessons, GAS-004 through GAS-011, develop cylinder water volume, gauge pressure, reference litres, inverse conversions, sixths and thirds, turn thresholds and four matching cases. Each lesson has an objective, prerequisites, explanation, worked example, guided calculation and delayed guided answer.

Eighteen open calculation questions, GAS-Q010 through GAS-Q027, provide two independent attempts per stage and two cumulative cases. Answers include working, units and reasoning follow-ups. The questions appear once in Module 4, before the existing consumption, demand, delay and oxygen questions. The course retains eight modules and now has 43 core questions, 20 optional questions and one project appendix. There are 30 knowledge entries and 64 questions overall.

## Calculation scope

All inventory arithmetic uses the stated ideal-gas, comparable-temperature approximation at a 1 bar reference. Gauge-based quantities are explained as approximate gas released toward zero gauge pressure, with deliverability limits kept separate.

The equal-capacity, different-start comparison uses an entry allowance based on the lower starting inventory and explicitly supplied equal exit-demand bounds. The different-capacity lessons use fixed individual exit-demand bounds equal to each starting third. These assumptions are stated separately; neither model supplies an actual route-dependent demand estimate. Both donor directions and the stricter retained threshold are checked. Required retained pressures round upward; allowable entry drops round downward. The block includes shortages and zero-entry boundaries.

## Validation

28 automated tests pass. Exact-fraction calculations independently recompute 18 authored question cases and 17 worked/guided lesson cases. The checked key results are also bound to the published lesson and answer text. Further checks cover rounding, inventory balance, both donor directions, inaccessible supply, insufficient inventory and zero allowance. Routing checks confirm the gas stages form a single core-sequence prefix and all authored question paths resolve.

Automated arithmetic and structural checks do not verify practical planning methods, actual exit demand, training privileges or usable gas after a real failure. New content remains draft for substantive review.
