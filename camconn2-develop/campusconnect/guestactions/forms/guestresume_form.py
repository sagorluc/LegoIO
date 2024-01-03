from zzz_lib.zzz_log import zzz_print

from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.utils.translation import ugettext_lazy as _

from ..validators import validate_email_guest
from ..models import GuestResumeModel

# ******************************************************************************
class GuestResumeForm(forms.ModelForm):
    file1 = forms.FileField(
        label = 'Resume',
        help_text=_("File format should be only in .doc or .docx"),
        widget = forms.FileInput(
            attrs = {
                'class': 'form-control form-control-xs rounded-0',
                'accept': 'application/doc'
            }
        )
    )
    email = forms.EmailField(
        max_length = 150,
        label = "Email Address",
        help_text=_("We never share your email address with any 3rd party company"),
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control form-control-xs rounded-0'
            }
        ),
        error_messages = {
            'invalid': _(u''),
        },
        validators=[validate_email_guest]
    )

    class Meta:
        model = GuestResumeModel
        fields = ('file1', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    def __str__(self):
        return "{}".format(self.email)
