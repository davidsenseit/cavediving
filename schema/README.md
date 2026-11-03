# Lightweight Markdown metadata

Use YAML front matter at the top of each learning file. Required keys:

- `id`: stable unique identifier, e.g. `NAV-001` or `NAV-Q001`.
- `title`: human-readable English title.
- `type`: `knowledge`, `question`, or `learning_path`.
- `topic`: lowercase topic tag.
- `status`: `draft`, `in_review`, or `verified`.
- `version`: semantic version, e.g. `0.1.0`.

Recommended keys:
- `knowledge_ids`: YAML list of IDs this question/path tests or teaches.
- `reviewed_by`: reviewer names or GitHub identities (only with consent).
- `reviewed_at`: ISO date, if actually reviewed.
- `review_notes`: short summary of verification, if applicable.

A `verified` label requires a recorded independent technical review; metadata alone must never be used as evidence of review. All IDs must remain stable when content is reworded. Use ordinary Markdown prose below the front matter so both humans and AI agents can read it without special software.

## Question format
Under each question's metadata use:
- `## Question`
- `## Choices` (A–D or another unambiguous set)
- `## Answer and explanation`
- `## Common misconceptions` (optional)

The AI must withhold the answer section until the learner responds. Keep generated practice questions separate from authored/verified questions.
