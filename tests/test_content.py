"""Repository contract checks; not factual or expert verification."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def metadata(path):
    text = path.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise AssertionError(f'Missing front matter: {path}')
    # Checks this repository's simple scalar/list subset without a YAML dependency.
    head = match.group(1)
    fields = dict(re.findall(r'^([a-z_]+): (.+)$', head, re.M))
    links = re.search(r'^knowledge_ids:\n((?:  - [^\n]+\n?)*)', head, re.M)
    fields['knowledge_ids'] = re.findall(r'  - (\S+)', links.group(1)) if links else []
    return fields


class ContentChecks(unittest.TestCase):
    def files(self):
        return sorted(p for folder in ('knowledge', 'questions', 'learning')
                      for p in (ROOT / folder).rglob('*.md'))

    def test_schema_unique_ids_and_drafts(self):
        seen = set()
        for path in self.files():
            m = metadata(path)
            for key in ('id', 'title', 'type', 'topic', 'status', 'version'):
                self.assertIn(key, m, str(path))
            self.assertNotIn(m['id'], seen)
            seen.add(m['id'])
            self.assertEqual(m['status'], 'draft', str(path))
            self.assertRegex(m['version'], r'^\d+\.\d+\.\d+$')
            expected = {'knowledge': 'knowledge', 'questions': 'question', 'learning': 'learning_path'}
            self.assertEqual(m['type'], expected[path.relative_to(ROOT).parts[0]])

    def test_question_and_path_references(self):
        known = {metadata(p)['id'] for p in (ROOT / 'knowledge').rglob('*.md')}
        for folder in ('questions', 'learning'):
            for path in (ROOT / folder).rglob('*.md'):
                ids = metadata(path)['knowledge_ids']
                self.assertTrue(ids, str(path))
                self.assertTrue(set(ids) <= known, str(path))
        for path in (ROOT / 'questions').rglob('*.md'):
            text = path.read_text()
            for heading in ('## Question', '## Choices', '## Answer and explanation'):
                self.assertIn(heading, text)
            choices = re.findall(r'^([A-D])\. ', text, re.M)
            self.assertEqual(choices, list('ABCD'), str(path))
            answer = re.search(r'## Answer and explanation\n\n\*\*([A-D])\.', text)
            self.assertIsNotNone(answer, str(path))

    def test_local_links(self):
        for path in ROOT.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((path.parent / target.split('#')[0]).exists(), f'{path}: {target}')

    def test_manifest_and_package_coverage(self):
        manifest = json.loads((ROOT / 'curriculum-manifest.json').read_text())
        self.assertEqual(manifest['status'], 'draft')
        self.assertEqual({e['issue'] for e in manifest['entries']}, set(range(2, 11)))
        indexed = [e['question_path'] for e in manifest['entries']]
        actual = {str(p.relative_to(ROOT)) for p in (ROOT / 'questions').rglob('*.md')}
        self.assertEqual(len(indexed), len(set(indexed)), 'Duplicate manifest question')
        self.assertEqual(set(indexed), actual, 'Manifest must index every question')
        for e in manifest['entries']:
            for kind in ('knowledge', 'question'):
                path = ROOT / e[f'{kind}_path']
                self.assertEqual(metadata(path)['id'], e[f'{kind}_id'])
                self.assertIn(e[f'{kind}_path'], (ROOT / 'catalog.md').read_text())

    def test_source_ids_resolve(self):
        evidence = (ROOT / 'reviews/2026-11-03-evidence.md').read_text()
        for path in (ROOT / 'knowledge').rglob('*.md'):
            head = path.read_text().split('---')[1]
            source_block = re.search(r'source_ids:\n((?:  - [^\n]+\n?)*)', head)
            if source_block:
                for sid in re.findall(r'  - (\S+)', source_block.group(1)):
                    self.assertIn(f'| {sid} |', evidence, str(path))


if __name__ == '__main__':
    unittest.main()
