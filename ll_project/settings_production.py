"""
Production settings for PythonAnywhere deployment.
"""

from .settings import *
import os

# Production settings
DEBUG = False

# You'll need to update this with your actual PythonAnywhere username
# Format: ['yourusername.pythonanywhere.com']
ALLOWED_HOSTS = ['danjwilko.pythonanywhere.com']

# Static files configuration for PythonAnywhere
STATIC_ROOT = '/home/danjwilko/learning_log/static'

# Database configuration (SQLite is fine for learning projects)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/danjwilko/learning_log/db.sqlite3',
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Generate a new secret key for production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-4yd&4)f^uhcj0lc)#^9*-ldozxg^wpm9nn+f7k8d7(^$gal2b%')
