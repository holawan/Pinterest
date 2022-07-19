# deploy
import os,environ
from .base import *

def read_secret(secret_name):
    
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    
    return secret

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

#1 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 베이스 디렉토리는 settings.py 경로에서 root폴더로 가서 그 폴더를 BASE_DIR로 하겠다.

# reading .env file

## env가 root 폴더에 있을 때 
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


 
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}