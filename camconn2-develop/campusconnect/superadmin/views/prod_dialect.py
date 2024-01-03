# from zzz_lib.zzz_log import zzz_print
# from django.contrib import admin
# from django import forms

# from inventory.models.posti20 import (
#     mprod_prei20,
#     mprod_prei20_serviceoption,

# )

from inventory.models.visaassist import (
    mprod_visaassist,
    mprod_visaassist_catlist,
    mprod_visaassist_serviceoption,

)

# from inventory.models.univcom import (
#     mprod_proflevel,
#     mprod_proflevel_list,
#     mprod_proflevel_serviceoption,
# )

# from inventory.models.prei20 import (
#     mprod_proglang,
#     mprod_proglang_serviceoption,

# )

# from inventory.models.prei20.mprod_proglang_list import mprod_proglang_list

# from inventory.models.strategy import (
#     mprod_strategy,
#     mprod_strategy_taglist,
#     mprod_strategy_serviceoption,    

# )

# from inventory.models.posti20 import mprod_exp180_deliveryoption
from inventory.models.visaassist import mprod_visaassist_deliveryoption
# from inventory.models.prei20 import mprod_prei20_deliveryoption
# from inventory.models.strategy import mprod_strategy_deliveryoption
# from inventory.models.univcom import mprod_proflevel_deliveryoption




# # Prog Lang cat list
# ########################################################################################
# @admin.register(mprod_proglang_list)
# class admin_mprod_proglang_catlist(admin.ModelAdmin):
#     list_display = (
#         "langname",
#     )




# # Prog Lang serv list
# ########################################################################################
# @admin.register(mprod_proglang)
# class AdminProglangServlist(admin.ModelAdmin):
#     list_display = (
#         "sku",
#         "title",
#         "deliverables",
#         "golivestatus",
#         "category",
#         "trending",
#         "homepage_showup"
#     )
#     # Fields to exclude from add/edit Admin Form
#     exclude = ('sku',)

#     fieldsets = (
#         ('General', {
#             'fields': ('title', 
#                 'description',
#                 "trending",
#                 "homepage_showup",
#                 "category",
#                 )
#         }),
#         ('Pricing', {
#             'fields': ('listprice', 'saleprice')
#         }),
#     )


#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super(AdminProglangServlist, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description' or db_field.name == 'title':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield




# ## service options
# ## *****************************************************************************************
# @admin.register(mprod_proglang_serviceoption)
# class AdminProglangServiceoption(admin.ModelAdmin):
#     list_display = (
#         "sku",
#         "name",
#         "listprice",
#         "price",
#         'products'
#     )
#     # Fields to exclude from add/edit Admin Form
#     exclude = ('sku',)


#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super(AdminProglangServiceoption, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description' or db_field.name == 'name':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield




# # delivery options
# ## *****************************************************************************************
# @admin.register(mprod_prei20_deliveryoption)
# class admin_mprod_prei20_deliveryoption(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "sku",
#         "listprice",
#         "price",
#         "hours_to_cancel_after_payment",
#         "hours_to_deliver_after_payment",
#     )
#     # Fields to exclude from add/edit Admin Form
#     exclude = ('sku',)



