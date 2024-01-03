# from __future__ import absolute_import

# import os
# from celery import Celery
# from django.conf import settings 


# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campusconnect.settings')
# app = Celery('campusconnect')
# app.config_from_object('django.conf:settings', namespace="CELERY")
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


##############################################################
# HAYSTACK CONNECTIONS
##############################################################
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE':'haystack.backends.solr_backend.SolrEngine',
#         'URL' : 'http://localhost:8983/solr/mySearchCore',
#     },
# }
# print("*******************************************")
# print("connecting to HAYSTACK_CONNECTIONS ->>>{}".format(HAYSTACK_CONNECTIONS['default']))
