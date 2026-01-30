# Epic Title: Password Recovery

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self) -> bool:
        expiration_time = self.created_at + timezone.timedelta(hours=24)
        return timezone.now() < expiration_time

    def __str__(self) -> str:
        return str(self.token)