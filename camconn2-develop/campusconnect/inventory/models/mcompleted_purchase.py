#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django.db import models

# ******************************************************************************
class mcompleted_purchase_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def add_mcompleted_purchase(self, paypaltransaction_id, payer_id, capture_id, first_name, last_name, email_address):
        instance = self.create(
            paypaltransaction_id    = paypaltransaction_id,
            payer_id                = payer_id,
            capture_id              = capture_id,
            first_name              = first_name,
            last_name               = last_name,
            email_address           = email_address
        )
        zzz_print("    %-28s: %s" % ("add_mcompleted_purchase", instance.__str__()))
        return instance

# ******************************************************************************
class mcompleted_purchase(models.Model):
    objects                     = mcompleted_purchase_instancemanager()
    paypaltransaction_id        = models.CharField      (max_length=100,  default="")
    payer_id                    = models.CharField      (max_length=100,  default="")
    capture_id                  = models.CharField      (max_length=100,  default="")
    first_name                  = models.CharField      (max_length=100,  default="")
    last_name                   = models.CharField      (max_length=100,  default="")
    email_address               = models.CharField      (max_length=1000, default="")
    guest_login_email_address   = models.CharField      (max_length=1000, blank=True, null=True)
    created                     = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated                     = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = "paypaltransaction_id ("   + self.paypaltransaction_id + ") "
        return_string += "first_name ("   + self.first_name + ") "
        return_string += "last_name ("   + self.last_name + ") "
        return format(return_string)

