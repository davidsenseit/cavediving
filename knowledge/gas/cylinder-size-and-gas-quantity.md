---
id: GAS-004
title: Cylinder size, pressure and gas quantity
type: knowledge
topic: gas
status: draft
version: 0.1.0
---

# Cylinder size, pressure and gas quantity

## Prerequisites

No calculation prerequisites. Start here before GAS-001.

## Learning objective

Identify cylinder water volume, gauge pressure and reference gas quantity without confusing their units.

## Predict first

Two cylinders both show 180 bar. One is 10 L and the other 15 L. Would equal pressure mean equal gas quantity? Explain your prediction before multiplying.

## Build the idea

Cylinder water volume describes internal capacity. Gauge pressure describes how compressed the gas is relative to the surrounding pressure. A reference gas quantity describes the amount of gas as litres at a stated reference pressure. A 12 L cylinder does not become a physically larger cylinder when filled.

Throughout this calculation block, use an ideal-gas classroom approximation at comparable temperature and a reference pressure of 1 bar. The simplified gauge-based inventory is Q = V × p / 1 bar. It estimates the gas released as gauge pressure falls toward zero, rather than the full contents at absolute cylinder pressure. It does not establish that all listed gas is deliverable in practice. Real-gas effects, temperature, residual pressure and delivery limitations need separate consideration in actual planning.

| Symbol | Meaning | Unit |
| --- | --- | --- |
| V | Cylinder water volume | L |
| p | Cylinder gauge pressure | bar |
| Q | Gas quantity expressed at 1 bar | reference L |

## Worked example

Two connected 10 L cylinders at a common 180 bar have V = 10 + 10 = 20 L. The classroom inventory is 20 × 180 = **3,600 reference L**. One 10 L cylinder at the same pressure has 1,800 reference L. Doubling water volume at unchanged pressure doubles quantity.

D12 conventionally describes two 12 L cylinders: total water volume is 24 L. It does not describe a 12 L total or a gas quantity of 24 reference L.

Independently used cylinders require their own readings. Calculate each quantity and then add: do not use one cylinder's pressure for both when pressures differ. Adding inventories does not prove both supplies remain accessible after a failure.

## Guided calculation

Two connected 9 L cylinders show a common 200 bar. Fill in: V = 9 + __ L; Q = __ × 200 = __ reference L. Explain why the pressure is not doubled.

## Guided answer — reveal after the learner attempts

V = 18 L; Q = 18 × 200 = **3,600 reference L**. Both cylinders share the stated pressure; their capacities add. Multiplying pressure by two as well would count the second cylinder twice.

## Explain before moving on

Name the two different meanings of litres in this lesson. Then use the independent questions in the gas calculation pathway.
