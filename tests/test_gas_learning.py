"""Independently recompute authored classroom arithmetic using exact fractions.

Fixtures are hand-entered expectations for lessons and answers, not outputs from
an operational planner. These tests do not validate the stipulated exit demands.
"""
import json
import re
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def ceil_step(value, step):
    scaled = F(value) / step
    return (-(-scaled.numerator // scaled.denominator)) * step


def floor_step(value, step):
    return (F(value) // step) * step


def recompute(kind, x):
    if kind == 'inventory':
        quantities = [F(v) * p for v, p in zip(x['volumes'], x['pressures'])]
        return dict(water_volume=sum(x['volumes']), individual_quantities=quantities,
                    quantity=sum(quantities))
    if kind == 'consumption':
        v, start, current = map(F, (x['volume'], x['start'], x['current']))
        return dict(drop=start-current, used=v*(start-current), remaining=v*current, starting=v*start)
    if kind == 'inverse':
        drops = [F(x['quantity'], v) for v in x['volumes']]
        return dict(drops=drops, readings=[x['start']-d for d in drops])
    if kind == 'fraction':
        p = F(x['start'], x['denominator'])
        return dict(starting=x['volume']*x['start'], entry_pressure=p,
                    entry_quantity=p*x['volume'], turn_pressure=x['start']-p,
                    retained=(x['start']-p)*x['volume'])
    if kind == 'fractions':
        rows = [recompute('fraction', dict(volume=x['volume'], start=x['start'], denominator=d))
                for d in x['denominators']]
        return dict(starting=x['volume']*x['start'],
                    entry_pressures=[r['entry_pressure'] for r in rows],
                    entry_quantities=[r['entry_quantity'] for r in rows],
                    turn_pressures=[r['turn_pressure'] for r in rows],
                    retained=[r['retained'] for r in rows])
    if kind == 'allowance_round':
        drop = floor_step(F(x['start'], x['denominator']), x['entry_step'])
        turn = x['start'] - drop
        threshold = ceil_step(turn, x['retained_step'])
        return dict(allowance_pressure=drop, intermediate_turn=turn, threshold=threshold,
                    entry_pressure=x['start']-threshold)
    if kind in ('retention', 'revised_demand'):
        threshold = ceil_step(F(x['required'], x['volume']), x.get('step', 1))
        inventory = x['volume'] * x['start']
        out = dict(starting=inventory, threshold=threshold,
                   shortage=max(0, x['required']-x.get('old_retained', inventory)),
                   feasible=threshold < x['start'])
        if threshold <= x['start']:
            out.update(entry_pressure=x['start']-threshold,
                       entry_quantity=(x['start']-threshold)*x['volume'],
                       retained=threshold*x['volume'], surplus=threshold*x['volume']-x['required'])
        return out
    if kind == 'common_matching':
        drop = floor_step(F(min(x['starts']), 3), x['entry_step'])
        thresholds = [p-drop for p in x['starts']]
        retained = [p*x['volume'] for p in thresholds]
        demand = 2*drop*x['volume']
        return dict(allowance_pressure=drop, allowance_quantity=drop*x['volume'],
                    thresholds=thresholds, combined=demand, retained=retained,
                    surpluses=[q-demand for q in retained])
    if kind == 'fixed_matching':
        inventories = [F(v)*p for v, p in zip(x['volumes'], x['starts'])]
        demands = [q/3 for q in inventories]
        total = sum(demands)
        ordinary = [F(p)*2/3 for p in x['starts']]
        thresholds = [ceil_step(max(p, total/v), x['step'])
                      for p, v in zip(ordinary, x['volumes'])]
        retained = [p*v for p, v in zip(thresholds, x['volumes'])]
        out = dict(inventories=inventories, demands=demands, combined=total,
                   initial_retained=[q*2/3 for q in inventories],
                   initial_shortages=[max(0, total-q*2/3) for q in inventories],
                   thresholds=thresholds, retained=retained,
                   surpluses=[q-total for q in retained],
                   shortages=[max(0, total-q) for q in inventories],
                   feasible=all(t<p for t, p in zip(thresholds, x['starts'])))
        if all(t<=p for t, p in zip(thresholds, x['starts'])):
            drops = [p-t for p, t in zip(x['starts'], thresholds)]
            out.update(entry_pressures=drops,
                       entry_quantities=[v*d for v, d in zip(x['volumes'], drops)])
        return out
    raise AssertionError('Unrecognised case: '+kind)


class GasLearningArithmetic(unittest.TestCase):
    def test_all_authored_questions_against_exact_arithmetic(self):
        cases = json.loads((ROOT/'exercises/gas-question-index.json').read_text())
        self.assertEqual(len(cases), 18)
        for case in cases:
            with self.subTest(case=case['id']):
                actual = recompute(case['kind'], case['inputs'])
                for key, expected in case['expected'].items():
                    self.assertEqual(actual[key], expected, key)

    def test_all_worked_and_guided_cases_against_exact_arithmetic(self):
        cases = json.loads((ROOT/'exercises/gas-lesson-cases.json').read_text())
        self.assertEqual(len(cases), 17)
        for case in cases:
            with self.subTest(lesson=case['lesson'], label=case['label']):
                actual = recompute(case['kind'], case['inputs'])
                for key, expected in case['expected'].items():
                    self.assertEqual(actual[key], expected, key)

    def test_checked_results_are_present_in_published_workings(self):
        # Keep fixtures tied to the learner-facing answer, so a prose typo cannot
        # leave a correct but disconnected arithmetic fixture passing unnoticed.
        cases = json.loads((ROOT/'exercises/gas-question-index.json').read_text())
        displayed = {'quantity', 'individual_quantities', 'used', 'remaining', 'starting',
                     'drops', 'readings', 'entry_pressure', 'entry_quantity', 'turn_pressure',
                     'entry_pressures', 'entry_quantities', 'turn_pressures', 'retained',
                     'inventories', 'demands', 'combined', 'allowance_pressure', 'allowance_quantity',
                     'thresholds', 'threshold', 'shortage'}
        for case in cases:
            text = (ROOT/case['path']).read_text().split('## Answer and explanation\n\n')[1].split('\n## ')[0]
            numbers = {F(token.replace(',', '')) for token in
                       re.findall(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?![\w.])', text)}
            for key, expected in case['expected'].items():
                if key not in displayed or key == 'entry_pressures':
                    continue
                if not case['expected'].get('feasible', True) and key in ('threshold', 'thresholds'):
                    continue
                values = expected if isinstance(expected, list) else [expected]
                for value in values:
                    with self.subTest(question=case['id'], field=key, value=value):
                        self.assertIn(F(value), numbers)

    def test_lesson_results_match_the_checked_cases(self):
        lessons = {l['id']:l['path'] for l in json.loads((ROOT/'exercises/gas-lesson-index.json').read_text())}
        cases = json.loads((ROOT/'exercises/gas-lesson-cases.json').read_text())
        shown = {'water_volume', 'quantity', 'drop', 'used', 'remaining', 'starting',
                 'entry_pressures', 'entry_quantities', 'turn_pressures', 'retained',
                 'allowance_pressure', 'intermediate_turn', 'threshold', 'entry_pressure',
                 'entry_quantity', 'inventories', 'demands', 'combined', 'initial_shortages',
                 'thresholds', 'allowance_quantity'}
        for case in cases:
            text = (ROOT/lessons[case['lesson']]).read_text()
            if case['label'] == 'Guided calculation':
                text = text.split('## Guided answer')[1].split('## Explain before')[0]
            else:
                text = text.split('## '+case['label'])[1].split('## ')[0]
            numbers = {F(token.replace(',', '')) for token in
                       re.findall(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?![\w.])', text)}
            for key, expected in case['expected'].items():
                if key not in shown:
                    continue
                for value in expected if isinstance(expected, list) else [expected]:
                    with self.subTest(lesson=case['lesson'], label=case['label'], field=key):
                        self.assertIn(F(value), numbers)

    def test_rounding_and_inventory_invariants(self):
        # Probe between exact thresholds as well as the authored round-number cases.
        for volume in (12, 18, 20, 24):
            for required in (2881, 3151, 3401, 3850):
                exact = F(required, volume)
                rounded = ceil_step(exact, 5)
                self.assertGreaterEqual(volume*rounded, required)
                self.assertLess(volume*(rounded-5), required)
        for starts in ([240, 210], [225, 195], [238, 212]):
            result = recompute('common_matching', dict(volume=24, starts=starts, entry_step=5))
            self.assertLessEqual(result['allowance_pressure'], F(min(starts), 3))
            self.assertTrue(all(q >= result['combined'] for q in result['retained']))

    def test_zero_allowance_and_unavailable_supply_boundaries(self):
        zero = recompute('retention', dict(volume=20, start=180, required=3600, step=1))
        self.assertEqual(zero['entry_quantity'], 0)
        self.assertFalse(zero['feasible'])  # No positive entry allowance.
        cases = json.loads((ROOT/'exercises/gas-question-index.json').read_text())
        for case in cases:
            if case['kind'] != 'fixed_matching' or not case['expected']['feasible']:
                continue
            result = recompute(case['kind'], case['inputs'])
            for inventory, used, kept in zip(result['inventories'], result['entry_quantities'], result['retained']):
                self.assertEqual(used+kept, inventory)
                self.assertGreaterEqual(kept, result['combined'])
                # An access loss greater than the numerical surplus invalidates that donor check.
                inaccessible = kept-result['combined']+1
                self.assertLess(kept-inaccessible, result['combined'])


class GasLearningRouting(unittest.TestCase):
    def test_stages_are_a_single_core_prefix_with_real_lessons(self):
        manifest = json.loads((ROOT/'curriculum-manifest.json').read_text())
        module = next(m for m in manifest['course']['modules'] if m['id']=='gas')
        questions = json.loads((ROOT/'exercises/gas-question-index.json').read_text())
        lessons = json.loads((ROOT/'exercises/gas-lesson-index.json').read_text())
        self.assertEqual([q['id'] for q in questions], [f'GAS-Q{i:03}' for i in range(10,28)])
        flattened = [qid for stage in module['stages'] for qid in stage['question_ids']]
        self.assertEqual(flattened, module['question_ids'][:18])
        self.assertEqual(len(flattened), len(set(flattened)))
        path = (ROOT/module['learning_path']).read_text()
        for lesson in lessons:
            text = (ROOT/lesson['path']).read_text()
            self.assertIn('status: draft', text)
            for heading in ('## Learning objective', '## Guided calculation',
                            '## Guided answer', '## Explain before moving on'):
                self.assertIn(heading, text, lesson['path'])
            self.assertIn(lesson['path'], path)
        for question in questions:
            text = (ROOT/question['path']).read_text()
            self.assertIn('response_type: calculation', text)
            self.assertIn('status: draft', text)
            self.assertIn('## Response format', text)
            self.assertNotIn('## Choices', text)
            self.assertTrue(text.split('## Answer and explanation\n\n')[1].split('\n## ')[0].strip())
        self.assertIn('GAS-Q026', path)
        self.assertIn('GAS-Q027', path)

    def test_case_ids_and_lesson_coverage_match_authored_files(self):
        manifest = json.loads((ROOT/'curriculum-manifest.json').read_text())
        entries = {e['question_id']:e for e in manifest['entries']}
        questions = json.loads((ROOT/'exercises/gas-question-index.json').read_text())
        for question in questions:
            self.assertEqual(question['path'], entries[question['id']]['question_path'])
        lessons = json.loads((ROOT/'exercises/gas-lesson-index.json').read_text())
        cases = json.loads((ROOT/'exercises/gas-lesson-cases.json').read_text())
        self.assertEqual({c['lesson'] for c in cases}, {l['id'] for l in lessons})
        for lesson in lessons:
            self.assertTrue(any(c['lesson']==lesson['id'] and c['label']=='Guided calculation' for c in cases))


if __name__ == '__main__':
    unittest.main()
