from zzz_lib.zzz_log import zzz_print
from django.contrib import admin
from django import forms

from inventory.models.adhoc.adhoc_req import (
    AdhocRequestModel,
)


## adhoc 
## ********************************************
@admin.register(AdhocRequestModel)
class AdminAdhocRequests(admin.ModelAdmin):
    list_display = (
        "id",
        "f_name",
        "l_name",
        "email",
        "created"
    )

