#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_prei20 import mprod_prei20
from inventory.models.mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_prei20_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_prei20)
    class_threeletterprefix = "prg"

    class Meta:
        verbose_name_plural = "05_Prei20_DelivOption_List"










