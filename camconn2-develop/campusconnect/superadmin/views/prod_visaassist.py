from zzz_lib.zzz_log import zzz_print
from django.contrib import admin
from django import forms

# from inventory.models import (
#     mprod_prei20,
#     mprod_prei20_serviceoption,

# )


# from inventory.models.visaassist import (
#     mprod_visaassist,
#     mprod_visaassist_catlist,
#     mprod_visaassist_serviceoption,

# )

from inventory.models.visaassist.mprod_visaassist import mprod_visaassist
from inventory.models.visaassist.mprod_visaassist_catlist import mprod_visaassist_catlist
from inventory.models.visaassist.mprod_visaassist_serviceoption import mprod_visaassist_serviceoption
from inventory.models.visaassist.mprod_visaassist_deliveryoption import mprod_visaassist_deliveryoption


# from resumeweb.models import (
#     mprod_proflevel,
#     mprod_proflevel_list,
#     mprod_proflevel_serviceoption,
# )


# from resumeweb.models import (
#     mprod_proglang,
#     mprod_proglang_list,
#     mprod_proglang_serviceoption,

# )


# from resumeweb.models import (
#     mprod_rolebased,
#     mprod_rolebased_list,
#     mprod_rolebased_serviceoption,

# )



# from resumeweb.models import (
#     mprod_strategy,
#     mprod_strategy_taglist,
#     mprod_strategy_serviceoption,    

# )



# from resumeweb.models import (
#     mprod_visabased,
#     mprod_visabased_list,
#     mprod_visabased_serviceoption,


# )

from inventory.models import (

    mprod_prei20_deliveryoption,
    # mprod_visaassist_deliveryoption,
    # mprod_proflevel_deliveryoption,
    # mprod_prei20_deliveryoption,
    # mprod_rolebased_deliveryoption,
    # mprod_strategy_deliveryoption,
    # mprod_visabased_deliveryoption,
)







# mprod_visaassist_catlist
########################################################################################
@admin.register(mprod_visaassist_catlist)
class admin_mprod_visaassist_catlist(admin.ModelAdmin):
    list_display = (
        "id",
        "catname",
    )




# # mprod_visaassist / Dialogue
# ########################################################################################
@admin.register(mprod_visaassist)
class AdminVisaassistServList(admin.ModelAdmin):
    list_display = (
        "sku",
        "title",
        "category",
        "listprice",
        "saleprice"
    )
    # Fields to exclude from add/edit Admin Form
    exclude = ('sku',)

    fieldsets = (
        ('General', {
            'fields': ('title', 
                'description',
                "category",
                "trending",
                "homepage_showup",
                )
        }),
        ('Pricing', {
            'fields': ('listprice', 'saleprice')
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(AdminVisaassistServList, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'title':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield



# ## service options
# ## *****************************************************************************************
@admin.register(mprod_visaassist_serviceoption)
class AdminVisaassistServiceoption(admin.ModelAdmin):
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
        formfield = super(AdminVisaassistServiceoption, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'name':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield





# ## delivery options
# ## *****************************************************************************************
@admin.register(mprod_visaassist_deliveryoption)
class admin_mprod_visaassist_deliveryoption(admin.ModelAdmin):
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


