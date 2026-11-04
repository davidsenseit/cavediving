---
id: REVIEW-QUIZ-20261104
title: Applied scenario question review
status: draft
version: 0.1.0
---

# Applied scenario question review — 2026-11-04

## Scope

Adds 24 scenario questions to the existing 18-question bank, linked to existing knowledge entries. No new qualification standard, emergency execution procedure, medical protocol or site condition is asserted. All 42 questions and all 18 knowledge entries remain draft.

| Topic | Added IDs | Count |
| --- | --- | --- |
| Gas | GAS-Q004–GAS-Q009 | 6 |
| Navigation | NAV-Q004–NAV-Q008 | 5 |
| Equipment | EQP-Q003–EQP-Q006 | 4 |
| Planning | PLN-Q003–PLN-Q005 | 3 |
| Emergencies | EMR-Q002–EMR-Q003 | 2 |
| Foundations | FND-Q003–FND-Q004 | 2 |
| Environment | ENV-Q003 | 1 |
| Resources | RES-Q002 | 1 |

Each question has four choices, one keyed answer, a concept explanation, and reasons for rejecting the alternatives. The catalog, manifest and applied pathway include the additions. The manifest also indexes the existing NAV-Q001 scaffold so every question is represented.


## Separate numerical checks

All volume calculations use an educational ideal-gas approximation at comparable temperature and a fixed 1 bar reference. Rates use constant stated absolute pressure. Accessible gas and actual emergency demand require a separate real-world assessment.

| Question | Recomputed result | Independent expression |
| --- | --- | --- |
| GAS-Q004 | 8 L/min; 12 L/min | Water volumes × 1 bar/min ÷ pressure ratio 2; separately multiply by 0.5 |
| GAS-Q005 | 3,680 L; 4,080 L | Total water volume × pressure; separately sum two 8 L or two 12 L cylinder inventories |
| GAS-Q006 | 1,980 L | Combined rate × pressure ratio × 15 min; separately sum 1,452 L exit and 528 L delay |
| GAS-Q008 | 0.90 bar; 1.20 bar | Oxygen fraction × absolute pressure; separately percentage multiplication and division |

Exact rational and separate decimal expressions are in `tests/test_scenario_calculations.py`. These checks address arithmetic consistency only. They do not validate any reserve strategy, turn pressure or operational plan.

## Validation and remaining review

Run `python -m unittest discover -s tests -v`. Structural checks cover unique IDs, draft metadata, knowledge references, local links, question layout and complete manifest coverage. Numerical checks recompute the four new quantitative scenarios. Passing tests do not prove factual accuracy or practical competence.

