"""Common settings and globals."""

from os.path import abspath, dirname
from pathlib import Path
from sys import path

from dotenv import load_dotenv
from settings.utils import get_env

# PATH CONFIGURATION
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Absolute filesystem path to the project directory:
PROJECT_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level package folder:
PACKAGE_ROOT = dirname(PROJECT_ROOT)

# .ENV CONFIGURATION
env_path = Path(PROJECT_ROOT) / ".env"

load_dotenv(dotenv_path=env_path)

# Site name:
SITE_NAME = get_env("SITE_NAME")
SITE_ID = int(get_env("SITE_ID"))
PROJECT_NAME = get_env("PROJECT_NAME", default="hive")

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(PACKAGE_ROOT)
# END OF PATH CONFIGURATION


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = get_env("DEBUG", default=True)
IS_DJANGO_DEBUG_ENABLED = get_env("IS_DJANGO_DEBUG_ENABLED", default=True)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END OF DEBUG CONFIGURATION


# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_env("DEFAULT_DATABASE_NAME"),
        "USER": get_env("DEFAULT_DATABASE_USER"),
        "PASSWORD": get_env("DEFAULT_DATABASE_PASSWORD"),
        "HOST": get_env("DEFAULT_DATABASE_HOST"),
        "PORT": get_env("DEFAULT_DATABASE_PORT"),
        "TEST": {
            "DEPENDENCIES": [],
        },
    },
}
# END OF DATABASE CONFIGURATION

# PASSWORD CONFIGURATION
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        + ".UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation" + ".MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation" + ".CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation" + ".NumericPasswordValidator",
    },
]
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# END OF PASSWORD CONFIGURATION


# GENERAL CONFIGURATION
# See: https://docs.djxangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = "UTC"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = get_env("LANGUAGE_CODE")

LANGUAGES = [
    ("en", "English"),
]
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# END OF GENERAL CONFIGURATION

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_env("ALLOWED_HOSTS", default="localhost").split(",")
# END OF SITE CONFIGURATION


# TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / get_env("TEMPLATE_DIR"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
# END OF TEMPLATE CONFIGURATION


# MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE = (
    # Default Django middleware.
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    # Custom middlewares
)
# END OF MIDDLEWARE CONFIGURATION


# URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "src.core.urls"
# END OF URL CONFIGURATION

# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
)

THIRD_PARTY_APPS = (
    "rest_framework",
    "corsheaders",
    "tinymce",
)

# Apps specific for this projeßßct go here.
LOCAL_APPS = (
    "src.api",
    "src.apps.storage",
    "src.apps.members",
    "src.apps.services",
    "src.apps.projects",
    "src.apps.website",
    "src.apps.chatbot",
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END OF APP CONFIGURATION


# WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "src.core.wsgi.application"
ASGI_APPLICATION = "src.core.asgi.application"
# END OF WSGI CONFIGURATION


# RESTFARMEWORK CONFIGURATION
REST_FRAMEWORK = {
    # Use JSON by default for API responses
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    # Allow the API to handle incoming JSON requests
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    # SessionAuthentication for web browsable API
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}
# END OF RESTFARMEWORK CONFIGURATION


# STATIC, MEDIA FILE CONFIGURATION
MEDIA_ROOT = get_env("MEDIA_ROOT")
MEDIA_URL = get_env("MEDIA_URL")
STATIC_ROOT = get_env("STATIC_ROOT")
STATIC_URL = get_env("STATIC_URL")
# END OF STATIC, MEDIA FILE CONFIGURATION

# CORSHEADERS CONFIGURATION
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# END CORSHEADERS CONFIGURATION

# CHANNELS CONFIGURATION
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(get_env("REDIS_HOST"), 6379)],
        },
    },
}
# END OF CHANNELS CONFIGURATION
