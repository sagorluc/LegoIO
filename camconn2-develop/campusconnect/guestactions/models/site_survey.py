from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from base64 import b64encode, b64decode
from dirtyfields import DirtyFieldsMixin
import uuid
from django.db import models
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print

from django.db import models
from inventory import const_inventory


class SiteSurveyModel(models.Model):
    site_used               = models.CharField(max_length=100,blank=True,null=True)
    hmpg_design             = models.CharField(max_length=100,blank=True,null=True)
    userfriendly            = models.CharField(max_length=100,blank=True,null=True)
    promo_offers            = models.CharField(max_length=100,blank=True,null=True)
    service_lineup          = models.CharField(max_length=100,blank=True,null=True)
    overall_exp             = models.CharField(max_length=100,blank=True,null=True)
    recommend               = models.CharField(max_length=100,blank=True,null=True)
    message                 = models.CharField(max_length=100,blank=True,null=True)
    name                    = models.CharField(max_length=100,blank=True,null=True)
    email                   = models.EmailField(max_length=100,blank=True,null=True)
    created_at              = models.DateTimeField(auto_now_add=True,help_text="timestamp of creation site survey")

    def __repr__(self):     # same as __str__(self):
        return "{}".format(self.id)
