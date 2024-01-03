from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from base64 import b64encode, b64decode
from dirtyfields import DirtyFieldsMixin

from inventory import const_inventory

# ******************************************************************************
class AdhocRequestModel(models.Model):
    # about the job description section
    target_JD_1 = models.CharField(
        max_length=5000, 
        null=True, 
        blank=True,
        help_text="Target Job Description"
    )
    target_JD_2 = models.CharField(
        max_length=5000, 
        null=True, 
        blank=True,
        help_text="Target Job Description"
    )

    # what customer needs
    ques_details = models.CharField(
        max_length=3000, 
        null=True, 
        blank=True
    )

    # customer feedback
    why_needed = models.CharField(
        max_length=100,
        choices=const_inventory.WHY_NEEDED,
        default='no'
    )

    # contact with submitter
    f_name = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )
    l_name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True
    )
    email = models.CharField(
        max_length=200, 
        null=True, 
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True, 
        help_text="timestamp of creation"
    )
    resume = models.FileField(
        default='null',
        upload_to='adhoc_resumes/%Y/%m/%d'
    )

    class Meta:
        verbose_name_plural = "Adhoc Requests"


    def __str__(self):
        return f'{self.f_name}'
