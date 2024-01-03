# from zzz_lib.zzz_log import zzz_print
# from django.contrib import admin
# from django import forms

# from inventory.models import (
#     mprod_prei20,
#     mprod_prei20_serviceoption,

# )


# from resumeweb.models import (
#     mprod_intprep,
#     mprod_intprep_catlist,
#     mprod_intprep_serviceoption,

# )


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
    # mprod_intprep_deliveryoption,
    # mprod_proflevel_deliveryoption,
    mprod_prei20_deliveryoption,
    # mprod_rolebased_deliveryoption,
    # mprod_strategy_deliveryoption,
    # mprod_visabased_deliveryoption,


)




# Tech Role cat list or Identity or rolebased or mprod_rolebased_list
########################################################################################
# @admin.register(mprod_rolebased_list)
# class AdminTechRoleCatList(admin.ModelAdmin):
#     list_display = (
#         "rolename",
#     )
#     # Fields to exclude from add/edit Admin Form
#     exclude = ('sku',)





# # mprod_rolebased serv list
# ########################################################################################
# @admin.register(mprod_rolebased)
# class AdminTechRoleServList(admin.ModelAdmin):
#     list_display = (
#         "sku",
#         "title",
#         "category",
#         "deliverables",
#         "golivestatus",
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
#         formfield = super(AdminTechRoleServList, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description' or db_field.name == 'title':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield




# ## service options
# ## *****************************************************************************************
# @admin.register(mprod_rolebased_serviceoption)
# class AdminTechRoleServiceoption(admin.ModelAdmin):
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
#         formfield = super(AdminTechRoleServiceoption, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description' or db_field.name == 'name':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield




# ## delivery options
# ## *****************************************************************************************
# @admin.register(mprod_rolebased_deliveryoption,)
# class AdminTechRoleDelivOption(admin.ModelAdmin):
#     list_display = (
#         "sku",
#         "name",
#         "listprice",
#         "price",
#         "hours_to_cancel_after_payment",
#         "hours_to_deliver_after_payment",
#     )
#     # Fields to exclude from add/edit Admin Form
#     exclude = ('sku',)


#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super(AdminTechRoleDelivOption, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description' or db_field.name == 'name':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield
