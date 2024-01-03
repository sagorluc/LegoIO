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


# ******************************************************************************
class invitefriends_instancemanager(models.Manager):

    def add_invitefriends(self, request, guest_first_name, guest_last_name, guest_email_address, friend_first_name, friend_email_address, consent):
        invitefriends_instance = self.create(
            guest_first_name      = guest_first_name,
            guest_last_name       = guest_last_name,
            guest_email_address   = guest_email_address,

            friend_first_name      = friend_first_name,
            friend_email_address   = friend_email_address,

            consent = consent

        )

        # if request.user.is_authenticated:
        #     zzz_print("    %-28s: %s" % ("*** request.user.is_authenticated", "TRUE"))
        #     mfeedback_instance.muser = request.user
        invitefriends_instance.save()

        zzz_print("    %-28s: %s" % ("add_invitefriends", invitefriends_instance.__str__()))
        return invitefriends_instance



# ******************************************************************************
class InviteFriendsModel(models.Model):
    objects               = invitefriends_instancemanager()
    guest_first_name      = models.CharField      (max_length=100, blank=False, null=False)
    guest_last_name       = models.CharField      (max_length=100, blank=False, null=False)
    guest_email_address   = models.CharField      (max_length=100, blank=False, null=False)
    
    friend_first_name      = models.CharField      (max_length=100, blank=False, null=False)
    friend_email_address   = models.CharField      (max_length=100, blank=False, null=False)

    consent         = models.BooleanField   (default=False)
    created         = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated         = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")


    def __str__(self):
        return_string = "friend_email_address>>{}".format(self.friend_email_address)
        return format(return_string)


    class Meta:
        verbose_name_plural = "Invite Friend List"

