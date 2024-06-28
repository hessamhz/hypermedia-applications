import re

from corsheaders.defaults import default_headers
from settings.common import *

# HOST CONFIGURATION
ALLOWED_HOSTS = get_env("ALLOWED_HOSTS").split(",")
# END OF HOST CONFIGURATION

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env("SECRET_KEY")
# END OF SECRET CONFIGURATION

# TODO Setup Gunicorn
INSTALLED_APPS = ("corsheaders",) + INSTALLED_APPS

# CSRF CONFIGURATION
CSRF_TRUSTED_ORIGINS = get_env("CSRF_TRUSTED_ORIGINS").split(",")
CSRF_COOKIE_DOMAIN = get_env("CSRF_COOKIE_DOMAIN")
CSRF_COOKIE_SAMESITE = get_env("CSRF_COOKIE_SAMESITE")
SESSION_COOKIE_SAMESITE = get_env("SESSION_COOKIE_SAMESITE")
CSRF_COOKIE_SECURE = get_env("CSRF_COOKIE_SECURE")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
SESSION_COOKIE_SECURE = True
# END CORSHEADERS CONFIGURATION

# CORSHEADERS CONFIGURATION
CORS_ALLOW_HEADERS = list(default_headers) + ["access", "Authorization"]
CORS_ORIGIN_REGEX_WHITELIST = [
    re.compile(r) for r in get_env("CORS_ORIGIN_REGEX_WHITELIST").split(",")
]
CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = re.compile(get_env("CORS_URLS_REGEX"))
CORS_EXPOSE_HEADERS = ["X-CSRFToken", "access", "Authorization"]
# END CORSHEADERS CONFIGURATION

MIDDLEWARE += ("corsheaders.middleware.CorsMiddleware",)
