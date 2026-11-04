# Lightweight Markdown metadata

Use YAML front matter at the top of each learning file. Required keys:

- `id`: stable unique identifier, e.g. `NAV-001` or `NAV-Q001`.
- `title`: human-readable English title.
- `type`: `knowledge`, `question`, or `learning_path`.
- `topic`: lowercase topic tag.
- `status`: `draft` or `verified`.
- `version`: semantic version, e.g. `0.1.0`.

Recommended keys:
- `knowledge_ids`: YAML list of IDs this question/path tests or teaches.

All IDs must remain stable when content is reworded. Use ordinary Markdown prose below the front matter so both humans and AI agents can read it without special software.

## Question format
For multiple-choice questions, under the metadata use:
- `## Question`
- `## Choices` (A–D or another unambiguous set)
- `## Answer and explanation`
- `## Common misconceptions` (optional)

The AI must withhold the answer section until the learner responds. Keep generated practice questions separate from authored/verified questions.

## Question authoring

Revised questions include Teaching notes (objective, level and prerequisites), followed by the existing Question, Choices and Answer and explanation sections. Follow-up discussion contains a short reasoning prompt; its Tutor guidance states the conceptual evidence to look for. Present these sections according to AGENTS.md.

Use a specific learning objective and enough information for one defensible answer. Alternatives should address the same decision or quantity and represent identifiable misconceptions. Keep their detail comparable. Use neutral titles and different numerical inputs in worked lessons and assessment questions. An applied question should require a distinct reasoning step rather than repeat an earlier question with changed scenery.

Explain each alternative after the response, and make scenario limits specific. Retain stable IDs and draft status when revising unverified material. Course metadata does not establish practical competence.

## Course sequencing

`curriculum-manifest.json` records `course.id`, `course.path`, ordered `course.modules` with `question_ids` and `practice_question_ids`, and `appendix_question_ids`. The module order and each core list define default progression; practice belongs to its module. Every authored question has exactly one course role. Keep `learning/core-pathway.md` in sync with these lists and preserve stable question IDs.


## Open calculation questions

Set `response_type: calculation` for authored numerical responses without choices. Use `## Question`, `## Response format`, `## Answer and explanation`, `## Follow-up discussion` and `## Tutor guidance`. The answer contains complete worked reasoning and units. Keep the answer and guidance hidden until the learner attempts the question. Questions without this field retain the existing multiple-choice format.

Gas question cases in `exercises/gas-question-index.json` bind IDs and paths to independently checked arithmetic expectations. Lesson examples are checked through `exercises/gas-lesson-cases.json`. These are educational test fixtures, not operational tools.

A module may include `learning_path` and ordered `stages` with `knowledge_ids` and `question_ids`. These stages group existing core questions, not additional course roles. The ordered stage questions must form the beginning of that module's core sequence.
