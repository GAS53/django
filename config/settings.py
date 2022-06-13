import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
DEBUG = False
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

if DEBUG:
    ALLOWED_HOSTS = ['*']
    STATICFILES_DIRS = (
        os.path.join(SITE_ROOT, 'static/'),
        )
else:
    ALLOWED_HOSTS = ['127.0.0.1', '192.168.2.81', 'localhost']
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
        # STATICFILES_FINDERS = (
        #     'django.contrib.staticfiles.finders.FileSystemFinder',
        #     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        # )




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
    "debug_toolbar",


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.locale.LocaleMiddleware',
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dz',
            'USER': 'myprojectuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
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
LOCALE_PATH = [BASE_DIR / 'locale']

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_ROOT = BASE_DIR / "media"
AUTH_USER_MODEL = "authapp.CustomUser"
LOGIN_REDIRECT_URL = "mainapp:main_page"
LOGOUT_REDIRECT_URL = "mainapp:main_page"
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "django.contrib.auth.backends.ModelBackend",
    )

SOCIAL_AUTH_GITHUB_KEY =  os.environ.get('SOCIAL_AUTH_GITHUB_KEY')
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

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"


# глобально
EMAIL_HOST = 'smtp.mail.ru'#"localhost" 
EMAIL_PORT = "465" # 465- mail, yandex
EMAIL_HOST_USER = os.environ.get('email') #"django@geekshop.local" # myname@yandex.ru
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') #
EMAIL_USE_SSL = True # yandex True # google False
EMAIL_USE_TLS = False # google True , yandex - False
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# локально
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'var', 'email_messages')
# EMAIL_FILE_PATH = "var/email-messages/"

# консоль
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False