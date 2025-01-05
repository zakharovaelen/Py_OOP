import pytest

from tests.conftest import products

def test_lawn_grass_init(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.color == "Зеленый"
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"

def test_lawn_grass_add(grass1, grass2):
    grass1 + grass2 == 16750.0

def test_lawn_grass_add_error(grass1, grass2):
    with pytest.raises(TypeError):
        grass1 + 1