#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print

from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string

from inventory.models.muniqueid import muniqueid_get_users_uniquid

# from django.urls import reverse

# ******************************************************************************
class mcoupon_given_instancemanager(models.Manager):
    def mcoupon_given_add(self, request, mcoupon):
        # owner_uniqid        = muniqueid_get_users_uniquid(request)
        random_string_32    = (get_random_string(length=32)[2:10]).upper()
        zzz_print("    %-28s: %s" % ("mcoupon_given_add", ""))
        # zzz_print("    %-28s: %s" % ("owner_uniqid", owner_uniqid))
        zzz_print("    %-28s: %s" % ("random_string_32", random_string_32))

        mcoupon_given_instance = self.create(mcoupon=mcoupon, random_string_32=random_string_32)
        # if request.user.is_authenticated:
        #     # zzz_print("    %-28s: %s" % ("*** request.user.is_authenticated", "TRUE"))
        #     mcoupon_given_instance.muser = request.user
        mcoupon_given_instance.save()
        return mcoupon_given_instance

    def get_valid_mcoupon_given_for_user(self, request, string_32):
        owner_uniqid = muniqueid_get_users_uniquid(request)
        zzz_print("    %-28s: %s" % ("get_valid_mcoupon_given_for_user", ""))
        zzz_print("    %-28s: %s" % ("owner_uniqid", owner_uniqid))
        zzz_print("    %-28s: %s" % ("string_32", string_32))

        try:
            imcoupon_given = mcoupon_given.objects.get(owner_uniqid=owner_uniqid, random_string_32=string_32)
            zzz_print("    %-28s: %s" % ("get_valid_mcoupon_given_for_user", "True by owner_uniqid"))
            return imcoupon_given
        except ObjectDoesNotExist:
            if request.user.is_authenticated:
                try:
                    imcoupon_given = mcoupon_given.objects.get(muser=request.user, random_string_32=string_32)
                    zzz_print("    %-28s: %s" % ("get_valid_mcoupon_given_for_user", "True by muser"))
                    return imcoupon_given
                except ObjectDoesNotExist:
                    zzz_print("    %-28s: %s" % ("get_valid_mcoupon_given_for_user", "False by muser"))
                    return None
            else:
                zzz_print("    %-28s: %s" % ("get_valid_mcoupon_given_for_user", "False for guest muser"))
                return None

    def check_coupon_exists(self, request, string_32):
        try:
            imcoupon_given = mcoupon_given.objects.get(random_string_32=string_32)
            zzz_print("    %-28s: %s" % ("check_coupon_validity", "coupon is valid"))
            return imcoupon_given

        except ObjectDoesNotExist:
            zzz_print("    %-28s: %s" % ("check_coupon_validity", "coupon is invalid"))
            return None

    # # --------------------------------------------------------------------------
    # def mcouponQS_validCouponsForProductsInCart(self, request, modelname_list):
    #     # zzz_print("    %-28s: %s" % ("mcouponQS_validCouponsForProductsInCart", ""))
    #     # zzz_print("    %-28s: %s" % ("modelname_list", modelname_list))
    #     owner_uniqid = muniqueid_get_users_uniquid(request)
    #
    #     mcoupon_given.objects.mcoupon_expire_coupons(owner_uniqid)
    #
    #     # TODO: IF ALLOWING ONLY ONE COUPON AT ALL FOR SHOPPING CART THEN .....
    #     # TODO: IF ALLOWING ONLY ONE COUPON PER PRODUCT LINE FOR SHOPPING CART THEN ....
    #     # TODO: ELSE ALLOWING ALL COUPONS .....
    #
    #     qs = mcoupon_given.objects \
    #         .filter(owner_uniqid=owner_uniqid) \
    #         .filter(expired=False) \
    #         .filter(usedinpurchase=False) \
    #         .filter(mcoupon__category__in=modelname_list) \
    #         .order_by('mcoupon__category', '-mcoupon__discount_percent', 'created')
    #     # zzz_print("    %-28s: %s" % ("qs.count()", qs.count()))
    #
    #
    #     # Hack allow only one coupon per category
    #     category_name_list = []
    #     qs_return_list = []
    #     for instance in qs:
    #         if instance.mcoupon.category not in category_name_list:
    #             category_name_list.append(instance.mcoupon.category)
    #             qs_return_list.append(instance)
    #     # zzz_print("    %-28s: %s" % ("len(qs_return_list)", len(qs_return_list)))
    #
    #     return qs_return_list





# ******************************************************************************
class mcoupon_given(models.Model):
    objects             = mcoupon_given_instancemanager()
    mcoupon             = models.ForeignKey     ('guestactions.mcoupon', on_delete=models.CASCADE, blank=False, null=False)
    random_string_32    = models.CharField      (max_length=33, blank=False, null=False)
    # owner_uniqid        = models.CharField      (max_length=100, blank=False, null=False)
    # muser               = models.ForeignKey     (settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    expired             = models.BooleanField   (default=False)
    usedinpurchase      = models.BooleanField   (default=False)
    created             = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = self.random_string_32
        return format(return_string)

    # --------------------------------------------------------------------------
    def is_coupon_expired(self):
        # zzz_print("    %-28s: %s" % ("is_coupon_expired", ""))
        now                 = timezone.now()  # using django timezone
        TD_since_created    = now - self.created
        TD_valid_until      = timedelta(hours=self.mcoupon.hours_to_expire)
        TD_valid_left       = TD_valid_until - TD_since_created
        if TD_valid_left < timedelta(hours=0):
            zzz_print("    %-28s: %s" % ("EXPIRING self", self))
            self.expired = True
            self.save()
        return self.expired

    class Meta:
        verbose_name_plural = "CouponCode List"

