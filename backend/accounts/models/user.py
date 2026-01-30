# Epic Title: User Registration

from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.email