import os
from .settings import *
from .settings import BASE_DIR


# SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

CSRF_TRUSTED_ORIGINS = [f'https://{ALLOWED_HOSTS[0]}']

DEBUG = False
