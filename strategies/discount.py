from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass

class NoDiscount(Discount):
    def apply(self, amount):
        return amount


class PercentDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, amount):
        return amount * (1 - self.percent / 100)


class FixedDiscount(Discount):
    def __init__(self, money):
        self.money = money

    def apply(self, amount):
        return max(0, amount - self.money)
