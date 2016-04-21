"""
Django settings for idea project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# DEV
SECRET_KEY = '^-k1d$y2mv_x+n06eyf-!l9&#n0&)5-hhv)h*r=(!c6l8!ad++'

# SECURITY WARNING: don't run with debug turned on in production!
# DEV
# DEBUG = True
# PROD
DEBUG=True

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
    #'django_ace',
    'pldata',
    'student',
    'concept',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'concept.mymiddleware.MyExceptionMiddleware'
)

ROOT_URLCONF = 'idea.urls'

WSGI_APPLICATION = 'idea.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# pour la prod postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASS'],
        'HOST': '',
        'PORT': '5432',
#        'OPTIONS': {
#          'autocommit': True,
#        },
   }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),
)
SETTINGS_PATH= os.path.realpath(os.path.dirname(__file__))



TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

ADMINS = (
	("patrice Herault", 'hp@univ-mlv.fr'),
	("dominique Revuz", 'dr@univ-mlv.fr'),
)
