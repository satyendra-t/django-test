from unittest.mock import PropertyMock

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Product(models.Model):
    #name, price, stock_count
    name=models.CharField(max_length=100)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    stock_count=models.IntegerField(default=0)

    def get_discounted_price(self, discount_percentage):
        """Calculate and return the discounted price"""
        return self.price*(1-discount_percentage/100)

    @property
    def in_stock(self)->bool:
        return self.stock_count > 0

    def clean(self):
        if self.price<0 :
            raise ValidationError("Price cannot be negative")
        if self.stock_count < 0:
            raise ValidationError("Stock count cannot be negative")