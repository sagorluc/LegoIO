from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

""" from shopcart.models import (
    mcart,
    mcompleted_purchase,
    
)
 """
from inventory.models.mcart import mcart
from inventory.models.mcompleted_purchase import mcompleted_purchase
from general.models.buyer_list import BuyerListGuest

# mcart
########################################
@admin.register(mcart)
class AdminCart(admin.ModelAdmin):
    list_display = (
        "tracking_id",
        "mcompleted_purchase",
        "created",
        "purchased",
        "final_price",
        
        "model_name",
        
    )


# mcompleted_purchase
########################################
@admin.register(mcompleted_purchase)
class AdminCart(admin.ModelAdmin):
    list_display = (
        "paypaltransaction_id",
        "created",
        "email_address",
        "guest_login_email_address"
        
    )


@admin.register(BuyerListGuest)
class AdminBuyerListGuest(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "reguser",
        "transaction_id"
    )
