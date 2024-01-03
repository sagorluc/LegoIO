from zzz_lib.zzz_log import zzz_print
from django.db import models

# ******************************************************************************
class msku(models.Model):
    threeletterprefix   = models.CharField(max_length=3)
    value               = models.IntegerField()

    class Meta:
        verbose_name_plural = "msku Services"

    def __str__(self):
        # formatted to return value prepended by zeros
        return self.threeletterprefix + f'{self.value:03d}'
        










