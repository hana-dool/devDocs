import unittest 
class MyTests(unittest.TestCase):
    def test_one_plus_two(self):
        self.assertEqual(1 + 2, 3)
    def test_one_plus_three(self):
        self.assertEqual(1 + 3, 4)
    def test_one_plus_four(self):
        self.assertEqual(1 + 4, 10)
    def test_one_plus_five(self):
        self.assertEqual(1 + 5, 10)


# 테스트를 진행
if __name__ == '__main__':
    unittest.main()
