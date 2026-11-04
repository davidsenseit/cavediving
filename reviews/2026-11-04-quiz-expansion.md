---
id: REVIEW-QUIZ-20261104
title: Applied scenario question review
status: draft
version: 0.1.0
---

# Applied scenario question review — 2026-11-04

## Scope

Adds 24 scenario questions to the existing 18-question bank, linked to existing knowledge entries. No new qualification standard, emergency execution procedure, medical protocol or site condition is asserted. All 42 questions and all 18 knowledge entries remain draft; independent expert review is pending.

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

## Factual checks

The following public references were opened on 2026-11-04 as factual cross-checks. They do not constitute review or approval of these questions. Existing knowledge references and their outstanding limits remain in the [evidence register](2026-11-03-evidence.md).

| Reference | Claim checked | Limits |
| --- | --- | --- |
| [DAN, Cavern and Cave Diving](https://dan.org/alert-diver/article/cavern-and-cave-diving/) | Overhead training, sediment-sensitive movement and return against inward flow | Does not establish current conditions or individual competence |
| [DAN, Low-Visibility Diving](https://world.dan.org/alert-diver/article/low-visibility-diving/) | Visibility can deteriorate; cave lighting and physical navigation reference matter | Does not validate a particular equipment configuration or response |
| [DAN, Breathing Gases](https://dan.org/alert-diver/article/breathing-gases/) | Partial pressure uses absolute pressure; gas analysis and identification matter | No exposure limit or gas selection is inferred from arithmetic |
| [TDI, We Are Outta Here](https://www.tdisdi.com/tdi-diver-news/we-are-outta-here/) | Dive termination is available without pressure to continue | Does not supply exit execution steps |
| [Natalie Gibb, Zen and the Art of Mexican Cave Navigation](https://indepthmag.com/zen-and-the-art-of-mexican-cave-navigation/) | Nondirectional cookies, team context and distinction between indicated exits and the team's exit | First-person regional instructor account; not a universal protocol |

Equipment access, combined failures, workload, permission scope and limits of recorded data are applications of the linked knowledge and explicitly framed scenario reasoning. They still require competent reviewer challenge. Navigation scenarios avoid assigning universal placement conventions or teaching recovery maneuvers.

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

Before status promotion, an independent competent reviewer must examine ambiguity, distractor plausibility, factual scope, configuration assumptions and safety implications. The pathway supplements the existing curriculum; it is not a complete training syllabus.
