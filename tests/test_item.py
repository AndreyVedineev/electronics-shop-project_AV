"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_item_init():
    assert item1.name == 'Смартфон'
    assert item1.price == 10000.0
    assert item1.quantity == 20


def test_repr():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(item1) == 'Смартфон'


def test_name():
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_verify_name():
    with pytest.raises(Exception):
        item1.name = 'СуперСмартфон'
        Item.verify_name(item1.name)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


@pytest.mark.parametrize("a, result", [('5', 5), ('5.0', 5), ('5.5', 5)])
def test_string_to_number(a, result):
    assert Item.string_to_number(a) == 5



def test_add():
    assert item1 + phone1 == 25
