class Pickup:
    def cost(self, subtotal):
        return 0
    def name(self):
        return "Самовывоз"

class DeliveryPaid:
    def __init__(self, cost):
        self.cost_value = cost
    def cost(self, subtotal):
        return self.cost_value
    def name(self):
        return f"Доставка за {self.cost_value}P"

class FreeOverAmount:
    def __init__(self, limit, cost):
        self.limit = limit
        self.cost_value = cost
    def cost(self, subtotal):
        if subtotal >= self.limit:
            return 0
        return self.cost_value
    def name(self):
        return f"Бесплатно от {self.limit}P"
