from typing import Iterable, Optional
from django.db import models

import random

# Generate random number for refund id
def unique_conf_id_genarator():
    code = random.randint(000000, 999999)
    if OrderCancellationRequest.objects.filter(submission_conf_id = code).exists():
        return unique_conf_id_genarator()
    return code


class OrderCancellationRequest(models.Model):
    message                 = models.TextField(max_length=2000)
    created_for             = models.CharField(max_length=50)
    submission_conf_id      = models.CharField(max_length=6, null=True, blank=True)
    created_at              = models.DateTimeField(auto_now_add=True, help_text="timestamp of creation order cancellation request")
    submitted_by            = models.EmailField(max_length=255)

    #this function will create the submission conf id before saving 
    def save(self, *args, **kwargs) -> None:
        self.submission_conf_id = unique_conf_id_genarator()
        super(OrderCancellationRequest,self).save(*args, **kwargs)

    def __repr__(self):     # same as __str__(self):
        return "{},{},{},{}".format(self.submission_conf_id, self.message, self.created_for, self.created_at)
