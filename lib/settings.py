# encoding=utf-8
"""
Django settings for ngspro project.
"""

import os
import local_settings
#import DATABASES from /home/ngspro/var/etc/local_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = local_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lib.mapbaloon',
    'lib.auth',
    'lib.photo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


DATABASES = local_settings.DATABASES 


TEMPLATE_DIRS = (
    '/home/ngspro/.www/tpl/',
)

ROOT_URLCONF = 'lib.urls'

WSGI_APPLICATION = 'lib.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = local_settings.STATIC_URL
STATIC_ROOT = local_settings.STATIC_ROOT
