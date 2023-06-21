"""
WSGI config for event_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

import environ
from django.core.wsgi import get_wsgi_application

environ.Env.read_env(Path(__file__).resolve().parent.parent / ".env")
env = environ.Env()
settings_module = env("SETTINGS_MODULE")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
