from load import load
import unittest


class ComplexTest(unittest.TestCase):
    def setUp(self):
        self.module = load("complex")

    def test_addition(self):
        result = self.module.add([0, 1], [2, 3])
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imaginary, 4)


if __name__ == "__main__":
    unittest.main()
