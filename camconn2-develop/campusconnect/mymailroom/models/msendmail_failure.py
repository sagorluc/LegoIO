#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django.db import models

# ******************************************************************************
class msendmail_failure_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def add_failure(self, msendmail, title, description, recipient_string):
        instance = self.create(msendmail=msendmail, title=title, description=description, recipient_string=recipient_string)
        return instance

# ******************************************************************************
class msendmail_failure(models.Model):
    objects             = msendmail_failure_instancemanager()
    msendmail           = models.ForeignKey     ('mymailroom.msendmail', on_delete=models.CASCADE)
    title               = models.CharField      (max_length=500)
    description         = models.TextField      (blank=False, null=False)
    recipient_string    = models.TextField      (blank=False, null=False)
    created             = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated             = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = self.title + ": " + self.description
        return format(return_string)
