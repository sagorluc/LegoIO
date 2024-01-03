#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mbase_viewtracker import mbase_viewtracker
from django.conf import settings

# ******************************************************************************
class mviewtracker(mbase_viewtracker):
    owner_uniqid    = models.CharField(max_length=100, blank=True, null=True)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    exception       = models.TextField(blank=True, null=True)

    # --------------------------------------------------------------------------
    class Meta:
        #     # ordering = ("visit_time",)
        #     get_latest_by = 'visit_time'
        verbose_name_plural = "Browse History"

    # --------------------------------------------------------------------------
    def __str__(self):
        return f"{self.url}, {self.visit_time}"


