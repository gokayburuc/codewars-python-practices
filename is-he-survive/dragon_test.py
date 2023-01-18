import unittest
from dragons import hero


class TestDragon(unittest.TestCase):

    def test_equal(self):
        got = hero(10, 5)
        want = True
        self.assertEqual(got, want)

    def test_less(self):
        got = hero(3, 11)
        want = False
        self.assertEqual(got, want)

    def test_bigger(self):
        got = hero(21, 10)
        want = True
        self.assertEqual(got, want)

    def test_zero_bullet(self):
        got = hero(0, 11)
        want = False
        self.assertEqual(got, want)

    def test_zero_dragon(self):
        got = hero(102, 0)
        want = True
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
