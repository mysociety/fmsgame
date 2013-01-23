# Django settings for fmsgame project.

# Some special mysociety preamble in order to get hold of our config
# file conf/general
import os
import sys
package_dir = os.path.abspath(os.path.split(__file__)[0])

from config_local import config  # put settings in config_local if you're not running in a fill mysociety vhost
SERVE_STATIC_FILES = True

# Now follows the normal Django stuff.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

FMS_URL           = config.get('FMSGAME_FMS_URL')

DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.postgresql_psycopg2',
        'NAME':     config.get('FMSGAME_DB_NAME'),
        'USER':     config.get('FMSGAME_DB_USER'),
        'PASSWORD': config.get('FMSGAME_DB_PASS'),
        'HOST':     config.get('FMSGAME_DB_HOST'),
        'PORT':     config.get('FMSGAME_DB_PORT'),
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(package_dir, "../web/static/")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = config.get('DJANGO_SECRET_KEY')

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# where should user go to start openid login/registration process.
# For now limit it only to Google accounts.
# Note that django-openid is outdated and might break for other openid
# providers: http://stackoverflow.com/questions/3145453
OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'

# create users if they don't exist
OPENID_CREATE_USERS = True

# If user details have changed then update them on login
OPENID_UPDATE_DETAILS_FROM_SREG = True

# openid related urls
LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/geolocate'


ROOT_URLCONF = 'fmsgame_project.urls'

TEMPLATE_DIRS = (
    os.path.join(package_dir, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django_openid_auth',
    'scoreboard',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)
