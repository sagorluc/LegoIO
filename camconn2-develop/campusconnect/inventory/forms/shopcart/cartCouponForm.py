from zzz_lib.zzz_log import zzz_print
from django import forms
from django.core.exceptions import ValidationError

from inventory.validators import validate_email_guest
from django.utils.translation import ugettext_lazy as _

from inventory.models.mcart_fileupload import mcart_fileupload


# ******************************************************************************
class mmhCouponForm(forms.Form):
    coupon_id = forms.CharField(
        max_length=8,
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-xs rounded-0'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        