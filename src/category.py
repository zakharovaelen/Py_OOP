from itertools import product

from src.product import Product


class Category:

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    def __str__(self):
        products_in_stock = 0
        for product in self.__products:
            products_in_stock += product.quantity
        return f'{self.name}, количество продуктов: {products_in_stock} шт.'

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{str(product)}\n'
        return product_str


    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError


    @property
    def products_list(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0








