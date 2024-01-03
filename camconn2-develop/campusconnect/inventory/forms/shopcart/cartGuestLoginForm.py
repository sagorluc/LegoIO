from zzz_lib.zzz_log import zzz_print
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from inventory.validators import validate_email_guest
from django.utils.translation import ugettext_lazy as _

from inventory.models.mcart_fileupload import mcart_fileupload


# ******************************************************************************
class mmhEmailForm(forms.Form):
    email = forms.EmailField(
        label=mark_safe("<strong>Email</strong>"),
        max_length=1000,
        help_text=_("<small style='color: grey'>We never share your email address with any 3rd party company</small>"),
		error_messages = {
	        'invalid': _(u''),
	    },
		validators=[validate_email_guest]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        for visible in self.visible_fields():
            if visible.field.widget.attrs.get('class'):
                visible.field.widget.attrs['class'] += ' form-control form-control-xs'
                visible.field.widget.attrs['style'] += ' border-radius: 0px;'
            else:
                visible.field.widget.attrs['class'] = 'form-control form-control-xs'
                visible.field.widget.attrs['style'] = 'border-color:orange; border-radius: 0px;'

