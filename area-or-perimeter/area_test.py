import unittest
from areaperimeter import area_or_perimeter


class area_test(unittest.TestCase):

    def test_one(self):
        got = area_or_perimeter(5, 5)
        want = 25
        self.assertEqual(got, want)

    def test_two(self):
        got = area_or_perimeter(5, 6)
        want = 22
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
