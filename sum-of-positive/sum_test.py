import unittest
from sumpositive import positive_sum


class sumTest(unittest.TestCase):

    def test_mixed(self):
        array = [1, -4, 7, 12]
        got = positive_sum(array)
        want = 20
        self.assertEqual(got, want)

    def test_negative(self):
        array = [-1, -4, -7, -12]
        got = positive_sum(array)
        want = 0
        self.assertEqual(got, want)

    def test_positive(self):
        array = [1, 4, 7, 12]
        got = positive_sum(array)
        want = 24
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
