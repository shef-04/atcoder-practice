
import pytest
from src.ex02_lists import even_squares, top_k, find_first


def test_even_squares():
    assert even_squares([1,2,3,4,5,6]) == [4,16,36]
    a = [2,2,3]
    out = even_squares(a)
    assert a == [2,2,3] and out == [4,4]


def test_top_k():
    assert top_k([5,1,7,3,7], 3) == [7,7,5]
    assert top_k([1,2], 5) == [2,1]


def test_find_first():
    is_odd = lambda x: x % 2 == 1
    assert find_first(is_odd, [2,4,6,7,8]) == 3
    assert find_first(is_odd, [2,4,6,8]) is None
