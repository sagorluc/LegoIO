from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, BadHeaderError
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from guestactions.myfunctions import generate_coupon_code


import logging
logger = logging.getLogger(__name__)


def send_email(subject,msg,change_notice, submission_time, submission_id, coupon_code_dict, email_address):

  from_email=settings.EMAIL_HOST_USER
  recipient_list=[email_address]

  context = {
          'user':                     email_address,
          'attached_file':            None,
          'customer_support_email':   settings.SUPPORT_EMAIL,
          'coupon_code_dict':         coupon_code_dict,
          'change_notice':            change_notice,
          'submission_time':          submission_time,
          'submission_id':            submission_id,
          'app_version' : settings.VER_RESUMEWEB,
  }

  template_name = 'resumeweb/email_templates/base.html'
  html_content=render_to_string(
      template_name=template_name,
      context=context,
      using=None,
      request=None
  )
  text_content = strip_tags(html_content)
  if len(recipient_list) > 0:
      try:
          send_mail(
              subject=subject, 
              message=msg, 
              from_email=from_email, 
              recipient_list=recipient_list, 
              html_message=html_content
          )
          logger.warning('email sent to {}'.format(recipient_list))
      except:
          raise BadHeaderError('something went wrong {0}'.format(email_address))

      return HttpResponseRedirect(template_name, context)
  else:
      logger.warning("email not sent from send_email_to_user")


# =============
#               # send coupon code through email

#               plain_message_text = render_to_string(TEMP_DIR_EMAIL + 'email_with_coupon_plain.html', context)
#               html_message_text  = render_to_string(TEMP_DIR_EMAIL + 'email_with_coupon_html.html', context)
#               # zzz_print("    %-28s: %s" % ("plain_message_text", plain_message_text))
#               # zzz_print("    %-28s: %s" % ("html_message_text", html_message_text))

#               to_emails_list = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS)
#               to_emails_list.append(email_add_given)

#               imsendmail = msendmail.objects.add(
#                   subject             = form.cleaned_data["first_name"] + ", thanks for the feedback!",
#                   plain_message       = plain_message_text,
#                   html_message        = html_message_text,
#                   from_email          = settings.EMAIL_HOST_USER,
#                   to_emails_list      = to_emails_list
#               )
#               imsendmail.send_to_each_recipient_seperately()
