from django import forms
from ..models import DeactivatedAccount


from zzz_lib.zzz_log import zzz_print
import json
from uuid import uuid4
from django.shortcuts import render
from base64 import b64decode, b64encode
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import connection
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


class AccDeactivateForm(forms.ModelForm):
    class Meta:
        model = DeactivatedAccount
        fields = (
            'email',
            'confirmation',
            'deactivate_status',
        )

    def __init__(self, *args, **kwargs):
        self.email = kwargs.pop('email')
        super(AccDeactivateForm, self).__init__(*args, **kwargs)
        self.label = ''
        for visible in self.visible_fields():
            if visible.field.widget.attrs.get('class'):
                visible.field.widget.attrs['class'] += ' form-control form-control-xs'
                visible.field.widget.attrs['style'] += ' border-color:blue; border-radius: 0px;'
            else:
                visible.field.widget.attrs['class'] = 'form-control form-control-xs'
                visible.field.widget.attrs['style'] = 'border-color:blue; border-radius: 0px;'


    def clean_deactivate_status(self):
        status_check = self.cleaned_data['deactivate_status']

        if not status_check:
            raise forms.ValidationError("Please check deactivate status")
        return status_check
    
    def clean_confirmation(self):
        confirmation = self.cleaned_data['confirmation']

        if confirmation != "confirm":
            raise forms.ValidationError("Please type \'confirm\' ")
        return confirmation

    def clean_email(self):
        email = self.cleaned_data['email']

        if email != self.email:
            raise forms.ValidationError("Enter correct user email")
        return email



from django.contrib.auth.forms import PasswordChangeForm
class PasswordUpdateForm(PasswordChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(PasswordUpdateForm, self).__init__(*args, **kwargs)
        self.label = ''
        for visible in self.visible_fields():
            if visible.field.widget.attrs.get('class'):
                visible.field.widget.attrs['class'] += ' form-control form-control-xs'
                visible.field.widget.attrs['style'] += ' border-color:blue; border-radius: 0px;'
            else:
                visible.field.widget.attrs['class'] = 'form-control form-control-xs'
                visible.field.widget.attrs['style'] = 'border-color:blue; border-radius: 0px;'

