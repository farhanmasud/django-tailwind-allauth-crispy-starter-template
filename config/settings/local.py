from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# whitenoise and django debug toolbar for development
INSTALLED_APPS = (
    ["whitenoise.runserver_nostatic"]
    + INSTALLED_APPS
    + ["debug_toolbar", "django_browser_reload", "django_extensions"]
)
INTERNAL_IPS = [
    "127.0.0.1",
]

# email backend for testing
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# middleware for django debug toolbar
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
