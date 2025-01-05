def test_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(first_category.products_list) == 3
    assert first_category.category_count == 1
    assert first_category.product_count == 3

def test_products(products):
   assert products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_new_product(add_product):
    assert add_product == "Samsung Galaxy S23 Ultra\n 256GB, Серый цвет, 200MP камера\n 180000.0\n 5"

def test_price(price):
    assert price == "Изменять цену? Введите y если да,и n если нет."

def test_category_with_quantity(category_with_quantity):
   assert category_with_quantity == "Cмартфоны, количество продуктов: 27шт"

def test_new_product_error(first_category, product):
    assert first_category.product == 1