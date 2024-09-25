import unittest
from utils import interpret_results

class TestABTesting(unittest.TestCase):
    def test_significance(self):
        self.assertEqual(interpret_results(0.01), "Statistically significant difference between groups.")
        self.assertEqual(interpret_results(0.10), "No statistically significant difference.")

if __name__ == '__main__':
    unittest.main()
