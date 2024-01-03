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

from zzz_lib.zzz_log import zzz_print
from django.conf import settings
from django.db import models



product_choices = const_inventory.CATEGORYNAME_DISPLAYNAME_TUPLE_ALL_COUPONS
# product_active = [n[0] for n in mcoupon.objects.values_list('category')]
# list1 = []
# for gh in product_choices:
#     for bh in product_active:
#         if gh[0] == bh:
#             list1.append(gh)

# ******************************************************************************
class mfeedback_instancemanager(models.Manager):

    def add_mfeedback(self, request, first_name, last_name, email_address, product_liked, feedback):
        # owner_uniqid = muniqueid_get_users_uniquid(request)

        mfeedback_instance = self.create(
            first_name      = first_name,
            last_name       = last_name,
            email_address   = email_address,
            product_liked   = product_liked,
            feedback        = feedback,
        )

        # if request.user.is_authenticated:
        #     zzz_print("    %-28s: %s" % ("*** request.user.is_authenticated", "TRUE"))
        #     mfeedback_instance.muser = request.user
        mfeedback_instance.save()

        zzz_print("    %-28s: %s" % ("add_mfeedback", mfeedback_instance.__str__()))
        return mfeedback_instance



# ******************************************************************************
class mfeedback(models.Model):
    objects         = mfeedback_instancemanager()
    first_name      = models.CharField      (max_length=100, blank=False, null=False)
    last_name       = models.CharField      (max_length=100, blank=False, null=False)
    email_address   = models.CharField      (max_length=1000, blank=False, null=False)
    product_liked   = models.CharField      (max_length=24, choices=product_choices, default='mprod_exp180')
    feedback        = models.TextField      (blank=False, null=False)
    # owner_uniqid    = models.CharField      (max_length=100)
    # muser           = models.ForeignKey     (settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    created         = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated         = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string = "product_liked>>{},email_address>>{}".format(self.product_liked, self.email_address)
        return format(return_string)


    class Meta:
        verbose_name_plural = "Feedback"

