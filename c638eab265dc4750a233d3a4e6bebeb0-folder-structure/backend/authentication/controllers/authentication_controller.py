# Epic Title: User Login

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from authentication.services.authentication_service import AuthenticationService
import json

authentication_service = AuthenticationService()

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        session_key = request.session.session_key

        user = authentication_service.login(username, password, session_key)
        if user:
            request.session['user_id'] = user.id
            return JsonResponse({'message': 'User logged in successfully'}, status=200)
        return JsonResponse({'error': 'Invalid username or password'}, status=401)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        authentication_service.logout(session_key)
        return JsonResponse({'message': 'User logged out successfully'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)