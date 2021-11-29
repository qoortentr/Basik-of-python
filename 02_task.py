from abc import ABC, abstractmethod


class Clothes(ABC):
    expence_count = 0

    @abstractmethod
    def calc_expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_count += self.calc_expence

    def __str__(self):
        return f"Общий расход ткани - {Coat.expence_count:.02f}, для пальто размером {self.size} - {self.calc_expence}"

    @property
    def calc_expence(self):
        exp = self.size / 6.5 + 0.5
        return float(f"{exp:.02f}")


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.expence_count += self.calc_expence

    def __str__(self):
        return f"Общий расход ткани - {Suit.expence_count:.02f}, для костюма человека ростом {self.height} см - " \
               f"{self.calc_expence}"

    @property
    def calc_expence(self):
        exp = 2 * self.height + 0.3
        return float(f"{exp:.02f}")


size = Coat(50)
print(size)

height = Suit(180)
print(height)

height = Suit(175)
print(height)

size = Coat(52)
print(size)