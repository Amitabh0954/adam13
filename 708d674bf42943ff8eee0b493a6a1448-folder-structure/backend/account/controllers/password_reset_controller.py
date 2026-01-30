# Epic Title: Password Recovery

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.services.password_reset_service import PasswordResetService
import json

password_reset_service = PasswordResetService()

@csrf_exempt
def request_password_reset(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')

        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        reset_link = password_reset_service.request_password_reset(email)
        if reset_link:
            return JsonResponse({'message': 'Password reset link sent to your email'}, status=200)
        return JsonResponse({'error': 'No account found with this email'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token')
        new_password = data.get('new_password')

        if not token or not new_password:
            return JsonResponse({'error': 'Token and new password are required'}, status=400)

        success = password_reset_service.reset_password(token, new_password)
        if success:
            return JsonResponse({'message': 'Password has been reset successfully'}, status=200)
        return JsonResponse({'error': 'Invalid or expired token'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)