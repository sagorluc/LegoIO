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


def guest_resume_location(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'resume-guest/{}'.format(filename)


class GuestResumeModel(models.Model):
    file1 = models.FileField(upload_to=guest_resume_location)
    email = models.EmailField(max_length=200, default=None)
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Resume Files by Guest'
        verbose_name_plural = 'Resume Files by Guest'

    def __str__(self):
        return self.email

