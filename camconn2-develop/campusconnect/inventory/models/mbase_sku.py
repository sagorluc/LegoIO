from zzz_lib.zzz_log import zzz_print
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import random 

# ******************************************************************************
class mbase_sku(models.Model):
    sku = models.CharField(max_length=6, unique=True)
    class_threeletterprefix = "zzz"

    # --------------------------------------------------------------------------
    class Meta:
        abstract = True

    # --------------------------------------------------------------------------
    # Generate and save imsku instance
    def generate_sku(self, threeletterprefix):
        #from .msku import msku
        from inventory.models.msku import msku
        try:
            imsku = msku.objects.get(threeletterprefix=threeletterprefix)
            imsku.value += random.randint(2,9) #1
            imsku.save()
        except ObjectDoesNotExist:
            imsku = msku.objects.create(threeletterprefix=threeletterprefix, value=10)
        zzz_print("    %-28s: %s" % ("imsku", imsku))
        return imsku.__str__()

    # --------------------------------------------------------------------------
    # Overridden save method which generates and saves an sku value
    def save(self, *args, **kwargs):
        if not self.sku:
            zzz_print("    %-28s: %s" % ("mbase_sku", "save sku"))
            self.sku = self.generate_sku(self.class_threeletterprefix)
        super().save(*args, **kwargs)









