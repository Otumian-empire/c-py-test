from load import load
import unittest


class SumTest(unittest.TestCase):
    def setUp(self):
        self.module = load('sum')

    def test_0_zero(self):
        self.assertEqual(self.module.sum(0), 0)

    def test_1_one(self):
        self.assertEqual(self.module.sum(1), 1)

    def test_2_multiple(self):
        self.assertEqual(self.module.sum(2), 2)
        self.assertEqual(self.module.sum(4), 2 + 4)


if __name__ == "__main__":
    unittest.main()
