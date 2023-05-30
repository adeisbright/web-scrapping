import unittest
from doubler import doubler


class TestModu(unittest.TestCase):
    def test_double_negative(self):
        self.assertEqual(
            doubler(3), 9, "Should fail since 9 is not the double of 3")

    def test_double_positive(self):
        self.assertEqual(
            doubler(3), 6, "Should return 6 and pass")


if __name__ == "__main__":
    unittest.main()
