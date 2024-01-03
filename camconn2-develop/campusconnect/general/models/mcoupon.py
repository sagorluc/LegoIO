#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print

from django.db import models
from inventory import const_inventory

# from datetime import timedelta
# from django.conf import settings
# from django.core.exceptions import ObjectDoesNotExist
# from django.urls import reverse
# from django.utils import timezone
# from django.utils.crypto import get_random_string

# from inventory.models.muniqueid import muniqueid_get_users_uniquid

# ******************************************************************************
class mcoupon(models.Model):
    product_liked       = models.CharField      (max_length=20, choices=const_inventory.CATEGORYNAME_DISPLAYNAME_TUPLE_ALL_COUPONS, blank=False, null=False, default='mprod_prei20')
    discount_percent    = models.IntegerField   (default=1, blank=False, null=False)
    hours_to_expire     = models.IntegerField   (default=336, blank=False, null=False)
    active              = models.BooleanField   (default=False)
    created             = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = str(self.discount_percent)
        return format(return_string)


    class Meta:
        verbose_name_plural = "Coupon Supported Product List"
