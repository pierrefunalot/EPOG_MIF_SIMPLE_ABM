import unittest

from equations.consumption_budget import consumption_budget
from equations.expected_demand import expected_demand
from equations.production import production


class TestEquations(unittest.TestCase):
    def test_production(self):
        self.assertEqual(production(productivity=2.0, employment=3), 6.0)

    def test_expected_demand(self):
        value = expected_demand(10.0, 20.0, 0.4)
        self.assertAlmostEqual(value, 14.0)

    def test_consumption_budget(self):
        self.assertAlmostEqual(consumption_budget(100.0, 0.8), 80.0)


if __name__ == "__main__":
    unittest.main()

