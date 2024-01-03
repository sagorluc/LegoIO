import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login


import logging
logger = logging.getLogger(__name__)

admin.site.site_header = "UMSRA is from here"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"


class MyLoginView(TemplateView, auth_views.LoginView):
	template_name = 'admin/login76.html'

