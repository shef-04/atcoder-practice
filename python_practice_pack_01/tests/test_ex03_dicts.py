
import pytest
from src.ex03_dicts import word_count, merge_scores, deep_get


def test_word_count():
    words = ["Apple", "banana", "apple", "BANANA", "kiwi"]
    assert word_count(words) == {"apple": 2, "banana": 2, "kiwi": 1}


def test_merge_scores():
    a = {"a": 1, "b": 2}
    b = {"b": 3, "c": 4}
    assert merge_scores(a, b) == {"a": 1, "b": 5, "c": 4}
    assert a == {"a": 1, "b": 2} and b == {"b": 3, "c": 4}


def test_deep_get():
    data = {"user": {"profile": {"name": "Yuta"}}}
    assert deep_get(data, ["user", "profile", "name"]) == "Yuta"
    assert deep_get(data, ["user", "age"], 0) == 0
