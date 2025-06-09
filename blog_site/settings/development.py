from .base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': config('DB_NAME', default=BASE_DIR / 'db.sqlite3'),
        'USER': config('DB_USER', default=''),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default=''),
        'PORT': config('DB_PORT', default=''),
    }
}

if config('USE_POSTGRES', default=False, cast=bool):
    DATABASES['default'].update({
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='blog_db'),
        'USER': config('DB_USER', default='blog_user'),
        'PASSWORD': config('DB_PASSWORD', default='blog_password'),
        'HOST': config('DB_HOST', default='db'),
        'PORT': config('DB_PORT', default='5432'),
    })

# Database URL override (useful for development with external DBs)
if config('DATABASE_URL', default=None):
    DATABASES['default'] = dj_database_url.parse(config('DATABASE_URL'))

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']