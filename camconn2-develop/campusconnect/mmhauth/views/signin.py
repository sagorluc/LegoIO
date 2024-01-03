from zzz_lib.zzz_log import zzz_print

import copy
from base64 import b64decode

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode

from ..forms import (
    mmhNewUserForm, 
    mmhSignInForm,
    PasswordResetCustomForm,
)
from django.utils.html import strip_tags
from mymailroom.myfunctions import send_email_customized
from ..my_function import user_is_deactivated

import logging
logger = logging.getLogger(__name__)

TEMP_DIR_HTML_SIGNIN    = 'mmhauth/layout/signin/signin-v3.html'
TEMP_DIR_EMAIL          = 'mymailroom/layout/mmhauth/'


# ******************************************************************************
def mmh_auth_login_request(request):
    zzz_print("    %-28s: %s" % ("mmh_auth_login_request", "********************"))
    redirect_url = request.GET.get('next', "/")
    form_error = ""
    logger.warning("platform is running at risk")
    if request.method == "GET":
        form = mmhSignInForm()
        if request.user.is_authenticated:
            zzz_print("    %-28s: %s" % ("GET is_authenticated redirect", redirect_url))
            return redirect(redirect_url)
    elif request.method == "POST":
        form = mmhSignInForm(data=request.POST)
        if form.is_valid():
            email    = form.cleaned_data.get("email").lower()
            password = form.cleaned_data.get("password")
            # zzz_print("    %-28s: %s" % ("email", email))
            # zzz_print("    %-28s: %s" % ("password", password))
            # 2021/05/25: Users now log in with their email address.
            #             But we are still using Django's default user model.
            #             We no longer ask for a username when creating a new account.
            #             Instead we force a lower case version of the users email address into their username.
            #             And we use this as their username.


            chk = user_is_deactivated(email)
            logger.warning("calling chk function")
            logger.warning("value of chk >>>{}".format(chk))
            if chk:
                form_error = "Account with this email is deactivated"
                form = mmhSignInForm()
                template_name = TEMP_DIR_HTML_SIGNIN
                context = {
                    'form_error': form_error,
                    'form':       form,
                    "pg_header": "Sign In",
                    'app_version'       : settings.VER_RESUMEWEB,
                }
                return render(
                    request = request,
                    template_name = template_name,
                    context = context
                )  

            user_qs = User.objects.filter(email=email)
            if not user_qs.exists():
                form_error = "We didnot find any account with this email"
                form = mmhSignInForm()
                template_name = TEMP_DIR_HTML_SIGNIN
                context = {
                    'form_error': form_error,
                    'form': form,
                    "pg_header": "Sign In",
                    'app_version'       : settings.VER_RESUMEWEB,
                }
                return render(
                    request = request,
                    template_name = template_name,
                    context = context
                )
            else:
                user = authenticate(username=email, password=password)
                if user is not None:
                    login(request, user)
                    zzz_print("    %-28s: %s" % ("login", request.user))
                    zzz_print("    %-28s: %s" % ("POST login redirect", redirect_url))
                    return redirect(redirect_url)
                else:
                    logger.warning("user is None")
                    form_error = "Email/Password or both not valid"
                    zzz_print("    %-28s: %s" % ("user did not authenticate", ""))
                    zzz_print("    %-28s: %s" % ("email", email))
                    zzz_print("    %-28s: %s" % ("password", password))

    template_name   = TEMP_DIR_HTML_SIGNIN
    context         = {
        "pg_header"         : "Sign In",
        "form"              : form, 
        "pg_layout_type"    : "signin",
        "form_error"        : form_error,
        'app_version'       : settings.VER_RESUMEWEB,
    }
    return render(request=request, template_name=template_name, context = context)


# ******************************************************************************
@login_required
def mmh_auth_logout_request(request):
    zzz_print("    %-28s: %s" % ("mmh_auth_logout_request", "********************"))
    zzz_print("    %-28s: %s" % ("logout", request.user))
    logout(request)
    zzz_print("    %-28s: %s" % ("redirect", "'site_homepage_link'"))
    return redirect("site_homepage_link",)
