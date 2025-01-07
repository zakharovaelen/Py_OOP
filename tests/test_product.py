# создание теста для класса Product
def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_str(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_with_quantity(product_with_quantity):
   assert product_with_quantity == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_count(product_count):
   assert product_count == "2580000.0"


"""def test_empty_price(product_without_quantity):
    assert product_without_quantity == "ValueError: Товар с нулевым количеством не может быть добавлен"""""
