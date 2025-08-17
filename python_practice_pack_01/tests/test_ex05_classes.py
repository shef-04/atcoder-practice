
import pytest
from src.ex05_classes import Item, Cart


def test_item_tax_property():
    it = Item("apple", 100)
    assert isinstance(it.price, int)
    assert hasattr(it, "price_with_tax")
    assert it.price_with_tax == 110  # 10%


def test_cart_flow():
    apple = Item("apple", 120)
    banana = Item("banana", 80)
    c = Cart()
    c.add(apple, 2)   # 240
    c.add(banana, 1)  # 80
    assert c.total() == int(240*1.1 + 80*1.1)
    c.remove(apple, 1)
    assert c.total() == int(120*1.1 + 80*1.1)
