"""Development settings and globals."""

from settings.common import *

# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END OF DEBUG CONFIGURATION


# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = "django-insecure-$s8)nd5a#=6mu--asj!uo@go%0y%m*px67jxnh8kd3^as#nw"
# END OF SECRET CONFIGURATION

# URL CONFIGURATION
IS_LOCAL_URL = True
# END OF URL CONFIGURATION
