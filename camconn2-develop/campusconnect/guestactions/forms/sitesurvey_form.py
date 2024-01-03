from django import forms
from ..models import SiteSurveyModel
from ..validators import validate_email_guest
from django.utils.translation import ugettext_lazy as _

########## FROM STYLE
TEXT_AREA_STYLE = {
    'row': 5,
    'cols': 10,
    'class': 'form-control form-control-xs rounded-0'
}
TEXT_INPUT_STYLE = {
    'class': 'form-control form-control-xs rounded-0'
}

HMPG_RATINGS = (
    ("excellent", "Excellent"),
    ("Good", "Good"),
    ("bad", "Didnot like it"),
)

USRFRNDLY_RATINGS = (
    ("veryfriendly", "Very Friendly"),
    ("ok", "It's Ok"),
    ("notfriendly", "Not user friendly at all"),
)

PROMO_RATINGS = (
    ("Yes", "Yes"),
    ("No", "No")
)

SERVICE_RATINGS = (
    ("excellent", "Excellent"),
    ("Good", "Good"),
    ("Bad", "Didnot like it"),    

)

OVERALL_RATINGS = (
    ("excellent", "Excellent"),
    ("Good", "Good"),
    ("bad", "Didnot like it"), 
)

CONSENTS = (
    ("Yes", "Yes"),
    ("No", "No")
    
)


class SiteSurveyForm(forms.ModelForm):
    site_used       = forms.ChoiceField(
        label="Have you made any purchase yet?",
        choices=CONSENTS,
        widget=forms.RadioSelect
    )
    hmpg_design     = forms.ChoiceField(
        label="What do you feel about our site homepage design?",
        choices=HMPG_RATINGS,
        widget=forms.RadioSelect
    )
    userfriendly    = forms.ChoiceField(
        label="How user-friendly the site is?",
        choices=USRFRNDLY_RATINGS,
        widget=forms.RadioSelect
    )
    promo_offers    = forms.ChoiceField(
        label="Have you used any promo offer yet?",
        choices=PROMO_RATINGS,
        widget=forms.RadioSelect
    )
    service_lineup  = forms.ChoiceField(
        label="What do you think about our service lines?",
        choices=SERVICE_RATINGS,
        widget=forms.RadioSelect
    )
    overall_exp     = forms.ChoiceField(
        label="How satisfied are you with overall experience?",
        choices=OVERALL_RATINGS,
        widget=forms.RadioSelect
    )
    recommend       = forms.ChoiceField(
        label="Will you recommend us to your friends?", 
        choices=CONSENTS,
        widget=forms.RadioSelect
    )    
    message         = forms.CharField(
        widget = forms.Textarea(
            attrs = TEXT_AREA_STYLE
        )
    )
    name            = forms.CharField(
        label = "Full Name",
        widget = forms.TextInput(
            attrs = TEXT_INPUT_STYLE
        )
    )
    email           = forms.EmailField(
        max_length = 200,
        label = "Email Address",
        help_text=_("<small style='color: grey'>We never share your email address with any 3rd party company</small>"),
        widget = forms.TextInput(
            attrs = TEXT_INPUT_STYLE
        ),
        error_messages = {
            'invalid': _(u''),
        },
        validators=[validate_email_guest]
    )

    class Meta:
        model = SiteSurveyModel
        fields = '__all__'
        exclude = ('created_at',)

    def __init__(self, *args, **kwargs):
        super(SiteSurveyForm, self).__init__(*args, **kwargs)
        # self.label_suffix = ""
        #
        # # Disable display of default field help text.
        # # Don't want to disable these any more as we are now formatting display of these in template.
        # # for fieldname in ("first_name", "last_name", "email", "password1", "password2"):
        # #     self.fields[fieldname].help_text = None
        
        ### Special help text for email field.
        self.fields['email'].help_text = "<small style='color: grey'>We never share your email address with any 3rd party company</small>"


        # ## form styling
        # for visible in self.visible_fields():
        #     # zzz_print("    %-28s: %s" % ("visible", visible))             
        #     # displays html of field, ex: <input type="text" name="first_name" maxlength="150" required id="id_first_name">
        
        #     # make all fields required
        #     visible.field.required = True
        
        #     # Set green outline to form input
        #     if visible.field.widget.attrs.get('class'):
        #         visible.field.widget.attrs['class'] += ' form-control form-control-xs'
        #         visible.field.widget.attrs['style'] += ' border-color:#f1f4f8; border-radius: 0px;'
        #     else:
        #         visible.field.widget.attrs['class'] = 'form-control form-control-xs'
        #         visible.field.widget.attrs['style'] = 'border-color:#f1f4f8; border-radius: 0px;'

        ### form validation error msessages
        # for k, field in self.fields.items():
        #     if 'required' in field.error_messages:
        #         field.error_messages['required'] = 'This is a required field'


    def is_valid(self):
        valid = super(SiteSurveyForm,self).is_valid()

        # # If a field has errors change it's border color to red.
        # for visible in self.visible_fields():
        #     if visible.errors:
        #         # zzz_print("    %-28s: %s" % ("visible", visible))
        #         if visible.field.widget.attrs.get('class'):
        #             visible.field.widget.attrs['class'] += ' form-control form-control-xs'
        #             visible.field.widget.attrs['style'] += ' border-color:red; border-radius: 0px;'
        #         else:
        #             visible.field.widget.attrs['class'] = 'form-control form-control-xs'
        #             visible.field.widget.attrs['style'] = 'border-color:red; border-radius: 0px;'

        return valid


