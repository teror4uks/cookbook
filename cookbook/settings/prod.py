from cookbook.settings.base import PROJECT_NAME
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': PROJECT_NAME,
        'USER': 'root',
        'PASSWORD': 'Air0oopp',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}