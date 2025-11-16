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

    def test_get_discounted_price(self):
        self.assertEqual(self.product.get_discounted_price(10), 90.00)
        self.assertEqual(self.product.get_discounted_price(50), 50.00)
        self.assertEqual(self.product.get_discounted_price(0), 100.00)

    def test_negative_price_validation(self):
        self.product.price=-10
        with self.assertRaises(ValidationError):
            self.product.clean()