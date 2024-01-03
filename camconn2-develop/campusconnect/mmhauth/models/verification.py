# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from base64 import b64encode, b64decode

# ******************************************************************************
class mverificationcode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.UUIDField(default=uuid4, help_text="unique")
    verified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, help_text="timestamp of creation")
    updated = models.DateTimeField(auto_now=True, help_text="timestamp of last update")

    @property
    def hash_value(self):
        combination = f"{self.user.email}:{str(self.code)}"
        code = b64encode(bytes(combination, encoding="utf-8"))
        return code.decode("utf-8")

    @staticmethod
    def decode(cls, activation_code):
        combination = b64decode(activation_code)
        email, code = combination.decode("utf-8").split(":")
        return email, code


# ##############################
# # TODO
# # Create a model called 'RegUser' by extending base 'User' model from django
# # Whenever a user submits a request for signin or password reset,
# # first check if that email exists in this 'RegUser' table.
# # If no record found in 'RegUser' table, then send an error message saying
# # there is no account with this email address
# ##############################
