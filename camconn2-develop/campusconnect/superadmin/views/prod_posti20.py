from zzz_lib.zzz_log import zzz_print
from django.contrib import admin
from django import forms


from inventory.models import (
    mprod_posti20,
    mprod_posti20_catlist,
    mprod_posti20_serviceoption,
    mprod_posti20_deliveryoption,
)



# PostI20 cat list
########################################################################################
@admin.register(mprod_posti20_catlist)
class PostI20CatListAdmin(admin.ModelAdmin):
    list_display = (
        "catname",
    )


# PostI20 serv list
########################################################################################
@admin.register(mprod_posti20)
class PostI20ServlistAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "title",
        "deliverables",
        "golivestatus",
        "category",
        "trending",
        "homepage_showup"
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
                )
        }),
        ('Pricing', {
            'fields': ('listprice', 'saleprice')
        }),
    )


    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PostI20ServlistAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'title':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield




## service options
## *****************************************************************************************
@admin.register(mprod_posti20_serviceoption)
class PostI20ServiceOptionAdmin(admin.ModelAdmin):
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
        formfield = super(PostI20ServiceOptionAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'name':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


# delivery options
## *****************************************************************************************
@admin.register(mprod_posti20_deliveryoption)
class PostI20DeliveryOptionAdmin(admin.ModelAdmin):
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


