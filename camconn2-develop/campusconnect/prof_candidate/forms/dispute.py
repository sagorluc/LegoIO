from django import forms
from django.forms import Textarea
from ..models import (DisputeSubmissionModel)
from resumeweb.models import mcart
from django.contrib.auth.models import User




class DisputeSubmissionForm(forms.ModelForm):
	class Meta:
		model = DisputeSubmissionModel
		fields = "__all__"
		exclude = ('created_aganist', 'created_by', 'submission_id')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""


