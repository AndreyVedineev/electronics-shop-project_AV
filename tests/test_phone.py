import pytest

from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_item_init():
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_verify_sim():
    with pytest.raises(ValueError):
        phone1.number_of_sim = 2
        Phone.verify_sim(phone1.number_of_sim)

