from django import forms

from zzz_lib.zzz_log import zzz_print
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from ..models import ContactUsModel
from ..validators import validate_email_guest
from django.utils.translation import ugettext_lazy as _


# last update 04-06-2023
# ******************************************************************************
class ContactUsForm(forms.ModelForm):
	f_name = forms.CharField(
		max_length = 200,
		label = "First Name",
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control form-control-xs rounded-0'
			}
		)
	)
	l_name = forms.CharField(
		max_length = 200,
		label = "Last Name",
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control form-control-xs rounded-0'
			}
		)
	)
	email = forms.EmailField(
		max_length = 200,
		label = "Email Address",
		help_text=_("<small style='color: grey'>We never share your email address with any 3rd party company</small>"),
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
	msg = forms.CharField(
		max_length = 2000,
		label = "Write about your question in details",
		widget = forms.Textarea(
			attrs = {
				"rows": 5,
				"cols": 10,
				'class': 'form-control form-control-xs rounded-0'
			}
		)
	)

	class Meta:
		model = ContactUsModel
		fields = [
			'f_name',
			'l_name',
			'email',
			'msg'
		]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""


# class ContactUsForm(forms.Form):
#     name = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)

#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass

