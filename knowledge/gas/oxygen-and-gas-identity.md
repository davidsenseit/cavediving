---
id: GAS-003
title: Gas percentage is not partial pressure
type: knowledge
topic: gas
status: draft
version: 0.2.0
---

# Gas percentage is not partial pressure

## Core idea

For a gas fraction F and absolute ambient pressure P, its partial pressure is F × P. The same oxygen percentage gives a different oxygen partial pressure at a different depth. Identify and analyze breathing gas, label it and check it against the intended exposure and training. An arithmetic result alone does not select a suitable mix or exposure limit.

## Original example

In a classroom model, 0.32 × 4 bar absolute = 1.28 bar oxygen partial pressure. No working-depth or exposure approval follows from that multiplication.

## Check the pressure input

Absolute ambient pressure includes surface pressure. If the exercise already supplies absolute pressure, use that value directly. Subtracting surface pressure before multiplying by the oxygen fraction underestimates the partial pressure.

A fraction is dimensionless; partial pressure has pressure units. For a fixed fraction, increasing absolute pressure increases partial pressure proportionally. Checking these units and relationships helps detect a mistaken calculation before discussing exposure limits.

## Check understanding

What is wrong with subtracting surface pressure from an input already stated as absolute?
