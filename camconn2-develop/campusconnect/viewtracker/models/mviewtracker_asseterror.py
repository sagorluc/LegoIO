#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .mbase_viewtracker import mbase_viewtracker
from django.db import models

# ******************************************************************************
class mviewtracker_asseterror(mbase_viewtracker):
    total_count     = models.IntegerField   (default=1)

    # --------------------------------------------------------------------------
    def __str__(self):
        return f"{self.url}, {self.visit_time}"
        