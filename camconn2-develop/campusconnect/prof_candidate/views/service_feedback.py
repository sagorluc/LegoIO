# from ..models import OrderFeedback
from ..forms import ServiceFeedbackForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
import os 

TEMPLATE_DIR = "prof_candidate/layout/my_orders/"
APP_VERSION = os.environ.get("VER_RESUMEWEB")

class ServiceFeedbackView(LoginRequiredMixin, CreateView):
    template_name   = TEMPLATE_DIR + 'order-feedback.html'
    form_class      = ServiceFeedbackForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.created_at = datetime.datetime.now()
        self.object.save()
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ServiceFeedbackForm()
        context['pgheader'] = "Order Feedback"
        context['app_version'] = APP_VERSION
        return context
