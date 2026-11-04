"""Check educational allocation arithmetic, not an operational reserve strategy."""
import unittest
from decimal import Decimal
from fractions import Fraction


class AllocationArithmetic(unittest.TestCase):
    def test_unequal_volume_donor_checks(self):
        start = Fraction(240)
        volumes = (Fraction(20), Fraction(24))
        inventories = tuple(volume * start for volume in volumes)
        demands = tuple(inventory / 3 for inventory in inventories)
        combined = sum(demands)
        self.assertEqual(inventories, (4800, 5760))
        self.assertEqual(demands, (1600, 1920))
        self.assertEqual(combined, 3520)

        ordinary_turn = start * Fraction(2, 3)
        self.assertEqual(combined - volumes[0] * ordinary_turn, 320)
        entry_allowance = inventories[0] - combined
        used_pressure = entry_allowance / volumes[0]
        adjusted_turn = start - used_pressure
        self.assertEqual(entry_allowance, 1280)
        self.assertEqual(used_pressure, 64)
        self.assertEqual(adjusted_turn, 176)
        self.assertEqual(volumes[0] * adjusted_turn - combined, 0)
        self.assertEqual(volumes[1] * ordinary_turn - combined, 320)
        self.assertLess(entry_allowance, demands[0])
        self.assertLess(volumes[0] * (adjusted_turn - 1), combined)

        # Independently sum each cylinder's nominal demand, then convert demand
        # directly to retained pressure instead of subtracting entry use.
        per_cylinder_a = Decimal('10') * Decimal('240') / 3
        per_cylinder_b = Decimal('12') * Decimal('240') / 3
        total = 2 * per_cylinder_a + 2 * per_cylinder_b
        self.assertEqual(total / (2 * Decimal('10')), Decimal('176'))
        self.assertEqual(2 * Decimal('12') * 160 - total, Decimal('320'))
        self.assertEqual(Decimal('240') - (total / 2) / 20, Decimal('152'))

    def test_variable_pressure_normalization_limits(self):
        # Five minutes at 2 bar absolute, ten at 4 bar; 1 bar reference.
        times = (Fraction(5), Fraction(10))
        ratios = (Fraction(2), Fraction(4))
        exposure = sum(t * p for t, p in zip(times, ratios))
        mean_pressure_ratio = exposure / sum(times)
        constant_rate = Fraction(20)
        gas_used = sum(constant_rate * t * p
                       for t, p in zip(times, ratios))
        self.assertEqual(gas_used, 1000)
        self.assertEqual(gas_used / exposure, 20)
        self.assertEqual(gas_used / sum(times) / mean_pressure_ratio, 20)
        self.assertNotEqual(gas_used / sum(times) / 3, 20)
        decimal_gas = Decimal('20') * (Decimal('5') * 2 + Decimal('10') * 4)
        self.assertEqual(decimal_gas / Decimal('50'), Decimal('20'))

        # Changing breathing rates shows why this need not equal the
        # time-average normalized rate when both depth and demand change.
        rates = (Fraction(10), Fraction(30))
        variable_gas = sum(r * t * p
                           for r, t, p in zip(rates, times, ratios))
        inferred_rate = variable_gas / exposure
        time_average = sum(r * t for r, t in zip(rates, times)) / sum(times)
        self.assertEqual(inferred_rate, 26)
        self.assertEqual(time_average, Fraction(70, 3))
        self.assertNotEqual(inferred_rate, time_average)


if __name__ == '__main__':
    unittest.main()
