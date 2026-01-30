# Epic Title: Password Recovery

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_account_management.services.password_reset_service import PasswordResetService
import json

password_reset_service = PasswordResetService()

@csrf_exempt
def request_reset_link(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        
        token = password_reset_service.request_password_reset(email)
        if token:
            return JsonResponse({'message': 'Password reset link sent'}, status=200)
        else:
            return JsonResponse({'error': 'Email not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token')
        new_password = data.get('new_password')
        
        if password_reset_service.reset_password(token, new_password):
            return JsonResponse({'message': 'Password reset successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid or expired token'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)