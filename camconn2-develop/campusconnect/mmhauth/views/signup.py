from zzz_lib.zzz_log import zzz_print

import copy
import datetime
from base64 import b64decode
from guestactions.myfunctions import gen_num_for_email
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

from ..models import mverificationcode

from ..forms import (
    mmhNewUserForm,
    mmhSignInForm,
    PasswordResetCustomForm,
)

from ..my_function import user_is_deactivated
from django.utils.html import strip_tags
import os
import logging
logger = logging.getLogger(__name__)


TEMP_DIR_HTMLPAGES      = 'mmhauth/layout/signup/'
TEMP_DIR_EMAIL          = 'mymailroom/layout/mmhauth/'

from mymailroom.myfunctions import send_email_customized

from ..extras import DivErrorList
# ******************************************************************************
def mmh_auth_register(request):
    zzz_print("    %-28s: %s" % ("mmh_auth_register", "********************"))
    form_error = ""
    if request.method == "POST":
        form = mmhNewUserForm(data=request.POST, error_class=DivErrorList)
        if form.is_valid():
            zzz_print("    %-28s: %s" % ("form.is_valid", ""))

            ## at first, save user given email add in a var 
            user_email_add = form.cleaned_data["email"]
            # save user_email_add in a session variable to be used in another view
            request.session['user_email_add'] = user_email_add

            ## Check if this email add is in 'deactivated acct' list
            chk = user_is_deactivated(user_email_add)
            if chk:
                form_error = "Email was used for account creation and then account was deactivated"
            ## else: do something
            else:
                # 2021/05/25: Users now log in with their email address.
                #             But we are still using Django's default user model.
                #             We no longer ask for a username when creating a new account.
                #             Instead we force a lower case version of the users email address into their username.
                #             And we use this as their username.
                user = form.save()
                # Note: form data, specifically the username, is already forced to lowercase in form.save() method
                vc = mverificationcode.objects.create(user=user)
                zzz_print("    %-28s: user = %s, email = %s, vc = %s" % ("account created", user, user_email_add, vc))

                # send email to the user
                appname = "AUTH"
                subject = "Hi" + (user.first_name).capitalize() + ", Welcome to Resumenalyzer"  + gen_num_for_email()
                email_context = {
                    'change_notice'     : 'your interest',
                    'submission_time'   : datetime.datetime.now(),
                    'activation_code'   : vc.hash_value,
                    'dns_name'          : settings.DNS_NAME,
                    'protocol'          : settings.PROTOCOL,

                }
                html_message_text = render_to_string(
                    template_name=TEMP_DIR_EMAIL + 'reg_step1.html',
                    context=email_context,
                    using=None,
                    request=None
                )
                plain_message_text = strip_tags(html_message_text)
                send_email_customized(subject, plain_message_text, html_message_text, user_email_add, appname)
                
                # redirect user to page thanking them for creating their account
                return redirect("mmhauth:signup_validation_link")
        
        else:
            zzz_print("    %-28s: %s" % ("NOT form.is_valid", ""))
    else:
        zzz_print("    %-28s: %s" % ("request.method", "!= POST"))
        form = mmhNewUserForm(error_class=DivErrorList)

    template_name   = TEMP_DIR_HTMLPAGES + "signup-step1.html"
    context         = {
        "pg_header"         : "Sign Up",
        "form"              : form, 
        "form_errors"       : form_error,
        "pg_layout_type"    : "signup",
        "app_version"       : settings.VER_AUTH,
        "change_notice"     : "your interest",
        'app_version'       : settings.VER_RESUMEWEB,
    }
    return render(request = request, template_name = template_name, context = context)


# ******************************************************************************
def mmh_auth_signup_validator(request):
    zzz_print("    %-28s: %s" % ("mmh_auth_signup_validator", "********************"))
    template_name   = TEMP_DIR_HTMLPAGES + "signup-step2.html"
    context         = {
        "user_email"    : request.session.get('user_email_add'),
        "from_email"    : settings.EMAIL_CONFIG["AUTH"]["EMAIL_HOST_USER"],
        'app_version'   : settings.VER_RESUMEWEB,
    }
    return render(request = request, template_name = template_name, context = context)


# ******************************************************************************
def mmh_auth_signup_account_verifier(request, activation_code):
    zzz_print("    %-28s: %s" % ("mmh_auth_signup_account_verifier", "********************"))
    zzz_print("    %-28s: %s" % ("activation_code", activation_code))
    logger.warning(activation_code)
    verified_message = ""
    verified_succeeded = True
    try:
        decoded = b64decode(bytes(activation_code, 'utf-8'))
        zzz_print("    %-28s: %s" % ("decoded", decoded))
        user_email, code = decoded.decode('utf-8').split(':')
        zzz_print("    %-28s: %s" % ("user_email", user_email))
        zzz_print("    %-28s: %s" % ("code", code))

        iVerificationCode = mverificationcode.objects.get(user__email=user_email, code=code)
        logger.warning(iVerificationCode)
        # Test if this user has already been validated
        if not iVerificationCode.user.is_active:
            zzz_print("    %-28s: %s" % ("user.is_active", iVerificationCode.user.is_active))

            iVerificationCode.verified = timezone.now()
            iVerificationCode.save()
            iVerificationCode.user.is_active = True
            iVerificationCode.user.save()

            zzz_print("    %-28s: %s" % ("user.is_active", iVerificationCode.user.is_active))

            # send email to the user
            appname = "AUTH"
            subject = (iVerificationCode.user.first_name).capitalize() + ", thanks for verifying your account!" + gen_num_for_email(),
            subject = subject[0]
            user_email_add = user_email
            email_context = {
                'change_notice'     : 'Signup',
                'submission_time'   : datetime.datetime.now(),
            }
            html_message_text = render_to_string(
                template_name=TEMP_DIR_EMAIL + 'reg_step2.html',
                context=email_context,
                using=None,
                request=None
            )
            plain_message_text = strip_tags(html_message_text)
            send_email_customized(subject, plain_message_text, html_message_text, user_email_add, appname)
            logger.warning("send_email_customized from line#171 is called")

            verified_message = "Your Resumenalyzer account is now created and verified"
            logger.warning(verified_succeeded)
        else:
            zzz_print("    %-28s: %s" % ("user.is_active", iVerificationCode.user.is_active))
            verified_message = "Your account was already verified"
            logger.warning(verified_succeeded)

    except Exception as e:
        logger.warning("this is the exception {}".format(e))
        zzz_print("    %-28s: %s" % ("ERROR: activation_code", activation_code))
        verified_message = "Something went wrong in our server. Please try again later"
        verified_succeeded = False
        logger.warning(verified_succeeded)

    template_name   = TEMP_DIR_HTMLPAGES + "signup-step3.html",
    context         = {
        "verified_message"  : verified_message,
        "verified_succeeded": verified_succeeded,
        "activation_code"   : activation_code,
        'app_version'       : settings.VER_RESUMEWEB,
        
    }
    return render(request = request, template_name = template_name, context = context)


