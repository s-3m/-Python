from abc import ABC, abstractmethod


class Clothes(ABC):
    title = 'Название проекта'

    def __init__(self, size=None, height=None):
        self.size = size
        self.height = height

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    @property
    def consumption(self):
        value_coat = round((self.size / 6.5 + 0.5), 2)
        return f'На пошив пальто уходит {value_coat} ткани'


class Suit(Clothes):

    @property
    def consumption(self):
        value_suit = round((2 * self.height + 0.3), 2)
        return f'На пошив костюма уходит {value_suit} ткани'


class TotalConsum(Clothes):

    @property
    def consumption(self):
        value_coat = round((self.size / 6.5 + 0.5), 2)
        value_suit = round((2 * self.height + 0.3), 2)
        return f'Итоговый расход ткани по - {value_suit + value_coat}'


user_size = int(input('Ваш размер: '))
user_height = int(input('Ваш рост: '))
coat = Coat(user_size, user_height)
suit = Suit(user_height, user_height)
total_consum = TotalConsum(user_size, user_height)
print(coat.consumption)
print(suit.consumption)
print(total_consum.consumption)
