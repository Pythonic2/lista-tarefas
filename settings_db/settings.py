import os, environ

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '../.env'))

SECRET_KEY = env('SECRET_KEY')
DEFAULT_AUTO_FIELD='django.db.models.AutoField'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD':os.getenv('DB_PASSWORD'),
        'HOST':  os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
print('ok')


INSTALLED_APPS = ("db",)

TIME_ZONE = 'America/Sao_Paulo'
