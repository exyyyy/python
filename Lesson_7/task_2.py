from abc import ABC, abstractmethod


class Clothes(ABC):
    res = 0

    def __init__(self, par):
        self.par = par

    @property
    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        Clothes.res = Clothes.res + self.expense + other.expense
        return Suit(0)

    def __str__(self):
        r = Clothes.res
        Clothes.res = 0
        return str(r)


class Coat(Clothes):
    @property
    def expense(self):
        return round(self.par / 6.5) + 0.5


class Suit(Clothes):
    @property
    def expense(self):
        return round((2 * self.par + 0.3) / 100)


palto = Coat(44)
kostum = Suit(189)
print(kostum + kostum + palto+ palto)
