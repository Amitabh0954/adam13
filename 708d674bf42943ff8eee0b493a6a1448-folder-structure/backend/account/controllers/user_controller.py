# Epic Title: User Login

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.services.user_service import UserService
import json
from django.contrib.auth import login, logout

user_service = UserService()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if not email or not username or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        user = user_service.register_user(email, username, password)
        if user:
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        return JsonResponse({'error': 'User with this email or username already exists'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        user = user_service.authenticate_user(email, password)
        if user:
            login(request, user)
            return JsonResponse({'message': 'User logged in successfully'}, status=200)
        return JsonResponse({'error': 'Invalid email or password'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'User logged out successfully'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)