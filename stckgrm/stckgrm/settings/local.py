from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'PASSWORD':'postgres',
        'USER':'postgres',
        'HOST':'db',
        'PORT':5432,
    }
}
