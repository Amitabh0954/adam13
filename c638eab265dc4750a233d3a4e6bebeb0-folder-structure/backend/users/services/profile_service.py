# Epic Title: Profile Management

from django.contrib.auth.models import User
from typing import Dict, Any

class ProfileService:

    def get_profile(self, user: User) -> Dict[str, Any]:
        return {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

    def update_profile(self, user: User, data: Dict[str, Any]) -> Dict[str, Any]:
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.save()
        return self.get_profile(user)