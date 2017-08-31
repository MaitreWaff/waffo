"""
Django settings for waffo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)

PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '14=(=$_xasqw$24ay_p(h7-pu*j@-8ev6lm2gxbbszg93v^i$9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'blog',
    'profiles',
    'waff',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.sites',
    # 'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 'bootstrap3',
    # 'django_forms_bootstrap',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'waffo.urls'

WSGI_APPLICATION = 'waffo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-fr' # 'en-us'

TIME_ZONE = 'Africa/Douala' # 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'assets')

STATICFILES_DIRS = (
    ("assets", STATIC_PATH),
    # STATIC_PATH,
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
LOGIN_URL='/account/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Add this to tell Django where to redirect after
# successful login

LOGIN_REDIRECT_URL = '/blog/feed-news/'

ROOT_URLCONF = 'waffo.urls'


# Settings for django-regitration
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
# REGISTRATION_DEFAULT_FROM_EMAIL =
# REGISTRATION_EMAIL_HTML = True # Email will be send in html
REGISTRATION_AUTO_LOGIN = True # Users automatically log in when they click on the activation link in their email.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
