# test_func.py
import pytest


def func(x):
    return x + 1


def test_answer1():
    assert func(3) == 4


if __name__ == "__main__":
    pytest.main()
