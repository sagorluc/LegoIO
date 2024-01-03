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

from inventory.models import (
    mfeedback, 
    mcoupon, 
    mcoupon_given, 
    msendmail
)

from inventory.models import (
    mprod_prei20,

   
)

from guestactions.forms import (
    ProductReviewForm,
    GuestResumeForm,

)


TEMP_DIR_GENERAL        = 'resumeweb/layout/general/'
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


# FAQ / general
##########################################
class GeneralFaq(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "faq-general.html"
    

# product docs / all services
##########################################
class AllServices(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "services_all.html"


# product docs / univ
##########################################
class AllPrimeServices(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "services_univ.html"


# product docs / proficiency
##########################################
class AllSeconServices(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "services_prof.html"

