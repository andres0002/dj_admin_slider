from dj_admin_slider.settings.base import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY_PRD")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG_PRD", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS_PRD", cast=lambda v: [host.strip() for host in v.split(',')])

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config("DB_ENGINE_PRD"),
        'NAME': BASE_DIR / config("DB_NAME_PRD"), # sqlite
        # 'NAME': config("DB_NAME_PRD"), # no sqlite
        # 'USER': config("DB_USER_PRD"),
        # 'PASSWORD': config("DB_PASSWORD_PRD"),
        # 'HOST': config("DB_HOST_PRD"),
        # 'PORT': config("DB_PORT_PRD"),
    }
}