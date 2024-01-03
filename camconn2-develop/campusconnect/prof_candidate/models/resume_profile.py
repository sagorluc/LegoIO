from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from base64 import b64encode, b64decode
from dirtyfields import DirtyFieldsMixin


class ResumeFormType(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid4,
            help_text="Unique ID",
            editable=False
    )

    Exp_1 = models.CharField(max_length=500, blank=False, null=False, default='Exp_1')
    start_date_1 = models.DateField(blank=True, null=True)
    end_date_1 = models.DateField(blank=True, null=True)
    Job_Duties_1 = models.TextField(
            max_length=7000,
            null=True,
            blank=True
    )

    Exp_2 = models.CharField(max_length=500, blank=False, null=False, default='Exp_2')
    start_date_2 = models.DateField(blank=True, null=True)
    end_date_2 = models.DateField(blank=True, null=True)
    Job_Duties_2 = models.TextField(
            max_length=7000,
            null=True,
            blank=True
    )
    
    Exp_3 = models.CharField(max_length=500, blank=False, null=False, default='Exp_3')
    start_date_3 = models.DateField(blank=True, null=True)
    end_date_3 = models.DateField(blank=True, null=True)
    Job_Duties_3 = models.TextField(
            max_length=7000,
            null=True,
            blank=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users_resume',
        null=True,
        blank=True
    )
    created = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")

    def __str__(self):
        return "{}".format(self.id)


class ResumeDocType(models.Model):
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='candidate_name',
            null=True,
            blank=True
        )
    document = models.FileField(upload_to='resume/candidate/')
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, help_text="timestamp of creation")
    updated = models.DateTimeField(auto_now=True, help_text="timestamp of last update")

    def __str__(self):
        return "{}".format(self.user)

