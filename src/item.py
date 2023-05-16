import csv
from abc import ABC


class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else '_Файл item.csv поврежден_'

    def __str__(self):
        return self.message


class Item(ABC):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.
    all = []

    # path = os.path.join('..', 'electronics-shop-project_AV', 'scr', 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.verify_name(name)

        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def verify_name(cls, name):
        """Проверяет, что длина наименования товара не больше 10 символов"""
        if len(name) >= 16:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        try:
            with open('../src/items.csv', encoding='windows-1251', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all = [cls((row['name']), float(row['price']), int(row['quantity'])) for row in reader]

        except FileNotFoundError:
            print('_Отсутствует файл item.csv_')
        except KeyError:
            raise InstantiateCSVError

        return cls.all

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.verify_name(name)
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        :return:  стоимость товара с скидкой.
        """
        self.price *= self.pay_rate
        return self.pay_rate

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"{__class__.__name__}('{str(self.__name)}', {str(self.price)}, {str(self.quantity)})"

    def __add__(self, other):
        temp = other.__class__.__name__  # имя другого класса (str)
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            return print("Складывать нельзя")
