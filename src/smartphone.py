from src.product import Product

class Smartphone(Product):

    def __init__(self, name, description, price, quantity, color, efficiency, model, memory):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
