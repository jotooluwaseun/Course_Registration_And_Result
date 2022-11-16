from re import M
import django_on_heroku
from decouple import core
from .base import *

SECRET_KEY = core('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['']

# Amazon S3 Settings
AWS_ACCESS_KEY_ID = core('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = core('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = core('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}
AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Heroku Logging
DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
# Heroku Settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']

# DATABASES = {'default': dj_database_url.config(default='postgres://adeptbloc_admin:Bloc2022###@database-1.chhjb0jl9uie.us-east-1.rds.amazonaws.com:5432/prodDB_adeptbloc', conn_max_age=600)}
# DATABASES = {'default': dj_database_url.config(default='DATABASE_URL', conn_max_age=600)}
