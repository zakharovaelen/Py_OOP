#создание теста для класса Category
def test_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(first_category.products) == 3
    assert first_category.category_count == 1
    assert first_category.product_count == 3
