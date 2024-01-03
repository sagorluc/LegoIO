from django import forms
from ..models import OrderCancellationRequest
from django import forms
from django.forms import Textarea
from ..models import ResumeFormType


class DateInput(forms.DateInput):
	input_type = 'date'


class OrderCancellationRequestForm(forms.ModelForm):
    message = forms.Textarea(
        attrs = {
            'class': 'form-control'
            }
    )

    class Meta:
        model   = OrderCancellationRequest
        fields  = '__all__'
        exclude = ('created_at','created_for', 'submitted_by','submission_conf_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

