from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def cost(self, subtotal):
        pass

    @abstractmethod
    def name(self):
        pass


class Pickup(Delivery):
    def cost(self, subtotal):
        return 0

    def name(self):
        return "Самовывоз"


class DeliveryPaid(Delivery):
    def __init__(self, cost):
        self.cost_value = cost

    def cost(self, subtotal):
        return self.cost_value

    def name(self):
        return f"Доставка за {self.cost_value}€"


class FreeOverAmount(Delivery):
    def __init__(self, limit, cost):
        self.limit = limit
        self.cost_value = cost

    def cost(self, subtotal):
        if subtotal >= self.limit:
            return 0
        return self.cost_value

    def name(self):
        return f"Бесплатно от {self.limit}€"
