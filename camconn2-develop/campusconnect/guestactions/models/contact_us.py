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


# general contact us page
class ContactUsModel(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    msg = models.TextField(max_length=2000)
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="timestamp of creation"
    )
    
    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f'{self.msg}'

