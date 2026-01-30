# Epic Title: Product Categorization

from django.db import models
from backend.models.category import Category

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.name