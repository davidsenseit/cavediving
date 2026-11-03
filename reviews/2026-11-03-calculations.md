---
id: REVIEW-CALC-001
title: Educational arithmetic and model boundaries
status: draft
version: 0.2.0
---

# Educational arithmetic and model boundaries

These independently constructed classroom exercises use ideal gases, comparable temperature and a 1 bar reference. They omit real-gas corrections and do not establish usable cylinder capacity, an emergency reserve or permission to dive. Exact rational arithmetic and a separately expressed decimal calculation check the numbers, not the safety of a model.

## Exercise 1: quantity versus pressure

At the same nominal 200 bar fill, 24 L water volume represents 4,800 reference litres while 18 L represents 3,600. The 1,200 L difference illustrates why equal gauge readings cannot establish equal supplies. Valve access, residual gas and the assumed failure must be assessed separately.

## Exercise 2: breathing volume rate

For 18 L water volume, 50 bar consumed over 15 minutes at a constant 3 bar absolute:

- Reference quantity consumed: 18 × 50 = 900 L.
- Surface-normalized rate: 900 / (15 × 3) = 20 L/min.
- Without depth normalization, the result would be 60 L/min.
- Halving cylinder water volume while keeping the other inputs fixed halves the inferred rate to 10 L/min.

Only the constant-depth exercise is evaluated here. A variable profile requires pressure-time normalization, and an observed average rate cannot be assumed to represent emergency breathing demand.

## Exercise 3: a stipulated failure model

The model supplies 2,600 accessible reference litres and demands 2,750. The shortage is 150 L. Supply divided by demand is 52/55, approximately 0.94545; this ratio is not a safety factor or a reserve recommendation.

Both quantities are stipulated, not field measurements. The exercise does not derive a turn pressure. A different turn time normally changes exit demand, so holding demand fixed while changing the turn cannot establish a general gas-matching method.

## Exercise 4: fractional allocation

For an educational 240 bar start with matched cylinder volumes, one third corresponds to 80 bar and the remaining two thirds to 160 bar. These quantities illustrate an allocation only. They do not assess different breathing rates, unavailable gas, delays, current, exertion or decompression. More restrictive limits can require turning earlier.

## Exercise 5: oxygen partial pressure

With a fraction of 0.32 and 4 bar absolute ambient pressure, oxygen partial pressure is 1.28 bar. Gas fraction is not entered as 32, and storage pressure is not ambient pressure. This multiplication does not select a breathing gas or exposure limit.

## Validation boundary

Run `python -m unittest discover -s tests -v`. Checks include exact/decimal recomputation, cylinder-size effects, invalid inputs and partial pressure. Independent expert review remains pending. There is no operational planner, range predictor, reserve optimizer or decompression engine in this change.
