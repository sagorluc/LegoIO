import os
from zzz_lib.zzz_log import zzz_print
import json
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.generic import (
    ListView,
    UpdateView,
)

from ..models import (
    mprod_posti20_catlist,
    mprod_posti20,
)

from .shopcart.rw_cart_detailview import (
    cartDetailView_byMode,
    cartDetailViewClass
)

from productops.data_prod_comp_v3 import (
    prod_comp_data_dialect,

)

from productops.product_selection import (
    generate_product_list,
)

from systemops.fetch_data import (
    fetch_data_faq,
    fetch_data_ta,
    fetch_data_impfact
)

from productops.fetch_product_data import (
    get_category,
    get_cat_list,
    get_other_services,
)

PATH_PRODUCT_LAYOUT     = "inventory/layout/products/posti20/"
PATH_ROOT               = os.path.join(settings.BASE_DIR)
PATH_PRODUCT_COMPONENT  = 'inventory/templates/inventory/components/products/posti20'

PRODUCT_LINE        = 'posti20'
PRODUCT_SLOGAN      = 'add slogan hereidentity'
MODEL_PRODUCT       = mprod_posti20
MODEL_PRODUCT_CAT   = mprod_posti20_catlist


# ******************************************************************************
class PostI20Home(ListView):
    template_name = PATH_PRODUCT_LAYOUT + "homepg.html"
    model = MODEL_PRODUCT

    def get_queryset(self):
        qs1 = super().get_queryset()
        qs1 = qs1.order_by('category')
        return qs1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['servicelist_posti20'] = self.model.objects.all().order_by('category')
        context['product_line'] = PRODUCT_LINE
        context['ta_list'] = fetch_data_ta(PRODUCT_LINE)
        context['pg_layout_type'] = 'homepg'
        
        return context


# ******************************************************************************
class PostI20ServiceAll(ListView):
    template_name = PATH_PRODUCT_LAYOUT + "all_serv.html"
    model = MODEL_PRODUCT

    def get_queryset(self):
        qs1 = super().get_queryset()
        qs1 = qs1.order_by('category')
        return qs1

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        ## special items
        # cat list section
        cat_list = MODEL_PRODUCT_CAT.objects.values_list('catname', flat=True).distinct()
        context['cat_list'] = cat_list

        ## left sidebar items
        context['all_serv_link'] = True
        context['prod_ins_menu'] = True
        context['need_help'] = True
        context['need_customization'] = True

        ## common items
        context['product_line'] = PRODUCT_LINE
        context['pg_header'] = 'All Services'
        context['pg_layout_type'] = 'all_serv_list'

        return context


# ******************************************************************************
class PostI20ServiceByCat(ListView):
    template_name = PATH_PRODUCT_LAYOUT + "all_serv.html"
    model = MODEL_PRODUCT

    def get_queryset(self):
        qs1 = super().get_queryset()
        category_selected = get_object_or_404(MODEL_PRODUCT_CAT, langname=self.kwargs.get('posti20'))
        qs1 = qs1.filter(category=category_selected)
        return qs1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_selected = self.kwargs['posti20']
        # cat_list / by_cat related info        
        cat_list = MODEL_PRODUCT_CAT.objects.all()

        # product, product page info
        # this section is common in all strategy solution product pages
        context['category_selected'] = category_selected
        context['cat_list'] = cat_list
        
        # left sidebar items
        context['all_serv_link'] = True
        context['prod_ins_menu'] = True
        context['need_help'] = True
        context['need_customization'] = True

        ## common items
        context['product_line'] = PRODUCT_LINE
        context['pg_header'] = 'Services by Category'
        context['pg_layout_type'] = 'all_serv_list'

        return context
        



# ******************************************************************************
def populate_cardDetailViewClass():
    product_model_name              = "mprod_posti20"
    product_detail_template_name    = "inventory/pg-contents/product-details-v2/prod-details.html"
    breadcrumb_url_name             = "posti20_all_services"     # Name of django view that is used for breadcrumb url for this product
    breadcrumb_url_displaytext      = "PostI20 All Services"     # Text to display in breadcrumb url
    return cartDetailViewClass(product_model_name, product_detail_template_name, breadcrumb_url_name, breadcrumb_url_displaytext)


# ******************************************************************************
def PostI20ServiceProdDetails_ajax(request, id):
    zzz_print("    %-28s: %s" % ("PostI20ServiceProdDetails_ajax (id)", id))
    icdvc = populate_cardDetailViewClass()
    html  = cartDetailView_byMode(request, icdvc, id, "ajax")
    # zzz_print("    %-28s: %s" % ("html", html))
    return html


# ******************************************************************************
def PostI20ServiceProdDetails(request, id):
    zzz_print("    %-28s: %s" % ("PostI20ServiceProdDetails (id)", id))
    full_template                   = loader.get_template(PATH_PRODUCT_LAYOUT+'prod-details.html')

    icdvc = populate_cardDetailViewClass()
    html  = cartDetailView_byMode(request, icdvc, id, "html")
    # zzz_print("    %-28s: %s" % ("html", html))

    cat_selected = get_category(id,MODEL_PRODUCT,MODEL_PRODUCT_CAT)
    print(MODEL_PRODUCT)
    cat_list = get_cat_list(id,MODEL_PRODUCT,MODEL_PRODUCT_CAT)
    other_services = get_other_services(id,MODEL_PRODUCT)

    context = {
        'mmh_product_details_contents': html,

        # right column items
        'cat_list': cat_list,
        'cat_selected': cat_selected,
        'serv_others': other_services,
        
        # common items
        'product_line'      : PRODUCT_LINE,
        'pg_header'         : 'Product Details',
        'questions_answers' : fetch_data_faq(PRODUCT_LINE),
        'ta_list'           : fetch_data_ta(PRODUCT_LINE),
        'fa_list'           : fetch_data_impfact(PRODUCT_LINE)
    }
    return HttpResponse(full_template.render(context, request))


# our speciality
# ******************************************************************************
class PostI20Ourspeciality(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT + "prod_ins_pg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'product_line': PRODUCT_LINE,
            'pg_header': 'FAQs',                        

            'identity_faq': "Identity FAQ",

        }

        return context


# how it works
# ******************************************************************************
class PostI20HowItWorks(TemplateView):
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


# Product Comparison
# ******************************************************************************
class PostI20CompareThis(TemplateView):
    template_name = "resumeweb/layout/base_prod_comparison_v2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        prod_comp_data = [i[1] for i in prod_comp_data_dialect]
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


# use cases
# ******************************************************************************
class PostI20UseCases(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT + "prod_ins_pg.html"

    def get_context_data(self, **kwargs):
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


# delivery methods
# ******************************************************************************
class PostI20ProductDeliveryMethods(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT + "prod_ins_pg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'product_line': PRODUCT_LINE,
            'prod_slogan': PRODUCT_SLOGAN,
            'common_items': True,

            'pg_header'         : 'Product Delivery Methods',
            'gen_pdm_section'   : True,
            'ta_list'           : fetch_data_ta(PRODUCT_LINE),
        }
        return context


# ******************************************************************************
# product faq
class PostI20FAQ(TemplateView):
    template_name = PATH_PRODUCT_LAYOUT + "prod_ins_pg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'product_line': PRODUCT_LINE,
            'prod_slogan': PRODUCT_SLOGAN,
            'common_items': True,

            'pg_header': 'FAQs',
            'dialect_faq_section': True,
            'questions_answers': fetch_data_faq(PRODUCT_LINE)
        }

        return context
