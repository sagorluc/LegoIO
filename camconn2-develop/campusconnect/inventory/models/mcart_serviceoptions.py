#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
#from .mbase_sku import mbase_sku

# ******************************************************************************
class mcart_serviceoptions_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def mcart_serviceoptions_add_or_update(self, mcart, name, price, serviceoption_id, sku):
        add_or_update_mode = "EXISTS"
        try:
            instance = mcart_serviceoptions.objects.get(mcart=mcart, name=name, price=price, serviceoption_id=serviceoption_id, sku=sku)
        except ObjectDoesNotExist:
            add_or_update_mode = "ADDED "
            instance = self.create(mcart=mcart, name=name, price=price, serviceoption_id=serviceoption_id, sku=sku)
        zzz_print("    %-28s: %s, %s" % ("mcart_serviceoptions", add_or_update_mode, instance.__str__()))

# ******************************************************************************
class mcart_serviceoptions(models.Model):
    objects                 = mcart_serviceoptions_instancemanager()
    mcart                   = models.ForeignKey     ('inventory.mcart', on_delete=models.CASCADE)
    name                    = models.CharField      (max_length=500, default="Not Set")
    sku                     = models.CharField      (max_length=6)
    price                   = models.DecimalField   (default=0, decimal_places=2, max_digits=1000, help_text="price")
    serviceoption_id        = models.IntegerField   (default=0)
    created                 = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated                 = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = "SO: mcart ("   + self.mcart.__str__() + ") "
        return_string += "name (" + self.name + ") "
        return format(return_string)

    # # --------------------------------------------------------------------------
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)


#admin.site.register(mcart_serviceoptions)
