# Epic Title: User Login

from accounts.authentication.repositories.user_repository import UserRepository
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from typing import Optional

class AuthenticationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def login_user(self, request, email: str, password: str) -> Optional[User]:
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return user
        return None

    def logout_user(self, request):
        logout(request)