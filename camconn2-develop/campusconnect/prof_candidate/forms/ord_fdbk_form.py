from django import forms
from ..models import ServiceFeedbackModel

class ServiceFeedbackForm(forms.ModelForm):
    
    class Meta:
        model   = ServiceFeedbackModel
        fields  = '__all__'
        exclude = ('created_at',)

    # def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.label_suffix = ""

