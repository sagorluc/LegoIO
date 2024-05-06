import requests
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from inventory.views.shopcart.rw_cart_views import mmh_CartPurchaseSuccess
import uuid
from inventory.models.mcompleted_purchase import mcompleted_purchase
from inventory.models.mcart import mcart
import os
from inventory.models.mamar_pay import mamar_pay
from general.models.buyer_list import BuyerListGuest
from inventory.views.shopcart.rw_cart_context import cart_context_forUser

global_dict={}

def generate_transaction_id():

    #generate transaction id by uuid module
    transaction_id=uuid.uuid4()

    #generate transaction id by string and random number
    '''character=string.ascii_letters+string.digits
    transaction_id=''.join(random.choice(character) for i in range(20))'''

    #generate transaction id by only random number 
    #transaction_id = f"{int(time.time())}-{random.randint(10000, 99999)}"

    return transaction_id



def initial_payment_amarPay(request):
    
    print(request.POST, 'line 34')
    
    request.session['mmh_guestemailaddress'] = request.user.email
    
    if 'mmh_guestemailaddress' not in request.session or not request.session['mmh_guestemailaddress']:
        return HttpResponse('Empty email in the session.line 37')


    global_dict.update(email=request.session['mmh_guestemailaddress'])
    
    total_price = cart_context_forUser(request)['total_cost']
    tran_id = generate_transaction_id()
    
    url = "https://sandbox.aamarpay.com/index.php"

    payload = {'store_id': 'aamarpaytest',
    'signature_key': 'dbb74894e82415a2f7ff0ec3a97e4183',
    'cus_name': 'Customer Name',
    'cus_email': request.session['mmh_guestemailaddress'],
    'cus_phone': '01870******',
    'amount': total_price,
    'currency': 'BDT',
    'tran_id': tran_id,
    'desc': 'test transaction',
    'success_url': os.environ.get('AMAR_PAY_SUCCESS_URL'),
    'fail_url': 'http://localhost/aamarpay/callback/failed.php',
    'cancel_url': 'http://localhost/aamarpay/callback/cancel.php',
    'type': 'json'}
    files=[]
    headers = {}

    print("Success Url ===================", payload['success_url'])

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print("Payment url------------ " ,response.text)

    data = response.json()
    print("Data ------", data)
    return redirect(data['payment_url'])
    #return redirect(data['payment_url'])

    #return HttpResponse("ok")

# this is success url
@csrf_exempt
def success(request):

    if request.method=='POST' or request.method=='post':
 
        
        if 'email' not in global_dict or not global_dict['email']:
            return HttpResponse('email not in the global dictionay. line 82')
        
        # email_from_session=request.session['mmh_guestemailaddress']
        # email_from_session="arifulhaque2010@yahoo.com"
        # print("Email from session  ---------------------", email_from_session)
        #getting json data from amar pay
        #convert json data to dictionary and save amar pay model
        payment_data=request.POST
        print("Payment data==========================",payment_data)

        convertedPaymentData=payment_data.dict()
        print(convertedPaymentData, 'line 94')
        save_payment_data= mamar_pay.objects.create(customer_email=global_dict['email'],
                amarpay_payment_data=convertedPaymentData)
        print(save_payment_data, 'line 97')
        save_payment_data.save()

        #Capturing transaction id
        transaction_id=payment_data['mer_txnid']

        print("transaction_id--------", transaction_id)

        paypaltransaction_id=transaction_id

        #Taking guest email from global_dict
        #Save  guest_email to BuyerListGuest model
        guest_login_email_address=global_dict['email']

        guest_email=BuyerListGuest.objects.create(email=guest_login_email_address,transaction_id=paypaltransaction_id)
        guest_email.save()

        mcomplete_purchased = mcompleted_purchase(
        paypaltransaction_id=paypaltransaction_id,
        email_address=guest_login_email_address,)
        mcomplete_purchased.save()

        cart_items= mcart.objects.filter(purchased=False)
        for items in cart_items:
            items.purchased=True
            items.save()

        return mmh_CartPurchaseSuccess(request,paypaltransaction_id)



