# from zzz_lib.zzz_log import zzz_print
from django.contrib import admin
from django import forms




# from resumeweb.models import (
#     mprod_exp180,
#     mprod_exp180_serviceoption,

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
#     mprod_posti20,
#     mprod_posti20_list,
#     mprod_posti20_serviceoption,

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

from inventory.models.strategy.mprod_strategy import mprod_strategy
from inventory.models.strategy.mprod_strategy_taglist import mprod_strategy_taglist
from inventory.models.strategy.mprod_strategy_serviceoption import mprod_strategy_serviceoption
from inventory.models.strategy.mprod_strategy_deliveryoption import mprod_strategy_deliveryoption




# from resumeweb.models import (
#     mprod_visabased,
#     mprod_visabased_list,
#     mprod_visabased_serviceoption,


# )

# from inventory.models import (

#     mprod_exp180_deliveryoption,
#     mprod_intprep_deliveryoption,
#     mprod_proflevel_deliveryoption,
#     mprod_prei20_deliveryoption,
#     mprod_rolebased_deliveryoption,
#     mprod_strategy_deliveryoption,
#     mprod_visabased_deliveryoption,
# )








## mprod_strategy_taglist 
## *****************************************************************************************
@admin.register(mprod_strategy_taglist)
class AdminStrategyCatList(admin.ModelAdmin):
    list_display = (
        "id","tagname",
    )
    # Fields to exclude from add/edit Admin Form
    exclude = ('sku',)



## mprod_strategy
## *****************************************************************************************
@admin.register(mprod_strategy)
class AdminStrategyServList(admin.ModelAdmin):
    list_display = (
        "sku",
        'title',
        "category",
        "deliverables",
        "golivestatus",
        "trending",
        "homepage_showup"
    )


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
        formfield = super(AdminStrategyServList, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'title':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield



## service options
## *****************************************************************************************
@admin.register(mprod_strategy_serviceoption)
class AdminStrategyServiceoption(admin.ModelAdmin):
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
        formfield = super(AdminStrategyServiceoption, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'name':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


## delivery options
## *****************************************************************************************
@admin.register(mprod_strategy_deliveryoption)
class admin_mprod_strategy_deliveryoption(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "listprice",
        "price",
        "hours_to_cancel_after_payment",
        "hours_to_deliver_after_payment",
    )
    # Fields to exclude from add/edit Admin Form
    exclude = ('sku',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(admin_mprod_strategy_deliveryoption, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description' or db_field.name == 'name':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
