from .settings import *
import os
import dj_database_url

# SECURITY
DEBUG = False
ALLOWED_HOSTS = ['*']  # Render will set the correct hostname
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# DATABASE - Render PostgreSQL
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = '/staticfiles/'

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = '/mediafiles/'

# PAYSTACK CONFIGURATION
PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY', '')
PAYSTACK_PUBLIC_KEY = os.environ.get('PAYSTACK_PUBLIC_KEY', '')
PAYSTACK_CALLBACK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'your-app.onrender.com')}/paystack/callback/"

# CORS HEADERS (if needed)
CORS_ALLOWED_ORIGINS = [
    "https://" + os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'your-app.onrender.com'),
]

# SECURITY SETTINGS
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# BASE URL for referral links
BASE_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'your-app.onrender.com')}"

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/tmp/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
