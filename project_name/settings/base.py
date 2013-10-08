"""
This is your project's main settings file that can be committed to your
repo. If you need to override a setting locally, use local.py
"""

import os
import logging
import djcelery
import dj_database_url

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


# Environment
# =======================================================================
def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

SITE_ID = 1
# SECURITY WARNING: don't run with debug turned on in production!
# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = False

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = False

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
# =======================================================================


#Path
# =======================================================================
# Your project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../")
# =======================================================================


# Other django settings
# =======================================================================
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
# Defines the views served for root URLs.
ROOT_URLCONF = '{{ project_name }}.urls'
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'
SUPPORTED_NONLOCALES = ['media', 'admin', 'static']
SECRET_KEY = get_env_setting('SECRET_KEY')
# The WSGI Application to use for runserver
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
FILE_UPLOAD_PERMISSIONS = 0664
# =======================================================================


# Apps & Middlewares & Bcrypt
# =======================================================================
INSTALLED_APPS = (
    # Django contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.staticfiles',

    # Third-party apps, patches, fixes
    'djcelery',
    'debug_toolbar',
    'compressor',
    'django_gravatar',
    'raven.contrib.django.raven_compat',
    #'debug_toolbar_user_panel',

    # Database migrations
    'south',

    # Application base, containing global templates.
    'base',

    # Local apps, referenced via appname
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Place bcrypt first in the list, so it will be the default password hashing
# mechanism
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)
# =======================================================================


# Sessions
# =======================================================================
# By default, be at least somewhat secure with our session cookies.
SESSION_COOKIE_HTTPONLY = True
# Set this to true if you are using https
SESSION_COOKIE_SECURE = False
# =======================================================================


# Media User uploaded files
# =======================================================================
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.example.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
# =======================================================================


# Static Media
# =======================================================================
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# URL prefix for static files.
# Example: "http://media.example.com/static/"
STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
# =======================================================================


#Template Settings
# =======================================================================
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
]

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
# =======================================================================


#Debug Toolbar
# =======================================================================
def custom_show_toolbar(request):
    """ Only show the debug toolbar to users with the superuser flag. """
    return request.user.is_superuser

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'HIDE_DJANGO_SQL': True,
    'TAG': 'body',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
}

DEBUG_TOOLBAR_PANELS = (
    #'debug_toolbar_user_panel.panels.UserPanel',
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
# =======================================================================


# Production database connections
# =======================================================================
DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}
# =======================================================================

# Email settings
# =======================================================================
ADMINS = (
    ('andus', 'anduslim@gozolabs.com'),
)
DEBUG_EMAILS = ['anduslim@gozolabs.com']
MANAGERS = ADMINS

EMAIL_BACKEND = 'django_ses.SESBackend'
SERVER_EMAIL = "webmaster@example.com"
DEFAULT_FROM_EMAIL = SERVER_EMAIL
SYSTEM_EMAIL_PREFIX = "[{{ project_name }}]"
# =======================================================================

# Amazon Services Settings (S3)
# =======================================================================
AWS_ACCESS_KEY_ID = get_env_setting['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = get_env_setting['AWS_SECRET_ACCESS_KEY']
#S3
if not DEBUG:
    S3_BUCKET_NAME = 'shipsmart-assets'
    # Production and test settings
    DEFAULT_FILE_STORAGE = 's3storages.MediaStorage'
    STATICFILES_STORAGE = 's3storages.StaticStorage'
    STATIC_URL = 'https://{0}.s3.amazonaws.com/assets/'.format(S3_BUCKET_NAME)
    ADMIN_MEDIA_PREFIX = '{0}admin'.format(STATIC_URL)
    MEDIA_URL = 'https://{0}/media/'.format(S3_BUCKET_NAME)
# =======================================================================


# CELERY CONFIGURATION
# =======================================================================
djcelery.setup_loader()

CELERY_ALWAYS_EAGER = False  # required to activate celeryd

BROKER_TRANSPORT = 'amqplib'
BROKER_URL = ''
# The maximum number of connections that can be open in the connection pool
BROKER_POOL_LIMIT = 0

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'database'
# Task hard time limit in seconds. The worker processing the task will
# be killed and replaced with a new one when this is exceeded.
CELERYD_TASK_TIME_LIMIT = 60 * 5
CELERYD_CONCURRENCY = 1
CELERYD_MAX_TASKS_PER_CHILD = 4
# =======================================================================

INTERNAL_IPS = ('127.0.0.1')

# Enable these options for memcached
#CACHE_BACKEND= "memcached://127.0.0.1:11211/"
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY=True

# Set this to true if you use a proxy that sets X-Forwarded-Host
#USE_X_FORWARDED_HOST = False


## Log settings
# =======================================================================
LOG_LEVEL = logging.INFO
HAS_SYSLOG = True
SYSLOG_TAG = "http_app_{{ project_name }}"  # Make this unique to your project.
# Remove this configuration variable to use your custom logging configuration
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'loggers': {
        '{{ project_name }}': {
            'handlers': ['console'],
            'level': "DEBUG"
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        }
    },
}

RAVEN_CONFIG = {
    'dsn': '',
}


# Common Event Format logging parameters
#CEF_PRODUCT = '{{ project_name }}'
#CEF_VENDOR = 'Your Company'
#CEF_VERSION = '0'
#CEF_DEVICE_VERSION = '0'
# =======================================================================
