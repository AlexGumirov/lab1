from models.cart import Cart
from strategies.discount import Discount, NoDiscount
from strategies.delivery import Delivery, Pickup
from strategies.payment import Payment, Cash

class CheckoutFacade:
    def __init__(self, cart: Cart):
        self.cart = cart
        self.discount: Discount = NoDiscount()
        self.delivery: Delivery = Pickup()
        self.payment: Payment = Cash()

    def set_discount(self, discount: Discount):
        self.discount = discount

    def set_delivery(self, delivery: Delivery):
        self.delivery = delivery

    def set_payment(self, payment: Payment):
        self.payment = payment

    def make_order(self, customer_name):
        subtotal = self.cart.subtotal()
        after_discount = self.discount.apply(subtotal)
        delivery_cost = self.delivery.cost(after_discount)
        total = after_discount + delivery_cost

        print("ИТОГО:", total)
        if self.payment.pay(total):
            print("Заказ оформлен для", customer_name)
            self.cart.clear()
