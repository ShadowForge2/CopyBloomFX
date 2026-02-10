"""
InfinityFree Settings for Crypto Investment Platform - FINAL VERSION
"""
from .settings import *
import os

# SECURITY
DEBUG = False
ALLOWED_HOSTS = ['copybloomfx.great-site.net', 'www.copybloomfx.great-site.net']
SECRET_KEY = os.environ.get('SECRET_KEY', 'AxG@=7"bkkjJ.:h{aaYGMeRc@NKQ*I)cU"~y1,>5\-;ymBDAW')

# DATABASE (InfinityFree uses MySQL) - YOUR REAL CREDENTIALS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'if0_41040096_XXX'),
        'USER': os.environ.get('DB_USER', 'if0_41040096'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'SSY4n1mZcU'),
        'HOST': os.environ.get('DB_HOST', 'sql212.infinityfree.com'),
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# STATIC FILES (InfinityFree specific) - FIXED PATHS
STATIC_URL = '/static/'
STATIC_ROOT = '/storage/ssd5/123/12345678/htdocs/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/storage/ssd5/123/12345678/htdocs/media/'

# CACHE (File-based for InfinityFree)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/storage/ssd5/123/12345678/cache/',
    }
}

# SESSIONS
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/storage/ssd5/123/12345678/sessions/'

# EMAIL (InfinityFree email)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.epizy.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'noreply@copybloomfx.great-site.net')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your-email-password')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@copybloomfx.great-site.net')

# SECURITY HEADERS
SECURE_SSL_REDIRECT = False  # InfinityFree handles SSL
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_FRAME_OPTIONS = 'DENY'
X_FRAME_OPTIONS = 'DENY'

# SESSION COOKIES
SESSION_COOKIE_SECURE = False  # Will be True once SSL is set up
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = False  # Will be True once SSL is set up
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/storage/ssd5/123/12345678/logs/django.log',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'crypto': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# PAYSTACK (Use your live keys) - FIXED CALLBACK URL
PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY', 'sk_live_02a118d0481e927f0a3c433bdff9a049485fc19c')
PAYSTACK_PUBLIC_KEY = os.environ.get('PAYSTACK_PUBLIC_KEY', 'pk_live_97a8f90d2f9f86c18bac7a36a7b558c26f2392a9')
PAYSTACK_CALLBACK_URL = 'https://copybloomfx.great-site.net/paystack/callback/'

# PERFORMANCE
CONN_MAX_AGE = 60

# Disable some features for free hosting
USE_S3 = False
CELERY_BROKER_URL = None
CELERY_RESULT_BACKEND = None
