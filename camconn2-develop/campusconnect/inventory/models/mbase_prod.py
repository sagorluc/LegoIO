from zzz_lib.zzz_log import zzz_print
from django.db import models
from inventory.models.mbase_sku import mbase_sku

# ******************************************************************************
# All products that use the cart system inherit from this class.
# ******************************************************************************
class mbase_prod(mbase_sku):
    listprice           = models.DecimalField(default=0.99, decimal_places=2, max_digits=100,)
    saleprice           = models.DecimalField(default=0.99, decimal_places=2, max_digits=100,)

    # --------------------------------------------------------------------------
    class Meta:
        abstract = True

    # --------------------------------------------------------------------------
    # Child classes should override this method if they require post purchase processing
    # Note: post purchase processing is dispatched to a non blocking thread so be careful what is done in there.
    def post_purchase_processing(self, request, imcompleted_purchase):
        zzz_print("    %-28s: %s" % ("post_purchase_processing", "fall through to mbase_prod"))
        pass


















