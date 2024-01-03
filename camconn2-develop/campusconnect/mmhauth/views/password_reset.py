from zzz_lib.zzz_log import zzz_print
import datetime
import copy
from base64 import b64decode
from guestactions.myfunctions import gen_num_for_email
from django.contrib.auth import views as auth_views
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
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.views import (
    PasswordResetCompleteView
)
import os
from ..forms import (
    mmhNewUserForm, 
    mmhSignInForm,
    PasswordResetCustomForm,
    SetPasswordCustomForm,
    MySetPasswordForm,

)

APP_VERSION             = os.environ.get("VER_RESUMEWEB")
TEMP_DIR_HTMLPAGES      = 'mmhauth/layout/'
TEMP_DIR_EMAIL          = 'mymailroom/layout/mmhauth/'

from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from mymailroom.myfunctions import send_email_customized


def password_reset_request_view(request):
    # import pdb; pdb.set_trace()
    zzz_print("    %-28s: %s" % ("PasswordRestViewCustom", "********************"))
    form_error = ""

    if request.method == "GET":
        form = PasswordResetCustomForm()
    
    elif request.method == "POST":
        # if 'reset_password' in request.POST:
        form = PasswordResetCustomForm(data=request.POST)
        if form.is_valid():
            # opts = {}
            # opts['email_template_name'] = TEMP_DIR + 'password_reset_email.html'
            # opts['use_https']           = request.is_secure()
            # opts['request']             = request
            # opts['domain_override']     = settings.DNS_NAME
            # form.save(**opts)
            # zzz_print("    %-28s: %s" % ("form.save(**opts)", "Email Hopefully Sent"))
            user_email_add = request.POST.get("email")
            # print(email)
            request.session['user_email_add'] = user_email_add
            user_qs  = User.objects.filter(email=user_email_add)
            if not user_qs.exists():
                # return HttpResponse('no user exists with this email')
                form_error = "We didnot find any account with this email address"
                template_name = TEMP_DIR_HTMLPAGES + "password_reset/step1_request.html"
                form = PasswordResetCustomForm()
                context = {
                    'form_error'    : form_error,
                    'form'          : form,
                    "pg_header"     : "Password Reset",
                    'app_version'   : APP_VERSION
                }
                return render(request=request, template_name=template_name, context=context)

            else:
                user = user_qs.get()
                user_id = User.objects.get(email=user_email_add).pk

                # send email to the user
                appname = "AUTH"
                subject = "Password Reset Request" + gen_num_for_email()
                email_context = {
                    'change_notice'     : 'Password Reset Request',
                    'submission_time'   : datetime.datetime.now(),
                    'dns_name'          : settings.DNS_NAME,
                    'protocol'          : settings.PROTOCOL,
                    'uid'               : urlsafe_base64_encode(force_bytes(user_id)),
                    'token'             : default_token_generator.make_token(user),                   

                }
                html_message_text = render_to_string(
                    template_name=TEMP_DIR_EMAIL + 'pass_reset.html',
                    context=email_context,
                    using=None,
                    request=None
                )
                plain_message_text = strip_tags(html_message_text)
                print("calling send_email_customized from password_reset#106")
                send_email_customized(subject, plain_message_text, html_message_text, user_email_add, appname)

                # redirect user to pass reset done page
                return HttpResponseRedirect(reverse_lazy('mmhauth:password_reset_done'))

        else:
            form_error = "Something went wrong!"
    
    form            = PasswordResetCustomForm()
    template_name   = TEMP_DIR_HTMLPAGES + "password_reset/step1_request.html"
    context         = {
        "form": form, 
        "form_error": form_error,
        "pg_layout_type" : "pass_reset",
        "app_version"   : APP_VERSION
    }
    return render(request=request, template_name=template_name, context=context)





# # MMH: VERY VERY OLD CODE, RETAINED FOR FUTURE REFERENCE
# # MMH: VERY VERY OLD CODE, RETAINED FOR FUTURE REFERENCE
# # ******************************************************************************
# def mmh_auth_confirm_password_reset(request, uidb64, token):
#     zzz_print("    %-28s: %s" % ("mmh_auth_confirm_password_reset", "********************"))
#     decoded_pk = urlsafe_base64_decode(uidb64)
#     user = User.objects.get(pk=decoded_pk)
#     p = PasswordResetTokenGenerator()
#     is_valid = p.check_token(user, token)
#     if is_valid:
#         login(request, user)
#     return render(
#         request=request,
#         # mmh: not changed during move to mmh_auth_views from pc_auth_views
#         template_name=TEMP_DIR+"confirm_password_reset.html",
#         context={'is_valid': is_valid}
#     )


class PasswordResetRequestEmailConfirmationWithLinkView(auth_views.PasswordResetDoneView):
    template_name='mmhauth/layout/password_reset/step2_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_email_add'] = self.request.session['user_email_add']
        context['app_version'] = APP_VERSION

        return context


class PasswordResetSetNewPasswordView(auth_views.PasswordResetConfirmView):
    template_name   = 'mmhauth/layout/password_reset/step3_set_password.html'
    success_url     = reverse_lazy('mmhauth:password_reset_complete')
    form_class      = SetPasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_email_add'] = self.request.session['user_email_add']
        context['app_version'] = APP_VERSION

        return context
        