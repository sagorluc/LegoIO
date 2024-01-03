import datetime
import copy
from itertools import chain

from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from zzz_lib.zzz_log import zzz_print
from ..forms import InviteFriendsForm
from guestactions.myfunctions import generate_coupon_code

TEMP_DIR_GENERAL      = 'resumeweb/layout/general/'
TEMP_DIR_INVITEFRIEND = 'guestactions/invite-friends/'
TEMP_DIR_EMAIL        = 'mymailroom/layout/'

from django.utils.html import strip_tags
from mymailroom.myfunctions.send_email import send_email_customized
# invite friends home
# ******************************************************************************
def InviteFriendsView(request):
    zzz_print("    %-28s: %s" % ("InviteFriendsGuestView", "********************"))


    if request.method == "POST":
        form = InviteFriendsForm(data=request.POST)

        if form.is_valid():
            zzz_print("    %-28s: %s" % ("form.is_valid", ""))

            invitedfriend = InviteFriends.objects.add_invitefriends(
                request               = request,

                guest_first_name      = form.cleaned_data["guest_first_name"],
                guest_last_name       = form.cleaned_data["guest_last_name"],
                guest_email_address   = form.cleaned_data["guest_email_address"],

                friend_first_name      = form.cleaned_data["friend_first_name"],
                friend_email_address   = form.cleaned_data["friend_email_address"],

                consent                = form.cleaned_data["consent"],
            )
            zzz_print("    %-28s: %s" % ("invitedfriend", invitedfriend))

            # save necessary info in a session variable to be used in another view
            email_guest = form.cleaned_data["guest_email_address"]
            email_friend = form.cleaned_data["friend_email_address"]
            request.session["email_guest"]  = email_guest
            request.session["email_friend"] = email_friend
            email_address_list = [email_guest, email_friend]

            # generate/select a coupon code from coupon table
            product_line = "exp180" #form.cleaned_data["product_liked"]
            cop_code = generate_coupon_code(product_liked=product_line)
            if cop_code is not None:
                cop_code = "No coupon code added"

            # send email to the user
            appname         = "GENERAL"
            subject         = "Resumenalyzer Invite Friends Confirmation"
            user_email_add  = email_guest

            email_context = {
                'submission_id'     : "datetime.datetime.now()",
                'submission_time'   : datetime.datetime.now(),
                'coupon_code'       : cop_code_dict,
            }
            html_message_text = render_to_string(
                template_name=TEMP_DIR_EMAIL + 'test106.html',
                context=email_context,
                using=None,
                request=None
            )
            plain_message_text = strip_tags(html_message_text)
            print("calling send_email_customized")
            send_email_customized(subject, plain_message_text, html_message_text, user_email_add, appname)


            # redirect user to page thanking them for their feedback
            return redirect("invite_friends_thankyou")
        else:
            zzz_print("    %-28s: %s" % ("NOT form.is_valid", ""))
    else:
        zzz_print("    %-28s: %s" % ("request.method", "!= POST"))
        form = InviteFriendsForm()


    template_name   = TEMP_DIR_INVITEFRIEND + "home.html"
    context         = {
        "form": form,
        "pg_headline": "Invite Friends"
    }
    return render(request = request, template_name = template_name, context = context)


# invite friends confirmation page
# ******************************************************************************
def InviteFriendsThankyou(request):
    zzz_print("    %-28s: %s" % ("invite_friends_thankyou", "********************"))
    template_name = TEMP_DIR_INVITEFRIEND + "confirmation.html"
    email_guest = request.session.get('email_guest')
    email_friend = request.session.get('email_friend')
    
    context = {
        "email_guest": email_guest,
        "email_friend": email_friend,
        "blue": "blue",
        "red":  "red",
    }
    return render(
        request = request, 
        template_name = template_name, 
        context = context
    )


