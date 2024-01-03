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

from ..models import msendmail

import os


def send_email_customized(subject, plain_message_text, html_message_text, user_email_add, appname):
    #import pdb ; pdb.set_trace()
    if appname == 'AUTH':
        from_email = settings.EMAIL_CONFIG["AUTH"]["EMAIL_HOST_USER"]
    elif appname == 'SHOPCART':
        from_email = settings.EMAIL_CONFIG["SHOPCART"]["EMAIL_HOST_USER"]
    elif appname == 'CUSTSUPP':
        from_email = settings.EMAIL_CONFIG["CUSTSUPP"]["EMAIL_HOST_USER"]
    else:
        from_email = settings.EMAIL_CONFIG["GENERAL"]["EMAIL_HOST_USER"]

    # zzz_print("    %-28s: %s" % ("plain_message_text", plain_message_text))
    # zzz_print("    %-28s: %s" % ("html_message_text", html_message_text))
    to_emails = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS) + user_email_add
    #to_emails.append(user_email_add)

    print("Email --------------------------", to_emails)

    imsendmail              = msendmail.objects.add(
        subject             = subject,
        plain_message       = plain_message_text,
        html_message        = html_message_text,
        from_email          = from_email,
        to_emails           = to_emails,
        appname             = appname
    )
    imsendmail.send_to_each_recipient_seperately()
