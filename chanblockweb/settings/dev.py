from .base import *



ALLOWED_HOSTS = ['www.chanblock.com','chanblock.com']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
SECURE_SSL_REDIRECT = TRUE

STATIC_ROOT= 'static'