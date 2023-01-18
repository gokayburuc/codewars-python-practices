import unittest
from centyear import century


class CenturyTest(unittest.TestCase):

    def test_seventeenth(self):

        got = century(1705)
        want = 18
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
