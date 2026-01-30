# Epic Title: User Registration

import os
import django
from django.core.management import execute_from_command_line
from django.conf import settings
from django.urls import path
from django.apps import apps
from accounts.registration.controllers.registration_controller import register_user
from accounts.authentication.controllers.authentication_controller import login_user, logout_user

settings.configure(
    DEBUG=os.getenv('DEBUG', 'on') == 'on',
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'accounts',
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
)

apps.populate(settings.INSTALLED_APPS)

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('logout/', logout_user),
]

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)
    django.setup()
    execute_from_command_line(sys.argv)