# deploy
import os,environ
from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

#1 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 베이스 디렉토리는 settings.py 경로에서 root폴더로 가서 그 폴더를 BASE_DIR로 하겠다.

# reading .env file

## env가 앱 내부에 있을 때 
environ.Env.read_env()

## env가 root 폴더에 있을 때 
# environ.Env.read_env(
#     env_file=os.path.join(BASE_DIR, '.env')
# )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

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
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}