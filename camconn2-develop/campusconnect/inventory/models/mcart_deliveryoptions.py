#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


# ******************************************************************************
class mcart_deliveryoptions_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def mcart_deliveryoptions_add_or_update(self, mcart, name, price, deliveryoption_id, hours_to_cancel_after_payment, hours_to_deliver_after_payment, sku):
        add_or_update_mode = "EXISTS"
        try:
            instance = mcart_deliveryoptions.objects.get(mcart=mcart, name=name, price=price, deliveryoption_id=deliveryoption_id, hours_to_cancel_after_payment=hours_to_cancel_after_payment, hours_to_deliver_after_payment=hours_to_deliver_after_payment, sku=sku)
        except ObjectDoesNotExist:
            add_or_update_mode = "ADDED"
            instance = self.create(mcart=mcart, name=name, price=price, deliveryoption_id=deliveryoption_id, hours_to_cancel_after_payment=hours_to_cancel_after_payment, hours_to_deliver_after_payment=hours_to_deliver_after_payment, sku=sku)
        zzz_print("    %-28s: %s, %s" % ("mcart_deliveryoptions", add_or_update_mode, instance.__str__()))

# ******************************************************************************
class mcart_deliveryoptions(models.Model):
    objects                         = mcart_deliveryoptions_instancemanager()
    mcart                           = models.OneToOneField  ('inventory.mcart', on_delete=models.CASCADE)
    name                            = models.CharField      (max_length=100, default="Not Set")
    sku                             = models.CharField      (max_length=6)
    price                           = models.DecimalField   (default=0, decimal_places=2, max_digits=1000, help_text="price")
    hours_to_cancel_after_payment   = models.IntegerField   (default=168)
    hours_to_deliver_after_payment  = models.IntegerField   (default=336)
    deliveryoption_id               = models.IntegerField   (default=0)
    created                         = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated                         = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    # # --------------------------------------------------------------------------
    # def __str__(self):
    #     return_string = "id = " + str(self.id)
    #     return_string += ", name = " + self.name
    #     return_string += ", hours to cancel = " + str(self.hours_to_cancel_after_payment)
    #     return_string += ", hours to deliver = " + str(self.hours_to_deliver_after_payment)
    #     return format(return_string)

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = "DO: mcart ("   + self.mcart.__str__() + ") "
        return_string += "name (" + self.name + ") "
        return_string += ", hours to cancel = " + str(self.hours_to_cancel_after_payment)
        return_string += ", hours to deliver = " + str(self.hours_to_deliver_after_payment)
        return format(return_string)


    # # --------------------------------------------------------------------------
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)



    