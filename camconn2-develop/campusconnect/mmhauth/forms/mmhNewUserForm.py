from zzz_lib.zzz_log import zzz_print
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _
# from pprint import pprint

from django.contrib.auth import (
    authenticate, 
    get_user_model, 
    password_validation,
)
from ..models import mverificationcode
from prof_candidate.models.acc_sett import DeactivatedAccount


# ******************************************************************************
class mmhNewUserForm(UserCreationForm):
    first_name = forms.CharField(label=mark_safe("<strong>First Name</strong>"), required=True)
    last_name  = forms.CharField(label=mark_safe("<strong>Last Name</strong>"), required=True)

    email = forms.EmailField(
        label=mark_safe("<strong>Email Address</strong>"),
        required=True, 
        help_text=_("<small style='color: grey'>We never share your email address with any 3rd party company</small>"),
    )
    password1 = forms.CharField(
        label=mark_safe("<strong>Password</strong>"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("<small style='color: grey'>Must be at least 8 characters long</small>"),
    )
    password2 = forms.CharField(
        label=_(mark_safe("<strong>Password Confirmation</strong>")),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("<small style='color: grey'>Enter the same password as above</small>"),
    )

    error_messages = {
        'password_mismatch': _("Passwords didnot match"),
    }

    # --------------------------------------------------------------------------
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    # --------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(mmhNewUserForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

        # form styling
        for visible in self.visible_fields():
            # zzz_print("    %-28s: %s" % ("visible", visible))             # displays html of field, ex: <input type="text" name="first_name" maxlength="150" required id="id_first_name">

            # make all fields required
            visible.field.required = True

            # Set green outline to form input
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
    ## validate user email address is unique
    def clean_email(self):
        email = self.cleaned_data["email"]
        if DeactivatedAccount.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(_("This email was once used to create an account, then the account was deactivated permanently by the User's request."))
        else:
            if User.objects.filter(email__iexact=email).exists():
                raise forms.ValidationError(_("A user with that email address already exists in our system. Please try a different email or Reset Password."))
        return email.lower()

    # --------------------------------------------------------------------------
    def save(self, commit=True):
        user = super(mmhNewUserForm, self).save(commit=False)
        user.email      = self.cleaned_data["email"]
        user.username   = self.cleaned_data["email"].lower()
        if commit:
            user.is_active = False  # they must verify via link in email
            user.save()
        return user

