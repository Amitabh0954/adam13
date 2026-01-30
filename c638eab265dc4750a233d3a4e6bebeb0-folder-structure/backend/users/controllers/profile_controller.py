# Epic Title: Profile Management

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.services.profile_service import ProfileService
from django.contrib.auth.models import User
import json

profile_service = ProfileService()

@csrf_exempt
def view_profile(request):
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            profile_data = profile_service.get_profile(user)
            return JsonResponse(profile_data, status=200)
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            data = json.loads(request.body)
            updated_profile = profile_service.update_profile(user, data)
            return JsonResponse(updated_profile, status=200)
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)