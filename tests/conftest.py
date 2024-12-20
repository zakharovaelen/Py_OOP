import pytest

from src.product import Product
from src.category import Category
# создание fixture

@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)]

    )

@pytest.fixture
def products():
    return ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.")

@pytest.fixture
def add_product():
    return ("Samsung Galaxy S23 Ultra\n 256GB, Серый цвет, 200MP камера\n 180000.0\n 5")

@pytest.fixture
def price():
    return ("Изменять цену? Введите y если да,и n если нет.")
