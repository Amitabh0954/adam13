# Epic Title: Password Recovery

from django.db import models
from django.utils import timezone
from backend.models.user import User
import uuid

class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_expired(self) -> bool:
        return timezone.now() > self.created_at + timezone.timedelta(hours=24)

    def __str__(self) -> str:
        return f"Password reset request for {self.user.email}"