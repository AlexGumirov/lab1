from models.cart import Cart
from strategies.discount import Discount, NoDiscount
from strategies.delivery import Pickup
from strategies.payment import Cash

class CheckoutFacade:
    def __init__(self, cart: Cart):
        self.cart = cart
        self.discount: Discount = NoDiscount()
        self.delivery = Pickup()
        self.payment = Cash()

    def set_discount(self, discount):
        self.discount = discount

    def set_delivery(self, delivery):
        self.delivery = delivery

    def set_payment(self, payment):
        self.payment = payment

    def make_order(self, customer_name):
        print("\n оформление заказа")
        self.cart.show()

        subtotal = self.cart.subtotal()
        after_discount = self.discount.apply(subtotal)
        delivery_cost = self.delivery.cost(after_discount)
        total = after_discount + delivery_cost

        print(f"Скидка: {subtotal - after_discount:.2f}P")
        print(f"Доставка ({self.delivery.name()}): {delivery_cost:.2f}P")
        print(f"ИТОГО К ОПЛАТЕ: {total:.2f}P")

        paid = self.payment.pay(total)
        if paid:
            print(f"Заказ оформлен на {customer_name}!\n")
            self.cart.clear()
        else:
            print("Ошибка оплаты")
