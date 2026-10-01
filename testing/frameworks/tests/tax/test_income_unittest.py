import unittest

from tax.income import calculate_tax
from tax.residence import is_resident


class TestResidence(unittest.TestCase):
    def test_183_days_is_resident(self):
        self.assertTrue(is_resident(183))

    def test_182_days_is_not_resident(self):
        self.assertFalse(is_resident(182))

    def test_invalid_days_raise(self):
        for days in (-1, 367):
            with self.subTest(days=days), self.assertRaises(ValueError):
                is_resident(days)


class TestIncomeTax(unittest.TestCase):
    def test_resident_pays_13_percent(self):
        self.assertEqual(calculate_tax(100_000, days_in_country=200), 13_000)

    def test_non_resident_pays_30_percent(self):
        self.assertEqual(calculate_tax(100_000, days_in_country=100), 30_000)

    def test_tax_is_rounded_to_kopecks(self):
        self.assertAlmostEqual(calculate_tax(100.55, days_in_country=200), 13.07)

    def test_negative_income_raises(self):
        with self.assertRaises(ValueError):
            calculate_tax(-1, days_in_country=200)


if __name__ == "__main__":
    unittest.main()
