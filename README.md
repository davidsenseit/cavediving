# Cave Diving Knowledge Base

An AI-agnostic, English-language learning resource for cave diving. Use it with an AI assistant that can read this repository: ChatGPT, Claude, Codex, local agents, or other compatible tools.

**Status: first curriculum draft.** There are 30 knowledge entries and 64 original questions, including the original scaffold and 24 applied scenarios. All learning content remains draft. This repository does not certify divers, replace supervised training, or provide an authoritative dive plan.

## Start here

1. Give your AI assistant access to the repository files (a URL alone does not guarantee access).
2. Ask it to read [AGENTS.md](AGENTS.md) and [catalog.md](catalog.md).
3. Start the [course](learning/core-pathway.md): "Start the cave-diving course, one question at a time. Teach the concepts and explain after I answer."
4. Continue from the last completed question in the current conversation, or choose a topic from the [catalog](catalog.md).

The course has eight modules with 43 core questions and 20 optional practice questions. Ten revised questions are integrated into this order, with focused lessons, detailed feedback and reasoning prompts. The remaining question addresses AI-provider evaluation in a separate project appendix. All 64 authored questions remain available.

## Gas calculations

Module 4 contains an [eight-stage calculation block](learning/gas-calculations.md): cylinder capacity, bar/litre conversions, sixths and thirds, turn pressures, equal configurations, different starting pressures, different capacities and combined differences. Each stage includes worked and guided examples followed by independent calculations. There are 18 new open-response questions including two cumulative cases. Plan enough sessions to explain and practise each prerequisite.

## Terminology

Follow the language-independent [glossary](GLOSSARY.md): keep canonical English cave-diving terms even when explanations are in Swedish or another language. Introduce unfamiliar concepts before assessment. Contributors must follow the [terminology guidance](governance/CONTRIBUTING.md#terminology).

## Structure

- `AGENTS.md` — vendor-neutral behavior contract for assistants.
- `catalog.md` — index of topics, lessons and quizzes.
- `knowledge/` — short, standalone facts and concepts with stable IDs.
- `questions/` — authored quiz questions linked to knowledge IDs.
- `learning/` — guided topic pathways; users may also pick a topic freely.
- `schema/` — metadata conventions for Markdown front matter.
- `governance/` — safety and original-content policy.

All published learning content is in English. AI assistants may converse in the learner's preferred language.

## Validation and review

Read the [coverage and gaps](reviews/2026-11-03-coverage.md), [separate calculation review](reviews/2026-11-03-calculations.md) and [portability test protocol](reviews/interoperability-protocol.md). Follow the [core pathway](learning/core-pathway.md) or select a topic in the catalog.

Run `python -m unittest discover -s tests -v` with Python 3.10 or newer; there are no third-party runtime dependencies. These checks establish structure and educational arithmetic only, not factual accuracy, practical competence or operational validation. Calculation examples use an explicit 1 bar reference and ideal-gas assumptions.

Use the [practice index](learning/applied-scenarios.md) to revisit questions by topic within the same course. See its [review record](reviews/2026-11-04-quiz-expansion.md).

## Roadmap

Expand independently authored, technically reviewed modules covering gas management, navigation, equipment, emergencies, and dive planning. Add deterministic calculation tools with executable test cases. Separate educational scenarios from real dive decisions.

## License note

The repository includes an MIT license. That license covers material the contributors are entitled to license; it does not grant rights in third-party manuals, exams, figures or other protected works. Do not commit such materials without permission.



