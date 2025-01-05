from src.product import Product

class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, color, country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
