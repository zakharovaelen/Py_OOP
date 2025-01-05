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
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "Серый")


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "Серый"),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "Серый"),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "Серый")]

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


@pytest.fixture
def category_with_quantity():
    return ("Cмартфоны, количество продуктов: 27шт")

@pytest.fixture
def product_with_quantity():
    return ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.")


@pytest.fixture
def product_count():
    return ("2580000.0")

@pytest.fixture
def smartphone1():
    return ("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")

@pytest.fixture
def smartphone2():
    return ("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def grass():
    return ("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")