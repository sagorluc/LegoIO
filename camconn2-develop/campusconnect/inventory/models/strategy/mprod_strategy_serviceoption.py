#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django.db import models
from inventory.models.mbase_sku import mbase_sku

# ******************************************************************************
class mprod_strategy_serviceoption(mbase_sku):
    # Note: field sku defined in parent classes
    name        = models.CharField(max_length=2000)
    listprice   = models.DecimalField(default=0.99, decimal_places=2, max_digits=1000,)
    price       = models.DecimalField(default=0.99, decimal_places=2, max_digits=1000)
    description = models.CharField(max_length=2000, blank=True, null=True)
    products    = models.ForeignKey(to='inventory.mprod_strategy', on_delete=models.CASCADE)

    # Following fields ARE NOT fields that should be saved/used/stored in Database
    ndb_checked = False
    class_threeletterprefix = "prg"

    class Meta:
        verbose_name_plural = "09_Strategy_ServOption_Serv_List"

    def __str__(self):
        return "{}{}".format(self.sku, self.name)

    # # --------------------------------------------------------------------------
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

