from labobooks.settings import *  # NOQA
import os
import dj_database_url


ALLOWED_HOSTS = ['*']

DEBUG = bool(os.environ.get('DEBUG'))

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
# SECURE_SSL_REDIRECT = True
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')

SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': dj_database_url.config()
}

LOGGING.update({'root': {'handlers': ['console', 'sentry']}})  # NOQA
