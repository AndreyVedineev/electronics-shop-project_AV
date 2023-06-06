from src.item import Item


class MixingLang:
    """ Хранение и изменение раскладки клавиатуры"""
    _language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'RU'
        return self

    @property
    def language(self):
        return self._language


class KeyBoard(Item, MixingLang):
    """Класс  для товара “клавиатура"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.name = name

    @classmethod
    def verify_name(cls, name):
        """Переопределяю метод """
        return cls.name
