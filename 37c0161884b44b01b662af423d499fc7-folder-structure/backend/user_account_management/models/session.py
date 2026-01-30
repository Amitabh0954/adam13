# Epic Title: User Login

from django.db import models
from django.utils import timezone
from user_account_management.models.user import User

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    last_activity = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'Session for {self.user.email}'