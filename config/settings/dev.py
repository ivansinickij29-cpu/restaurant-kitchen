# SECURITY WARNING: don't run with debug turned on in production!
import os
from .base import *


DEBUG = os.environ.get("DEBUG", "") != "False"

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}