#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django import forms
from django.db import models
from inventory import const_inventory

# ******************************************************************************
class mcompleted_refund_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def add_mcompleted_refund(self, paypalrefund_id, amount_currencycode, amount_value, reason, explanation):
        instance = self.create(
            paypalrefund_id         = paypalrefund_id,
            amount_currencycode     = amount_currencycode,
            amount_value            = amount_value,
            reason                  = reason,
            explanation             = explanation
        )
        zzz_print("    %-28s: %s" % ("add_mcompleted_refund", instance.__str__()))
        return instance

# ******************************************************************************
class mcompleted_refund(models.Model):
    objects                 = mcompleted_refund_instancemanager()
    paypalrefund_id         = models.CharField      (max_length=100) # ,  default=""
    amount_currencycode     = models.CharField      (max_length=5)
    amount_value            = models.DecimalField   (max_digits=10, decimal_places=2)
    reason                  = models.CharField      (max_length=5, choices=const_inventory.CANCELLED_ORDER_REASON_CHOICES, default='r01')
    explanation             = models.TextField      ()
    created                 = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated                 = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = "paypalrefund_id ("   + self.paypalrefund_id + ") "
        return_string += "amount_currencycode ("   + self.amount_currencycode + ") "
        return_string += "amount_value ("   + str(self.amount_value) + ") "
        return format(return_string)

# ******************************************************************************
class form_mcompleted_refund(forms.ModelForm):
    class Meta:
        model = mcompleted_refund
        fields = ('reason', 'explanation')
