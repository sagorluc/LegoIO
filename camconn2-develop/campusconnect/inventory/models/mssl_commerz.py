from django.db import models


class mssl_commerz(models.Model):

    customer_email=models.CharField(max_length=500,blank=True,null=True)
    ssl_payment_data=models.JSONField(blank=True,null=True)

    def __str__(self) -> str:
        
        return str(self.id)

