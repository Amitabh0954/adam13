# Epic Title: Profile Management

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_account_management.services.profile_service import ProfileService
import json

profile_service = ProfileService()

@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        date_of_birth = data.get('date_of_birth')
        
        profile = profile_service.update_profile(email, first_name, last_name, date_of_birth)
        if profile:
            return JsonResponse({'message': 'Profile updated successfully'}, status=200)
        else:
            return JsonResponse({'error': 'User not found or invalid data'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)