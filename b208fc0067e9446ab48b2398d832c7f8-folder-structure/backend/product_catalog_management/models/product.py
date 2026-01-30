# Epic Title: Add New Product

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name