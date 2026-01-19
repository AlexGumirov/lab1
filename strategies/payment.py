from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayByCard(Payment):
    def pay(self, amount):
        print(f"Оплата картой: {amount}P")
        return True


class PayPal(Payment):
    def pay(self, amount):
        print(f"Оплата PayPal: {amount}P")
        return True


class Cash(Payment):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}P")
        return True


class DeclinedPayment(Payment):
    def pay(self, amount):
        print("Платёж отклонён")
        return False
