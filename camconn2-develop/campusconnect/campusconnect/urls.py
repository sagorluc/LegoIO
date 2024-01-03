import debug_toolbar
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings




urlpatterns = [

    # app name >> general
    ##############################################
    # path("app/rw/", include('general.urls')),
    path('home/',    include('general.urls')),

    # app name >> resumeweb
    ##############################################
    path('',    include('inventory.urls')),
    #path('rw/', include('inventory.urls')),

   

    # app name >> mmhauth
    ##############################################
    path('app/mmhauth/v2/', include('mmhauth.urls')),

    # app name >> guestactions
    ##############################################
    path('app/actions/', include('guestactions.urls')),

      # app name >> mydocumentations
    ##############################################
    path('app/docs/', include('mydocumentations.urls')),

  
    
    # app name >>> superadmin
    ##############################################
    path('app/superadmin/', include('superadmin.urls')),





]
