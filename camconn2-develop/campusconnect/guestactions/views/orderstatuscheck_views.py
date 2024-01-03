from datetime import datetime
import psycopg2
import os
from django.db.models import Q
from itertools import chain

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from zzz_lib.zzz_log import zzz_print
from django.http import HttpResponse

from ..forms import OrderStatusCheckForm
from systemops.db_conn import get_db_conn1
from ..myfunctions.fetch_record import (
	fetch_record_buyerinfo,
	fetch_record_orderinfo
)


TEMP_DIR_ACTION = 'guestactions/orderstatuscheck/'


# order status check homepage
##*******************************************
class CheckOrderStatusView(FormView):
	template_name 	= TEMP_DIR_ACTION + "layout.html"
	form_class 		= OrderStatusCheckForm
	success_url 	= reverse_lazy('general_resumeupload_success_url')

	def get(self, request, *arg, **kwargs):
		form_class 						= self.get_form_class()
		form 							= self.get_form(form_class)
		context 						= self.get_context_data(**kwargs)
		context['form_order_search'] 	= form
		context["pg_headline"] 			= "Check Order Status"
		context["resp_time"] 			= "1"

		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST or None)
		if form.is_valid():
			context 	= self.get_context_data(**kwargs)
			tracking_id = form.cleaned_data.get('tracking_id')
			email_add   = form.cleaned_data.get('email_add')

			# check if any buyer exists with this email_add
			buyer_true = fetch_record_buyerinfo(email_add)
			if not buyer_true:
				order_status_latest = 'nobuyerfound'
				context = {
					'posted_info'			: [email_add,tracking_id],
					'order_status_latest' 	: order_status_latest,
					'form_order_search'		: self.form_class(),
					'pg_headline'			: "Check Order Status"
				}
				return render(request=self.request, template_name=self.template_name, context=context)
			else:
				# fetch record with this tracking_id
				order_status_latest = fetch_record_orderinfo(tracking_id)
				if len(order_status_latest) == 0:
					order_status_latest = 'No record found'
					context = {
						'posted_info'			: [email_add,tracking_id],
						'order_status_latest' 	: order_status_latest,
						'form_order_search'		: self.form_class(),
						'pg_headline'			: "Check Order Status"
					}
					return render(request=self.request, template_name=self.template_name, context=context)
				else:
					context = {
						'posted_info'			: [email_add,tracking_id],
						'order_status_latest' 	: order_status_latest,
						'form_order_search'		: self.form_class(),
						'pg_headline'			: "Check Order Status"
					}
					return render(request=self.request, template_name=self.template_name, context=context)

		else:
		    return self.form_invalid(form, **kwargs)

	def form_invalid(self, form, **kwargs):
		return HttpResponse("form_invalid was hit line3111")

