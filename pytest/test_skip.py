# test_skip.py
import pytest 
import sys
print (sys.version_info)

def func(x):
    return x + 1

@pytest.mark.skip(reason="no way of currently testing this")
def test_answer1():
    assert func(3) == 4

@pytest.mark.skipif(sys.version_info > (3,3),
                    reason="파이썬은 3.3 이상이면 안되요!")
def test_answer2():
    assert func(3) == 5

def test_answer3():
    assert func(3) == 6