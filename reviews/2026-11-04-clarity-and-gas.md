---
id: REVIEW-CLARITY-GAS-20261104
title: Navigation, time limits and gas calculation review
status: draft
version: 0.1.0
---

# Navigation, time limits and gas calculation review

## Changes

- NAV-Q001 explicitly places the unlined space inside the overhead environment.
- PLN-001 and PLN-Q003 distinguish a turnaround deadline from maximum total dive time, with time for exit and contingencies.
- GAS-001 separates cylinder capacity, gas used, reference-volume rate and surface normalization. It states the limits of averaging a variable profile.
- GAS-002 adds an original unequal-volume allocation exercise with explicit fixed demand assumptions and both donor failure checks. GAS-Q002 tests retained pressure versus pressure drop.
- DEC-001 and DEC-Q001 use titles that distinguish decompression guidance from individual safety.
- The revised navigation, time-limit and gas questions use alternatives based on specific reasoning errors. IDs and answer keys remain stable; the bank still contains 42 draft questions.

## Arithmetic recomputation

The allocation exercise uses two 10 L cylinders and two 12 L cylinders, both starting at 240 bar. Quantities are idealized at a 1 bar reference and comparable temperature.

| Check | Result |
| --- | --- |
| Starting inventories | 4,800 L and 5,760 L |
| Assumed individual exit demands | 1,600 L and 1,920 L |
| Combined exit demand | 3,520 L |
| Smaller donor at ordinary 160 bar turn | 3,200 L; short by 320 L |
| Smaller donor's entry allowance | 1,280 L, or 64 bar |
| Smaller donor's adjusted retained pressure | 176 bar; exactly 3,520 L |
| Larger donor at ordinary 160 bar turn | 3,840 L; 320 L above assumed combined demand |

`tests/test_allocation_calculations.py` recomputes the allocation with exact fractions and a separate per-cylinder decimal calculation. It checks both donor cases, the lack of additional margin for the smaller donor, and that a lower retained pressure fails the stated requirement. A separate segmented example checks pressure-time normalization and demonstrates its limitation when breathing rate also varies.

The fixed exit demands are assumptions supplied to the exercise. They are not inferred from a measured exit, and adjusting the entry allowance does not validate them. No route distance, actual reserve or operational planning tool is established.

## Public factual checks

Checked on 2026-11-04:

- [DAN, Dive Safety: It's No Accident](https://dan.org/alert-diver/article/dive-safety-its-no-accident/) supports fractional gas allocation, agreed return points and more conservative responses to conditions. It does not validate this exercise's fixed demands or thresholds.
- [DAN, Effective Use of Your Dive Computer](https://dan.org/health-medicine/health-resource/dive-medical-reference-books/decompression-sickness/use-of-dive-computers/) distinguishes model guidance from individual physiology and notes that displayed limits do not guarantee outcomes. Existing source IDs and the [evidence register](2026-11-03-evidence.md) remain applicable.
- Time terminology and question wording are editorial clarifications. Numerical statements are algebra under stated assumptions, not an external certification standard.

## Validation and review limits

Command: `python -m unittest discover -s tests -v`.

Result: 16 tests passed locally on 2026-11-04. `git diff --check` also passed. These results do not assert that GitHub Actions or independent expert review has run.

All learning content remains draft. Independent competent review must examine the fixed-demand assumptions, donor access, margins, pressure interpretation, wording and applicability before any status promotion. Automated checks establish numerical and structural consistency only.
