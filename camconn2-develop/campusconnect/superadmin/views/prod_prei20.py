from zzz_lib.zzz_log import zzz_print
from django.contrib import admin
from django import forms

from inventory.models import (
    mprod_prei20,
    mprod_prei20_serviceoption,
    mprod_prei20_catlist,

    mprod_prei20_deliveryoption,


)





# Prei20
########################################################################################
@admin.register(mprod_prei20)
class AdminPrei20ServList(admin.ModelAdmin):
    # Fields to display in admin listing
    list_display = (
        "sku",
        "title",
        "listprice",
        "saleprice",
        "trending",
        "homepage_showup",
        "category",
        'golivestatus'
    )
    # Fields to exclude from add/edit Admin Form
    exclude = ('sku',)

    fieldsets = (
        ('General', {
            'fields': ('title', 
                'description',
                "trending",
                "homepage_showup",
                "category",
                'golivestatus'
                )
        }),
        ('Pricing', {
            'fields': ('listprice', 'saleprice')
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(AdminPrei20ServList, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'title':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield



@admin.register(mprod_prei20_catlist)
class AdminPrei20CatList(admin.ModelAdmin):
    list_display = (
        'id',
        
    )

## service options
## *****************************************************************************************
@admin.register(mprod_prei20_serviceoption)
class AdminPrei20Serviceoption(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "listprice",
        "price",
        'products'
    )
    # Fields to exclude from add/edit Admin Form
    exclude = ('sku',)


    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(AdminPrei20Serviceoption, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'name':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield





## delivery options
## *****************************************************************************************
@admin.register(mprod_prei20_deliveryoption)
class admin_mprod_prei20_deliveryoption(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "listprice",
        "price",
        "hours_to_cancel_after_payment",
        "hours_to_deliver_after_payment",
    )
    # Fields to exclude from add/edit Admin Form
    exclude = ('sku',)


    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(admin_mprod_prei20_deliveryoption, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'name':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


