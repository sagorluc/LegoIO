from ..models import SiteSurveyModel
from ..forms import SiteSurveyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import (CreateView, FormView, FormMixin, )
from django.views.generic.list import ListView
import datetime
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.template.loader import render_to_string
from django.http import HttpResponse
from guestactions.myfunctions import generate_coupon_code
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from guestactions.myfunctions import gen_num_for_email
import logging
logger = logging.getLogger(__name__)

import copy
from django.conf import settings
from mymailroom.myfunctions.send_email import send_email_customized

TEMP_DIR_GENERAL        = 'resumeweb/layout/general/'
TEMP_DIR_ACTION         = 'guestactions/site-survey/'
TEMP_DIR_CONF           = 'resumeweb/layout/'
TEMP_DIR_PRODABOUT      = 'resumeweb/layout/product-docs/'
TEMP_DIR_PRODFEEDBACK   = 'resumeweb/layout/guest-actions/site-survey/'
TEMP_DIR_EMAIL          = 'mymailroom/layout/'

# site survey homepage
# ************************
class SiteSurveyView(CreateView):
  template_name = TEMP_DIR_ACTION + 'home.html'
  form_class = SiteSurveyForm
  success_url = reverse_lazy('guestactions:site_survey_thankyou')
  model = SiteSurveyModel

  def form_valid(self, form):

    # save user data in db
    self.object = form.save(commit=False)
    self.object.created_at = datetime.datetime.now()
    self.object.save()

    # at first, save user given email add in a variable
    user_email_add = form.cleaned_data["email"]
    # save user_email_add in a session variable to be used in another view
    self.request.session['user_email_add'] = user_email_add

    # generate/select a coupon code from coupon table
    cop_code = generate_coupon_code()

    # send email fucntion 
    if cop_code is not None:
      # send email to the user
      appname = "GENERAL"
      subject = 'Resumenalyzer Product Review Submission Confirmation' + gen_num_for_email()
      to_emails_list = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS)
      to_emails_list.append(user_email_add)
      email_context = {
          'change_notice'     : 'reviewing our product',
          'submission_time'   : datetime.datetime.now(),
          'msg'               : 'thanks for your contacting us',
          'coupon_code_dict'  : cop_code,
      }
      html_message_text = render_to_string(
          template_name=TEMP_DIR_EMAIL + 'common.html',
          context=email_context,
          using=None,
          request=None
      )
      plain_message_text = strip_tags(html_message_text)
      logger.warning("calling send_email_customized")
      send_email_customized(subject, plain_message_text, html_message_text, to_emails_list, appname)
      # email function ends

    return super(SiteSurveyView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["pg_headline"] = "Submit Site Survey"
    return context


# confirmation page
# *****************
class SurveyThankyouView(TemplateView):
  template_name  = TEMP_DIR_ACTION + "confirmation.html"

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)

    context['task'] = "Site Survey"
    context['email_address'] = self.request.session.get('user_email_add')
    context['date_time'] = datetime.datetime.now()             # self.request.session['date_time']
    return context
