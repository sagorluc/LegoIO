from django.db import models


class mamar_pay(models.Model):

    customer_email=models.CharField(max_length=500,blank=True,null=True)
    amarpay_payment_data=models.JSONField(blank=True,null=True)

    def __str__(self) -> str:
        
        return str(self.id)