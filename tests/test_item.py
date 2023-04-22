"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

item1 = Item('Смартфон', 36000.0, 5)


def test_item_init():
    assert item1.name == 'Смартфон'
    assert item1.price == 36000.0
    assert item1.quantity == 5


def test_repr():
    assert repr(item1) == "Item('Смартфон', 36000.0, 5)"


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
    assert item1.calculate_total_price() == 180000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 28800.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
