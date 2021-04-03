import unittest
from load import load


class AddTest(unittest.TestCase):

    def test_addition(self):
        module = load('add')

        self.assertEqual(module.add(1, 2), 1+2)


if __name__ == "__main__":
    unittest.main()
