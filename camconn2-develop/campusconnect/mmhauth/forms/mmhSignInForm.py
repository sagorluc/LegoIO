from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from prof_candidate.models.acc_sett import DeactivatedAccount
from zzz_lib.zzz_log import zzz_print

# ******************************************************************************
class mmhSignInForm(forms.ModelForm):
    email = forms.EmailField(label=mark_safe("<strong>Email Address</strong>"), required=True)
    password = forms.CharField(label=mark_safe("<strong>Password</strong>"), widget=forms.PasswordInput())

    # --------------------------------------------------------------------------
    class Meta:
        model = User
        fields = ("email", "password")

    # --------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(mmhSignInForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

        # form styling        
        for visible in self.visible_fields():
            # zzz_print("    %-28s: %s" % ("visible", visible))             # displays html of field, ex: <input type="text" name="first_name" maxlength="150" required id="id_first_name">

            # make all fields required
            visible.field.required = True

            if visible.field.widget.attrs.get('class'):
                visible.field.widget.attrs['class'] += ' form-control form-control-xs'
                visible.field.widget.attrs['style'] += ' border-color:orange; border-radius: 0px;'
            else:
                visible.field.widget.attrs['class'] = 'form-control form-control-xs'
                visible.field.widget.attrs['style'] = 'border-color:orange; border-radius: 0px;'

        # form validation error msessages
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = 'This is a required field'

    # --------------------------------------------------------------------------
    # def clean(self):
    #     email       = self.cleaned_data.get('email').lower()
    #     password    = self.cleaned_data.get('password')
    #     # zzz_print("    %-28s: %s" % ("email", email))
    #     # zzz_print("    %-28s: %s" % ("password", password))

    #     if DeactivatedAccount.objects.filter(email__iexact=email).exists():
    #         raise ValidationError("This email is used once and acc deactivated")



    #     return self.cleaned_data

