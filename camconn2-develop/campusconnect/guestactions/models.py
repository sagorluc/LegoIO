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
from . import const_resumeweb


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


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django.conf import settings
from django.db import models
from . import const_resumeweb


product_choices = const_resumeweb.CATEGORYNAME_DISPLAYNAME_TUPLE_ALL_COUPONS
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
    product_liked   = models.CharField      (max_length=24, choices=product_choices, default='mprod_prei20')
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
class InviteFriends(models.Model):
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



def guest_resume_location(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'resume-guest/{}'.format(filename)


class GuestResumeFiles(models.Model):
    file1 = models.FileField(upload_to=guest_resume_location)
    email = models.EmailField(max_length=200, default=None)
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Resume Files by Guest'
        verbose_name_plural = 'Resume Files by Guest'


    def __str__(self):
        return self.email

