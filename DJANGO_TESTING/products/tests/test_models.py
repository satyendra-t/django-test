from django.test import TestCase
from django.core.exceptions import ValidationError
from products.models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product(name="Test Product",price=100.00,stock_count=10)

    def test_in_stock_property(self):
        self.assertTrue(self.product.in_stock)

        #Set Stock count to zero and test again
        self.product.stock_count=0
        self.assertFalse(self.product.in_stock)

