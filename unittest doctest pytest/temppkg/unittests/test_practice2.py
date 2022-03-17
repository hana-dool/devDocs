# test_module1.py

from unittest import TestCase, main

class MyTests(TestCase):
    def test_one_plus_two(self):
        print(1)
        self.assertEqual(1 + 2, 3)

# 위에서 정의한 테스트들을 모두 실행시켜 주세요! 
if __name__ == '__main__':
    main()