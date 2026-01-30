# Epic Title: Password Recovery

import os
import django
from django.core.management import execute_from_command_line
from django.conf import settings
from django.urls import path
from django.apps import apps

from backend.services.user_account.user_registration_service import UserRegistrationService
from backend.services.user_account.user_login_service import UserLoginService
from backend.services.user_account.password_reset_service import PasswordResetService
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

settings.configure(
    DEBUG=os.getenv('DEBUG', 'on') == 'on',
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'backend',
    ],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    ],
    ROOT_URLCONF=__name__,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DATABASE_NAME', 'mydatabase'),
            'USER': os.getenv('DATABASE_USER', 'mydatabaseuser'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD', 'mypassword'),
            'HOST': os.getenv('DATABASE_HOST', 'localhost'),
            'PORT': os.getenv('DATABASE_PORT', '3306'),
        }
    },
    FRONTEND_URL=os.getenv('FRONTEND_URL', 'http://localhost:3000'),
    DEFAULT_FROM_EMAIL=os.getenv('DEFAULT_FROM_EMAIL', 'noreply@example.com'),
    SESSION_TIMEOUT=1800, # 30 minutes in seconds
)

apps.populate(settings.INSTALLED_APPS)

user_registration_service = UserRegistrationService()
user_login_service = UserLoginService()
password_reset_service = PasswordResetService()

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not email or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)
        
        success, message = user_registration_service.register_user(username, email, password)
        
        if success:
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        else:
            return JsonResponse({'error': message}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)
        
        success, message, user_data = user_login_service.login_user(email, password)
        
        if success:
            request.session['user'] = user_data
            return JsonResponse({'message': message}, status=200)
        else:
            return JsonResponse({'error': message}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def logout_user(request):
    if 'user' in request.session:
        del request.session['user']
        return JsonResponse({'message': 'Logout successful'}, status=200)
    return JsonResponse({'error': 'User not logged in'}, status=400)

@csrf_exempt
def request_password_reset(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        email = data.get('email')
        
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)
        
        success, message = password_reset_service.request_password_reset(email)
        
        if success:
            return JsonResponse({'message': message}, status=200)
        else:
            return JsonResponse({'error': message}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def reset_password(request, token):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        new_password = data.get('new_password')
        
        if not new_password:
            return JsonResponse({'error': 'New password is required'}, status=400)
        
        success, message = password_reset_service.reset_password(token, new_password)
        
        if success:
            return JsonResponse({'message': message}, status=200)
        else:
            return JsonResponse({'error': message}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('logout/', logout_user),
    path('request-password-reset/', request_password_reset),
    path('reset-password/<str:token>/', reset_password, name='reset_password'),
]

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)
    django.setup()
    execute_from_command_line(sys.argv)