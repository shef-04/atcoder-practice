
import pytest
from src.ex04_functions import clamp, apply_all, make_adder


def test_clamp():
    assert clamp(-1) == 0.0
    assert clamp(0.5) == 0.5
    assert clamp(2, 0, 1) == 1


def test_apply_all():
    funcs = [lambda x: x+1, lambda x: x*2, lambda x: x-3]
    assert apply_all(funcs, 4) == ((4+1)*2-3)


def test_make_adder():
    add5 = make_adder(5)
    assert add5(10) == 15
