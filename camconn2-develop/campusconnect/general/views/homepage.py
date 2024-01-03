from datetime import datetime
import os
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
from guestactions.models import mfeedback
from guestactions.models.guest_resume_upload import GuestResumeModel
from general.models import mcoupon, mcoupon_given
from mymailroom.models import msendmail

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from inventory.models.mprod_prei20 import mprod_prei20
from inventory.models.mprod_prei20_catlist import mprod_prei20_catlist
from inventory.models.strategy.mprod_strategy import mprod_strategy
from inventory.models.posti20.mprod_posti20 import mprod_posti20
from inventory.models.univcom.mprod_univcom import mprod_univcom
from inventory.models.visaassist.mprod_visaassist import mprod_visaassist




from guestactions.forms import ProductReviewForm
from guestactions.forms import GuestResumeForm

import boto3
from inventory.models import mcart_fileupload
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
#from inventory.get_coupon_code import generate_coupon_code

import logging
logger = logging.getLogger(__name__)

TEMP_DIR_GENERAL    = 'general/layout/pages/'
TEMP_DIR_PRODABOUT  = 'resumeweb/layout/product-docs/'
TEMP_DIR_EMAIL      = 'resumeweb/email_templates/'

PRODUCT_LINE        = 'prei20'
PRODUCT_SLOGAN      = 'add slogan hereidentity'
MODEL_PRODUCT       = mprod_prei20
MODEL_PRODUCT_CAT   = mprod_prei20_catlist


class HomePageView(FormMixin, ListView):
    template_name           = TEMP_DIR_GENERAL + "homepage.html"
    login_url               = "/login/"
    redirect_field_name     = "redirect_to"
    context_object_name     = 'exp180_list'
    form_class              = GuestResumeForm
    msg_succ                = 'your resume submitted successfully'
    success_url             = reverse_lazy('site_homepage_url')
    model                   = MODEL_PRODUCT

    # def get_queryset(self):
    #     qs1 = super().get_queryset()
    #     qs1 = qs1.order_by('category')
    #     return qs1

    def post(self, request, *args, **kwargs):
        form_guest_resume = GuestResumeForm(self.request.POST, self.request.FILES)
        # logger.warning("line55>>>guest resume from home page ")
        if form_guest_resume.is_valid():
            return self.form_valid(form_guest_resume)
        else:
            return self.form_invalid(form_guest_resume)

    def form_valid(self, form_guest_resume):
        
        given_email = form_guest_resume.cleaned_data['email']
        form_guest_resume.save()

        ## step 1: generate coupon code
        coupon_code_dict = generate_coupon_code(product_liked="mprod_xyz")    
        ## step2: send email including that coupon code
        # submission_id = datetime.datetime.now().strftime('%f') # random number
        # email_address = given_email
        # self.request.session['user_email'] = given_email
        # subject = 'Resumenalizer Confirmation'+' # '+ str(submission_id)
        # msg = 'this msg should not be seen anywhere'
        # change_notice ='uploading your resume'
        # submission_time = datetime.datetime.now()
        
        # sent_email(email_address,
        #             subject,
        #             msg,
        #             change_notice, 
        #             submission_time, 
        #             submission_id, 
        #             coupon_code_dict,
                    
        #         )
        
        return super(HomePageView, self).form_valid(form_guest_resume)

    def form_invalid(self, form_guest_resume):
        form_guest_resume = GuestResumeForm()
        failed_url = reverse_lazy('site_homepage_url')
        return HttpResponseRedirect(failed_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        staircase_service_list = {
            # 'internship':   mprod_proflevel.objects.all(), #filter(category="1"),
            # 'junior':       mprod_proflevel.objects.filter(category="2"),
        }

        context = {
            'strategy_product_list': mprod_strategy.objects.all(),
            'prei20_product_list': mprod_prei20.objects.all(),
            # 'servicelist_dialog_startup': mprod_intprep.objects.filter(category='2'),
            # 'servicelist_dialog_bigtech': mprod_intprep.objects.filter(category='1'),
            'posti20_product_list': mprod_posti20.objects.all(),
            # #'servicelist_identy': mprod_rolebased.objects.all().order_by('category'),
            # 'servicelist_stairc': mprod_proflevel.objects.all().order_by('category'),
            # #'servicelist_bandwd': mprod_visabased.objects.all().order_by('category'),
            'univcom_product_list': mprod_univcom.objects.all(),
            'visaassist_product_list' :mprod_visaassist.objects.all(),

            'form_guest_resume' : self.get_form(),
            'app_version'       : settings.VER_RESUMEWEB,
            'server_type'       : settings.SERVER_TYPE
        }

        return context
