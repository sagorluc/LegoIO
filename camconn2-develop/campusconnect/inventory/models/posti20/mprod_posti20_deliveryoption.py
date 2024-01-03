#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_posti20 import mprod_posti20
from ..mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_posti20_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_posti20)
    class_threeletterprefix = "prg"

    class Meta:
        verbose_name_plural = "04-PostI20_DelivOption_List"

