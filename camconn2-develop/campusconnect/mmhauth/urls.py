from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy



app_name ='mmhauth'

from .forms import (
    SetPasswordCustomForm,
    MySetPasswordForm,
)

from .views import (
    mmh_auth_login_request,
    mmh_auth_logout_request,
)

from .views import (    
    mmh_auth_register,
    mmh_auth_signup_validator,
    mmh_auth_signup_account_verifier,
)

from .views import (    
    password_reset_request_view,
    PasswordResetRequestEmailConfirmationWithLinkView,
    PasswordResetSetNewPasswordView,    
)


#app_name = 'mmhauth'


# signin 
# --------------------------------------------------------------
signin_urls = [
    path("signin",                          
        mmh_auth_login_request,             
        name="mmh_auth_login_request"
    ),

    path("logout",                          
        mmh_auth_logout_request,            
        name="mmh_auth_logout_request"
    ),

]



# signup 
# --------------------------------------------------------------
signup_urls = [
    path("signup/request",    
        mmh_auth_register,                  
        name="mmh_auth_register_url"
    ),

    path("signup/validation",                 
        mmh_auth_signup_validator,    
        name="signup_validation_link"
    ),

    path("signup/account-verification/<str:activation_code>",    
        mmh_auth_signup_account_verifier,
        name="mmh_auth_verification_completed_link"
    ),

]



# password reset 
# --------------------------------------------------------------
password_reset_urls = [    
    path(
        "password-reset",
            password_reset_request_view,
            name="password_reset"
        ),

    # path(
    #     "password-reset-done",
    #         auth_views.PasswordResetDoneView.as_view(
    #             template_name='mmhauth/layout/password_reset/step2_done.html'
    #             ),
    #         name="password_reset_done"
    #     ),

    path(
        "password-reset-done",
            PasswordResetRequestEmailConfirmationWithLinkView.as_view(),
            name="password_reset_done"
        ),
    
    # path(
    #     "password-reset-confirm/<str:uidb64>/<str:token>",
    #         auth_views.PasswordResetConfirmView.as_view(
    #             template_name='mmhauth/layout/password_reset/step3_set_password.html',
    #             success_url=reverse_lazy('mmhauth:password_reset_complete'),
    #             form_class=SetPasswordCustomForm
    #             ),
    #         name="password_reset_confirm"
    #     ),
    
    path(
        "password-reset-confirm/<str:uidb64>/<str:token>",
            PasswordResetSetNewPasswordView.as_view(),
            name="password_reset_confirm"
        ),


    path(
        "password-reset-complete/",
            auth_views.PasswordResetCompleteView.as_view(
                template_name='mmhauth/layout/password_reset/step4_complete.html',
                ),
            name="password_reset_complete"
        ),

]







urlpatterns = [
    path("", include(signin_urls)),
    path("", include(signup_urls)),
    path("", include(password_reset_urls)),
    
    # update/change password urls
    # path('password-update/', auth_views.PasswordChangeView.as_view(), name='update-password'),
    # path('password-update/done/',auth_views.PasswordChangeDoneView.as_view(), name='update-password-done'),


]
