"""Educational arithmetic checks, deliberately not an operational planner."""
import math
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction


def normalized_rate(volume_l, pressure_drop_bar, minutes, absolute_bar):
    """Surface-equivalent L/min at a fixed 1 bar reference; ideal gas."""
    values = (volume_l, pressure_drop_bar, minutes, absolute_bar)
    if any(isinstance(v, bool) or not isinstance(v, (int, float))
           or not math.isfinite(v) for v in values):
        raise ValueError('finite numeric inputs required')
    if volume_l <= 0 or minutes <= 0 or absolute_bar <= 0 or pressure_drop_bar < 0:
        raise ValueError('positive volume/time/absolute pressure; nonnegative drop')
    return Fraction(str(volume_l)) * Fraction(str(pressure_drop_bar)) / (
        Fraction(str(minutes)) * Fraction(str(absolute_bar)))


class ArithmeticChecks(unittest.TestCase):
    def test_supplied_example_exact(self):
        large, small = Fraction(24 * 210), Fraction(22 * 210)
        self.assertEqual((large, small), (5040, 4620))
        demand = large / 3 + small / 3
        self.assertEqual(demand, 3220)
        self.assertEqual(demand - small * 2 / 3, 140)
        drop = (small - demand) / 22
        self.assertEqual(drop, Fraction(700, 11))
        self.assertEqual(210 - drop, Fraction(1610, 11))

    def test_separate_decimal_recomputation(self):
        # Remaining-pressure path, expressed independently of pressure-drop path.
        with localcontext() as ctx:
            ctx.prec = 40
            demand = Decimal('24') * Decimal('210') / 3 + Decimal('22') * Decimal('210') / 3
            remaining = demand / Decimal('22')
            exact = Fraction(210) - Fraction(1400, 22)
            independent = Decimal(exact.numerator) / Decimal(exact.denominator)
            self.assertEqual(remaining, independent)
            self.assertEqual(remaining.quantize(Decimal('.1')), Decimal('146.4'))
            self.assertEqual(Decimal(700) / 11, Decimal(1400) / 22)
            self.assertNotEqual(Decimal(700) / 11, Decimal('63.3'))
            self.assertEqual(Decimal(210) - Decimal('63.3'), Decimal('146.7'))

    def test_normalized_rate(self):
        self.assertEqual(normalized_rate(24, 40, 20, 2), 24)
        # Same pressure loss in half the water volume consumes half the gas.
        self.assertEqual(normalized_rate(12, 40, 20, 2), 12)
        self.assertEqual(normalized_rate(24, 0, 20, 2), 0)
        with localcontext() as ctx:
            ctx.prec = 30
            independently = (Decimal('24') * Decimal('40') / Decimal('20')) / Decimal('2')
            self.assertEqual(independently, Decimal('24'))

    def test_invalid_inputs(self):
        for values in [(0, 40, 20, 2), (24, -1, 20, 2), (24, 40, 0, 2),
                       (24, 40, 20, 0), (24, 40, 20, -1),
                       (True, 40, 20, 2), ('24', 40, 20, 2),
                       (24, float('nan'), 20, 2), (24, 40, float('inf'), 2)]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                normalized_rate(*values)

    def test_partial_pressure(self):
        self.assertEqual(Fraction(32, 100) * 4, Fraction(128, 100))
        self.assertNotEqual(Fraction(32, 100) * 3, Fraction(128, 100))


if __name__ == '__main__':
    unittest.main()
