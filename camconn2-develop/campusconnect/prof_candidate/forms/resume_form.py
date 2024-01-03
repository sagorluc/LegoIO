from django import forms
from django.forms import Textarea
from ..models import ResumeFormType


class DateInput(forms.DateInput):
	input_type = 'date'


class ResumeTypeForm(forms.ModelForm):
	Exp_1 = forms.CharField(
		max_length = 2000,
		label = "Most recent position 1",
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control'
			}
		)
	)
	start_date_1= forms.DateField(widget=DateInput)
	end_date_1= forms.DateField(widget=DateInput)
	Job_Duties_1= forms.Textarea(
		attrs = {
			'class': 'form-control'
		}
	)

	Exp_2 = forms.CharField(
		max_length = 2000,
		label = "Most recent position 2",
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control'
			}
		)
	)
	start_date_2= forms.DateField(widget=DateInput)
	end_date_2= forms.DateField(widget=DateInput)
	Job_Duties_2= forms.Textarea(
		attrs = {
			'class': 'form-control'
		}
	)

	Exp_3 = forms.CharField(
		max_length = 2000,
		label = "Most recent position 3",
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control'
			}
		)
	)
	start_date_3= forms.DateField(widget=DateInput)
	end_date_3= forms.DateField(widget=DateInput)
	Job_Duties_3= forms.Textarea(
		attrs = {
			'class': 'form-control'
		}
	)

	class Meta:
		model = ResumeFormType
		fields = (
			'Exp_1',
			'start_date_1',
			'end_date_1',
			'Job_Duties_1',
			'Exp_2',
			'start_date_2',
			'end_date_2',
			'Job_Duties_2',
			'Exp_3',
			'start_date_3',
			'end_date_3',
			'Job_Duties_3'
			)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""
