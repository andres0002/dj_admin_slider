from dj_admin_slider.settings.base import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY_QAS")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG_QAS", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS_QAS", cast=lambda v: [host.strip() for host in v.split(',')])

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config("DB_ENGINE_QAS"),
        'NAME': BASE_DIR / config("DB_NAME_QAS"), # sqlite
        # 'NAME': config("DB_NAME_QAS"), # no sqlite
        # 'USER': config("DB_USER_QAS"),
        # 'PASSWORD': config("DB_PASSWORD_QAS"),
        # 'HOST': config("DB_HOST_QAS"),
        # 'PORT': config("DB_PORT_QAS"),
    }
}