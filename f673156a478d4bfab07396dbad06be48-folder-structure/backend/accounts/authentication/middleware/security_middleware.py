# Epic Title: User Login

from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.core.cache import cache
from django.conf import settings
from django.http import JsonResponse

class LimitLoginAttemptsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and '/login/' in request.path:
            email = request.POST.get('email')
            if email:
                cache_key = f'login_attempts_{email}'
                attempts = cache.get(cache_key, 0)

                if attempts >= settings.MAX_LOGIN_ATTEMPTS:
                    return JsonResponse({'error': 'Too many login attempts, try again later'}, status=429)

                cache.set(cache_key, attempts + 1, settings.LOGIN_ATTEMPTS_TIMEOUT)

    def process_response(self, request, response):
        if response.status_code == 200 and request.method == 'POST' and '/login/' in request.path:
            email = request.POST.get('email')
            if email:
                cache_key = f'login_attempts_{email}'
                cache.delete(cache_key)
        return response

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            limit = settings.SESSION_TIMEOUT
            last_activity = request.session.get('last_activity', None)
            current_time = int(time.time())

            if last_activity and (current_time - last_activity) > limit:
                logout(request)
                return JsonResponse({'error': 'Session timed out'}, status=440)

            request.session['last_activity'] = current_time