#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# ******************************************************************************
class mcart_coupons_instancemanager(models.Manager):

    def mcart_coupons_add_or_update(self, mcart, mcoupon_given):
        add_or_update_mode = "EXISTS"
        try:
            instance = mcart_coupons.objects.get(mcart=mcart, mcoupon_given=mcoupon_given)
        except ObjectDoesNotExist:
            add_or_update_mode = "ADDED"
            instance = self.create(mcart=mcart, mcoupon_given=mcoupon_given)
        zzz_print("    %-28s: %s, %s" % ("mcart_coupons", add_or_update_mode, instance.__str__()))


    def mcart_coupons_delete_any_existing_for_cart_items(self, request):
        from .mcart import mcart
        mcart_qs = mcart.objects.mcartQS_usersItemsInCart(request)
        # zzz_print("    %-28s: %s" % ("mcart_qs.count()", mcart_qs.count()))

        for imcart in mcart_qs:
            try:
                imcart_coupons = imcart.mcart_coupons
                imcart_coupons.delete()
                imcart.refresh_from_db() # To refresh instance because we just deleted a one to one relationship
                imcart.save()  # trigger update_final_price
            except ObjectDoesNotExist:
                pass

# ******************************************************************************
class mcart_coupons(models.Model):
    objects                         = mcart_coupons_instancemanager()
    mcart                           = models.OneToOneField  ('inventory.mcart', on_delete=models.CASCADE)
    mcoupon_given                   = models.OneToOneField  ('general.mcoupon_given', on_delete=models.CASCADE)
    created                         = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated                         = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")
 

    def __str__(self):
        return_string  = "CO: mcart ("   + self.mcart.__str__() + ") "
        return_string += self.mcoupon_given.__str__()
        return format(return_string)



    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
