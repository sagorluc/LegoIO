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


def send_email(email_address,subject,msg,change_notice, sent_time):

    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email_address]

    context = {
            'user':             email_address,
            'attached_file':    None,
            'customer_support_email': settings.SUPPORT_EMAIL,
    }

    template_name = 'resumeweb/email_templates/general_resume_submission/main.html'
    html_content=render_to_string(
        template_name=template_name,
        context=context,
        using=None,
        request=None
    )
    text_content = strip_tags(html_content)
    if len(recipient_list)>0:
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
