# from zzz_lib.zzz_log import zzz_print
# from django.contrib import admin
# from django import forms

# from inventory.models.posti20 import (
#     mprod_exp180,
#     mprod_exp180_serviceoption,

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
#     mprod_proglang_list,
#     mprod_proglang_serviceoption,

# )



# from inventory.models.strategy import (
#     mprod_strategy,
#     mprod_strategy_taglist,
#     mprod_strategy_serviceoption,    

# )

# from inventory.models.posti20 import mprod_exp180_deliveryoption
from inventory.models.visaassist import mprod_visaassist_deliveryoption
# from campusconnect.inventory.models.prei20 import mprod_prei20_deliveryoption
# from inventory.models.strategy import mprod_strategy_deliveryoption
# from inventory.models.univcom import mprod_proflevel_deliveryoption









# # usvisa serv list
# ########################################################################################
# @admin.register(mprod_visabased)
# class Admin_USVISA_SERV_LIST(admin.ModelAdmin):
#     list_display = (
#         "sku",
#         "title",
#         "deliverables",
#         "category",
#         "golivestatus",
#         "trending",
#         "homepage_showup"
#     )
#     # Fields to exclude from add/edit Admin Form
#     exclude = ('sku',)

#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super(Admin_USVISA_SERV_LIST, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description' or db_field.name == 'title':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield




# ## service options
# ## *****************************************************************************************
# @admin.register(mprod_visabased_serviceoption)
# class AdminUSvisaServiceoption(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "sku",
#         "listprice",
#         "price",
#         'products'
#     )
#     # Fields to exclude from add/edit Admin Form
#     exclude = ('sku',)


#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super(AdminUSvisaServiceoption, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description' or db_field.name == 'name':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield






# ## delivery options
# ## *****************************************************************************************
# @admin.register(mprod_visabased_deliveryoption)
# class admin_mprod_visabased_deliveryoption(admin.ModelAdmin):
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


#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super(admin_mprod_visabased_deliveryoption, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description' or db_field.name == 'name':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield


        