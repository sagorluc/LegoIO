#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print, zzz_print_exit

import datetime
from datetime import timedelta
from decimal import Decimal
from threading import Thread

import random
import urllib.parse
import decimal

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone

from inventory.models.mcart_deliveryoptions import mcart_deliveryoptions
from inventory.models.mcart_serviceoptions import mcart_serviceoptions
from .mcart_coupons import mcart_coupons


from inventory import const_inventory

from inventory.models.muniqueid import muniqueid_get_users_uniquid

# ******************************************************************************
class mcart_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def mcart_add_or_update_ver2(self, request, item_id, model_name, quantity, service_option_id_list, delivery_option_id_list, resume_required):
        owner_uniqid = muniqueid_get_users_uniquid(request)
        add_or_update_mode = "EXISTS"
        try:
            mcart_instance = mcart.objects.get(owner_uniqid=owner_uniqid, item_id=item_id, model_name=model_name, purchased=False)
            if request.user.is_authenticated:
                zzz_print("    %-28s: %s" % ("*** request.user.is_authenticated", "TRUE"))
                mcart_instance.muser = request.user
        except ObjectDoesNotExist:
            add_or_update_mode = "ADDED"
            mcart_instance = self.create(owner_uniqid=owner_uniqid, item_id=item_id, model_name=model_name)
            if request.user.is_authenticated:
                zzz_print("    %-28s: %s" % ("*** request.user.is_authenticated", "TRUE"))
                mcart_instance.muser = request.user

        product_model_name          = model_name
        deliveryoption_model_name   = product_model_name + "_deliveryoption"
        serviceoption_model_name    = product_model_name + "_serviceoption"
        # zzz_print("    %-28s: %s" % ("product_model_name", product_model_name))
        # zzz_print("    %-28s: %s" % ("deliveryoption_model_name", deliveryoption_model_name))
        # zzz_print("    %-28s: %s" % ("serviceoption_model_name", serviceoption_model_name))

        # Generate dynamic models for product, deliveryoption and serviceoption.
        # These will be used in queries below.
        product_dynamic_django_model        = apps.get_model("inventory", product_model_name)

        #deliveryoption_dynamic_django_model = apps.get_model("inventory", deliveryoption_model_name)
        #serviceoption_dynamic_django_model  = apps.get_model("inventory", serviceoption_model_name)
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

        # Get product_instance for item_id as it contains salesprice and title
        product_instance = product_dynamic_django_model.objects.get(id=item_id)
        mcart_instance.base_price       = product_instance.saleprice
        mcart_instance.title            = product_instance.title
        mcart_instance.sku              = product_instance.sku
        mcart_instance.quantity         = quantity
        mcart_instance.resume_required  = resume_required
        mcart_instance.save()

        zzz_print("    %-28s: %s, %s" % ("mcart_instancemanager", add_or_update_mode, mcart_instance.__str__()))
        mcart_instance.clear_removed()

        if deliveryoption_dynamic_django_model:
            mcart_instance.handleCurrentDeliveryOptionIdList(delivery_option_id_list, deliveryoption_dynamic_django_model)

        if serviceoption_dynamic_django_model:
            mcart_instance.handleCurrentServiceOptionIdList (service_option_id_list,  serviceoption_dynamic_django_model)

    # --------------------------------------------------------------------------
    def remove_ver2(self, request, item_id, model_name):
        owner_uniqid = muniqueid_get_users_uniquid(request)
        try:
            mcart_instance = mcart.objects.get(owner_uniqid=owner_uniqid, item_id=item_id, model_name=model_name, purchased=False)
            mcart_instance.set_removed()

            # delete all mcart_serviceoptions that currently refer to this mcart instance
            deleteTuple = mcart_serviceoptions.objects.filter(mcart=mcart_instance).delete()
            zzz_print("    %-28s: %s" % ("serviceoptions DELETED", deleteTuple[0]))

            # delete all mcart_deliveryoptions that currently refer to this mcart instance
            deleteTuple = mcart_deliveryoptions.objects.filter(mcart=mcart_instance).delete()
            zzz_print("    %-28s: %s" % ("deliveryoptions DELETED", deleteTuple[0]))

            # delete all mcart_coupons that currently refer to this mcart instance
            deleteTuple = mcart_coupons.objects.filter(mcart=mcart_instance).delete()
            zzz_print("    %-28s: %s" % ("mcart_coupons DELETED", deleteTuple[0]))

        except ObjectDoesNotExist:
            zzz_print("    %-28s: %s" % ("owner_uniqid", owner_uniqid))
            zzz_print("    %-28s: %s" % ("item_id", item_id))
            zzz_print("    %-28s: %s" % ("model_name", model_name))
            zzz_print_exit("    %-28s: %s" % ("ERROR: DOES NOT EXIST", "Exception Exit"))

    # --------------------------------------------------------------------------
    def mcartQS_usersItemsInCart(self, request):
        # zzz_print("    %-28s: %s" % ("mcartQS_usersItemsInCart", ""))
        owner_uniqid = muniqueid_get_users_uniquid(request)
        qs = mcart.objects \
            .filter(owner_uniqid=owner_uniqid) \
            .filter(removed=False) \
            .filter(purchased=False) \
            .order_by('-id')
        # zzz_print("    %-28s: %s" % ("mcartQS_usersItemsInCart qs.count()", qs.count()))
        return qs

    # --------------------------------------------------------------------------
    def mcartQS_modelNameAndIdItemsInCart(self, request, model_name, item_id):
        zzz_print("    %-28s: model_name = %s, item_id = %s" % ("mcartQS_modelNameAndIdItemsInCart", model_name, item_id))
        owner_uniqid = muniqueid_get_users_uniquid(request)
        qs = mcart.objects \
            .filter(owner_uniqid=owner_uniqid) \
            .filter(model_name=model_name) \
            .filter(item_id=item_id) \
            .filter(removed=False) \
            .filter(purchased=False) \
            .order_by('-id')
        # zzz_print("    %-28s: %s" % ("mcartQS_modelNameAndIdItemsInCart qs.count()", qs.count()))
        return qs

    # --------------------------------------------------------------------------
    def mcartInstance_modelNameAndId(self, request, model_name, item_id):
        zzz_print("    %-28s: model_name = %s, item_id = %s" % ("mcartInstance_modelNameAndId", model_name, item_id))
        owner_uniqid = muniqueid_get_users_uniquid(request)
        return_instance = mcart.objects \
            .filter(owner_uniqid=owner_uniqid) \
            .filter(model_name=model_name) \
            .filter(item_id=item_id) \
            .filter(purchased=False) \
            .order_by('-id') \
            .first()
        return return_instance

    # --------------------------------------------------------------------------
    def mcartQS_userOrderHistory_byStatus(self, request, processing_status):
        # zzz_print("    %-28s: processing_status = %s" % ("mcartQS_userOrderHistory_byStatus", processing_status))
        owner_uniqid = muniqueid_get_users_uniquid(request)
        qs = mcart.objects \
            .filter(owner_uniqid=owner_uniqid) \
            .filter(purchased=True) \
            .filter(processing_status=processing_status) \
            .order_by('id')
        # zzz_print("    %-28s: %s" % ("qs.count()", qs.count()))
        return qs

    # --------------------------------------------------------------------------
    def mcartInstance_userOrderHistory_byTrackingId(self, request, tracking_id):
        # zzz_print("    %-28s: tracking_id = %s" % ("mcartInstance_userOrderHistory_byTrackingId", tracking_id))
        owner_uniqid = muniqueid_get_users_uniquid(request)
        qs = mcart.objects \
            .filter(owner_uniqid=owner_uniqid) \
            .filter(purchased=True) \
            .filter(tracking_id=tracking_id)
        # zzz_print("    %-28s: %s" % ("qs.count()", qs.count()))
        return qs

    # --------------------------------------------------------------------------
    def mcartInstance_userOrderHistory_all(self, request):
        # zzz_print("    %-28s: tracking_id = %s" % ("mcartInstance_userOrderHistory_all", ""))
        owner_uniqid = muniqueid_get_users_uniquid(request)
        qs = mcart.objects \
            .filter(owner_uniqid=owner_uniqid) \
            .filter(purchased=True)
        # zzz_print("    %-28s: %s" % ("qs.count()", qs.count()))
        return qs

# ******************************************************************************
class mcart(models.Model):
    objects                 = mcart_instancemanager()
    owner_uniqid            = models.CharField      (max_length=100)
    muser                   = models.ForeignKey     (settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    title                   = models.CharField      (max_length=500, default="mcart title value Not Set")
    sku                     = models.CharField      (max_length=6)
    removed                 = models.BooleanField   (default=False)
    purchased               = models.BooleanField   (default=False)
    resume_required         = models.BooleanField   (default=False)
    processing_status       = models.CharField      (max_length=20, choices=const_inventory.PURCHASE_STATUS, default='pending')
    mcompleted_purchase     = models.ForeignKey     ('inventory.mcompleted_purchase', blank=True, null=True, on_delete=models.CASCADE)
    mcompleted_refund       = models.ForeignKey     ('inventory.mcompleted_refund', blank=True, null=True, on_delete=models.CASCADE)
    tracking_id             = models.CharField      (max_length=50, blank=True, null=True)
    model_name              = models.CharField      (max_length=50)
    item_id                 = models.IntegerField   (default=0)
    base_price              = models.DecimalField   (default=0, decimal_places=2, max_digits=1000, help_text="this is the sale price at the time.")
    coupon_subtract         = models.DecimalField   (default=0, decimal_places=2, max_digits=1000, help_text="this is the amount subtracted from base price due to coupons.")
    final_price             = models.DecimalField   (default=0, decimal_places=2, max_digits=1000, help_text="this is the final price after discounts.")
    tax_price               = models.DecimalField   (default=0, decimal_places=2, max_digits=1000, help_text="this is the tax that will be calculated on this mcart item.")
    quantity                = models.IntegerField   (default=0)
    created                 = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated                 = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    # --------------------------------------------------------------------------
    def __str__(self):
        # return_string  = "ID ("   + str(self.id) + ") "
        # return_string += "owner_uniqid ("   + self.owner_uniqid + ") "
        # return_string += "muser ("   + str(self.muser) + ") "
        # return_string += "MODEL_NAME (" + self.model_name + ") "
        # return_string += "TITLE: "   + self.title
        # return format(return_string)
        return "{}".format(self.tracking_id)

    # --------------------------------------------------------------------------
    def save(self, *args, **kwargs):
        self.calculate_tax_price_per_item()
        self.update_final_price()
        super().save(*args, **kwargs)

    # --------------------------------------------------------------------------
    def calculate_tax_price_per_item(self):
        tax_rate = 6
        self.tax_price = self.final_price * decimal.Decimal(tax_rate/100)
        # return self.tax_price
        # self.save()

    # --------------------------------------------------------------------------
    def set_processing_status_cancelled(self):
        self.processing_status = "cancelled"
        self.save()
        zzz_print("    %-28s: %s" % ("set_processing_status_cancelled", self.__str__()))

    # --------------------------------------------------------------------------
    def set_processing_status_delivered(self):
        self.processing_status = "delivered"
        self.save()
        zzz_print("    %-28s: %s" % ("set_processing_status_delivered", self.__str__()))

    # --------------------------------------------------------------------------
    def set_processing_status_error(self):
        self.processing_status = "error"
        self.save()
        zzz_print("    %-28s: %s" % ("set_processing_status_error", self.__str__()))

    # --------------------------------------------------------------------------
    def set_removed(self):
        self.removed = True
        self.save()
        zzz_print("    %-28s: %s" % ("set_removed", self.__str__()))

    # --------------------------------------------------------------------------
    def clear_removed(self):
        if self.removed:
            self.removed = False
            self.save()
            zzz_print("    %-28s: %s" % ("clear_removed", self.__str__()))

    # --------------------------------------------------------------------------
    def handleCurrentServiceOptionIdList(self, service_option_id_list, serviceoption_dynamic_django_model):
        # zzz_print("    %-28s: %s" % ("handleCurrentServiceOptionIdList", self.__str__()))

        # delete all mcart_serviceoptions that currently refer to this mcart instance
        deleteTuple = mcart_serviceoptions.objects.filter(mcart=self).delete()
        # zzz_print("    %-28s: %s" % ("serviceoptions OLD DELETED", deleteTuple[0]))

        # add service options found in service_option_id_list
        for service_option_id in service_option_id_list:
            # zzz_print("    %-28s: %s" % ("service_option_id", service_option_id))
            service_option_instance = serviceoption_dynamic_django_model.objects.get(id=service_option_id)
            mcart_serviceoptions.objects.mcart_serviceoptions_add_or_update(
                mcart               = self,
                name                = service_option_instance.name,
                price               = service_option_instance.price,
                serviceoption_id    = service_option_id,
                sku                 = service_option_instance.sku,
            )

    # --------------------------------------------------------------------------
    def handleCurrentDeliveryOptionIdList(self, delivery_option_id_list, deliveryoption_dynamic_django_model):
        # zzz_print("    %-28s: %s" % ("handleCurrentDeliveryOptionIdList", self.__str__()))

        if len(delivery_option_id_list) != 1:
            zzz_print("    %-28s: %s" % ("ERROR: len(delivery_option_id_list)", len(delivery_option_id_list)))

        # delete all mcart_deliveryoptions that currently refer to this mcart instance
        deleteTuple = mcart_deliveryoptions.objects.filter(mcart=self).delete()
        # zzz_print("    %-28s: %s" % ("deliveryoptions OLD DELETED", deleteTuple[0]))

        # add delivery options found in delivery_option_id_list
        for delivery_option_id in delivery_option_id_list:
            # zzz_print("    %-28s: %s" % ("delivery_option_id", delivery_option_id))
            delivery_option_instance = deliveryoption_dynamic_django_model.objects.get(id=delivery_option_id)
            mcart_deliveryoptions.objects.mcart_deliveryoptions_add_or_update(
                mcart                           = self,
                name                            = delivery_option_instance.name,
                price                           = delivery_option_instance.price,
                deliveryoption_id               = delivery_option_id,
                hours_to_cancel_after_payment   = delivery_option_instance.hours_to_cancel_after_payment,
                hours_to_deliver_after_payment  = delivery_option_instance.hours_to_deliver_after_payment,
                sku                             = delivery_option_instance.sku,
            )

    # --------------------------------------------------------------------------
    def get_user_visible_product_line(self):
        if self.model_name in const_inventory.MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_WORK_IN_CART_SYSTEM:
            return const_inventory.MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_WORK_IN_CART_SYSTEM[self.model_name]
        else:
            return "ERROR " + self.model_name + " NOT FOUND IN MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_WORK_IN_CART_SYSTEM"

    # --------------------------------------------------------------------------
    def grace_left_in_seconds(self):
        # zzz_print("    %-28s: %s" % ("calculate_grace_period", ""))
        now = timezone.now()  # using django timezone

        TD_since_purchase       = now - self.mcompleted_purchase.created
        TD_cancel_grace_hours   = timedelta(hours=self.mcart_deliveryoptions.hours_to_cancel_after_payment)
        TD_grace_left           = TD_cancel_grace_hours - TD_since_purchase
        if TD_grace_left < timedelta(hours=0):
            TD_grace_left = timedelta(hours=0)
            # zzz_print("    %-28s: %s" % ("TD_grace_left NEGATIVE", TD_grace_left))

        td_grace_left_in_seconds = int(TD_grace_left.total_seconds())
        # zzz_print("    %-28s: %s" % ("td_grace_left_in_seconds", td_grace_left_in_seconds))
        return td_grace_left_in_seconds

    # --------------------------------------------------------------------------
    def grace_period_ends(self):
        # zzz_print("    %-28s: %s" % ("grace_period_ends", ""))
        dt_grace_period_ends     = self.mcompleted_purchase.created + timedelta(hours=self.mcart_deliveryoptions.hours_to_cancel_after_payment)
        # zzz_print("    %-28s: %s" % ("dt_grace_period_ends", dt_grace_period_ends))
        return dt_grace_period_ends

    # --------------------------------------------------------------------------
    def delivery_time_ends(self):
        # zzz_print("    %-28s: %s" % ("delivery_time_ends", ""))
        dt_delivery_time_ends     = self.mcompleted_purchase.created + timedelta(hours=self.mcart_deliveryoptions.hours_to_deliver_after_payment)
        # zzz_print("    %-28s: %s" % ("dt_delivery_time_ends", dt_delivery_time_ends))
        return dt_delivery_time_ends

    # --------------------------------------------------------------------------
    def set_purchased(self, request, imcompleted_purchase):
        zzz_print("    %-28s: %s" % ("set_purchased", "----------------------------"))
        zzz_print("    %-28s: %s" % ("set_purchased", imcompleted_purchase))
        self.purchased = True
        self.mcompleted_purchase = imcompleted_purchase

        # v1: Old implementation which doesn't provide fixed length
        # t_body = str(imcompleted_purchase.id) + str(self.id)

        # v2: New implemenation which does provide fixed length
        # t_head = str(random.randint(100,999))
        # t_body = '{0:05d}'.format(imcompleted_purchase.id)
        # t_tail = str(random.randint(100000,999999))

        # v3: added mmyy in the first 4digit for better search performance
        t_head = str(datetime.datetime.today().year)[2:4] + str((datetime.date.today()).strftime('%m'))
        t_body = str(random.randint(10000,99999))
        t_tail = str(random.randint(10000,99999))


        # v4: applied model_name_id = [111, 222, 333, 444, 555, 666, 777]
        # to be implemented product mapping conecpt
        # t_head = str(random.randint(100,999))
        # t_head = str(datetime.datetime.today().year)[2:4] + str((datetime.date.today()).strftime('%m'))
        # t_body = str(random.randint(100000,999999))
        # t_tail = str(random.randint(100000,999999))


        self.tracking_id = t_head + '-' + t_body + '-' + t_tail
        zzz_print("    %-28s: %s" % ("self.tracking_id", self.tracking_id))
        self.save()

        # zzz_print("    %-28s: %s" % ("set_purchased", "dynamic model specific purchased processing"))
        # zzz_print("    %-28s: %s" % ("self.model_name", self.model_name))
        # zzz_print("    %-28s: %s" % ("self.item_id", self.item_id))

        # If coupon associated with this mcart purchased item set coupons usedinpurchase True
        try:
            if self.mcart_coupons:
                self.mcart_coupons.mcoupon_given.usedinpurchase = True
                self.mcart_coupons.mcoupon_given.save()
                zzz_print("    %-28s: %s" % ("mcoupon_given usedinpurchase SET True", self.mcart_coupons.mcoupon_given))
        except ObjectDoesNotExist:
            pass

        product_dynamic_django_model = apps.get_model("resumeweb", self.model_name)
        product_instance = product_dynamic_django_model.objects.get(id=self.item_id)
        # zzz_print("    %-28s: %s" % ("product_instance", product_instance))

        # call product_instance.post_purchase_processing() method in a non blocking thread
        thread = Thread(target = product_instance.post_purchase_processing, args = (request, imcompleted_purchase,))
        thread.start()

        zzz_print("    %-28s: %s" % ("set_purchased", "----------------------------"))

    # --------------------------------------------------------------------------
    def update_final_price(self):
        zzz_print("    %-28s: %s" % ("update_final_price", "----------------------------"))
        zzz_print("    %-28s: %s" % ("self.base_price", self.base_price))

        self.coupon_subtract = Decimal(0)
        self.final_price     = self.base_price
        try:
            if self.mcart_coupons:
                discount_percent_decimal    = Decimal(self.mcart_coupons.mcoupon_given.mcoupon.discount_percent / 100)
                self.coupon_subtract        = Decimal(self.base_price) * discount_percent_decimal
                self.final_price            = Decimal(self.base_price - self.coupon_subtract)

                zzz_print("    %-28s: %s" % ("discount_percent_decimal", discount_percent_decimal))
        except ObjectDoesNotExist:
            pass

        zzz_print("    %-28s: %s" % ("self.coupon_subtract", self.coupon_subtract))
        zzz_print("    %-28s: %s" % ("self.final_price", self.final_price))
        zzz_print("    %-28s: %s" % ("update_final_price", "----------------------------"))













