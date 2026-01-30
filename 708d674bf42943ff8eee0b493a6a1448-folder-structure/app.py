# Epic Title: User Registration

import os
import django
from django.core.management import execute_from_command_line
from django.conf import settings
from django.urls import path
from django.apps import apps
from account.controllers.user_controller import register

settings.configure(
    DEBUG=os.getenv('DEBUG', 'on') == 'on',
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'account',
    ],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
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
)

apps.populate(settings.INSTALLED_APPS)

urlpatterns = [
    path('register/', register),
]

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)
    django.setup()
    execute_from_command_line(sys.argv)