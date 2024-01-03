from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from base64 import b64encode, b64decode
from dirtyfields import DirtyFieldsMixin

from resumeweb.models import mcart

from random import randint
def random_num_generator():
    n = 10
    range_start = 10**(n-1)
    range_end = (10**n)-1
    random_value = randint(range_start, range_end)
    return random_value


class DispCause(models.Model):
    reason = models.CharField(
        max_length = 100,
        default = 'Late Delivery'
    )

    def __str__(self):
        return "{}".format(self.reason)


class Dispute(models.Model):
    created_aganist = models.ForeignKey(
            mcart,
            on_delete=models.CASCADE,
            related_name='mcart',
            null=True,
            blank=True
        )
    
    # submission_id = models.PositiveIntegerField(default=0) 

    dispcause = models.ManyToManyField(
            DispCause,
            related_name='disputes',
            help_text="Hold down “Control”, or “Command” on a Mac, to select more than one."
        )
    msg = models.TextField(
            max_length=2000
        )
    
    created_at = models.DateTimeField(
            auto_now_add=True,
            help_text="timestamp of creation"
        )
    created_by = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='user',
            null=True,
            blank=True
        )


    def __str__(self):
        return "{}{}".format(self.id, self.created_by)





class DisputeClaim(models.Model):
    created_aganist = models.CharField(
            max_length=255,
            null=True,
            blank=True
        )
    
    dispcause = models.ManyToManyField(
            DispCause,
            related_name='disputesclaims',
            help_text="Hold down “Control”, or “Command” on a Mac, to select more than one."
        )
    msg = models.TextField(
            max_length=2000
        )
    
    created_at = models.DateTimeField(
            auto_now_add=True,
            help_text="timestamp of creation dispute"
        )
    created_by = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='disputeuser',
            null=True,
            blank=True
        )


    def __str__(self):
        return "{}{}".format(self.id, self.created_by)

