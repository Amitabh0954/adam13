# Epic Title: User Login

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_account_management.services.session_service import SessionService
import json

session_service = SessionService()

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        session = session_service.login_user(email, password)
        if session:
            return JsonResponse({'message': 'Logged in successfully', 'session_id': session.session_id}, status=200)
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)