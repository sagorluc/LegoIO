from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy  as _

from django.contrib.auth.forms import (
	PasswordChangeForm, 
	PasswordResetForm, 
	SetPasswordForm
)


# ******************************************************************************
class PasswordResetCustomForm(PasswordResetForm):
    email = forms.EmailField(
        label=mark_safe("<strong>Email Address</strong>"),
        required=True, 
        help_text=_("<small style='color: grey'>We never share your email address with any 3rd party company</small>"),
    )

    def __init__(self, *args, **kwargs):
	    super(PasswordResetCustomForm, self).__init__(*args, **kwargs)
	    self.label_suffix = ""

	    for visible in self.visible_fields():
	    	if visible.field.widget.attrs.get('class'):
	    		visible.field.widget.attrs['class'] += ' form-control form-control-xs'
	    		visible.field.widget.attrs['style'] += ' border-color:orange; border-radius: 0px;'
	    	else:
	    		visible.field.widget.attrs['class'] = 'form-control form-control-xs'
	    		visible.field.widget.attrs['style'] = 'border-color:orange; border-radius: 0px;'
