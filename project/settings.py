import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = "true" in os.getenv('DB_DEBUG').lower()

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['127.0.0.1:8000']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': os.getenv('DB_BACKEND'),
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = os.getenv('DB_LANGUAGE_CODE')

TIME_ZONE = os.getenv('DB_TIME_ZONE')

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
