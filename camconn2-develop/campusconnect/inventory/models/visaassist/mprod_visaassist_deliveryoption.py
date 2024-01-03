#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from inventory.models.mbase_deliveryoption import mbase_deliveryoption
#from inventory.models.visaassist.mprod_visaassist import mprod_visaassist
from inventory.models.visaassist.mprod_visaassist import mprod_visaassist

# ******************************************************************************
class mprod_visaassist_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_visaassist)
    class_threeletterprefix = "dd4"

    class Meta:
        verbose_name_plural = "03_Visaassist_DelivOption_List"











