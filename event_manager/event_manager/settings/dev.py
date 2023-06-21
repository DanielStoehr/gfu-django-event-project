from event_manager.settings.base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INSTALLED_APPS.extend(["debug_toolbar", "django_extensions"])
MIDDLEWARE.extend(["debug_toolbar.middleware.DebugToolbarMiddleware"])
INTERNAL_IPS = ("127.0.0.1",)
