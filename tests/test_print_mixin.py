from pyexpat.errors import messages

from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass

def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "red")
    message = capsys.readouterr()
    assert message.out().strip() == "Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5, red"
