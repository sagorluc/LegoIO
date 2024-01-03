from zzz_lib.zzz_log import zzz_print
from django import forms
from django.core.exceptions import ValidationError

from inventory.models.adhoc import AdhocRequestModel
from inventory.validators import validate_email_guest
from django.utils.translation import ugettext_lazy as _


WHY_NEEDED = (
    ('', 'Choose...'),
    ('cd01', 'Didnot Find this serv in exp180'),
    ('cd02', 'I donot know where to search'),
    ('cd03', 'it was time consuming to search for this'),
)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# last update 04-27-2022
# ******************************************************************************
class AdhocRequestForm(forms.ModelForm):
	target_JD_1 = forms.CharField(
		max_length = 5000,
		label = "Your Target Job Description Sample 1",
		widget = forms.Textarea(
			attrs = {
				"rows": 5,
				"cols": 10,
				'class': 'form-control form-control-xs rounded-0'
			}
		),
		help_text = 'max 5000 char'
	)
	target_JD_2 = forms.CharField(
		max_length = 5000,
		label = "Your Target Job Description Sample 2",
		widget = forms.Textarea(
			attrs = {
				"rows": 5,
				"cols": 10,
				'class': 'form-control form-control-xs rounded-0'
			}
		)
	)
	ques_details = forms.CharField(
		max_length = 3000,
		label = "Write in details about your enquery for us such as what type of service you want us to provide",
		widget = forms.Textarea(
			attrs = {
				"rows": 5,
				"cols": 10,
				'class': 'form-control form-control-xs rounded-0'
			}
		)
	)
	why_needed = forms.CharField(
		label='Why do you think you need to request for an Adhoc Service',
		widget=forms.Select(
			choices=WHY_NEEDED,
			attrs = {
				'class': 'form-control form-control-xs rounded-0'
			}
		)
	)
	resume = forms.FileField(
        label='Which Resume you intend to submit in your next Job Application',
		help_text='Max Filesize 5MBs'
    )
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
		label = "Contact Email",
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


	class Meta:
		model = AdhocRequestModel
		fields = (
			"target_JD_1",
			"target_JD_2",
			"ques_details",
			"why_needed",
			"resume",
			"f_name",
			"l_name",
			"email"

		)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""
