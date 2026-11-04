"""Separate recomputation of classroom question quantities; no dive validation."""
import unittest
from decimal import Decimal
from fractions import Fraction


class ScenarioArithmetic(unittest.TestCase):
    def test_pressure_rates(self):
        self.assertEqual(Fraction(16, 2), 8)
        self.assertEqual(Fraction(24, 2), 12)
        self.assertEqual(Decimal('16') * Decimal('0.5'), Decimal('8'))
        self.assertEqual(Decimal('24') * Decimal('0.5'), Decimal('12'))

    def test_inventory(self):
        self.assertEqual(Fraction(16) * 230, 3680)
        self.assertEqual(Fraction(24) * 170, 4080)
        self.assertEqual(Decimal('230') * 8 * 2, Decimal('3680'))
        self.assertEqual(Decimal('170') * 12 * 2, Decimal('4080'))
        self.assertEqual(4080 - 3680, 400)

    def test_combined_exit_and_delay(self):
        self.assertEqual(Fraction(44) * 3 * (11 + 4), 1980)
        exit_demand = Decimal('44') * Decimal('3') * Decimal('11')
        delay_demand = Decimal('44') * Decimal('3') * Decimal('4')
        self.assertEqual(exit_demand, Decimal('1452'))
        self.assertEqual(delay_demand, Decimal('528'))
        self.assertEqual(exit_demand + delay_demand, Decimal('1980'))

    def test_partial_pressures(self):
        self.assertEqual(Fraction(30, 100) * 3, Fraction(9, 10))
        self.assertEqual(Fraction(30, 100) * 4, Fraction(6, 5))
        self.assertEqual(Decimal('3') * 30 / 100, Decimal('0.90'))
        self.assertEqual(Decimal('4') * 30 / 100, Decimal('1.20'))


if __name__ == '__main__':
    unittest.main()
