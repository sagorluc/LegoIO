# import os

# CELERY_BROKER_URL = 'redis://127.0.0.1:6379' # this URL may not be correct
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
# CELERY_ACCEPT_CONTENT =['application/json']
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SELERLIZER = 'json'
# ###############################################################
# # REDIS_CACHE CONNEECTIONS
# ###############################################################
# # CELERY_RESULT_BACKEND = 'django-db'
# # CELERY_CACHE_BACKEND = 'django-cache'


# ###############################################################
# # REDIS_CACHE CONNEECTIONS
# ###############################################################
# REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
# REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': "redis://{}:{}/1".format(REDIS_HOST, REDIS_PORT),
#         'OPTIONS': {
#             'CLIENT_CLASS': "django_redis.client.DefaultClient",
#         },
#     },
# }
# print("*******************************************")
# print("connecting to HAYSTACK_CONNECTIONS ->>>{}".format(CACHES['default']))


