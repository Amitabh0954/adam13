# Epic Title: User Login

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_account_management.services.user_service import UserService
import json

user_service = UserService()

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = user_service.register_user(username, email, password)
        if user:
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Email already in use'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = user_service.login_user(email, password)
        if user:
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)