from gtbackend.settings import *

# ALLOWED_HOSTS = ['15.206.123.92','backend.growtechlab.com','growtechlab.com', 'growtechlab.support']
CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOWED_ORIGINS = [
    'https://www.growtechlab.com',
    'https://cms.growtechlab.com',
]

CORS_ORIGIN_WHITELIST = [
    'https://www.growtechlab.com',
    'https://cms.growtechlab.com',
]


ALLOWED_HOSTS = ['127.0.0.1', "gt.thelearningsetu.com",'growtech.up.railway.app']

CSRF_TRUSTED_ORIGINS = [
    'https://gt.thelearningsetu.com',
    'https://growtech.up.railway.app',
    # Add other domains as needed
]




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
        'OPTIONS': {'sslmode': 'require'},
        }
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLN_CLOUD_NAME'),
    'API_KEY': config('CLN_API_KEY'),
    'API_SECRET': config('CLN_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'