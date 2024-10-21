
from src.product import Product


class Category(Product):
    pass
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
    def add_product(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{str(product)}\n'
        return product_str

    @add_product.setter
    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products
