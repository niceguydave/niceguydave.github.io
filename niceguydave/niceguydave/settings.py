# system
from os import environ
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# core django
from django.core.exceptions import ImproperlyConfigured

# third party
from configurations import Configuration

# Reinclude this variables if you wish to use multiple languages
# gettext = lambda s: s


def _get_env_variable(var_name):
    """
    Get the environment variable or return exception."""
    try:
        return environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
    raise ImproperlyConfigured(error_msg)


class BaseSettings(Configuration):
    """
    Common settings and globals."""

    ########## PATH CONFIGURATION
    # Absolute filesystem path to the Django project directory:
    DJANGO_ROOT = dirname(dirname(abspath(__file__)))
    REPO_ROOT = dirname(DJANGO_ROOT)

    # Absolute filesystem path to the top-level project folder:
    SITE_ROOT = DJANGO_ROOT

    # Site name:
    SITE_NAME = basename(DJANGO_ROOT)

    # Add our project to our pythonpath.
    # This way we don't need to type our project name in our dotted
    # import paths
    path.append(DJANGO_ROOT)
    ########## END PATH CONFIGURATION

    ########## DEBUG CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = False

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG
    ########## END DEBUG CONFIGURATION

    ########## MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ('Administrator', 'admin@admin.com'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    ########## END MANAGER CONFIGURATION

    ########## DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
    ########## END DATABASE CONFIGURATION

    ########## GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'Europe/London'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'en'

    LANGUAGES = [
        ('en', 'English'),
        #('de', 'German'),
        #('es', 'Spanish'),
        #('pt', 'Portuguese'),
        #('it', 'Italian'),
        #('ja', 'Japanese'),
        #('zh-cn', 'Chinese simplified'),
        #('nl', 'Dutch'),
    ]

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    ########## END GENERAL CONFIGURATION

    ########## MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = normpath(join(SITE_ROOT, 'assets/media'))

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    ########## END MEDIA CONFIGURATION

    ########## STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = normpath(join(SITE_ROOT, 'assets/static'))

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        normpath(join(SITE_ROOT, 'static')),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    ########## END STATIC FILE CONFIGURATION

    ########## SECRET CONFIGURATION
    SECRET_KEY = _get_env_variable('DJANGO_SECRET_KEY')

    ########## FIXTURE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        normpath(join(SITE_ROOT, 'fixtures')),
    )
    ########## END FIXTURE CONFIGURATION

    ########## TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        'sekizai.context_processors.sekizai',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        normpath(join(SITE_ROOT, 'templates')),
    )
    ########## END TEMPLATE CONFIGURATION

    ########## MIDDLEWARE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    ########## END MIDDLEWARE CONFIGURATION

    ########## URL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
    ROOT_URLCONF = '%s.urls' % SITE_NAME
    ########## END URL CONFIGURATION

    ########## APP CONFIGURATION
    THIRD_PARTY_APPS = (
        # We are overriding the look 'n' feel of the admin interface.
        # For this to work 'suit' needs to be installed above
        # 'django.contrib.admin'. This is why this import is here!
        'suit',
    )

    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
    )

    THIRD_PARTY_APPS += (
        'django_extensions',
        'sekizai',
        'south'
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        'niceguydave',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
    ########## END APP CONFIGURATION

    ########## LOGGING CONFIGURATION
    # A logging configuration that in dev writes log messages to the console.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        # Formatting of messages.
        'formatters': {
            # Don't need to show the time when logging to console.
            'console': {
                'format': '%(levelname)s %(module)s.%(funcName)s (%(lineno)d) %(message)s'
            },
            'textlog': {
                'format': '%(levelname)s %(asctime)s %(module)s.%(funcName)s (%(lineno)d) %(message)s'
            },
        },
        # Used by handlers to filter down the logs sent to it.
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        # The handlers decide what we should do with a logging message - do we email
        # it, ditch it, or write it to a file?
        'handlers': {
            # Writing to console. Use only in dev.
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            # Mail error-level logs to the admins.
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            # Send logs to /dev/null.
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
            },
        },
        # Loggers decide what is logged.
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
            # In the requests, all errors get emailed to admins.
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            # logging of SQL statements. Default is to ditch them (send them to
            # null). Note that this logger only works if DEBUG = True.
            'django.db.backends': {
                'handlers': ['null'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }

    # When running South, it generates lots of DEBUG messages - we don't
    # need to see these.
    import logging
    south_logger = logging.getLogger('south')
    south_logger.setLevel(logging.INFO)

    ########## END LOGGING CONFIGURATION

    ########## WSGI CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    #WSGI_APPLICATION = 'wsgi.application'
    ########## END WSGI CONFIGURATION

    ########## TEST SPECIFIC

    SOUTH_TESTS_MIGRATE = False

    # If the tests from some 3rd party app keep failing when used with this
    # project, add them here so that they always get skipped.
    TEST_RUNNER = "ignoretests.DjangoIgnoreTestSuiteRunner"
    IGNORE_TESTS = (
        'django.contrib.auth',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django_extensions',
        'sekizai',
    )


class DevSettings(BaseSettings):
    """Override base settings with defaults suitable for a development
    environment.

    Note that this is the default settings selected when running
    a checkout of the project."""

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'niceguydave_development',
            'USER': 'vagrant',
            'PASSWORD': _get_env_variable('POSTGRES_PASSWORD'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

    #############################
    # used by developer toolbar #
    #############################

    #BaseSettings.MIDDLEWARE_CLASSES += (
        #'debug_toolbar.middleware.DebugToolbarMiddleware',
    #)
    #BaseSettings.INSTALLED_APPS += (
        #'debug_toolbar',
    #)
    #INTERNAL_IPS = ('10.0.2.2',)
    #DEBUG_TOOLBAR_CONFIG = {
        #'INTERCEPT_REDIRECTS': False,
    #}

    ##################################
    # END: used by developer toolbar #
    ##################################

    # In dev, do not actually send emails - instead print them to the console.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class StagingSettings(BaseSettings):
    pass


class LiveSettings(BaseSettings):

    pass


########## Sample Settings adaption
# The class below shows how an existing class can be changed to have different
# requirements
class ExampleDevSettings(DevSettings):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'niceguydave_development',
            'USER': 'django',
            'PASSWORD': _get_env_variable('POSTGRES_PASSWORD'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }


class DavidDevSettings(DevSettings):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'niceguydave_development',
            'USER': _get_env_variable('POSTGRES_PASSWORD'),
            'PASSWORD': _get_env_variable('POSTGRES_PASSWORD'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }
