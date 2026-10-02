import unittest

from model import Economy


class TestModel(unittest.TestCase):
    def test_model_runs_and_collects_each_period(self):
        economy = Economy()
        economy.run()
        self.assertEqual(len(economy.history), economy.parameters.PERIODS)
        self.assertGreaterEqual(min(b.loans for b in economy.banks), -1e-9)
        self.assertGreaterEqual(min(h.deposits for h in economy.households), -1e-9)


if __name__ == "__main__":
    unittest.main()

