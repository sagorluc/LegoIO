from zzz_lib.zzz_log import zzz_print, zzz_print_exit
import datetime
import copy
from decimal import Decimal
from pprint import pprint
import os
from guestactions.myfunctions import for_now_check_order_status
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
from resumeweb.models import mcart, mprod_exp180
from resumeweb.views.rw_cart_context import (
    cart_context_forQuerySet, 
    cart_context_forTrackingId, 
    cart_context_loggit
)

from resumeweb.views.vusergroup import test_is_default_group

from mymailroom.myfunctions import send_email_customized
from resumeweb.models import mcart_fileupload
from prof_candidate.models import OrderCancellationRequest

# from io import BytesIO
# from xhtml2pdf import pisa


TEMPLATE_DIR = "prof_candidate/layout/my_orders/"
APP_VERSION = os.environ.get("VER_RESUMEWEB")

# ******************************************************************************
@user_passes_test(test_is_default_group, login_url=reverse_lazy("vug_failed_test", kwargs={'testname': "test_is_default_group", 'viewname': "OrderHistoryAll"}))
def OrderHistoryAll(request):
    zzz_print("    %-28s: %s" % ("OrderHistoryAll", "********************"))
    template = loader.get_template(TEMPLATE_DIR + "order_history.html")
    qs = mcart.objects.mcartInstance_userOrderHistory_all(
        request).order_by('-created')
    # zzz_print("    %-28s: %s" % ("qs.count()", qs.count()))
    context = {
        "no_of_orders": qs.count(),
        "object_list": qs,
        "section_header_1": "My Order History",
    }
    return HttpResponse(template.render(context, request))


# ******************************************************************************
@user_passes_test(test_is_default_group, login_url=reverse_lazy("vug_failed_test", kwargs={'testname': "test_is_default_group", 'viewname': "OrderDetails"}))
def OrderDetails(request, tracking_id):
    zzz_print("    %-28s: %s" % ("OrderDetails", tracking_id))

    cart_context = cart_context_forTrackingId(request, tracking_id)
    cart_context_loggit(cart_context)

    mcart_instance = cart_context['products_list'][0]['mcart']

    serviceoption_total = 0
    for serviceoption in cart_context['products_list'][0]['mcart_serviceoptions']:
        serviceoption_total += serviceoption.price
    zzz_print("    %-28s: %s" % ("serviceoption_total", serviceoption_total))

    resume_uploaded = ""
    if cart_context['resume_required']:
        imcart_fileupload = mcart_fileupload.objects.get(
            mcompleted_purchase=mcart_instance.mcompleted_purchase
        )
        resume_uploaded = imcart_fileupload.document

    mcart_delivery_total = 0
    if len(cart_context['products_list'][0]['mcart_deliveryoptions']):
        mcart_delivery_total = cart_context['products_list'][0]['mcart_deliveryoptions'][0]
    
    order_cancelation_id = None
    order_cancelation_q = OrderCancellationRequest.objects.filter(created_for=mcart_instance.tracking_id)
    if order_cancelation_q.exists():
        order_cancelation_id = order_cancelation_q.first().submission_conf_id

    ##########################  Check Order Status
    user_email = request.user.email
    order_data = for_now_check_order_status(str(user_email), str(tracking_id))

    order_processing_status = None
    order_is_purchased = None

    m_order = mcart.objects.mcartInstance_userOrderHistory_byTrackingId(request, tracking_id)
    if m_order.exists():
        order_processing_status = m_order.first().processing_status
        order_is_purchased = m_order.first().purchased

    order_status = f"Your order status: {order_processing_status}"
    if order_is_purchased and order_data:
        if order_data[0]["is_reviewed"]:
            order_status = "Your product is being reviewed!"
        elif order_status[0]["is_delivered"]:
            order_status = "Your order is delivered!"
        else:
            order_status = f"Your order status is {order_processing_status}"
    print(f"t_i: {tracking_id}, status:{order_status}")
    ###################################################

    context = {
        "mcart_instance": mcart_instance,
        "mcart_item_totalcost": cart_context['products_list'][0]['item_totalcost'],
        "mcart_serviceoptions": cart_context['products_list'][0]['mcart_serviceoptions'],
        "mcart_serviceoption_total": serviceoption_total,
        "mcart_delivery_total" :mcart_delivery_total,
        'resume_uploaded1': resume_uploaded,
        'section_header_1': "Order Details",
        "order_cancelation_id": order_cancelation_id,
        "app_version": APP_VERSION,
        "order_status": order_status
       
    }
    template = loader.get_template(TEMPLATE_DIR + "order_details.html")
    return HttpResponse(template.render(context, request))


# ******************************************************************************
# def DownloadMyResume(request):
#     # filename = 'JRW-for-Python-Developer-(003).docx'
#     filepath = '/Users/zoti01011989/ZotisDrive/media/resume-cart/' + filename
#     # print('SLA FILE: ', filepath)
#     if os.path.exists(filepath):
#         with open(filepath, 'rb') as worddoc: # read as binary
#             content = worddoc.read() # Read the file
#             response = HttpResponse(
#                 content,
#                 content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
#             )
#             response['Content-Disposition'] = 'attachment; filename=download_filename.docx'
#             response['Content-Length'] = len(content) #calculate length of content
#             return response
#     else:
#         return HttpResponse("Failed to Download SLA")



import boto3
from django.http import HttpResponse

# ******************************************************************************
def resume_download_view(request, bucket_name, object_name):
    # Set the AWS credentials
    ACCESS_KEY  = os.environ.get('AWS_ACCESS_KEY_ID')
    SECRET_KEY  = os.environ.get('AWS_SECRET_ACCESS_KEY')

    bucket_name = os.environ.get('AWS_S3_MASTER_BUCKET_NAME')
    folder_name = os.environ.get('AWS_S3_MCART_RESUME_FOLDER')

    # Connect to S3
    # s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    # # Download the file from S3 bucket to local memory
    # response = s3.get_object(Bucket=bucket_name, Key=object_name)
    # print(bucket_name)
    # print(folder_name)
    # print(object_name)
    # file_object = s3.get_object(Bucket=bucket_name, Key=folder_name + '/' + object_name)
    # # Extract the file content from the response
    # file_content = response['Body'].read()
    # # Create a Django response with the file content
    # response = HttpResponse(file_content, content_type='application/octet-stream')
    # response['Content-Disposition'] = f'attachment; filename="{object_name}"'

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(bucket_name)
    objects = my_bucket.objects.filter(Prefix='resume-cart-249/')
    for obj in objects:
        path, filename = os.path.split(obj.key)
        my_bucket.download_file(obj.key, filename)


    return HttpResponse("Download successful")



import boto3
from django.http import HttpResponse

def download_file(request):
    # Replace 'my-bucket' with your actual bucket name
    s3 = boto3.resource('s3')
    bucket_name = os.environ.get('AWS_S3_MASTER_BUCKET_NAME')
    # Replace 'my-folder' with the folder path you want to download from
    folder_path = os.environ.get('AWS_S3_MCART_RESUME_FOLDER')+'/'
    # Construct the S3 object key by combining the folder path and file name
    file_name = 'd887077a-125f-4e76-9516-e700d3343a9e_2023-04-16_192856.7501070000_demo.docx'
    s3_object_key = folder_path + file_name

    try:
        # Get the S3 object and its contents
        s3_object = s3.Object(bucket_name, s3_object_key)
        response = HttpResponse(s3_object.get()['Body'].read())
        # Set the content type based on the file extension
        if file_name.endswith('.pdf'):
            response['Content-Type'] = 'application/pdf'
        elif file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
            response['Content-Type'] = 'image/jpeg'
        else:
            response['Content-Type'] = 'application/octet-stream'
        # Set the content disposition to attachment to force download
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    except Exception as e:
        response = HttpResponse(str(e), status=400)

    return response
