from models.product import Product
from models.cart import Cart
from facade.checkout_facade import CheckoutFacade
from strategies.discount import PercentDiscount, FixedDiscount, NoDiscount
from strategies.delivery import FreeOverAmount, DeliveryPaid, Pickup
from strategies.payment import PayByCard, PayPal, Cash, DeclinedPayment

if __name__ == "__main__":
    
    laptop = Product("Ноутбук", 1000, stock=5)
    mouse = Product("Мышка", 50, stock=20)
    headphones = Product("Наушники", 80, stock=10)

    # первый пример
    cart = Cart()
    cart.add(laptop, 1)
    cart.add(mouse, 2)

    checkout = CheckoutFacade(cart)
    checkout.set_discount(PercentDiscount(10))
    checkout.set_delivery(FreeOverAmount(500, 25))
    checkout.set_payment(PayByCard())
    checkout.make_order("Александр Гумиров")

    # второй
    cart2 = Cart()
    cart2.add(laptop, 1)
    cart2.add(mouse, 1)
    checkout2 = CheckoutFacade(cart2)
    checkout2.set_discount(FixedDiscount(30))
    checkout2.set_delivery(DeliveryPaid(10))
    checkout2.set_payment(PayPal())
    checkout2.make_order("Роман Попов")

    # третий
    cart3 = Cart()
    cart3.add(mouse, 1)
    checkout3 = CheckoutFacade(cart3)
    checkout3.set_discount(NoDiscount())
    checkout3.set_delivery(Pickup())
    checkout3.set_payment(Cash())
    checkout3.make_order("Млакир Глеб")

    # четвертый
    cart4 = Cart()
    cart4.add(headphones, 1)
    checkout4 = CheckoutFacade(cart4)
    checkout4.set_discount(NoDiscount())
    checkout4.set_delivery(DeliveryPaid(5))
    checkout4.set_payment(DeclinedPayment())
    checkout4.make_order("неуспешная оплата")