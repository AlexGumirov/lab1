class PayByCard:
    def pay(self, amount):
        print(f"Оплачено картой: {amount:.2f}P")
        return True

class PayPal:
    def pay(self, amount):
        print(f"Оплачено через SberPay: {amount:.2f}P")
        return True

class Cash:
    def pay(self, amount):
        print(f"Оплата наличными при получении: {amount:.2f}P")
        return True

# Для тестирования сценария ошибки оплаты
class DeclinedPayment:
    def pay(self, amount):
        print(f"Платёж отклонён для суммы: {amount:.2f}P")
        return False
