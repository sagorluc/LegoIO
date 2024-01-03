from django import forms
from django.forms import Textarea
from ..models import CandidateInternalMsg


class CandidateInternalMsgForm(forms.ModelForm):
	subject = forms.CharField(
		max_length = 2000,
		label = "Write a subject line",
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control'
			}
		)
	)
	msg = forms.CharField(
		max_length = 2000,
		label = "Write in details about your question",
		widget = forms.Textarea(
			attrs = {
				"rows": 5,
				"cols": 10,
				'class': 'form-control'
			}
		)
	)


	class Meta:
		model = CandidateInternalMsg
		fields = ('subject', 'msg')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""

	def __str__(self):
		return "{}".format(self.id)
