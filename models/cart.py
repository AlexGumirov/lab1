from typing import List, Tuple
from models.product import Product

class Cart:
    def __init__(self):
        # сохраним список кортежей (product, qty)
        self.items: List[Tuple[Product, int]] = []

    def add(self, product: Product, qty: int):
        if qty <= 0:
            print("Количество должно быть > 0")
            return
        if product.stock < qty:
            print(f"Товара {product.name} нет в нужном количестве")
            return
        self.items.append((product, qty))
        product.stock -= qty
        print(f"Добавлено {qty} шт. {product.name}")

    def subtotal(self):
        total = 0
        for p, q in self.items:
            total += p.price * q
        return total

    def clear(self):
        # вернуть товары на склад
        for p, q in self.items:
            p.stock += q
        self.items = []
        print("Корзина очищена")

    def show(self):
        print("КОРЗИНА")
        if not self.items:
            print("Пусто")
            return
        for p, q in self.items:
            print(f"{p.name} x{q} = {p.price * q:.2f}P")
        print(f"Итого без скидки: {self.subtotal():.2f}P")
