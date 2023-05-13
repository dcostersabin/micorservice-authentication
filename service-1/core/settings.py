import os
from pathlib import Path
from configurations import Configuration
from configurations import values
from dotenv import load_dotenv
from datetime import timedelta
from corsheaders.defaults import default_headers
from corsheaders.defaults import default_methods

load_dotenv()


class Dev(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = values.SecretValue()

    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(";")

    CORS_ALLOW_HEADERS = list(default_headers)

    CORS_ALLOW_ALL_ORIGINS = True

    CORS_ALLOW_METHODS = list(default_methods)

    DEBUG = True

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "corsheaders",
        "rest_framework",
        "rest_framework_simplejwt",
        "v1",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "core.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
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

    WSGI_APPLICATION = "core.wsgi.application"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "POST": os.getenv("DATABASE_PORT"),
        }
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = "static/"

    STATIC_ROOT = BASE_DIR / "staticfiles"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticated",
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication",
        ],
        "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 10,
        "TEST_REQUEST_DEFAULT_FORMAT": "json",
    }

    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
        "ALGORITHM": "HS256",
        "SIGNING_KEY": os.getenv("JWT_SIGNING_KEY"),
        "AUTH_HEADER_TYPES": ("Bearer",),
        "USER_ID_FIELD": "id",
        "USER_ID_CLAIM": "user_id",
        "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    }

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
            "simple": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
        },
        "handlers": {
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": os.getenv("DJANGO_LOG_PATH"),
            },
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": os.getenv("DJANGO_LOG_LEVEL").upper(),
                "propagate": True,
                "formatter": "verbose",
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "INFO",
            },
        },
    }


class Prod(Dev):
    DEBUG = False

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
            "simple": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
        },
        "handlers": {
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": os.getenv("DJANGO_LOG_PATH"),
            },
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": os.getenv("DJANGO_LOG_LEVEL").upper(),
                "propagate": True,
                "formatter": "verbose",
            },
        },
    }
