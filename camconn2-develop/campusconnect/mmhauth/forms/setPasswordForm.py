from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.utils.translation import ugettext_lazy  as _

from zzz_lib.zzz_log import zzz_print


# ******************************************************************************
class SetPasswordCustomForm(SetPasswordForm):
    # new_password1 = forms.CharField(
    #     label=mark_safe("<strong>Password</strong>"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     help_text=None #password_validation.password_validators_help_text_html(),
    # )
    # new_password2 = forms.CharField(
    #     label=mark_safe("<strong>Password Confirmation</strong>"),
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     strip=False,
    #     help_text=_("<small style='color: grey'>Enter the same password as above, for verification</small>"),
    # )

    # error_messages = {
    #     'password_mismatch': _("The two password fields didn't match."),
    # }
    class Meta:
        # model = User
        fields = ("new_password1", "new_password2")

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(SetPasswordCustomForm, self).__init__(user, *args, **kwargs)
        self.label_suffix = ""

        for visible in self.visible_fields():
            if visible.field.widget.attrs.get('class'):
                visible.field.widget.attrs['class'] += ' form-control form-control-xs'
                visible.field.widget.attrs['style'] += ' border-color:orange; border-radius: 0px;'
            else:
                visible.field.widget.attrs['class'] = 'form-control form-control-xs'
                visible.field.widget.attrs['style'] = 'border-color:orange; border-radius: 0px;'





# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
# from django import forms
# from authtools.forms import UserCreationForm

# class UserCreationForm(UserCreationForm):
#     """
#     A UserCreationForm with optional password inputs.
#     """

#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         self.fields['password1'].required = False
#         self.fields['password2'].required = False
#         # If one field gets autocompleted but not the other, our 'neither
#         # password or both password' validation will be triggered.
#         self.fields['password1'].widget.attrs['autocomplete'] = 'off'
#         self.fields['password2'].widget.attrs['autocomplete'] = 'off'

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = super(UserCreationForm, self).clean_password2()
#         if bool(password1) ^ bool(password2):
#             raise forms.ValidationError("Fill out both fields")
#         return password2    
