from django import forms
from ..validators import validate_email_guest
from django.utils.translation import ugettext_lazy as _

# ******************************************************************************
class OrderStatusCheckForm(forms.Form):
	tracking_id = forms.CharField(
		max_length=20,
		label="Order Tracking ID",
		widget=forms.TextInput(
			attrs={
				'class': 'form-control form-control-xs rounded-0'
			}
		),
		help_text = """<span class='text-muted fs-sm'><ul><li>For example 111-222-3333 or 111222333</li></span>""",
	)
	email_add = forms.EmailField(
		label = "Email Address",
		widget = forms.TextInput(
			attrs={
				'class': 'form-control form-control-xs rounded-0'
			}
		),
		help_text = "<span class='text-muted'><ul><li>Please enter the email address in which you received purchase confirmation email</li></ul></span>",
		error_messages = {
			'invalid': _(u''),
		},
		validators=[validate_email_guest]
	)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ''
