#!/usr/bin/env python
import os
import sys
import django

BASE_PATH = os.path.dirname(__file__)


def main():
    """Standalone django model test with a
    'memory-only-django-installation'.  You can play with a django
    model without a complete django app installation.
    http://www.djangosnippets.org/snippets/1044/

    """
    os.environ["DJANGO_SETTINGS_MODULE"] = "django.conf.global_settings"
    from django.conf import global_settings

    global_settings.ROOT_URLCONF = "django_membersuite_auth.urls"

    global_settings.USE_TZ = True

    global_settings.STATIC_URL = os.environ.get('STATIC_URL', '/static/')
    global_settings.STATIC_ROOT = os.environ.get(
        'STATIC_ROOT',
        os.path.join(BASE_PATH, global_settings.STATIC_URL.strip('/')))

    global_settings.INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_membersuite_auth'
    )

    if django.VERSION > (1, 2):
        global_settings.DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_PATH,
                                     'django-membersuite-auth.sqlite'),
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            }
        }
    else:
        global_settings.DATABASE_ENGINE = "sqlite3"
        global_settings.DATABASE_NAME = ":memory:"

    if django.VERSION < (1, 9):
        global_settings.MIDDLEWARE_CLASSES = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
    else:
        global_settings.MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

    global_settings.SECRET_KEY = "blahblah"

    global_settings.SITE_ID = 1

    global_settings.MS_ACCESS_KEY = os.environ["MS_ACCESS_KEY"]
    global_settings.MS_SECRET_KEY = os.environ["MS_SECRET_KEY"]
    global_settings.MS_ASSOCIATION_ID = os.environ["MS_ASSOCIATION_ID"]

    global_settings.DMA_COOKIE_SESSION = (
        "SESS119812a4f54200aec862c73cf2ee")
    global_settings.DMA_COOKIE_DOMAIN = ".aashe.org"

    global_settings.TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_PATH + 'django_membersuite_auth/templates'],
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

    from django.test.utils import get_runner
    test_runner = get_runner(global_settings)

    django.setup()

    test_runner = test_runner()
    test_labels = (sys.argv[1:] if len(sys.argv) > 1
                   else ["django_membersuite_auth"])

    failures = test_runner.run_tests(test_labels)

    sys.exit(failures)


if __name__ == '__main__':
    main()
