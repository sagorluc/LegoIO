from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from base64 import b64encode, b64decode
from dirtyfields import DirtyFieldsMixin


class CandidateInternalMsg(models.Model):
    subject = models.CharField(
            max_length=500,
            default="Message Subject"
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
            related_name='msg_creator',
            null=True,
            blank=True
        )


    def __str__(self):
        return "{}".format(self.id)

