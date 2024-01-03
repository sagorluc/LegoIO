#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# from datetime import timedelta
# import random
# from threading import Thread
# import urllib.parse
# from django.apps import apps
# from django.utils import timezone
# from .. import const_resumeweb

# ******************************************************************************
def muniqueid_get_users_uniquid(request):
    owner_uniqid = muniqueid_FROM_SESSCOOK(request)

    if request.user.is_authenticated:
        imuniqueid = muniqueid.objects.get(muser=request.user)
        if owner_uniqid != imuniqueid.owner_uniqid:
            zzz_print("    %-28s: %s" % ("***************************", "***************************"))
            zzz_print("    %-28s: %s" % ("Authorized User", request.user))
            zzz_print("    %-28s: %s" % ("Sesscook uniqid", owner_uniqid))
            zzz_print("    %-28s: %s" % ("OVERWRITTEN BY muniqueid", imuniqueid.owner_uniqid))
            zzz_print("    %-28s: %s" % ("***************************", "***************************"))
            owner_uniqid = imuniqueid.owner_uniqid
    return owner_uniqid

# ******************************************************************************
def muniqueid_FROM_SESSCOOK(request):
    owner_uniqid = None
    found_mode = ""

    if 'mmh_uniqid_cookie' in request.COOKIES:
        owner_uniqid = request.COOKIES['mmh_uniqid_cookie']
        found_mode = "AAA: request.COOKIES[mmh_uniqid_cookie]"
    if owner_uniqid is None:
        if request.method == "POST":
            owner_uniqid = request.POST.get("mmh_guest_user_unique_id")
            found_mode = "BBB: request.POST.get(mmh_guest_user_unique_id)"
        elif request.method == "GET":
            owner_uniqid = request.GET.get("mmh_guest_user_unique_id")
            found_mode = "CCC: request.GET.get(mmh_guest_user_unique_id)"

    if owner_uniqid is None:    zzz_print("    %-28s: %s" % ("WARNING: owner_uniqid is None, found_mode = ", found_mode))
    else:                       zzz_print("    %-28s: %s" % ("SESSCOOKIES found_mode", found_mode))

    return owner_uniqid

# ******************************************************************************
class muniqueid_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def muniqueid_add(self, request):
        try:
            muniqueid_instance = muniqueid.objects.get(muser=request.user)

            # # MMH: Next three lines are for debug only.
            # #      Can comment them out and avoid one call to muniqueid_FROM_SESSCOOK()
            owner_uniqid = muniqueid_FROM_SESSCOOK(request)
            if muniqueid_instance.owner_uniqid != owner_uniqid: zzz_print("    %-28s: %s: %s != %s" % ("muniqueid_add", "WARNING muniqueid_instance.owner_uniqid != owner_uniqid", muniqueid_instance.owner_uniqid, owner_uniqid))
            else:                                               zzz_print("    %-28s: %s" % ("muniqueid_add", "and everything is fine"))
        except ObjectDoesNotExist:
            owner_uniqid = muniqueid_FROM_SESSCOOK(request)
            muniqueid_instance = self.create(muser=request.user, owner_uniqid=owner_uniqid)
            zzz_print("    %-28s: %s, %s" % ("muniqueid_add", "ADDED", muniqueid_instance.__str__()))

# ******************************************************************************
class muniqueid(models.Model):
    objects                 = muniqueid_instancemanager()
    owner_uniqid            = models.CharField      (max_length=100, blank=True, null=True)
    muser                   = models.ForeignKey     (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created                 = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated                 = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = "ID ("   + str(self.id) + ") "
        return_string += "owner_uniqid ("   + self.owner_uniqid + ") "
        return_string += "muser ("   + str(self.muser) + ") "
        return format(return_string)









