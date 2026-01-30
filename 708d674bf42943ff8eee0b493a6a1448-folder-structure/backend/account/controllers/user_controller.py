# Epic Title: User Registration

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.services.user_service import UserService
import json

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