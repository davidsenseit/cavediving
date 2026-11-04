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
    def test_classroom_quantities_exact(self):
        large, small = Fraction(24 * 200), Fraction(18 * 200)
        self.assertEqual((large, small, large - small), (4800, 3600, 1200))
        supply, demand = Fraction(2600), Fraction(2750)
        self.assertEqual(demand - supply, 150)
        self.assertEqual(supply / demand, Fraction(52, 55))
        self.assertEqual(Fraction(240, 3), 80)
        self.assertEqual(Fraction(240) - Fraction(240, 3), 160)

    def test_separate_decimal_recomputation(self):
        # Independent expressions for deficit, allocation and a repeating ratio.
        with localcontext() as ctx:
            ctx.prec = 40
            self.assertEqual(Decimal('2750') - Decimal('2600'), Decimal('150'))
            self.assertEqual(Decimal('240') * Decimal(2) / 3, Decimal('160'))
            ratio = Decimal('2600') / Decimal('2750')
            exact = Fraction(52, 55)
            self.assertEqual(ratio, Decimal(exact.numerator) / Decimal(exact.denominator))
            self.assertEqual(ratio.quantize(Decimal('.00001')), Decimal('.94545'))

    def test_normalized_rate(self):
        self.assertEqual(normalized_rate(18, 50, 15, 3), 20)
        # Same pressure loss in half the water volume consumes half the gas.
        self.assertEqual(normalized_rate(9, 50, 15, 3), 10)
        self.assertEqual(normalized_rate(24, 0, 20, 2), 0)
        with localcontext() as ctx:
            ctx.prec = 30
            independently = (Decimal('18') * Decimal('50') / Decimal('15')) / Decimal('3')
            self.assertEqual(independently, Decimal('20'))

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

