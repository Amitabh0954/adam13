# Epic Title: Profile Management

from django.db import models
from backend.accounts.models.user import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    preferences = models.JSONField(default=dict, blank=True)
    
    def __str__(self) -> str:
        return f"Profile of {self.user.email}"