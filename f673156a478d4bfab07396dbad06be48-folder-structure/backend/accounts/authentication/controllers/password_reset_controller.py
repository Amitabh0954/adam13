# Epic Title: Password Recovery

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

from accounts.authentication.repositories.password_reset_repository import PasswordResetRepository

reset_repository = PasswordResetRepository()

@csrf_exempt
def request_password_reset(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')

        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'No user found with this email'}, status=404)

        token = get_random_string(64)
        reset_repository.create_reset_token(user, token)

        reset_link = f"{settings.FRONTEND_URL}{reverse('reset_password', args=[token])}"
        send_mail(
            'Password Reset Request',
            f'Please use the following link to reset your password: {reset_link}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Password reset link sent'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def reset_password(request, token: str):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if not new_password or not confirm_password:
            return JsonResponse({'error': 'Both password fields are required'}, status=400)

        if new_password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        user = reset_repository.get_user_by_token(token)
        if not user:
            return JsonResponse({'error': 'Invalid or expired token'}, status=400)

        user.set_password(new_password)
        user.save()

        reset_repository.delete_reset_token(token)
        return JsonResponse({'message': 'Password has been reset successfully'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)