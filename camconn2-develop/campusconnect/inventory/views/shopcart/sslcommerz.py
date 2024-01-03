import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from inventory.models.mcart import mcart
from inventory.models.mssl_commerz import mssl_commerz
from inventory.views.shopcart.rw_cart_context import cart_context_forUser
from general.models.buyer_list import BuyerListGuest
from django.urls import reverse
import hashlib
import time 
import random
import string
import uuid
# from inventory.send_email_v2 import send_email
# from inventory.send_email_v3 import send_email
import datetime
from inventory.views.shopcart.rw_cart_views import mmh_CartPurchaseSuccess
from inventory.models.mcompleted_purchase import mcompleted_purchase
import os

#capturing guest email from session
global_dict={}

# generate random transaction id for different user 
def generate_transaction_id():

    #generate transaction id by uuid module
    transaction_id=uuid.uuid4()

    #generate transaction id by string and random number
    '''character=string.ascii_letters+string.digits
    transaction_id=''.join(random.choice(character) for i in range(20))'''

    #generate transaction id by only random number 
    #transaction_id = f"{int(time.time())}-{random.randint(10000, 99999)}"

    return transaction_id

#@csrf_exempt
def initiate_payment(request):

    # store id and store password from sslcommerz and sandbox is true
    store_id = os.environ.get('STORE_ID')
    store_password = os.environ.get('STORE_PASSWORD')
    sandbox_mode = os.environ.get('SANDBOX_MODE')

    # calling transaction_id function to create individual transaction id for user
    tran_id = generate_transaction_id()
    #print("transaction_id = ",transaction_id)

    #get total price from cart
    send_total_price=cart_context_forUser(request)['total_cost']
    #print("Total price=",send_total_price)

    # capturing guest email from this function and update global_dict variable
    global_dict.update(email=request.session['mmh_guestemailaddress'])

    # Construct the payment request parameters
    payload = {
        'store_id': store_id,
        'store_passwd': store_password,
        'total_amount': send_total_price,
        'currency': 'BDT',
        'tran_id': tran_id,
        'success_url': os.environ.get('SSL_SUCCESS_URL'),
        'fail_url': os.environ.get('SSL_FAIL_URL'),
        'cancel_url': os.environ.get('SSL_CANCEL_URL'),
        'ipn_url': os.environ.get('SSL_IPN_URL'),
        'cus_name': 'John Doe',
        'cus_email': request.session['mmh_guestemailaddress'], # guest email from session
        
        'cus_phone':'None',
        'cus_add1': 'Dhaka',
        'cus_city': 'Dhaka',
        'cus_country': 'Bangladesh',
        'shipping_method': 'NO',
        'num_of_item': 'None',
        'product_name': 'Test Product',
        'product_category': 'Test Category',
        'product_profile':'general',
    }

    if sandbox_mode:
        payload['sandbox'] = '1'

        #print("Global Dict", global_dict)

    # Make a POST request to initiate the payment
        response = requests.post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php', data=payload)
        print("Response-------------------------",response)
        #print("This is response" ,response)

        # Extract the sessionkey and redirect the user to the payment gateway
        if response.status_code == 200:
            data = response.json()
            print('This is data', data)
            if data['status'] == 'SUCCESS':
                return redirect(data['GatewayPageURL'])
            return HttpResponse('Payment initiation failed 404.')

    # Handle the error case here
    return HttpResponse('Payment initiation failed.')



# This fuction for successful payment
@csrf_exempt
def payment_success(request):

    if request.method=='POST' or request.method=='post':
        #getting json data from sslcommerz
        #convert json data to dictionary and save mssl_commerz model
        payment_data=request.POST
        print("Payment data==========================",payment_data)
        
        convertedPaymentData=payment_data.dict()
        save_payment_data= mssl_commerz.objects.create(customer_email=global_dict['email'],
                ssl_payment_data=convertedPaymentData)
        save_payment_data.save()

        #Capturing transaction id
        paypaltransaction_id=payment_data['tran_id']

        #Taking guest email from global_dict
        #Save  guest_email to BuyerListGuest model
        guest_login_email_address=global_dict['email']
        print("email  ----------------------------------",guest_login_email_address)
        guest_email=BuyerListGuest.objects.create(email=guest_login_email_address,transaction_id=paypaltransaction_id)
        guest_email.save()
        
        #reverse purchas function for clearing cart after successful payment
        #return HttpResponseRedirect(reverse("purchased_complete", kwargs={'tran_id':tran_id},))


        mcomplete_purchased = mcompleted_purchase(
        paypaltransaction_id=paypaltransaction_id,
        email_address=guest_login_email_address,)
        mcomplete_purchased.save()

        cart_items= mcart.objects.filter(purchased=False)
        for items in cart_items:
            items.purchased=True
            items.save()

        return mmh_CartPurchaseSuccess(request,paypaltransaction_id)
        #return HttpResponseRedirect(reverse("purchased_complete", kwargs={'paypaltransaction_id':tran_id},))

        #return HttpResponse('payment successful007')
    else:
        return HttpResponse('payment failed404')
       
        

@csrf_exempt
def payment_fail(request):
    # Handle the payment failure callback here
    return HttpResponse('Payment failed.')

@csrf_exempt
def payment_cancel(request):
    # Handle the payment cancellation callback here
    return HttpResponse('Payment cancelled.')

@csrf_exempt
def ipn_callback(request):
    # Handle the IPN (Instant Payment Notification) callback here
    return HttpResponse('IPN received.')
