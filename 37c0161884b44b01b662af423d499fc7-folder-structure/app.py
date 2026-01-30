# Epic Title: User Registration

import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

if __name__ == "__main__":
    execute_from_command_line()