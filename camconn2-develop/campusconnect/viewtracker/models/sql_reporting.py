#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from uuid import uuid4
# from base64 import b64encode, b64decode
# from dirtyfields import DirtyFieldsMixin

# ******************************************************************************
class SQLReporting(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    query = models.TextField()
