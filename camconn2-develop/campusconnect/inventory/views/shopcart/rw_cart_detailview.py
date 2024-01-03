from zzz_lib.zzz_log import zzz_print

from django.apps import apps
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.template.loader import render_to_string

from inventory.models import mcart
from inventory.models.mcart_deliveryoptions import mcart_deliveryoptions
from inventory.models.mcart_serviceoptions import mcart_serviceoptions

# ******************************************************************************
class cartDetailViewClass:

    # --------------------------------------------------------------------------
    def __init__(self, product_model_name, product_detail_template_name, breadcrumb_url_name, breadcrumb_url_displaytext):
        self.product_model_name = product_model_name
        self.product_detail_template_name = product_detail_template_name
        self.breadcrumb_url_name = breadcrumb_url_name
        self.breadcrumb_url_displaytext = breadcrumb_url_displaytext

# ******************************************************************************
def cartDetailView_byMode(request, icdvc, id, mode):
    zzz_print("    %-28s: %s %s %s %s" % ("cartDetailView_byMode", "id =", id, "mode =", mode))
    zzz_print("    %-48s: %s" % ("  ++++ icdvc.product_model_name",           icdvc.product_model_name))
    zzz_print("    %-48s: %s" % ("  ++++ icdvc.product_detail_template_name", icdvc.product_detail_template_name))
    zzz_print("    %-48s: %s" % ("  ++++ icdvc.breadcrumb_url_name",          icdvc.breadcrumb_url_name))
    zzz_print("    %-48s: %s" % ("  ++++ icdvc.breadcrumb_url_displaytext",   icdvc.breadcrumb_url_displaytext))

    deliveryoption_model_name   = icdvc.product_model_name + "_deliveryoption"
    serviceoption_model_name    = icdvc.product_model_name + "_serviceoption"
    zzz_print("    %-28s: %s" % ("deliveryoption_model_name", deliveryoption_model_name))
    zzz_print("    %-28s: %s" % ("serviceoption_model_name", serviceoption_model_name))

    # Generate dynamic models for product, deliveryoption and serviceoption.
    # These will be used in queries below.
    product_dynamic_django_model        = apps.get_model("inventory", icdvc.product_model_name)

    deliveryoption_dynamic_django_model = None
    try:
        deliveryoption_dynamic_django_model = apps.get_model("inventory", deliveryoption_model_name)
    except LookupError:
        zzz_print("    %-28s: %s" % ("deliveryoption_dynamic_django_model", "NOT FOUND"))

    serviceoption_dynamic_django_model  = None
    try:
        serviceoption_dynamic_django_model  = apps.get_model("inventory", serviceoption_model_name)
    except LookupError:
        zzz_print("    %-28s: %s" % ("serviceoption_dynamic_django_model", "NOT FOUND"))

    # First use of a dynamic model name
    instance = product_dynamic_django_model.objects.get(id=id)
    mcart_instance = mcart.objects.mcartInstance_modelNameAndId(request, icdvc.product_model_name, instance.id)
    if not mcart_instance:
        zzz_print("    %-28s: %s" % ("mcart_instance", "IS NONE"))

    # GET AVAILABLE DELIVERY OPTIONS and SERVICE OPTIONS for this instance
    qs_delivery_options = []
    if deliveryoption_dynamic_django_model:
        qs_delivery_options = deliveryoption_dynamic_django_model.objects.filter(products=instance)

    qs_service_options = []
    if serviceoption_dynamic_django_model:
        qs_service_options = serviceoption_dynamic_django_model.objects.filter(products=instance)

    # for item in qs_delivery_options:
    #     zzz_print("    %-28s: %s" % ("delivery option name", item.name))
    #     zzz_print("    %-28s: %s" % ("delivery option price", item.price))
    #     zzz_print("    %-28s: %s" % ("delivery option ndb_checked", item.ndb_checked))
    # for item in qs_service_options:
    #     zzz_print("    %-28s: %-25s price %s" % ("service option", item, item.price))

    # get list of selected service options and selected delivery options
    selected_deliveryoption_id_list = []
    selected_serviceoption_id_list = []
    if mcart_instance and not mcart_instance.purchased:
        for item in mcart_deliveryoptions.objects.filter(mcart=mcart_instance):
            selected_deliveryoption_id_list.append(item.deliveryoption_id)
        for item in mcart_serviceoptions.objects.filter(mcart=mcart_instance):
            selected_serviceoption_id_list.append(item.serviceoption_id)

    # for id in selected_deliveryoption_id_list:
    #     zzz_print("    %-28s: %s" % ("selected_deliveryoption_id", id))
    # for id in selected_serviceoption_id_list:
    #     zzz_print("    %-28s: %s" % ("selected_serviceoption_id", id))

    # update qs_service_options based on mcart_instance data
    if mcart_instance and not mcart_instance.purchased:
        for item in qs_service_options:
            if item.id in selected_serviceoption_id_list:
                item.ndb_checked = True

    for item in qs_delivery_options:
        if item.id in selected_deliveryoption_id_list:
            item.ndb_checked = True
            break
        if not selected_deliveryoption_id_list:
            item.ndb_checked = True
            break

    disable_item = False
    if mcart_instance:
        if not mcart_instance.removed or mcart_instance.purchased:
            disable_item = True

    context = {
        'model_name'                            : icdvc.product_model_name,
        'object'                                : instance,
        'qs_delivery_options'                   : qs_delivery_options,
        'qs_service_options'                    : qs_service_options,
        'disable_item'                          : disable_item,
        'similar_services'                      : product_dynamic_django_model.objects.exclude(id=id),
        'breadcrumb_url_name'                   : icdvc.breadcrumb_url_name,
        'breadcrumb_url_displaytext'            : icdvc.breadcrumb_url_displaytext,
    }

    html = render_to_string(icdvc.product_detail_template_name, context)

    if   mode == "html":    return html
    elif mode == "ajax":    return JsonResponse({"html":html})
    else:                   return "<b> ERROR: SHOULD NOT GET HERE </b>"



















