"""
Django settings for labobooks project.

Generated by 'django-admin startproject' using Django.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import dirname
BASE_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (os.environ.get('DJANGO_SECRET_KEY') or
              'ki#5=8$)1xtp98zoufjbfvmd7!)m8k7@i-*)3)g!0m$a5+2oy1')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third-party programs
    'account',
    'rest_framework',
    'bootstrapform',
    'social_django',
    'oauth2_provider',
    'raven.contrib.django.raven_compat',

    # Project applications
    'accountapp',
    'core',
    'coreapi',
    'slackapp',
    'webfront',

    # third-party templates
    'pinax_theme_bootstrap',
]

MIDDLEWARE = [
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'core.middleware.DisableClientSideCachingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'labobooks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'pinax_theme_bootstrap.context_processors.theme',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'labobooks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 6}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

X_FRAME_OPTIONS = 'DENY'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(name)s %(levelname)s %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
        }
    },
    'loggers': {
        'newrelic': {
            'propagate': False
        },
        'django.request': {
            'level': 'ERROR',  # ignore 404 warinig
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

RAVEN_CONFIG = {'dsn': os.environ.get("SENTRY_DSN", "")}

CSP_DEFAULT_SRC = (
    "'self'", "'unsafe-inline'", "'unsafe-eval'", 'cdnjs.cloudflare.com', 'labobooks.com')
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", 'cdnjs.cloudflare.com', 'fonts.googleapis.com')
CSP_IMG_SRC = ("'self'", 'labobooks.com', 'images-fe.ssl-images-amazon.com', 'via.placeholder.com')
CSP_FONT_SRC = ("'self'", 'cdnjs.cloudflare.com', 'fonts.googleapis.com', 'fonts.gstatic.com')
CSP_REPORT_ONLY = True
CSP_REPORT_URI = os.environ.get("CSP_REPORT_URI", "")


####################
# Your application #
####################

EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

SITE_ID = 1
LOGIN_REDIRECT_URL = '/dashboard'

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_URL = '/accounts/'

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('SOCIAL_AUTH_TWITTER_SECRET')

AMAZON_PRODUCT_ADVERTISING_ID = os.environ.get('AMAZON_PRODUCT_ADVERTISING_ID')
AMAZON_PRODUCT_ADVERTISING_SECRET = os.environ.get('AMAZON_PRODUCT_ADVERTISING_SECRET')
AMAZON_ASSOCIATE_TAG = os.environ.get('AMAZON_ASSOCIATE_TAG')
AMAZON_ASSOCIATE_REGION = 'JP'

RAKUTEN_APPLICATION_ID = os.environ.get('RAKUTEN_APPLICATION_ID')

OPENBD_API = 'https://api.openbd.jp/v1/get'

MULTIPLE_ORGANIZATIONS = False
