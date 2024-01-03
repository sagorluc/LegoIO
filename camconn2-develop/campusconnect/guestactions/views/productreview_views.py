from datetime import datetime
import copy
import logging
from django.db.models import Q
from itertools import chain
import os

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from zzz_lib.zzz_log import zzz_print
from ..models import mfeedback
from guestactions.models import mcoupon, mcoupon_given


from ..forms import ProductReviewForm

from mymailroom.myfunctions.send_email import send_email_customized
from guestactions.myfunctions import generate_coupon_code
from django.utils.html import strip_tags
logger = logging.getLogger(__name__)

TEMP_DIR_GENERAL        = 'resumeweb/layout/general/'
TEMP_DIR_ACTION         = 'guestactions/product-review/'
TEMP_DIR_CONF           = 'resumeweb/layout/'
TEMP_DIR_PRODABOUT      = 'resumeweb/layout/product-docs/'
TEMP_DIR_EMAIL          = 'mymailroom/layout/'
TEMP_DIR_PRODFEEDBACK   = 'guestactions/product-review/'

import datetime
# product review system homepage
# ************************
def ProductReviewGuestView(request):
  zzz_print("    %-28s: %s" % ("ProductReviewGuestView", "********************"))

  if request.method == "POST":
    form = ProductReviewForm(data=request.POST)

    if form.is_valid():
        user_email_add = form.cleaned_data["email_address"]
        # save user_email_add in a session variable to be used in another view
        request.session['user_email_add'] = user_email_add

        # save form data in db 
        imfeedback = mfeedback.objects.add_mfeedback(
            request         = request,
            first_name      = form.cleaned_data["first_name"],
            last_name       = form.cleaned_data["last_name"],
            email_address   = form.cleaned_data["email_address"],
            product_liked   = form.cleaned_data["product_liked"],
            feedback        = form.cleaned_data["feedback"],
        )
        zzz_print("    %-28s: %s" % ("imfeedback", imfeedback))

        # generate coupon code
        coupon_code_dict = generate_coupon_code()
        logger.warning(f"coupon_code_dict from product review >>>{coupon_code_dict}")
        
        # send email to the user
        appname         = "GENERAL"
        subject         = 'Resumenalyzer Product Review Confirmation'
        email_context   = {
            'submission_time'   : datetime.datetime.now(),
            'submission_id'     : "adhocReq.id",
            'ques_details'      : "adhocReq.ques_details",
            'coupon_code_dict'  : coupon_code_dict

        }
        html_message_text = render_to_string(
            template_name=TEMP_DIR_EMAIL + 'product-review.html',
            context=email_context,
            using=None,
            request=None
        )
        plain_message_text = strip_tags(html_message_text)
        send_email_customized(subject, plain_message_text, html_message_text, user_email_add, appname)
        # email function ends

        messages.success(request, 'Form submitted successfully!')
        
        # redirect user to thankyou page
        return redirect("guestactions:submit_site_survey_as_guest")
    else:
        zzz_print("    %-28s: %s" % ("NOT form.is_valid", ""))
  else:
      zzz_print("    %-28s: %s" % ("request.method", "!= POST"))
      form = ProductReviewForm()

  template_name   = TEMP_DIR_ACTION + "home.html"
  context         = {
    "form": form,
    "pg_headline": "Submit Product Review",
    "resp_time": "1"
  }
  
  return render(
      request = request, 
      template_name = template_name, 
      context = context
  )


# confirmation page
# *****************
def feedback_submit_confirmation_view(request):
  zzz_print("    %-28s: %s" % ("feedback_submit_confirmation_view", "********************"))
  template_name  = TEMP_DIR_PRODFEEDBACK + "confirmation.html"

  email_add = request.session.get('user_email_add')
  
  context = {
      "email_address":  email_add,
      "date_time":      datetime.datetime.now(),
      "blue":           "blue",
      "red":            "red",
      "task":           "Product Review"
  }
  return render(
      request = request, 
      template_name = template_name, 
      context = context
  )
