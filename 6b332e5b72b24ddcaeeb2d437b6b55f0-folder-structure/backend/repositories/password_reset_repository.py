# Epic Title: Password Recovery

from backend.models.password_reset_request import PasswordResetRequest
from backend.models.user import User
from typing import Optional
from django.utils import timezone

class PasswordResetRepository:

    def create_reset_request(self, user: User) -> PasswordResetRequest:
        reset_request = PasswordResetRequest(user=user)
        reset_request.save()
        return reset_request

    def get_reset_request_by_token(self, token: str) -> Optional[PasswordResetRequest]:
        try:
            return PasswordResetRequest.objects.get(token=token)
        except PasswordResetRequest.DoesNotExist:
            return None

    def invalidate_reset_requests(self, user: User) -> None:
        PasswordResetRequest.objects.filter(user=user, created_at__lte=timezone.now() - timezone.timedelta(hours=24)).delete()