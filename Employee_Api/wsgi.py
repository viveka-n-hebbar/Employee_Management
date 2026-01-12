"""
WSGI config for Employee_Api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# --- 1. Set Django settings module first ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Employee_Api.settings')

# --- 2. Initialize Django application ---
application = get_wsgi_application()

# --- 3. Run test admin creation after Django is ready ---
from employees.create_test_admin import run as create_admin
create_admin()
