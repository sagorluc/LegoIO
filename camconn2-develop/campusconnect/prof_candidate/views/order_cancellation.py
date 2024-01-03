from zzz_lib.zzz_log import zzz_print, zzz_print_exit
import datetime
import copy
from decimal import Decimal
from pprint import pprint
import os
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template.loader import render_to_string, get_template
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView  # , UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from resumeweb.models import mcart
from resumeweb.models import mcompleted_refund, form_mcompleted_refund
from resumeweb.models import mpaypal

from resumeweb.views.rw_cart_context import (
    cart_context_forQuerySet, 
    cart_context_forTrackingId, 
    cart_context_loggit
)
from ..models import OrderCancellationRequest, CandidateInternalMsg
from resumeweb.views.vusergroup import test_is_default_group

from mymailroom.myfunctions import send_email_customized
from ..forms import OrderCancellationRequestForm
TEMPLATE_DIR = "prof_candidate/layout/order_cancellation/"
APP_VERSION = os.environ.get("VER_RESUMEWEB")

from guestactions.myfunctions import gen_num_for_email
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
# ******************************************************************************
class OrderCancellationRequestView(LoginRequiredMixin, CreateView):
    template_name   = TEMPLATE_DIR + 'submit_request.html'
    form_class      = OrderCancellationRequestForm
    model           = OrderCancellationRequest
    success_url     = reverse_lazy('prof_candidate:order_history_all')  

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.created_at = datetime.datetime.now()
        self.object.created_for = self.kwargs.get('tracking_id')
        self.object.submitted_by = self.request.user.email

        qs = mcart.objects.mcartInstance_userOrderHistory_byTrackingId(self.request, tracking_id=self.object.created_for)
        zzz_print("    %-28s: %s" % ("qs.count()", qs.count()))

        mcart_instance = qs[0]
        mcart_instance.processing_status = "cancelled"
        mcart_instance.save()

        # super(OrderCancellationRequestView, self).form_valid(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderCancellationRequestView, self).get_context_data(**kwargs)
        context['header_text'] = "Order Cancellation Form"
        # get relevant order details
        # context['qs'] = mcart.objects.mcartInstance_userOrderHistory_byTrackingId(id=kwargs['tracking_id'])
        context['tracking_id'] = self.kwargs.get('tracking_id')
        context['app_version'] = APP_VERSION
        return context


# ******************************************************************************
class CancellationDetailsView(LoginRequiredMixin, DetailView):
    template_name   = TEMPLATE_DIR + 'details.html'
    model           = OrderCancellationRequest

    def get_object(self, queryset=None):
        # return MyModel.objects.get(pk=self.kwargs['pk'])
        return OrderCancellationRequest.objects.filter(created_for=self.kwargs['tracking_id'])

    def get_context_data(self, **kwargs):
        context = super(CancellationDetailsView, self).get_context_data(**kwargs)

        # get relevant order details
        # qs = OrderCancellationRequest.objects.filter(created_for=self.kwargs.get('tracking_id'))
        # context['qs'] = qs

        context['section_header_1'] = "Order Cancellation Information"
        context['app_version'] = APP_VERSION
        return context



### ******************************************************************************
# class CancellationDetailsView(LoginRequiredMixin, DetailView):
#     template_name   = TEMPLATE_DIR + 'details.html'
#     model           = OrderCancellationRequest

#     def get_context_data(self, **kwargs):
#         context = super(CancellationDetailsView, self).get_context_data(**kwargs)

#         # get relevant order details
#         qs = OrderCancellationRequest.objects.filter(created_for=self.kwargs.get('tracking_id'))
#         context['qs'] = qs

#         context['header_text'] = "Order Cancellation Message"
#         context['app_version'] = APP_VERSION
#         return context


# ******************************************************************************
class OrderCancellationConfirmationView(LoginRequiredMixin, DetailView):
    template_name   = TEMPLATE_DIR + 'confirmation.html'
    model           = OrderCancellationRequest

    def get_context_data(self, **kwargs):
        context = super(OrderCancellationConfirmationView, self).get_context_data(**kwargs)
        context['header_text'] = "Order Cancellation Message"
        # get relevant order details
        qs = OrderCancellationRequest.objects.filter(created_for=self.kwargs.get('tracking_id'))
        context['qs'] = qs
        context['app_version'] = APP_VERSION
        return context



# ******************************************************************************
@user_passes_test(test_is_default_group, login_url=reverse_lazy("vug_failed_test", kwargs={'testname': "test_is_default_group", 'viewname': "CancelOrder_mmh"}))
def CancelOrder_mmh(request, tracking_id):
    zzz_print("    %-28s: %s" % ("CancelOrder_mmh", tracking_id))

    qs = mcart.objects.mcartInstance_userOrderHistory_byTrackingId(request, tracking_id)
    zzz_print("    %-28s: %s" % ("qs.count()", qs.count()))

    # FATAL ERROR:
    # MMH: CHANGE THIS TO CAPTURING ERROR MESSAGE AND REDIRECTING TO AN ERROR VIEW PAGE WHERE THIS MESSAGE IS DISPLAYED AND LOGGED
    if qs.count() != 1:
        zzz_print_exit("    %-28s: %s" % ("qs.count() != 1", qs.count()))

    mcart_instance = qs[0]

    # FATAL ERROR:
    # MMH: CHANGE THIS TO CAPTURING ERROR MESSAGE AND REDIRECTING TO AN ERROR VIEW PAGE WHERE THIS MESSAGE IS DISPLAYED AND LOGGED
    if mcart_instance.grace_left_in_seconds() < 1:
        zzz_print_exit("    %-28s: %s" % ("grace_left_in_seconds < 1",
                       mcart_instance.grace_left_in_seconds()))

    # FATAL ERROR:
    # MMH: CHANGE THIS TO CAPTURING ERROR MESSAGE AND REDIRECTING TO AN ERROR VIEW PAGE WHERE THIS MESSAGE IS DISPLAYED AND LOGGED
    if mcart_instance.processing_status == "delivered":
        zzz_print_exit("    %-28s: %s" % ("mcart_instance.processing_status",
                       mcart_instance.processing_status))
    if mcart_instance.processing_status == "cancelled":
        zzz_print_exit("    %-28s: %s" % ("mcart_instance.processing_status",
                       mcart_instance.processing_status))
    if mcart_instance.processing_status == "error":
        zzz_print_exit("    %-28s: %s" % ("mcart_instance.processing_status",
                       mcart_instance.processing_status))

    zzz_print("    %-28s: %s" % ("request.method", request.method))
    if request.method == 'POST':
        form = form_mcompleted_refund(request.POST, request.FILES)
        if form.is_valid():
            reason = form.cleaned_data.get('reason')
            explanation = form.cleaned_data.get('explanation')
            zzz_print("    %-28s: %s" % ("reason", reason))
            zzz_print("    %-28s: %s" % ("explanation", explanation))

            capture_id = mcart_instance.mcompleted_purchase.capture_id
            zzz_print("    %-28s: %s" % ("capture_id", capture_id))

            if not capture_id:
                zzz_print("    %-28s: %s" % ("CAPTURE_ID",
                          "NOT SET. ARE YOU USING OLD PURCHASES???"))
                zzz_print("    %-28s: %s" % ("CAPTURE_ID",
                          "NOT SET. ARE YOU USING OLD PURCHASES???"))
                zzz_print("    %-28s: %s" % ("CAPTURE_ID",
                          "NOT SET. ARE YOU USING OLD PURCHASES???"))
                zzz_print("    %-28s: %s" % ("CAPTURE_ID",
                          "NOT SET. ARE YOU USING OLD PURCHASES???"))
                zzz_print_exit("    %-28s: %s" % ("CAPTURE_ID",
                               "NOT SET. ARE YOU USING OLD PURCHASES???"))

            mcart_qs = mcart.objects.filter(id=mcart_instance.id)
            zzz_print("    %-28s: %s" % ("mcart_qs.count()", mcart_qs.count()))

            cart_context = cart_context_forQuerySet(request, mcart_qs)

            ipaypal = mpaypal.objects.mpaypal_add("mpaypal_capture_refund")
            ipaypal.mpaypal_capture_refund(capture_id, cart_context)
            data = ipaypal.get_response_data()

            # zzz_print("    %-28s: %s" % ("data", "-----------------------------"))
            # pprint(data)
            # zzz_print("    %-28s: %s" % ("data", "-----------------------------"))

            # EXAMPLE OF DATA
            # {'amount': {'currency_code': 'USD', 'value': '2.00'},
            #  'create_time': '2021-06-07T10:20:06-07:00',
            #  'id': '6R6981378Y194730V',
            #  'links': [{'href': 'https://api.sandbox.paypal.com/v2/payments/refunds/6R6981378Y194730V',
            #             'method': 'GET',
            #             'rel': 'self'},
            #            {'href': 'https://api.sandbox.paypal.com/v2/payments/captures/1BK406470M5627505',
            #             'method': 'GET',
            #             'rel': 'up'}],
            #  'seller_payable_breakdown': {'gross_amount': {'currency_code': 'USD',
            #                                                'value': '2.00'},
            #                               'net_amount': {'currency_code': 'USD',
            #                                              'value': '1.94'},
            #                               'paypal_fee': {'currency_code': 'USD',
            #                                              'value': '0.06'},
            #                               'total_refunded_amount': {'currency_code': 'USD',
            #                                                         'value': '2.00'}},
            #  'status': 'COMPLETED',
            #  'update_time': '2021-06-07T10:20:06-07:00'}

            to_emails_list = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS)
            if request.user.is_authenticated:
                to_emails_list.append(request.user.email)
            elif 'mmh_guestemailaddress' in request.session:
                to_emails_list.append(request.session['mmh_guestemailaddress'])
            elif mcart_instance.mcompleted_purchase.guest_login_email_address:
                to_emails_list.append(
                    mcart_instance.mcompleted_purchase.guest_login_email_address)
            else:
                zzz_print("    %-28s: %s" % ("WARNING", "(NOT request.user.is_authenticated) AND (mmh_guestemailaddress NOT in request.session) and (NOT IN mcart_instance.mcompleted_purchase.guest_login_email_address)"))

            if data and data['status'] == 'COMPLETED':
                # zzz_print("    %-28s: %s" % ("refund data['id']", data['id']))
                mcart_instance.set_processing_status_cancelled()

                # create mcompleted_refund instance
                icompleted_refund = mcompleted_refund.objects.add_mcompleted_refund(
                    paypalrefund_id=data['id'],
                    amount_currencycode=data['amount']['currency_code'],
                    amount_value=Decimal(data['amount']['value']),
                    reason=reason,
                    explanation=explanation
                )

                
                # and update mcart_instance foreign key for this new mcompleted_refund instance
                mcart_instance.mcompleted_refund = icompleted_refund
                mcart_instance.save()

                # SEND AN EMAIL CONFIRMING REFUND APPROVED.
                plain_message_text = "About the cancellation: \n" + os.linesep
                # plain_message_text  += "date: "+ str(datetime.datetime.now())+"\n"
                plain_message_text += "Amount: $" + \
                    data['amount']['value'] + "\n" + os.linesep
                plain_message_text += "PayPal Refund Reference Id: " + \
                    data['id']+"\n" + os.linesep
                plain_message_text += "About the original order: " + \
                    mcart_instance.title + "." + os.linesep
                change_notice = plain_message_text

                
                # imsendmail = msendmail.objects.add(
                #     subject             = request.user.first_name + ", a refund was processed",
                #     plain_message       = plain_message_text,
                #     html_message        = html_message_text,
                #     from_email          = settings.EMAIL_HOST_USER,
                #     to_emails_list      = to_emails_list
                # )
                # imsendmail.send_to_each_recipient_seperately()
                email_address = request.user.email
                subject = "Order cancelled successfully" + gen_num_for_email()
                time = datetime.datetime.now()
                send_email_customized(email_address, subject, change_notice, time)

                return HttpResponseRedirect(
                    reverse('prof_candidate:mmh_cancel_order_success', kwargs={
                            'tracking_id': mcart_instance.tracking_id})
                )
            else:  # refund failed
                mcart_instance.set_processing_status_error()

                # SEND AN EMAIL INDICATING REFUND FAILED
                plain_message_text = "A refund of " + \
                    data['amount']['value'] + " was NOT, REPEAT NOT, successfully processed for the cancellation of " + \
                    mcart_instance.title + "."
                plain_message_text += " PayPal Refund Reference Id = " + \
                    data['id'] + "."
                plain_message_text += " This email text and its html version need work."
                html_message_text = plain_message_text
                # imsendmail = msendmail.objects.add(
                #     subject=request.user.first_name + ", a refund FAILED TO process",
                #     plain_message=plain_message_text,
                #     html_message=html_message_text,
                #     from_email=settings.EMAIL_HOST_USER,
                #     to_emails_list=to_emails_list
                # )
                # imsendmail.send_to_each_recipient_seperately()

                return HttpResponseRedirect(
                    reverse('prof_candidate:mmh_cancel_order_failed', kwargs={
                            'tracking_id': mcart_instance.tracking_id})
                )
        else:
            zzz_print("    %-28s: %s" % ("form.is NOT valid()", ""))
    else:
        form = form_mcompleted_refund()

    context_data = {'form': form}
    form_html = render_to_string(
        template_name = "prof_candidate/pg-contents/order_cancellation/form.html", 
        context=context_data, request=request
    )
    
    template = loader.get_template(TEMPLATE_DIR + "order_cancel.html")
    context = {
        "header_text": "Cancelling Order",
        "object": mcart_instance,
        "form": form_html,
        "app_version" : APP_VERSION
       
    }
    return HttpResponse(template.render(context, request))


# ******************************************************************************
@user_passes_test(test_is_default_group, login_url=reverse_lazy("vug_failed_test", kwargs={'testname': "test_is_default_group", 'viewname': "CancelOrderSuccess_mmh"}))
def CancelOrderSuccess_mmh(request, tracking_id):
    zzz_print("    %-28s: %s" % ("CancelOrderSuccess_mmh", tracking_id))

    qs = mcart.objects.mcartInstance_userOrderHistory_byTrackingId(request, tracking_id)
    zzz_print("    %-28s: %s" % ("qs.count()", qs.count()))
    mcart_instance = qs[0]

    template = loader.get_template(TEMPLATE_DIR + "order_cancel.html")
    context = {
        "header_text": "Order Cancelled",
        "object": mcart_instance,
        "form": "",
        "app_version": APP_VERSION
        
    }
    return HttpResponse(template.render(context, request))

