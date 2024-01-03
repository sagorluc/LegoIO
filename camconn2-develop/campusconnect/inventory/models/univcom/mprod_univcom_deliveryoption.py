#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_univcom import mprod_univcom
from inventory.models.mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_univcom_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_univcom)
    class_threeletterprefix = "prf"

    class Meta:
        verbose_name_plural = "07_Univcom_DelivOption_List"











