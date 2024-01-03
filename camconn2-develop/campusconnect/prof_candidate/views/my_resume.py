from zzz_lib.zzz_log import zzz_print
from base64 import b64decode, b64encode
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import (
    redirect,
    render
)
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView
)
from guestactions.myfunctions import gen_num_for_email
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..forms import (
    ResumeTypeForm,
    ResumeDocForm,
    AccDeactivateForm,
)
from ..models import (ResumeDocType, ResumeFormType,) 
from django.urls import reverse
from mymailroom.myfunctions import send_email_customized
import datetime
import logging
logger = logging.getLogger(__name__)

TEMPLATE_DIR = "prof_candidate/layout/resume/"



# page: resume doc file upload
# ******************************************************************************
class ResumeDocView(LoginRequiredMixin, CreateView): 
    # why this view name has no View in the name?
    template_name = TEMPLATE_DIR + "resume_doc_file_upload.html"
    model = ResumeDocType
    form_class = ResumeDocForm    
    success_url = 'resume-upload-url' 

    def form_valid(self, form):
        # step1: save the form 
        messages.success(self.request, "File Uploaded Successfully")

        # step2: send email
        form.instance.user = self.request.user
        email_address = self.request.user.email
        subject = "Resume File Uploaded Successfully" + gen_num_for_email()
        change_notice = "uploaded your resume"
        time = datetime.datetime.now()
        send_email_customized(email_address,subject,change_notice,time)

        # step3: return to the desired url
        return super(ResumeDocView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sys_user = self.request.user
        logger.warning("sys_user >>{}".format(sys_user))
        docCount = ResumeDocType.objects.filter(user=sys_user).exclude(deleted=True).count()
        if docCount == 0:
            context = {
                "docCount": docCount,
                "form"    : ResumeDocForm,
                "msg"     : "you donot have any resume uploaded yet",
                "pgheader": "Your Resume Document Format",
                "app_version": settings.VER_RESUMEWEB
            }
        else:
            doc = ResumeDocType.objects.filter(user=sys_user).exclude(deleted=True).order_by('-updated').first()
            context = {
                "document"  : doc.document,
                "doc_id": doc.id,
                "updated"   : doc.updated,
                "form"      : ResumeDocForm(),
                'section_header_1'  : "Upload your resume Doc Format",
                'section_header_2'  : "Your current resume",
                "app_version": settings.VER_RESUMEWEB
            }
        return context


def delete_doc(request, doc_id):
    q1 = ResumeDocType.objects.filter(id=doc_id).update(deleted=True)
    messages.success(request, "File Deleted Successfully")
    email_address = request.user.email
    subject = "Resume File Deleted Successfully" + gen_num_for_email()
    change_notice = "deleted your resume"
    time = datetime.datetime.now()
    send_email_customized(email_address,subject,change_notice,time)
    return HttpResponseRedirect('/app/candidate/my-resume/resume-upload-url')



# page: resume form submission
# ******************************************************************************
class ResumeFormView(LoginRequiredMixin, TemplateView):
    template_name = TEMPLATE_DIR + "resume_form.html"
    model = ResumeFormType
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sys_user = self.request.user
        formCount = ResumeFormType.objects.all().count()
        form = ResumeTypeForm()

        if formCount == 0:
            context = {
                'form': form,
                # print this msg in template when a user has no form submit yet
                'empty_msg': "you have not filled this one yet",  
                "app_version": settings.VER_RESUMEWEB
            }

        else:
            data = ResumeFormType.objects.filter(user=sys_user).order_by('-updated')[0]
            context = {
                "Exp_1": data.Exp_1,
                "start_date_1": data.start_date_1,
                "end_date_1": data.end_date_1,
                "Job_Duties_1": data.Job_Duties_1,
                "Exp_2": data.Exp_2,
                "start_date_2": data.start_date_2,
                "end_date_2": data.end_date_2,
                "Job_Duties_2": data.Job_Duties_2,
                "Exp_3": data.Exp_3,
                "start_date_3": data.start_date_3,
                "end_date_3": data.end_date_3,
                "Job_Duties_3": data.Job_Duties_3,
                "pgheader" : "Your Personalized Resume",
                "app_version": settings.VER_RESUMEWEB

            }
        return context





# ******************************************************************************
class ResumeFormEditView(LoginRequiredMixin, FormView):
    template_name = TEMPLATE_DIR + "resume_edit_form.html"
    form_class = ResumeTypeForm
    template_success = TEMPLATE_DIR + "resume_form_view.html"
    success_url = 'resume-form-submission-confirm'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        subject = "Resume Information Updated Successfully" + gen_num_for_email()
        email_body = "entered your latest resume information"   
        time = datetime.datetime.now()     
        send_email_customized(self.request.user,subject,email_body,time)
        return super(ResumeFormEditView, self).form_valid(form)




# ******************************************************************************
class ResumeFormConfirm(LoginRequiredMixin, TemplateView):
    template_name = TEMPLATE_DIR + "confirm.html"




# ******************************************************************************
class ResumeFormTips(LoginRequiredMixin, TemplateView):
    template_name = TEMPLATE_DIR + "resume_form_tips.html"



