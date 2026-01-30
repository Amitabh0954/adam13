# Epic Title: Password Recovery

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.services.password_reset_service import PasswordResetService
import json

password_reset_service = PasswordResetService()

@csrf_exempt
def request_password_reset(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')

        token = password_reset_service.request_password_reset(email)
        if token:
            return JsonResponse({'message': 'Password reset email sent successfully'}, status=200)
        return JsonResponse({'error': 'User with this email does not exist'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token')
        new_password = data.get('new_password')

        user = password_reset_service.reset_password(token, new_password)
        if user:
            return JsonResponse({'message': 'Password reset successfully'}, status=200)
        return JsonResponse({'error': 'Invalid or expired token'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)