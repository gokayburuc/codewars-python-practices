import unittest
from converter import string_to_number

# class TestConverter(unittest.TestCase):

#     def test_convert(self):
#         print('Test "1234"  passed')
#         self.assertEqual(int("1234"), 1234)

#     def test_split(self):
#         word = "hello world"
#         self.assertEqual(word.split(), ["hello", "world"])
#         print("Split Test Passed")


# if __name__ == '__main__':
#     unittest.main()

class converter_test(unittest.TestCase):

    def test_one(self):
        self.assertEqual(string_to_number("1234"), 1234)
        print("test 1 passed!")

    def test_two(self):
        self.assertEqual(string_to_number("-7"), -7)
        print("test 2 passed!")

    def test_three(self):
        self.assertEqual(string_to_number("1405"), 1405)
        print("test 3 passed!")


if __name__ == "__main__":
    unittest.main()
