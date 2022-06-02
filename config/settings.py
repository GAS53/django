import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('django_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    INTERNAL_IPS = ["127.0.0.1",]


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'markdownify.apps.MarkdownifyConfig',
    'authapp.apps.AuthappConfig',
    'social_django',
    'crispy_forms',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "mainapp.context_processors.example.simple_context_processor",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],

        'libraries':{'email_to_link':'mainapp.context_processors.example'}
        },
    },
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
        "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },}}

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATICFILES_DIRS = (
  os.path.join(SITE_ROOT, 'static/'),
)


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
AUTH_USER_MODEL = "authapp.CustomUser"
LOGIN_REDIRECT_URL = "mainapp:main_page"
LOGOUT_REDIRECT_URL = "mainapp:main_page"
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "django.contrib.auth.backends.ModelBackend",
    )

SOCIAL_AUTH_GITHUB_KEY = '8b4874c2b4c54df66fe3'
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('django_git_password')
AUTH_USER_MODEL = 'authapp.CustomUser'
CRISPY_TEMPLATE_PACK = "bootstrap4"
LOG_FILE = BASE_DIR / "var" / "log" / "main_log.log"
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "[%(asctime)s] %(levelname)s %(name)s (%(lineno)d)%(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "console"}, },
    "loggers": {"django": {"level": "INFO", "handlers": ["console"]},
    },
}
# глобально
EMAIL_HOST = "localhost" #'smtp.yandex.ru'
EMAIL_PORT = "465" # 465- mail, yandex
EMAIL_HOST_USER = os.environ.get('email') #"django@geekshop.local" # myname@yandex.ru
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') #
EMAIL_USE_SSL = False # yandex True # google False
EMAIL_USE_TLS = True # google True , yandex - False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'email_messages')