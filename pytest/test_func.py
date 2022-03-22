def func(x):
    return x + 1

def test_answer1():
    assert func(3) == 4

def test_answer2():
    assert func(3) == 5

def test_answer3():
    assert func(3) == 6

# 터미널에 $ pytest test_func.py 를 붙여넣으세요!
