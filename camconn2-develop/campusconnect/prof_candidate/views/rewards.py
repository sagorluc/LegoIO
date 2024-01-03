from zzz_lib.zzz_log import zzz_print
import json
from uuid import uuid4
from django.shortcuts import render
from base64 import b64decode, b64encode
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import connection
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder

from django.views.generic import (
    ListView,
    UpdateView,
    DetailView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


TEMPLATE_DIR = "prof_candidate/layout/rewards/"



"""
TODO: in this page, you should see a list of current offers


"""
#===============================
class MyCurrentRewardOffers(LoginRequiredMixin, TemplateView):
    template_name = TEMPLATE_DIR + "offers.html"

    def get_context_data(self, **kwargs):
        context = super().__init__(**kwargs)


        context = {
            'pgheader': 'Your Current Offers',

        }


        return context


#===============================
class MyEarnedCoupons(LoginRequiredMixin, TemplateView):
    template_name = TEMPLATE_DIR + "earnings.html"


