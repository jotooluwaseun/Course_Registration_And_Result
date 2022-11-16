from .base import *
import os


SECRET_KEY = 'django-insecure-297++kw8l2_mqwayhr_2qd7xyvt=r@ct=g0^=&*cl3!*+vy!)n'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


MEDIA_URL = ''
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images/')