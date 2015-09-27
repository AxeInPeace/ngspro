"""
Django settings for ngspro project.
"""

import os
from lib.settings_local import SettingsLocal
#import DATABASES from /home/ngspro/var/etc/local_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iuv^=%2b+apns!z%+t6za+-+#ppobpv^cex0^8_hqrl+td7_m!'

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
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'django',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


TEMPLATE_DIRS = (
    '/home/ngspro/.www/tpl/',
)

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR,  'tpl'),  # ты еще t назови, чего так длинно-то?
#)

ROOT_URLCONF = 'lib.urls'

WSGI_APPLICATION = 'lib.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/'
STATIC_ROOT = '/home/ngspro/.www/static/'

#распишите в settingslocal это, а?

#STATIC_URL = SettingsLocal.STATIC_URL
#STATICFILES_DIRS = SettingsLocal.STATICFILES_DIR
