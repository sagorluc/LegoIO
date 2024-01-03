from django.contrib.auth.models import User
from django.db import models


class DeactivatedAccount(models.Model):
    # Taking user email from system by default
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    
    )

    # Taking user input email address
    email = models.EmailField(max_length=500)

    confirmation= models.CharField(max_length=7, help_text="Please type \'confirm\' ")
    deactivate_status= models.BooleanField(default=False)
    created = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    # updated = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")  

    def __str__(self):
        return "{}".format(self.email)
        