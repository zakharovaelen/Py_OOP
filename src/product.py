# создание класса Product:
from itertools import product


class Product:
    pass
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        price_float = ""
        for price_float in self.__price:
            price_float += f"{product.price} руб.\n"
        return price_float

    @price.setter
    def price(self, new_price: float):
        self.__price.append(str(new_price))
        if new_price < 0 :
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price









if __name__ == "__main__":
    product = Product.new_product("телефон", "большой и дорогой", "100500", 3)
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)