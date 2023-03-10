import unittest
from middlechar import get_middle


class MiddleTest(unittest.TestCase):

    def test_middle(self):
        self.assertEqual(get_middle("test"), "es")
        self.assertEqual(get_middle("testing"), "t")
        self.assertEqual(get_middle("middle"), "dd")
        self.assertEqual(get_middle("A"), "A")
        self.assertEqual(get_middle("of"), "of")


if __name__ == "__main__":
    unittest.main()
