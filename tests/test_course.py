"""Course routing checks; not a validation of diving knowledge."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CourseRouting(unittest.TestCase):
    def test_every_question_has_one_course_role_and_links_match_order(self):
        manifest = json.loads((ROOT / 'curriculum-manifest.json').read_text())
        entries = {entry['question_id']: entry for entry in manifest['entries']}
        course = manifest['course']
        path = ROOT / course['path']
        text = path.read_text()
        self.assertRegex(text, rf'(?m)^id: {re.escape(course["id"])}$')
        assigned = []
        module_ids = []
        for index, module in enumerate(course['modules'], 1):
            module_ids.append(module['id'])
            self.assertTrue(module['question_ids'])
            heading = f"## Module {index}: {module['title']}\n"
            self.assertIn(heading, text)
            section = text.split(heading, 1)[1].split('\n## ', 1)[0]
            for key, label in [('question_ids', 'Core sequence'),
                               ('practice_question_ids', 'Optional practice')]:
                ids = module[key]
                assigned.extend(ids)
                line = re.search(rf'^{label}: (.+)$', section, re.M).group(1)
                linked_ids = re.findall(r'\[([A-Z]+-Q\d+)\]', line)
                self.assertEqual(linked_ids, ids)
                for question_id in ids:
                    entry = entries[question_id]
                    self.assertIn(f"../{entry['question_path']}", line)
                    question = (ROOT / entry['question_path']).read_text()
                    for knowledge_id in re.findall(r'^  - ([A-Z]+-\d+)$', question, re.M):
                        self.assertIn(f'[{knowledge_id}]', section)
        self.assertEqual(len(module_ids), len(set(module_ids)))
        assigned.extend(course['appendix_question_ids'])
        self.assertEqual(len(assigned), len(set(assigned)))
        self.assertEqual(set(assigned), set(entries))
        self.assertEqual(course['appendix_question_ids'], ['AI-Q001'])


if __name__ == '__main__':
    unittest.main()
