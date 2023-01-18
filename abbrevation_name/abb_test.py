import unittest
from abb import abbrev_name


class abbTestCase(unittest.TestCase):

    def test_first(self):
        got = abbrev_name("Gökay BÜRÜÇ")
        want = "G.B"
        self.assertEqual(got, want)

    def test_second(self):
        self.assertEqual(abbrev_name("Esin Karslı"), "E.K")

    def test_third(self):
        self.assertEqual(abbrev_name("berk yildiz"), "B.Y")


if __name__ == "__main__":
    unittest.main()
