
""" Persite Cache"""
# To Use Persite Cache include Following Middlewares:
# 'django.middleware.cache.UpdateCacheMiddleware',
# 'django.middleware.common.CommonMiddleware',
# 'django.middleware.cache.FetchFromCacheMiddleware'

""" For Cache Database Setup"""
# CACHES={
#     'default':{
#         'BACKEND':'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION':'student_cache'
#     }
# }

from pathlib import Path
from django.contrib.messages import constants as messages_s

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR=BASE_DIR/'templates'
STATIC_DIR=BASE_DIR/'static'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_6)y!t^c0abh89h-e%5o7ql_755x#nw8j5k(fe^y=&jwy64iz2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'studentapp',
    'studentblog',
    'sessionapp',
    'persitecacheapp',
    'perviewcacheapp',
    'signalapp',
    'customsignalapp',
    'functionbasedmiddleware',
    'classbasedmiddleware',
    'relationshipApp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'functionbasedmiddleware.middlewares.my_middleware',
    # 'classbasedmiddleware.middlewares.MyMiddleware'
]

ROOT_URLCONF = 'studentmanagement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'studentmanagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS=[STATIC_DIR]

"""message_tag change"""
MESSAGE_TAGS={messages_s.ERROR:'danger'}


"""FILE BASED SESSION"""
# SESSION_ENGINE='django.contrib.sessions.backends.file'
# #FILE BASED SESSION PATH
# SESSION_FILE_PATH=BASE_DIR/'session'
"""Session Expiration Time"""
# SESSION_COOKIE_AGE=20

""" For Cache Database Setup"""
CACHES={
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'student_cache'
    }
}
"""File Sytem Caching"""
# CACHES={
#     'default':{
#         'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION':BASE_DIR+'filebasedcache'
#     }
# }
""" Local Memory Caching"""
# CACHES={
#     'default':{
#         'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION':'unique-snowflake'
#     }
# }
""" Cache Expiration Time"""
# CACHE_MIDDLEWARE_SECONDS=30


""" 
To Create Cache Table Type Command:
py manage.py createcachetable

"""