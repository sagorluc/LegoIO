from django import forms
from django.forms import Textarea
from ..models import ResumeDocType

class ResumeDocForm(forms.ModelForm):
    class Meta:
        model = ResumeDocType
        fields = (
            'document',
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

        