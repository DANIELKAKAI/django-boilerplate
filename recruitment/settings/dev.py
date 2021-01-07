import os
from .base import INSTALLED_APPS, MIDDLEWARE, BASE_DIR

ALLOWED_HOSTS = ["*"]

DEBUG = True
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(
    0,
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
