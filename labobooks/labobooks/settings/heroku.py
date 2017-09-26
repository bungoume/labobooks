from labobooks.settings import *  # NOQA
import dj_database_url


ALLOWED_HOSTS = ['*']

DEBUG = False

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': dj_database_url.config()
}

LOGGING.update({'root': {'handlers': ['console', 'sentry']}})
