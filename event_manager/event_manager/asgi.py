"""
ASGI config for event_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from pathlib import Path

import environ
from django.core.asgi import get_asgi_application

environ.Env.read_env(Path(__file__).resolve().parent.parent / ".env")
env = environ.Env()
settings_module = env("SETTINGS_MODULE")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_asgi_application()
