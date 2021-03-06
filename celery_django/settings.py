"""
Django settings for celery_django project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p448e!ejsj1vth$!44&kwf28^mua5@a+b2-mpkintjc_qx^g#7'

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
    'apps.app1',
    'apps.app2',
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

ROOT_URLCONF = 'celery_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'celery_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'



#Celery 配置


#不需要手动加入了因为在celery.py中有了app.autodiscover_tasks()
# CELERY_IMPORT = (
#     'apps.app1.tasks',
#     'apps.app2.tasks',
# )


#防止死锁
CELERY_FORCE_EXECV = True
#设置celery workerbi 并发数
CELERY_CONCURRENCY= 8
#如果任务失败的时候允许重试
CELERY_ACKS_LATE = True
#设置每个worker最多执行多个任务就可以销毁，防止内存泄漏
CELERYD_MAX_TASKS_CHILD= 100
#设置单个任务执行超时时间 秒
CELERY_TASK_TIME_LIMIT = 60




CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0' # Broker配置，使用Redis作为消息中间件

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1' # BACKEND配置，这里使用redis

CELERY_RESULT_SERIALIZER = 'json' # 结果序列化方案




#setting 中设置无效
# CELERY_QUEUES = {
#     'deafult':
#         {
#             'exchange': 'deafult',
#             'exchange_type': 'direct',
#             'binding_key': 'deafult'
#         },
#     'beat_queue':
#         {
#             'exchange':'beat_queue',
#             'exchange_type':'direct',
#             'binding_key':'beat_queue'
#         },
#     'worker_queue':
#         {
#             'exchange': 'worker_queue',
#             'exchange_type': 'direct',
#             'binding_key': 'worker_queue'
#         }
#
# }



# #默认使用worker_queue作为消息队列
# CELERY_DEFAULT_QUEUE = 'worker_queue'

# 配置队列
# CELERY_QUEUES = (
#     Queue('default', routing_key='default'),
#     Queue('队列1', routing_key='key1'),
#     Queue('队列2',  routing_key='key2'),
# )

# from kombu import Queue,Exchange
# #设置add队列,绑定routing_key
# CELERY_QUEUES = (
#     Queue('default',Exchange('default'), routing_key='default'),
#     Queue('add_queue', Exchange('add_queue'),routing_key='add_queue'),
# )
# #
# #projq.tasks.add这个任务进去add队列并routeing_key为
# CELERY_ROUTES = {
#     'apps.app1.tasks.add': {'queue': 'add_queue'}
# }

# 配置队列
# CELERY_QUEUES = (
#     Queue('default', routing_key='default'),
#     Queue('队列1', routing_key='key1'),
#     Queue('队列2', routing_key='key2'),
# )
#
# # 路由（哪个任务放入哪个队列）
# CELERY_ROUTES = {
#     '任务1': {'queue': '队列1', 'routing_key': 'key1'},
#     '任务2': {'queue': '对列2', 'routing_key': 'key2'},
# }


#队列
# CELERY_QUEUES = (
# Queue('default', Exchange('default'), routing_key='default', consumer_arguments={'x-priority': 1}),
# Queue('for_task_A', Exchange('for_task_A'), routing_key='for_task_A', consumer_arguments={'x-priority': 4}),
# Queue('for_task_B', Exchange('for_task_B'), routing_key='for_task_B', consumer_arguments={'x-priority': 6})
# )


# 为每个task启动不同的worker
# celery -A tasks worker -l info -n workerA -Q for_tesk_A
# celery -B tasks worker -l info -n workerB -Q for_task_B
