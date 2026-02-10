from .settings import *
import os

# SECURITY
DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# DATABASE - PythonAnywhere MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$database_name',
        'USER': 'yourusername',
        'PASSWORD': 'your_database_password',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = '/home/yourusername/mysite/static/'

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/yourusername/mysite/media/'

# PAYSTACK CONFIGURATION
PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY', 'sk_live_02a118d0481e927f0a3c433bdff9a049485fc19c')
PAYSTACK_PUBLIC_KEY = os.environ.get('PAYSTACK_PUBLIC_KEY', 'pk_live_97a8f90d2f9f86c18bac7a36a7b558c26f2392a9')
PAYSTACK_CALLBACK_URL = f"https://yourusername.pythonanywhere.com/paystack/callback/"

# SECURITY SETTINGS
SECURE_SSL_REDIRECT = False  # PythonAnywhere handles SSL
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
