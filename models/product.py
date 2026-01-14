class Product:
    def __init__(self, name, price, stock=10):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, stock={self.stock})"
