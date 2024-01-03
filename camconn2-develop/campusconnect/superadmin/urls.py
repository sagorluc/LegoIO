from django.conf.urls import url, include
from django.urls import path
from superadmin.views import MyLoginView
from django.contrib import admin

# app_name = 'superadmin'

general_urls_1 = [
    # path('home/login/', MyLoginView.as_view(), name='superadminlogin_url'),
    path('home/login/', admin.site.urls, name="admin"),
]

general_urls = [
    path('home/login/', MyLoginView.as_view()), #, name='superadminlogin_url'),
    path('home/', admin.site.urls),
]


urlpatterns = [
    # path("v2/",  include(general_urls)),
    path('v1/', include(general_urls_1)),
]
