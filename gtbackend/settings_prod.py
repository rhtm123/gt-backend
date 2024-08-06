from gtbackend.settings import *

# ALLOWED_HOSTS = ['15.206.123.92','backend.growtechlab.com','growtechlab.com', 'growtechlab.support']

ALLOWED_HOSTS += ["*"]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DATABASE_NAME'),
#         'USER': config('DATABASE_USER'),
#         'PASSWORD': config('DATABASE_PASSWORD'),
#         'HOST': config('DATABASE_HOST'),
#         'PORT': config('DATABASE_PORT'),
#         'OPTIONS': {'sslmode': 'require'},
#         }
# }

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': config('CLN_CLOUD_NAME'),
#     'API_KEY': config('CLN_API_KEY'),
#     'API_SECRET': config('CLN_API_SECRET'),
# }

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'