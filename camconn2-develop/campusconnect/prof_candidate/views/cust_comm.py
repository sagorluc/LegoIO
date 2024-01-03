import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView
)
from guestactions.myfunctions import gen_num_for_email
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
import os
from prof_candidate.models import (
    CandidateInternalMsg,
)
from zzz_lib.zzz_log import zzz_print
from ..forms import CandidateInternalMsgForm
from mymailroom.myfunctions import send_email_customized
from django.template.loader import render_to_string
from django.utils.html import strip_tags

TEMPLATE_DIR = "prof_candidate/layout/cust_comm/"
APP_VERSION = os.environ.get("VER_RESUMEWEB")

# ******************************************************************************
class CandidateMsg(LoginRequiredMixin, CreateView):
    template_name = TEMPLATE_DIR + "contact-us.html"
    form_class = CandidateInternalMsgForm
    success_msg = "You message has been received successfully"
    success_url   = reverse_lazy('prof_candidate:msg_submit')

    def form_valid(self, form):
        m = form.save(commit=False)
        m.created_by = self.request.user
        m.created_at = datetime.datetime.now()
        m.save()
        messages.success(self.request, self.success_msg)

        user_email_add = self.request.user.email
        subject = "We are here to listen you " + gen_num_for_email()
        email_body = "Thank You for contacting us. Our resposible person will contact you soon"     
        time = datetime.datetime.now()   
        appname = "CUSTSUPP"
        html_message_text = email_body
        #render_to_string(
        #     email_body
        # )
        plain_message_text = strip_tags(html_message_text)
        
        send_email_customized(subject, plain_message_text, html_message_text, user_email_add, appname)
        return super(CandidateMsg, self).form_valid(form)


# ******************************************************************************
class MsgHistory(LoginRequiredMixin, ListView):
    model = CandidateInternalMsg
    template_name = TEMPLATE_DIR + "msg-history.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        zzz_print("    %-28s: %s" % ("get_context_data()", ""))

        context = super().get_context_data(**kwargs)
        context['no_of_msg'] = CandidateInternalMsg.objects.filter(created_by=self.request.user).count()
        context['app_version'] = APP_VERSION
        context['section_header_1'] = 'no_of_msg'
        for key in context:
            zzz_print("    key %-24s: value %s" % (key, context[key]))

        return context

    def get_queryset(self):
        qs = CandidateInternalMsg.objects.filter(created_by=self.request.user)\
            .order_by('-created_at')
        return qs



# ******************************************************************************
class MsgDetails(LoginRequiredMixin, DetailView):
    model = CandidateInternalMsg
    template_name = TEMPLATE_DIR + "msg-details.html"



# ******************************************************************************
class MsgConfirm(LoginRequiredMixin, TemplateView):
    template_name = TEMPLATE_DIR + "msg_confirm.html"

