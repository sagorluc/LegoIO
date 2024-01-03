from unicodedata import category
from zzz_lib.zzz_log import zzz_print
from django.db import models
from inventory.models.mbase_prod import mbase_prod
from inventory import const_inventory
from inventory.models.visaassist.mprod_visaassist_catlist import mprod_visaassist_catlist

# ******************************************************************************
class mprod_visaassist(mbase_prod):
    # Note: fields listprice, saleprice and sku defined in parent classes
    title = models.CharField(max_length=500)
    
    description = models.TextField(blank=False, null=False)
    deliverables = models.TextField(blank=True, null=True)
    golivestatus = models.CharField(max_length=20,
                                choices=const_inventory.GOLIVE_STATUS,
                                default='draft'
                            )
    trending = models.CharField(max_length=10,
                                choices=const_inventory.TRENDING,
                                default='no'
                            )
    homepage_showup = models.CharField(max_length=20,
                                choices=const_inventory.HOMEPAGE_SHOWUP,
                                default='no'
                            )
    category = models.ForeignKey(mprod_visaassist_catlist, on_delete=models.CASCADE, null=True)

    class_threeletterprefix = "int"

    class Meta:
        verbose_name_plural = "03-Visaassist-services"

    def __str__(self):
        return f'{self.sku}, {self.category}, {self.title}'

    # # --------------------------------------------------------------------------
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)




















