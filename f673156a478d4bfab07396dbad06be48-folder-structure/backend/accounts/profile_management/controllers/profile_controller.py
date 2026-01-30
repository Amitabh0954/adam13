# Epic Title: Profile Management

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@login_required
@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')

        if not first_name or not last_name or not email:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return JsonResponse({'message': 'Profile updated successfully'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)