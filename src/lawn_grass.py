from src.product import Product

class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, color, country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

if __name__ == '__main__':
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)