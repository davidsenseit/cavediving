---
id: GAS-001
title: Use absolute pressure and explicit units
type: knowledge
topic: gas
status: draft
version: 0.3.0
source_ids:
  - DAN-GAS
  - DAN-DEMAND
  - ALGEBRA
---

# Use absolute pressure and explicit units

## Core idea

Pressure tells you how compressed the gas is; cylinder size tells you how much space contains it. Use both when estimating a gas quantity.

**Cylinder water volume** means the internal capacity of the cylinder, not the volume of compressed gas expressed at the surface. Two 12 L cylinders have 24 L total water volume. Count both only when the measured pressure drop applies to both; independently used cylinders may need separate calculations.

In these classroom calculations, a **reference litre** is a gas quantity expressed at 1 bar. Assume ideal gas and comparable temperature throughout.

## Start with a constant-depth example

Use three steps:

1. **Gas quantity used:** total cylinder water volume in L × pressure drop in bar ÷ reference pressure of 1 bar.
2. **Reference-volume rate during the dive:** divide that quantity by elapsed minutes.
3. **Surface-normalized breathing rate:** divide that rate by the ratio of absolute ambient pressure to the 1 bar reference pressure.

Absolute ambient pressure includes surface pressure. It is not the pressure shown on the cylinder gauge. A pressure loss in **bar/min** depends on cylinder size; a normalized volume rate in **L/min** allows comparison between configurations under the stated assumptions.

## Original example

For 18 L total water volume, 50 bar used in 15 min at a constant 3 bar absolute:

- Gas quantity used: 18 × 50 ÷ 1 = 900 reference L.
- Reference-volume rate during the dive: 900 ÷ 15 = 60 L/min.
- Pressure ratio: 3 bar absolute ÷ 1 bar = 3.
- Surface-normalized breathing rate: 60 ÷ 3 = 20 L/min.

The same record shows 50 ÷ 15, or about 3.33 bar/min. That is a cylinder pressure-loss rate, not the normalized 20 L/min volume rate. Neither rate establishes future emergency demand.

## When depth changes

The constant-pressure shortcut needs care when pressure varies. With approximately constant surface-normalized breathing demand, divide total reference gas used by the sum of time × absolute-pressure ratio for each part of the dive. A time-weighted mean pressure gives the same result under that assumption; a simple average of maximum and minimum depth does not generally do so.

If breathing demand also changes, this calculation gives a pressure-weighted estimate rather than necessarily the diver's time-average surface-normalized rate. Gas used for buoyancy or other purposes also affects an estimate made from cylinder pressure loss. Use appropriate segment data and state what the record includes.

## Limits and review

Draft learning material; source checking is not expert approval. This entry is not a field procedure or a dive authorization. See [evidence and open questions](../../reviews/2026-11-03-evidence.md).

## Check understanding

Explain the assumption most likely to make the example unsafe if ignored.


