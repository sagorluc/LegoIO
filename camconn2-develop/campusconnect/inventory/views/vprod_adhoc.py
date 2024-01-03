import os
import datetime
import copy
import json

# ******************************************************************************
from django.contrib import messages
import datetime
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import (
    render_to_string,
    get_template
)
from django.template import Context
from django.core.mail import send_mail, BadHeaderError
from django.utils.html import strip_tags
from django.views.generic.edit import FormMixin
from mymailroom.myfunctions import send_email
#from inventory.get_coupon_code import generate_coupon_code
import logging
logger = logging.getLogger(__name__)

from django.db.models import Q
from django.views.generic.base import TemplateView, View
from django.shortcuts import render, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    # UpdateView,
    # DetailView
)
from django.conf import settings
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from zzz_lib.zzz_log import zzz_print

from inventory.models.adhoc.adhoc_req import (
    AdhocRequestModel
)

from inventory.models import mprod_posti20

from inventory.forms.adhoc.adhocForm import (
    AdhocRequestForm,
)

prod_comp_data_adhoc = [
    ('1', 'You can order for a service that suits your needs'),
    ('2', 'We intent to respond to your request within 48 regular hours'),
    ('3', 'You will be informed if we are not able to provide a solution to your needs'),
    ('4', 'You can order for a service that suits your needs'),
    ('5', 'Submitting an Adhoc Request is free, you will be asked to make payment only if we provide with your service'),
    ('6', 'Service delivery within as minimum as 6 hours'),
]

# from resumeweb.product_selection import (
#     generate_product_list,

# )

from systemops.fetch_data import (
    fetch_data_faq
)

from systemops.fetch_data import fetch_data_ta


PATH_ROOT               = os.path.join(settings.BASE_DIR)
PATH_PRODUCT_LAYOUT     = 'inventory/pg-contents/adhoc/layout/'
PATH_PRODUCT_COMPONENT  = 'adhoc/templates/adhoc/components/'
TEMP_DIR_EMAIL          = 'adhoc/email_templates/adhoc/'

PRODUCT_LINE            = 'adhoc'
PRODUCT_SLOGAN          = 'add slogan for adhoc'

    
# homepage
# ***************************************************************
class AdhocHome(ListView):
    template_name = PATH_PRODUCT_LAYOUT+"homepg.html"
    queryset      = mprod_posti20.objects.all() #.filter(adhoc_get_started='yes')

    def get_context_data(self, **kwargs):
        context = super(AdhocHome, self).get_context_data()

        context['product_line'] = PRODUCT_LINE
        context['ta_list'] = fetch_data_ta(PRODUCT_LINE)
        context['pg_layout_type'] = 'homepg'
        return context



# This is adhoc sub req page
# ***************************************************************
class AdhocRequestByGuest(CreateView):
    template_name   = PATH_PRODUCT_LAYOUT+"request/create.html"
    form_class      = AdhocRequestForm
    model           = AdhocRequestModel


    def form_valid(self, form, **kwargs):

        adhocReq = form.save(commit=False)
        adhocReq.id = datetime.datetime.now().strftime('%f') 
        given_email = form.cleaned_data['email']
        adhocReq.save()

        # generate coupon code
        coupon_code_dict = generate_coupon(product_liked="mprod_adhoc")
        print(coupon_code_dict)
        

        email_address = given_email
        self.request.session['user_email'] = given_email
        subject = 'Adhoc Request Confirmation'+' #'+str(adhocReq.id)
        msg='thanks for your resume submission'
        change_notice ='resume upload at adhoc'
        submission_time = datetime.datetime.now()
        submission_id = adhocReq.id                 # random number

        send_email(email_address,
                    subject,msg,
                    change_notice, 
                    submission_time, 
                    submission_id, 
                    coupon_code_dict,
                    
                )
        
        return super(AdhocRequestByGuest, self).form_valid(form)


    def form_invalid(self, form, **kwargs):
        return HttpResponse('form_invalid is called')

    def get_success_url(self, **kwargs):
        token = '12665240228767'
        return reverse_lazy('adhoc_req_sub_conf', 
            kwargs={'id':self.object.pk, 'token':token}
        )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     logger.warning("line116>>>homepage get context")
    #     context = {
    #         'proflevel_list': mprod_proflevel.objects.all().order_by('levelname'),
    #         'strategysol_list': mprod_strategy.objects.all(),
    #         'posti20_list': mprod_posti20.objects.distinct('langname'),
    #         'rolebased_list': mprod_rolebased.objects.distinct('rolename'),
    #         'app_version': "1.0",           # settings.APP_VERSION_RW,
    #         'form_guest_resume': self.get_form()
    #     }

    #     return context


# ******************************************************************************
class AdhocRequestSubmitConf(View):
    template_name = PATH_PRODUCT_LAYOUT + "request/" + "conf-1.html"

    def get(self, request, *args, **kwargs):
        adhocReq = get_object_or_404(mprod_adhoc, id=kwargs['id'])

        context = {
                'submission_id':            adhocReq.id,
                'date_time':                adhocReq.created,
                'email_address_list':       [adhocReq.email],
                'electronic_delivery_email':adhocReq.email,
                'task':                     'Adhoc Service Request',
            }
        return render(request, self.template_name, context)


# ******************************************************************************
# terms and conditions
class AdhocTermsCond(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT+"terms-cond.html"


# ******************************************************************************
# app checklist
class AdhocAppChecklist(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT+"app-checklist.html"


# ******************************************************************************
# how it works
class AdhocHowItWorks(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT + "prod_ins_pg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'product_line': PRODUCT_LINE,
            'prod_slogan': PRODUCT_SLOGAN,
            'common_items': True,

            'pg_header': 'How it works',
            'how_it_works_section': True
        }
        return context


# use cases
# ******************************************************************************
class AdhocUseCases(ListView):
    template_name = PATH_PRODUCT_LAYOUT + "prod_ins_pg.html"

    def get_queryset(self):
        return mprod_posti20.objects.all().filter(level='adhoc_get_started')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'product_line': PRODUCT_LINE,
            'prod_slogan': PRODUCT_SLOGAN,
            'common_items': True,

            'ta_list': fetch_data_ta(PRODUCT_LINE),
            'pg_header': 'Use Cases',
            'use_cases_section': True,
        }  
        return context


# product Comparison
# ******************************************************************************
class AdhocCompareThis(TemplateView):
    template_name = "resumeweb/layout/base_prod_comparison_v2.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        prod_comp_data = [i[1] for i in prod_comp_data_adhoc]
        prod_list_others = generate_product_list(PRODUCT_LINE)

        context = {
            'prod_comp_data': prod_comp_data,
            'prod_list_others': prod_list_others,
            'product_line': PRODUCT_LINE,
            'prod_slogan': PRODUCT_SLOGAN,
            'common_items': True,
            'pg_header': 'Product Comparison',
            'prod_comp_section': True,

        } 
        return context


# ******************************************************************************
# deliver method
class AdhocProductDeliveryMethods(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT + "prod_ins_pg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'product_line': PRODUCT_LINE,
            'prod_slogan': PRODUCT_SLOGAN,
            'common_items': True,

            'pg_header': 'Product Delivery Methods',
            'gen_pdm_section': True
        }
        return context


# ******************************************************************************
# product faq
class AdhocFAQ(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT + "prod_ins_pg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {
            'product_line': PRODUCT_LINE,
            'prod_slogan': PRODUCT_SLOGAN,
            'common_items': True,

            'pg_header': 'FAQs',
            'adhoc_faq_section': True,
            'questions_answers': fetch_data_faq(PRODUCT_LINE)
        }

        return context
