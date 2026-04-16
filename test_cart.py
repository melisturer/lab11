import pytest
from cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("milk", 10, 2)
    assert cart.get_total() == 20

def test_add_two_items():
    cart = ShoppingCart()
    cart.add_item("milk", 10, 2)
    cart.add_item("bread", 5, 1)
    assert cart.get_total() == 25

def test_zero_quantity():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("milk", 10, 0)

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("milk", 10, 1)
    cart.remove_item("milk")
    assert cart.get_total() == 0

def test_wrong_discount():
    cart = ShoppingCart()
    cart.add_item("milk", 10, 2)
    with pytest.raises(ValueError):
        cart.apply_discount("abc")

def test_discount():
    cart = ShoppingCart()
    cart.add_item("milk", 10, 2)
    cart.apply_discount("SAVE10")
    assert cart.get_total() == 18

def test_item_count():
    cart = ShoppingCart()
    cart.add_item("milk", 10, 2)
    cart.add_item("bread", 5, 3)
    assert cart.get_item_count() == 5
