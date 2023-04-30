from src.item import Item


class Phone(Item):
    """
    Телефон с разным количеством sim: quantity_sim
    """

    def __init__(self, name, price: float, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.verify_sim(number_of_sim)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{__class__.__name__}('{str(self.name)}', {str(self.price)}, {str(self.quantity)}, {str(self.__number_of_sim)})"

    @classmethod
    def verify_sim(cls, __number_of_sim):
        """Проверяет, что длина наименования товара не больше 10 символов"""
        if __number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        """Возвращает количество sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """ Проверяет перед внесением изменения на количество sim <=0"""
        self.verify_sim(number_of_sim)
        self.__number_of_sim = number_of_sim


# phone1 = Phone("iPhone 14", 120_000, 5, 2)
# print(phone1.number_of_sim)
# phone1.number_of_sim = 0
# # print(phone1.number_of_sim)
