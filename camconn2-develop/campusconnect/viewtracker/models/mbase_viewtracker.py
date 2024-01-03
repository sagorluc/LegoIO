#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from uuid import uuid4

# ******************************************************************************
class mbase_viewtracker(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    visit_time      = models.DateTimeField(auto_now_add=True, verbose_name="timestamp of page visit")
    url             = models.CharField(max_length=2000)
    status_code     = models.PositiveSmallIntegerField()
    method          = models.CharField(max_length=20)
    http_user_agent = models.CharField(max_length=2000, blank=True, null=True)
    http_referer    = models.CharField(max_length=2000, blank=True, null=True)
    query_string    = models.CharField(max_length=2000, blank=True, null=True)
    remote_addr     = models.CharField(max_length=200, blank=True, null=True)
    remote_host     = models.CharField(max_length=2000, blank=True, null=True)

    # --------------------------------------------------------------------------
    class Meta:
        abstract = True



