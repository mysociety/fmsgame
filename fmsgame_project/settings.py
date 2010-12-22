# Django settings for fmsgame_project project.

# Some special mysociety preamble in order to get hold of our config
# file conf/general
import os
import sys
package_dir = os.path.abspath(os.path.split(__file__)[0])

paths = (
    os.path.normpath(package_dir + "/../pylib"),
    os.path.normpath(package_dir + "/../commonlib/pylib"),
    )

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

try:
    from config_local import config  # put settings in config_local if you're not running in a fill mysociety vhost
    SERVE_STATIC_FILES = True
except ImportError:
    SERVE_STATIC_FILES = False
    from mysociety import config
    config.set_file(os.path.abspath(package_dir + "/../conf/general"))

# Now follows the normal Django stuff.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE   = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME     = config.get('FMSGAME_DB_NAME')
DATABASE_USER     = config.get('FMSGAME_DB_USER')
DATABASE_PASSWORD = config.get('FMSGAME_DB_PASS')
DATABASE_HOST     = config.get('FMSGAME_DB_HOST')
DATABASE_PORT     = config.get('FMSGAME_DB_PORT')

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
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fic59b+!ni(xw2+b)tn!4t5fv#a0jc%rq@10y2(+@f8=*+@9gf'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',    
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
LOGIN_REDIRECT_URL = '/FIXME'


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
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    )
