from django.contrib.auth.forms import SetPasswordForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from guestactions.myfunctions import gen_num_for_email

UserModel = get_user_model()

class MySetPasswordForm(SetPasswordForm):

    def send_email(self, to_mail):
        # subject = 'Password changed successfully'
        # body = 'Your password has been changed successfully'
        # email = EmailMultiAlternatives(subject, body, None, [to_email])
        # email.send()

        subject = 'Password changed successfully' + gen_num_for_email()
        message = None
        recipient_list = [UserModel.get_email_field_name()]
        html_content = '<strong>i am confirming that password reset is complete</strong>'
        send_mail(
            subject=subject, 
            message=None, 
            from_email=from_email, 
            recipient_list=recipient_list, 
            html_message=html_content
        )

    def save(self, commit=True):
        if commit:
            email = email_field_name = UserModel.get_email_field_name()
            user_email = getattr(self.user, email_field_name)
            self.send_email(user_email)
        super().save_(commit=commit)
