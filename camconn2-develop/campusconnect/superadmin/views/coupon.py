from zzz_lib.zzz_log import zzz_print
from django.contrib import admin

from guestactions.models import mfeedback
from inventory.models import mcoupon, mcoupon_given

# ******************************************************************************
@admin.register(mcoupon)
class admin_mcoupon(admin.ModelAdmin):
    list_display = (
        "product_liked",
        "discount_percent",
        "hours_to_expire",
        "active",
    )

@admin.register(mcoupon_given)
class admin_mcoupon_given(admin.ModelAdmin):
    list_display = (
        "random_string_32",
        "mcoupon",
        

    )

@admin.register(mfeedback)
class admin_mfeedback(admin.ModelAdmin):
    list_display = (
        "id",
        "email_address",
        "created",
    )

