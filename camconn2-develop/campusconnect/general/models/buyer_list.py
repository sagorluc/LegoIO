import uuid
from django.db import models


class BuyerListGuest(models.Model):
    email 		    = models.CharField		(max_length=300)
    reguser         = models.BooleanField   (default=False)
    transaction_id  = models.CharField      (max_length=100, default="00000000000")
    created         = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated         = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    class Meta:
        verbose_name 		= 'Buyer Email List'
        verbose_name_plural = 'Buyer Email List'


    def __str__(self):
        return "{}->{}".format(self.email, self.reguser)
