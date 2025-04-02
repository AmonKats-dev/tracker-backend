"""
WSGI config for muk_support_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Check if running on Railway
if os.environ.get('RAILWAY_ENVIRONMENT'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muk_support_backend.settings_railway')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muk_support_backend.settings')

application = get_wsgi_application()
