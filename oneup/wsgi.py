"""
WSGI config for oneup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# load environment settings
try:
    from settings.environment import environment
except:
    environment = ''

if environment in ['development','testing','production']:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oneup.settings.%s' % environment)
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oneup.settings.default')

application = get_wsgi_application()
