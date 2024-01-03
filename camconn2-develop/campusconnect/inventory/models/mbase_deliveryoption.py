from zzz_lib.zzz_log import zzz_print
from django.db import models
from .mbase_sku import mbase_sku

# All products that have delivery options inherit from this class.
# ******************************************************************************
class mbase_deliveryoption(mbase_sku):
    name                            = models.CharField      (max_length=2000)
    listprice                       = models.DecimalField   (default=0.99, decimal_places=2, max_digits=1000,)
    price                           = models.DecimalField   (default=0.99, decimal_places=2, max_digits=1000)
    description                     = models.CharField      (max_length=2000, blank=True, null=True)
    hours_to_cancel_after_payment   = models.IntegerField   (default=168)
    # Next field must always be greater than or equal to previous field.
    hours_to_deliver_after_payment  = models.IntegerField   (default=336)

    # Following fields ARE NOT fields that should be saved/used/stored in Database
    ndb_checked             = False

    # --------------------------------------------------------------------------
    class Meta:
        abstract = True
        ordering = ['price']   # Auto sort queries by lowest price first.

    # --------------------------------------------------------------------------
    def __str__(self):
        return f"{self.name}"

    # --------------------------------------------------------------------------
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)














