from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from uuid import uuid4
from base64 import b64encode, b64decode

from dirtyfields import DirtyFieldsMixin

# ******************************************************************************
class mprod_univcom_list(models.Model):
    levelname = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "07_Univcom_Cat_List"

    def __str__(self):
        return "{}".format(self.levelname)




















