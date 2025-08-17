
import pytest
from src.ex01_strings import normalize_spaces, snake_to_camel, format_report


def test_normalize_spaces():
    assert normalize_spaces("  a   b  ") == "a b"
    assert normalize_spaces("\t a\n b  c ") == "a b c"


def test_snake_to_camel():
    assert snake_to_camel("user_name_id") == "userNameId"
    assert snake_to_camel("x") == "x"
    assert snake_to_camel("") == ""


def test_format_report():
    assert format_report("Yuta", 89.44) == "Name: Yuta, Score: 89.4"
    assert format_report("A", 90) == "Name: A, Score: 90.0"
