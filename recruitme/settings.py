"""
Copyright (C) 2019 René Dohmen <acidjunk@gmail.com>

Licensed under the GNU GENERAL PUBLIC LICENSE Version 3
A copy of the LICENSE is included in the project.

Settings for RecruitMe
======================
- Defaults should be ok for dev purposes
- DB,SECRET,MEDIA_LOCATION should be configured with ENV variables in production
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'VERY_SECRET_OVERRULE_FOR_PROD!!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', '0') not in ('', '0'))

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'suit',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'sitetree',
    'django_gravatar',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
    'recruitme.apps.social_login',
    'recruitme.apps.static_page',
    'recruitme.apps.utils',
    'recruitme.apps.skills',
    'recruitme.apps.developers',
    'recruitme.apps.recruiters',
    'recruitme.navigation',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
    'social.backends.linkedin.LinkedinOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'recruitme.urls'

WSGI_APPLICATION = 'recruitme.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Default Database (overrule it for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'recruitme'),
        'USER': os.environ.get('DB_USER', 'recruitme'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'recruitme'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '',
    }
}

CRISPY_TEMPLATE_PACK='semantic-ui'

LOGIN_URL = '/login'

LOGIN_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

#LANGUAGE_CODE = 'nl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '../assets'),
)
STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../static')  # third party package assets
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../media')  # third party package assets

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATIC_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages')


gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('nl', gettext('Dutch')),
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Recruit Me Admin',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}

from recruitme.social_config import *

"""
Disables the migration module when an environment setting "DISABLE_MIGRATIONS"
is set to '1'.

Inspired by https://gist.github.com/NotSqrt/5f3c76cd15e40ef62d09
and https://github.com/henriquebastos/django-test-without-migrations

Unfortunately we can't use the django-test-without-migrations as it breaks
pycharms test runner.

Warning: to use it in development you have to provide an extra OS Environment setting:
bash:
export DISABLE_MIGRATIONS=1
or
windows:
set DISABLE_MIGRATIONS=1
"""


class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "nomigrations"


if os.getenv('DISABLE_MIGRATIONS') == '1':
    print("disabling migrations")
    MIGRATION_MODULES = DisableMigrations()
