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
from general.models import mcoupon, mcoupon_given
from mymailroom.models import msendmail


from django.conf import settings
from guestactions.models.guest_resume_upload import GuestResumeModel


TEMP_DIR_GENERAL        = 'genaral/layout/general/'
TEMP_DIR_PRODUCT_DOCS   = 'resumeweb/layout/product-docs/'
TEMP_DIR_EMAIL          = 'resumeweb/email_templates/'
##########################################
##########################################
### general 
##########################################
##########################################
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, BadHeaderError
RESUME_FILE_TYPES = ['doc', 'docx']
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.edit import FormMixin

import datetime
from django.http import HttpResponse


class Page404View(TemplateView):
    pass



class Covid19ResponseView(TemplateView):
    template_name = TEMP_DIR_GENERAL +  'covid19.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {
            'refund_policy_gen': "General Refund Policy"
        }

        return context




class BLMResponseView(TemplateView):
    template_name = TEMP_DIR_GENERAL + 'blm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {
            'refund_policy_gen': "General Refund Policy"
        }

        return context

# promo offers 
##########################################
class PromotionalOffersView(TemplateView):
    template_name = TEMP_DIR_GENERAL + 'promo-offers-2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {
            'refund_policy_gen': "General Refund Policy"
        }

        return context

# about us 
##########################################
class AboutUsView(TemplateView):
    template_name = TEMP_DIR_GENERAL + 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {
            'refund_policy_gen': "General Refund Policy"
        }

        return context


# this is beta 
##########################################
class ThisIsBeta(TemplateView):
    template_name = TEMP_DIR_GENERAL + 'this-is-beta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {
            'refund_policy_gen': "General Refund Policy"
        }

        return context

# us only support
##########################################
class UsOnlySupport(TemplateView):
    template_name = TEMP_DIR_GENERAL + 'us-only-support.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {
            'refund_policy_gen': "General Refund Policy"
        }

        return context


# member benefits
##########################################
class MemberBenefitsView(TemplateView):
    template_name = TEMP_DIR_GENERAL + 'member-benefits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {
            'refund_policy_gen': "General Refund Policy"
        }

        return context



# customer service home
##########################################
class HelpCenterHome(TemplateView):
    template_name = TEMP_DIR_GENERAL + "help-center-home.html"


