import unittest
from mangoes import mango


class MangoTest(unittest.TestCase):

    def test_less_three(self):
        self.assertEqual(mango(2, 5), 10)
        self.assertEqual(mango(1, 3), 3)
        self.assertEqual(mango(2, 4), 8)

    def test_bigger_three(self):
        self.assertEqual(mango(4, 7), 21)
        self.assertEqual(mango(5, 12), 48)
        self.assertEqual(mango(9, 6), 36)
        self.assertEqual(mango(9, 5), 30)

    def test_three(self):
        self.assertEqual(mango(3, 2), 4)
        self.assertEqual(mango(3, 4), 8)


if __name__ == "__main__":
    unittest.main()
