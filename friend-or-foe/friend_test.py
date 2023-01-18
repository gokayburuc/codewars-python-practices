import unittest
from friendorfoe import friend


class FriendTest(unittest.TestCase):
    def test_one(self):

        self.assertEqual(
            friend(["Ryan", "Kieran", "Mark", ]), ["Ryan", "Mark"])

    def test_two(self):
        self.assertEqual(
            friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])

    def test_three(self):
        self.assertEqual(
            friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke",
                   "sixtyiscooooool"]), ["Jimm", "Cari", "aret"]
        )


if __name__ == "__main__":
    unittest.main()
