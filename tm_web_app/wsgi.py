"""
WSGI config for tm_web_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'tm_web_app.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'tm_web_app.settings'

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tm_web_app.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
