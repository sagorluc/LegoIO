from zzz_lib.zzz_log import zzz_print
from django import forms
from django.core.exceptions import ValidationError

from inventory.validators import validate_email_guest
from django.utils.translation import ugettext_lazy as _

from inventory.models.mcart_fileupload import mcart_fileupload


# ******************************************************************************
class mmhFileUploadForm(forms.ModelForm):
    document = forms.FileField(
        label = '',
    )

    class Meta:
        model = mcart_fileupload
        fields = ('document', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = ''
        for visible in self.visible_fields():
            if visible.field.widget.attrs.get('class'):
                visible.field.widget.attrs['class'] += ' form-control form-control-xs'
                visible.field.widget.attrs['style'] += ' border-color:orange; border-radius: 0px;'
            else:
                visible.field.widget.attrs['class'] = 'form-control form-control-xs'
                visible.field.widget.attrs['style'] = 'border-color:orange; border-radius: 0px;'
