from highlow import high_and_low
import unittest


class HighLowTest(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(high_and_low(
            "8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")

    def test_case_two(self):
        # self.assertEquals(high_and_low("1 2 3"), "3 1")
        self.assertEqual(high_and_low("1 2 3"), "3 1")


if __name__ == "__main__":
    unittest.main()
