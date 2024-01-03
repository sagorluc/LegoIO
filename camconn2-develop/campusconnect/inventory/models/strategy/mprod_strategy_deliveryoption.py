#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_strategy import mprod_strategy
from inventory.models.mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_strategy_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_strategy)
    class_threeletterprefix = "dd8"

    class Meta:
        verbose_name_plural = "09_Strategy_DelivOption_List"



