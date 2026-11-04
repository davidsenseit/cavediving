"""Editorial contract checks, not validation of diving procedures."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TerminologyChecks(unittest.TestCase):
    def test_glossary_entries_have_reviewable_definitions(self):
        text = (ROOT / 'GLOSSARY.md').read_text()
        self.assertIn('status: draft', text)
        sections = dict(re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', text, re.M | re.S))
        required = {'guideline', 'main line', 'primary reel', 'jump', 'gap',
                    'T-junction', 'line marker', 'directional arrow', 'cookie', 'REM'}
        self.assertTrue(required <= sections.keys())
        for term in required:
            with self.subTest(term=term):
                for field in ('Definition', 'Function and context', 'Distinctions',
                              'Usage variations', 'Review status'):
                    self.assertRegex(sections[term], rf'\*\*{field}:\*\* \S')
                self.assertIn('**Review status:** Draft.', sections[term])

    def test_authored_content_uses_canonical_spellings(self):
        # Deliberately limited to unambiguous aliases; ordinary words like
        # line, marker and junction must remain available for broader concepts.
        aliases = r'\b(?:mainline|guide line|line arrows?|T intersection|T junction)\b'
        for folder in ('knowledge', 'questions', 'learning'):
            for path in (ROOT / folder).rglob('*.md'):
                self.assertIsNone(re.search(aliases, path.read_text(), re.I), str(path))

    def test_glossary_internal_anchors_resolve(self):
        text = (ROOT / 'GLOSSARY.md').read_text()
        anchors = {re.sub(r'[^\w -]', '', h.lower()).replace(' ', '-')
                   for h in re.findall(r'^## (.+)$', text, re.M)}
        for path in ROOT.rglob('*.md'):
            for anchor in re.findall(r'\]\([^)]*GLOSSARY\.md#([^)]*)\)', path.read_text()):
                self.assertIn(anchor, anchors, str(path))


if __name__ == '__main__':
    unittest.main()
