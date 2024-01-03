#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print, zzz_print_exit

import json

from django.http import Http404, JsonResponse
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

# MMH: CONSIDER
# from ..models.muniqueid import muniqueid, muniqueid_FROM_SESSCOOK

from ..models import mcart
from ..models import muniqueid_get_users_uniquid
from ..models import mcart_fileupload
from ..models import mcompleted_purchase
from ..models import mpaypal

from .rw_cart_context import cart_context_forUser

# from pprint import pprint
# import random

# ******************************************************************************
def vcreate(request):
    zzz_print("    %-28s: %s" % ("vcreate", ""))
    if request.method == "POST":
        ipaypal = mpaypal.objects.mpaypal_add("mpaypal_create_order")
        ipaypal.mpaypal_create_order(cart_context_forUser(request))
        return JsonResponse(ipaypal.get_response_data())
    else:
        return JsonResponse({'details': "request.method not equal to POST"})


# ******************************************************************************
def vcapture(request, order_id):
    zzz_print("    %-28s: %s" % ("vcapture: order_id", order_id))
    if request.method == "POST":
        zzz_print("    %-28s: %s" % ("vcapture", "request.method == 'POST'"))
        ipaypal = mpaypal.objects.mpaypal_add("mpaypal_capture_order")
        ipaypal.mpaypal_capture_order(order_id)

        data = ipaypal.get_response_data()
        extracted_capture_id = ipaypal.extract_capture_id_from_captured_order_data()
        zzz_print("    %-28s: %s" % ("typeof (extracted_capture_id)", type(extracted_capture_id)))

        if (data and data['status'] == "COMPLETED"):
            zzz_print("    %-28s: %s %s (email_address = %s) (payer_id = %s)" % (
                "PAYMENT COMPLETED to payer",
                data['payer']['name']['given_name'],
                data['payer']['name']['surname'],
                data['payer']['email_address'],
                data['payer']['payer_id'],
            ))

            imcompleted_purchase = mcompleted_purchase.objects.add_mcompleted_purchase(
                paypaltransaction_id    = data['id'],
                payer_id                = data['payer']['payer_id'],
                capture_id              = extracted_capture_id,
                first_name              = data['payer']['name']['given_name'],
                last_name               = data['payer']['name']['surname'],
                email_address           = data['payer']['email_address']
            )
            zzz_print("    %-28s: %s" % ("imcompleted_purchase", imcompleted_purchase))

            data['icompletedpurchase_id'] = imcompleted_purchase.id
            data['paypaltransaction_id']  = imcompleted_purchase.paypaltransaction_id
            # zzz_print("    %-28s: %s" % ("paypaltransaction_id", imcompleted_purchase.paypaltransaction_id))

            # # Since order is completed now ...
            vpaypal_markItemsInCartAsPurchased(request, order_id, imcompleted_purchase)

            # # New July 6th, test attempt to capture payment_details to see if we can determine if a credit card was used.
            # ipaypal_payment_details = mpaypal.objects.mpaypal_add("mpaypal_payment_details")
            # ipaypal_payment_details.mpaypal_payment_details(extracted_capture_id)
            # data = ipaypal_payment_details.get_response_data()
            # pprint(data)

            return JsonResponse(data)
        else:
            # STUB CODE, ADD BETTER ERROR HANDLING HERE
            zzz_print("    %-28s: %s" % ("data and data[status]==COMPLETED", "FAILED"))
            zzz_print("    %-28s: %s" % ("data and data[status]==COMPLETED", "FAILED"))
            zzz_print("    %-28s: %s" % ("data and data[status]==COMPLETED", "FAILED"))
            zzz_print("    %-28s: %s" % ("data and data[status]==COMPLETED", "FAILED"))
            zzz_print_exit("    %-28s: %s" % ("data and data[status]==COMPLETED", "FAILED"))
    else:
        zzz_print("    %-28s: %s" % ("vcapture", "request.method != 'POST'"))
        return JsonResponse({'details': "request.method not equal to POST"})


# ******************************************************************************
def vpaypal_markItemsInCartAsPurchased(request, order_id, imcompleted_purchase):
    zzz_print("    %-28s: %s" % ("markItemsInCartAsPurchased", ""))
    zzz_print("    %-28s: %s" % ("order_id", order_id))
    zzz_print("    %-28s: %s" % ("imcompleted_purchase", imcompleted_purchase))

    # Update mcart instances purchased status
    qs = mcart.objects.mcartQS_usersItemsInCart(request)
    resume_required = False
    for imcart in qs:
        imcart.set_purchased(request, imcompleted_purchase)
        if imcart.resume_required:
            resume_required = True

    # mmh: deal with sometimes there wont be an mcart_fileupload
    zzz_print("    %-28s: %s" % ("resume_required", resume_required))
    if resume_required:
        # update mcart_fileupload instances
        owner_uniqid = muniqueid_get_users_uniquid(request)
        imcart_fileupload = mcart_fileupload.objects \
            .filter(owner_uniqid=owner_uniqid) \
            .filter(purchased=False) \
            .filter(validation_passed=True) \
            .order_by('-id') \
            .first()
        imcart_fileupload.purchased = True
        imcart_fileupload.mcompleted_purchase = imcompleted_purchase
        imcart_fileupload.save()



