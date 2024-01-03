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
from django.conf import settings


TEMP_DIR_PRODUCT_DOCS   = 'mydocumentations/productdocs/layout/'


import datetime
from django.http import HttpResponse


# product docs / all services
##########################################
class AllServices(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "services_all.html"


# product docs / univ
##########################################
class AllPrimeServices(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "universal.html"


# product docs / proficiency
##########################################
class AllSeconServices(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "proficiency.html"


# FAQ / general
##########################################
class GeneralFaq(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "faq-general.html"


# product comparison
##########################################
class CompareAllServices(TemplateView):
    template_name = TEMP_DIR_PRODUCT_DOCS + "product-feature-matrix.html"
