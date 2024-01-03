from datetime import datetime

from django.db.models import Q
from itertools import chain

# from haystack.query import SearchQuerySet 
import datetime
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from zzz_lib.zzz_log import zzz_print
from ..models import ContactUsModel

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

import logging
logger = logging.getLogger(__name__)

from ..forms import ContactUsForm

from django.template import Context
from django.core.mail import send_mail, BadHeaderError
RESUME_FILE_TYPES = ['doc', 'docx']
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.edit import FormMixin


import datetime
from django.http import HttpResponse


from django.views.generic.edit import FormView
from mymailroom.myfunctions.send_email import send_email_customized
import copy
from guestactions.myfunctions import generate_coupon_code

TEMP_DIR_ACTION         = 'guestactions/contact-us/'
TEMP_DIR_EMAIL          = 'mymailroom/layout/'


class ContactUsGuestView(FormView):
    template_name   = TEMP_DIR_ACTION + "home.html"
    form_class      = ContactUsForm
    success_url     = reverse_lazy('guestactions:contact_us_guest')
    success_msg     = "You message has been received successfully"

    def get(self, request, *arg, **kwargs):
        form_class                      = self.get_form_class()
        form                            = self.get_form(form_class)
        context                         = self.get_context_data(**kwargs)
        context['form_order_search']    = form
        context["pg_headline"]          = "Contact Us"
        context["resp_time"]            = "1"

        return self.render_to_response(context)

    def form_valid(self, form):
        user_email_add = form.cleaned_data['email']
        messages.success(self.request, self.success_msg)

        # generate/select a coupon code from coupon table
        cop_code_dict   = generate_coupon_code()

        # send email to the user
        appname         = "CUSTSUPP"
        subject         = "Resumenalyzer Message Confirmation"
        user_email_add  = user_email_add
        
        email_context   = {
                'submission_id'     : "datetime.datetime.now()",
                'submission_time'   : datetime.datetime.now(),
                'coupon_code'       : cop_code_dict,
        }
        html_message_text = render_to_string(
            template_name=TEMP_DIR_EMAIL + 'contactus.html',
            context=email_context,
            using=None,
            request=None
        )
        plain_message_text = strip_tags(html_message_text)
        send_email_customized(subject, plain_message_text, html_message_text, user_email_add, appname)
        # email function ends

        return super().form_valid(form)
