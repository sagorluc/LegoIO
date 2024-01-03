#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print, zzz_print_exit

from ...models.mcart import mcart
from ...models.mcart_deliveryoptions import mcart_deliveryoptions
#from ...models.mcart_serviceoptions import mcart_serviceoptions
from inventory.models.mcart_serviceoptions import mcart_serviceoptions
from general.models.mcoupon_given import mcoupon_given

from datetime import timedelta
from django.utils import timezone

# ******************************************************************************
# returns context dict of cart for mcart QuerySet
# consisting of these entries:
#
# 'products_list' : {
#     "mcart":                  mcart_instance,
#     "mcart_serviceoptions":   serviceoptions_list,
#     "mcart_deliveryoptions":  deliveryoptions_list,
#     "item_totalcost":         item_totalcost
#     }
# 'total_cost'      : total of all products_list item_totalcost
# 'resume_required' : True or False
# 'qs_mcoupon_given': query_string of mcoupon_given that are applicable to current cart
#
import decimal
def cart_context_forQuerySet(request, mcart_qs):
    zzz_print("    %-28s: %s" % ("cart_context_forQuerySet", ""))
    # zzz_print("    %-28s: %s" % ("mcart_qs", mcart_qs))
    # zzz_print("    %-28s: %s" % ("mcart_qs.count()", mcart_qs.count()))

    products_list = []
    final_total_cost = 0
    final_subtotal = 0
    final_taxtotal = 0
    final_deliverytotal = 0
    resume_required = False
    for mcart_instance in mcart_qs:
        # zzz_print("    %-28s: %s" % ("mcart_instance", mcart_instance))
        serviceoptions_list = []
        deliveryoptions_list = []
        deliverydate_list = []
        item_totalcost = mcart_instance.final_price  # was base_price
        final_subtotal += mcart_instance.final_price  # was base_price

        if mcart_instance.resume_required:
            resume_required = True

        # add each serviceoptions to item_totalcost
        qs2 = mcart_serviceoptions.objects.filter(mcart=mcart_instance)
        print("QS@================================", qs2)
        for serviceoption_instance in qs2:
            serviceoptions_list.append(serviceoption_instance)
            print("serviceoptions_list================================", serviceoptions_list)
            item_totalcost += serviceoption_instance.price
            final_subtotal += serviceoption_instance.price

        # add each deliveryoption to item_totalcost
        qs2 = mcart_deliveryoptions.objects.filter(mcart=mcart_instance)
        
        for deliveryoption_instance in qs2:
            deliveryoptions_list.append(deliveryoption_instance)
            item_totalcost += deliveryoption_instance.price
            final_deliverytotal += deliveryoption_instance.price

            now                     = timezone.now()    # using django timezone
            TD_delivered            = timedelta(hours=deliveryoption_instance.hours_to_deliver_after_payment)
            TD_to_delivery          = now + TD_delivered
            # zzz_print("    %-32s: %s" % ("now", str(now)))
            # zzz_print("    %-32s: %s" % ("TD_delivered", str(TD_delivered)))
            # zzz_print("    %-32s: %s" % ("TD_to_delivery", str(TD_to_delivery)))
            deliverydate_list.append(TD_to_delivery)

        # calculate tax_price per item
        tax_rate = 0.06
        # item_tax_price = mcart_instance.tax_price
        item_tax_price = round((decimal.Decimal(item_totalcost) * decimal.Decimal(tax_rate)), 2)
        final_taxtotal += item_tax_price

        # calculate item_totalcost per item
        item_totalcost = item_totalcost + (decimal.Decimal(item_totalcost) * decimal.Decimal(tax_rate))
        item_totalcost = round(item_totalcost, 2)

        final_total_cost += item_totalcost
        products_list.append({
            "mcart":                    mcart_instance,
            "mcart_serviceoptions":     serviceoptions_list,
            "mcart_deliveryoptions":    deliveryoptions_list,
            "item_totalcost":           item_totalcost,
            "item_tax_price":           item_tax_price,
            "deliverydate_list":        deliverydate_list
        })

    # # Get list of all model_names in cart. Will be used to dtermine which coupons are applicable for cart items.
    # modelname_list_in_cart = []
    # for product in products_list:
    #     if product['mcart'].model_name not in modelname_list_in_cart:
    #         modelname_list_in_cart.append(product['mcart'].model_name)
    # # for modelname in modelname_list_in_cart:
    # #     zzz_print("    %-28s: %s" % ("modelname", modelname))
    # qs_mcoupon_given = mcoupon_given.objects.mcouponQS_validCouponsForProductsInCart(request, modelname_list_in_cart)
    print("servie lice +++++++++++++++++++++++++++++++ ",products_list)
    context = {
        'products_list'         : products_list,
        'total_cost'            : final_total_cost,
        'resume_required'       : resume_required,
        'final_subtotal'        : final_subtotal,
        'final_taxtotal'        : final_taxtotal,
        'final_deliverytotal'   : final_deliverytotal,
        # 'qs_mcoupon_given'      : qs_mcoupon_given,
    }

    # zzz_print(context, pretty=True)
    # ******************************************************************************************** ZZZ_PRETTY | START:
    # {
    #     'products_list': [
    #         {
    #             'item_tax_price'        : Decimal('0.18'),
    #             'item_totalcost'        : Decimal('3.18'),
    #             'mcart'                 : <mcart: ID (1) owner_uniqid (fafb8c33-04c5-4c8b-8e00-6cf5b723d486) muser (def274753@gmail.com) MODEL_NAME (mprod_exp180) TITLE: exp_180_product_01>,
    #             'mcart_deliveryoptions' : [
    #                 <mcart_deliveryoptions: DO: mcart (ID (1) owner_uniqid (fafb8c33-04c5-4c8b-8e00-6cf5b723d486) muser (def2747530@gmail.com) MODEL_NAME (mprod_exp180) TITLE: exp_180_product_01) name (exp_180_product_all_delivery_option_01) , hours to cancel = 168, hours to deliver = 336>
    #             ],
    #             'mcart_serviceoptions'  : [
    #                 <mcart_serviceoptions: SO: mcart (ID (1) owner_uniqid (fafb8c33-04c5-4c8b-8e00-6cf5b723d486) muser (def274753@gmail.com) MODEL_NAME (mprod_exp180) TITLE: exp_180_product_01) name (exp_180_product_01_service_option_01) >
    #             ]
    #         }
    #     ],
    #     'resume_required': True,
    #     'total_cost': Decimal('3.18')
    # }
    # ******************************************************************************************** ZZZ_PRETTY | END:


    return context


# ******************************************************************************
def highest_priced_product_item_in_cart_context_forUser(request, model_name):
    zzz_print("    %-28s: %s" % ("highest_priced_product_item_in_cart_context_forUser", ""))
    zzz_print("    %-28s: %s" % ("model_name", model_name))

    mcart_qs = mcart.objects.mcartQS_usersItemsInCart(request)
    zzz_print("    %-28s: %s" % ("mcart_qs.count()", mcart_qs.count()))

    return_mcart_instance = None
    for mcart_instance in mcart_qs:
        if (mcart_instance.model_name == model_name) or (mcart_instance.model_name != model_name):
            print("(mcart_instance.model_name == model_name) or (mcart_instance.model_name != model_name) is true")
            if return_mcart_instance is None:
                return_mcart_instance = mcart_instance
            elif mcart_instance.base_price > return_mcart_instance.base_price:
                return_mcart_instance = mcart_instance
        else:
            print("mcart_instance.model_name == model_name_from_coupon is false")

    if return_mcart_instance is None:
        zzz_print_exit("    %-28s: %s" % ("WARNING NO ITEM FOUND IN CART for", model_name))

    return return_mcart_instance


# ******************************************************************************
def cart_context_forUser(request):
    zzz_print("    %-28s: %s" % ("cart_context_forUser", ""))
    qs = mcart.objects.mcartQS_usersItemsInCart(request)
    context = cart_context_forQuerySet(request, qs)
    return context

# ******************************************************************************
def cart_context_forTrackingId(request, tracking_id):
    zzz_print("    %-28s: %s" % ("cart_context_forTrackingId", tracking_id))
    qs = mcart.objects.mcartInstance_userOrderHistory_byTrackingId(request, tracking_id)
    context = cart_context_forQuerySet(request, qs)
    return context

# ******************************************************************************
# returns context dict of cart for purchase_order_id
def cart_context_forMcompletedPurchase(request, imcompleted_purchase):
    zzz_print("    %-28s: %s" % ("cart_context_forMcompletedPurchase", ""))
    zzz_print("    %-28s: %s" % ("imcompleted_purchase", imcompleted_purchase))
    mcart_qs = mcart.objects.filter(mcompleted_purchase=imcompleted_purchase)
    context = cart_context_forQuerySet(request, mcart_qs)
    return context

# ******************************************************************************
def cart_context_loggit_serviceoption(serviceoption):
    # zzz_print("    %-28s: %s" % ("cart_context_loggit_serviceoption", ""))
    zzz_print("    %-28s: %s" % ("serviceoption", serviceoption))

# ******************************************************************************
def cart_context_loggit_deliveryoptionoption(deliveryoption):
    # zzz_print("    %-28s: %s" % ("cart_context_loggit_deliveryoptionoption", ""))
    # zzz_print("    %-28s: %s" % ("cart_context_loggit_deliveryoptionoption", ""))
    zzz_print("    %-28s: %s" % ("deliveryoption", deliveryoption))

# ******************************************************************************
def cart_context_loggit_product(product):
    # zzz_print("    %-28s: %s" % ("cart_context_loggit_product", ""))
    zzz_print("    %-28s: %s" % ("product['mcart']", product['mcart']))

    for serviceoption in product['mcart_serviceoptions']:
        cart_context_loggit_serviceoption(serviceoption)
    for deliveryoption in product['mcart_deliveryoptions']:
        cart_context_loggit_deliveryoptionoption(deliveryoption)

# ******************************************************************************
def cart_context_loggit(cart_context):
    zzz_print("    %-28s: %s" % ("cart_context_loggit", "------------------"))
    # zzz_print("    %-28s: %s" % ("len(cart_context['products_list'])", len(cart_context['products_list'])))
    for product in cart_context['products_list']:
        cart_context_loggit_product(product)

    zzz_print("    %-28s: %s" % ("cart_context['total_cost']", cart_context['total_cost']))
    zzz_print("    %-28s: %s" % ("cart_context['resume_required']", cart_context['resume_required']))
    zzz_print("    %-28s: %s" % ("cart_context_loggit", "------------------"))






