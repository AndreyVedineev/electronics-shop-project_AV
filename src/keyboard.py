from src.item import Item


class MixingLang:
    """ Хранение и изменение раскладки клавиатуры"""
    __slots__ = ['EN', 'RU']
    language = 'EN'

    @classmethod
    def change_lang(cls):
        if cls.language == 'EN':
            cls.language = 'RU'
        elif cls.language == 'RU':
            return cls


class KeyBoard(Item, MixingLang):
    """Класс  для товара “клавиатура"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.name = name

    @classmethod
    def verify_name(cls, name):
        """Переопределяю метод """
        return cls.name

