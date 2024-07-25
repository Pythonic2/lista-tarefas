import os, environ

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEFAULT_AUTO_FIELD='django.db.models.AutoField'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}



INSTALLED_APPS = ("db",)

TIME_ZONE = 'America/Sao_Paulo'
