# Epic Title: User Login

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, unique=True)
    start_time = models.DateTimeField(default=timezone.now)
    last_activity = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Session for {self.user.username}"