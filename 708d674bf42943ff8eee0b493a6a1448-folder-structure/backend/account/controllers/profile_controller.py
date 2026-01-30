# Epic Title: Profile Management

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.services.profile_service import ProfileService
from django.contrib.auth.decorators import login_required
import json

profile_service = ProfileService()

@csrf_exempt
@login_required
def update_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')

        if not username or not first_name or not last_name or not email:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        user = profile_service.update_profile(request.user, username, first_name, last_name, email)
        if user:
            return JsonResponse({'message': 'Profile updated successfully'}, status=200)
        return JsonResponse({'error': 'Failed to update profile'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)