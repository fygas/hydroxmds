"""
Django settings for sdmx project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'azafu$_9zlmc42((52cg2jp@+_hmz77!g5&@6ifr$qo1rqe$)-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # third party apps
    'rest_framework',
    'django_tables2',
    'crispy_forms',
    'django_fullclean',
    # 'hvad',
    # my apps
    # 'sdmx',
    'sdmx.apps.SdmxConfig',
    'common.apps.CommonConfig',
    'hybrid.apps.HybridConfig',
    'structure.apps.StructureConfig',
    # 'structure.categorisation',
    # 'structure.category', 
    'structure.codelist.apps.CodelistConfig',
    # 'structure.concept.apps.ConceptConfig',
    # 'structure.constraint',
    'structure.data_structure.apps.DataStructureConfig',
    'structure.dataflow.apps.DataflowConfig',
    # 'structure.hierarchical_codelist',
    # 'structure.metadata_structure',
    # 'structure.metadataflow',
    # 'structure.process',
    # 'structure.provision',
    # 'structure.reporting_taxonomy',
    # 'structure.structure_set',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sdmx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'sdmx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djansdmx',
        'USER': 'djansdmxuser',
        'PASSWORD': 'S2a2dthae4102#',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static_in_env', 'static_root')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static_in_env', 'media_root')

MAX_LENGTH = 255

# Crispy forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'
DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap-responsive.html'
