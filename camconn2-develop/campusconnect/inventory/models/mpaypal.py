#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from zzz_lib.zzz_log import zzz_print
from django.db import models
from paypalcheckoutsdk.orders import OrdersCreateRequest, OrdersCaptureRequest
from paypalcheckoutsdk.payments import CapturesGetRequest, CapturesRefundRequest
from paypalcheckoutsdk.core import (
    SandboxEnvironment, 
    PayPalHttpClient,
    PayPalEnvironment, 
    LiveEnvironment
)
from paypalhttp.http_error import HttpError
from pprint import pprint
from django.conf import settings

CONST_MPAYPAL_CLIENT_ID     = os.environ.get('PAYPAL_CLIENT_ID')
CONST_MPAYPAL_SECRET_ID     = os.environ.get('PAYPAL_SECRET_ID')
print("Paypal Environment triggered from settings ->>>{}".format(settings.PAYPAL_CLIENT_ENV))

def get_paypal_env():
    if os.environ.get("SERVER_TYPE") == "production":
        environment = LiveEnvironment(client_id=CONST_MPAYPAL_CLIENT_ID, client_secret=CONST_MPAYPAL_SECRET_ID)
    else:
        environment = SandboxEnvironment(client_id=CONST_MPAYPAL_CLIENT_ID, client_secret=CONST_MPAYPAL_SECRET_ID)

    print("Paypal Environment triggered from mpaypal ->>>{}".format(environment))
    return PayPalHttpClient(environment)


# For Testing purpose
# environment = LiveEnvironment(client_id=CONST_MPAYPAL_CLIENT_ID, client_secret=CONST_MPAYPAL_SECRET_ID)    


# ******************************************************************************
class mpaypal_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def mpaypal_add(self, order_label):
        instance = self.create(order_label=order_label)
        return instance


# *****************************************************************************
class mpaypal(models.Model):
    objects                 = mpaypal_instancemanager()
    order_label             = models.CharField(max_length=100)
    response_data_json      = models.JSONField(blank=True, null=True)
    client                  = get_paypal_env()
    clientexecutionfailed   = False
    __response_data         = None

    # --------------------------------------------------------------------------
    def save(self, *args, **kwargs):
        if self.__response_data:
            zzz_print("    %-28s: %s" % ("mpaypal", "save"))
            # Don't have to encode json to store it in JSONField
            # self.response_data_json = json.dumps(self.__response_data)
            self.response_data_json = self.__response_data
        super().save(*args, **kwargs)

    # --------------------------------------------------------------------------
    def extract_capture_id_from_captured_order_data(self):
        # zzz_print("    %-28s: %s" % ("extract_capture_id_from_captured_order_data()", ""))
        capture_id = "INVALID_ID"

        if self.__response_data is None:
            zzz_print("self.__response_data is None")
            zzz_print("    %-28s: %s" % ("self.__response_data['purchase_units']", type(self.__response_data)))
        else:
            # EXAMPLE OF self.__response_data['purchase_units']
            # EXAMPLE OF self.__response_data['purchase_units']
            # [{'payments': {'captures': [{'amount': {'currency_code': 'USD',
            #                                         'value': '2.00'},
            #                              'create_time': '2021-06-06T13:01:30Z',
            #                              'final_capture': True,
            #                              'id': '0C5201334U0561514',
            #                              'links': [{'href': 'https://api.sandbox.paypal.com/v2/payments/captures/0C5201334U0561514',
            #                                         'method': 'GET',
            #                                         'rel': 'self'},
            #                                        {'href': 'https://api.sandbox.paypal.com/v2/payments/captures/0C5201334U0561514/refund',
            #                                         'method': 'POST',
            #                                         'rel': 'refund'},
            #                                        {'href': 'https://api.sandbox.paypal.com/v2/checkout/orders/0NG02099W5591232B',
            #                                         'method': 'GET',
            #                                         'rel': 'up'}],
            #                              'seller_protection': {'dispute_categories': ['ITEM_NOT_RECEIVED',
            #                                                                           'UNAUTHORIZED_TRANSACTION'],
            #                                                    'status': 'ELIGIBLE'},
            #                              'seller_receivable_breakdown': {'gross_amount': {'currency_code': 'USD',
            #                                                                               'value': '2.00'},
            #                                                              'net_amount': {'currency_code': 'USD',
            #                                                                             'value': '1.64'},
            #                                                              'paypal_fee': {'currency_code': 'USD',
            #                                                                             'value': '0.36'}},
            #                              'status': 'COMPLETED',
            #                              'update_time': '2021-06-06T13:01:30Z'}]},
            #   'reference_id': 'default',
            #   'shipping': {'address': {'address_line_1': '1 Main St',
            #                            'admin_area_1': 'CA',
            #                            'admin_area_2': 'San Jose',
            #                            'country_code': 'US',
            #                            'postal_code': '95131'},
            #                'name': {'full_name': 'John Doe'}}}]

            zzz_print("    %-28s: %s" % ("self.__response_data['purchase_units']", len(self.__response_data['purchase_units'])))
            capture_dict = self.__response_data['purchase_units'][0]

            # testing access to proper place in dict structure
            # zzz_print("    %-28s: %s" % ("capture_dict['reference_id']", capture_dict['reference_id']))

            payments_captures = capture_dict['payments']['captures']

            if len(payments_captures) != 1:
                zzz_print("    %-28s: %s" % ("len(payments_captures)", len(payments_captures)))
            else:
                capture = payments_captures[0]
                capture_id = capture['id']
        return capture_id

    # --------------------------------------------------------------------------
    def get_response_data(self):
        return self.__response_data

    # --------------------------------------------------------------------------
    def generateOrderJson(self, cart_context):
        order_json = {
            "intent": "CAPTURE",
            'purchase_units': [{
                'amount': {
                    "currency_code": "USD",
                    'value': str(cart_context['total_cost'])
                }
            }]
        }
        zzz_print("    %-28s: %s" % ("generateOrderJson", order_json))
        return order_json

    # --------------------------------------------------------------------------
    def generateRefundOrderJson(self, cart_context):
        order_json = {
            'amount': {
                'value': str(cart_context['total_cost']),
                "currency_code": "USD",
            }
        }
        zzz_print("    %-28s: %s" % ("generateRefundOrderJson", order_json))
        return order_json

    # --------------------------------------------------------------------------
    def executeClientOrder(self, client, order_request):
        zzz_print("    %-28s: %s" % ("executeClientOrder()", self.order_label))
        try:
            response = client.execute(order_request)
        except HttpError as e:
            zzz_print("    %-28s: %s" % ("MMH: NEED TO HANDLE ERRORS BETTER HERE ", "MMH: NEED TO HANDLE ERRORS BETTER HERE "))
            zzz_print("    %-28s: %s" % ("MMH: NEED TO HANDLE ERRORS BETTER HERE ", "MMH: NEED TO HANDLE ERRORS BETTER HERE "))
            zzz_print("    %-28s: %s" % ("MMH: NEED TO HANDLE ERRORS BETTER HERE ", "MMH: NEED TO HANDLE ERRORS BETTER HERE "))
            zzz_print("    %-28s: %s" % ("MMH: NEED TO HANDLE ERRORS BETTER HERE ", "MMH: NEED TO HANDLE ERRORS BETTER HERE "))
            zzz_print("    %-28s: %s" % ("MMH: NEED TO HANDLE ERRORS BETTER HERE ", "MMH: NEED TO HANDLE ERRORS BETTER HERE "))
            zzz_print("    %-28s: %s" % ("e.message", ""))
            pprint(e.message)
            self.clientexecutionfailed = True


            # MMH: NEED TO HANDLE ERRORS BETTER HERE
            # MMH: NEED TO HANDLE ERRORS BETTER HERE
            # MMH: NEED TO HANDLE ERRORS BETTER HERE
            # MMH: NEED TO HANDLE ERRORS BETTER HERE


            # ('{"name":"UNPROCESSABLE_ENTITY","message":"The requested action could not be '
            #  'performed, semantically incorrect, or failed business '
            #  'validation.","debug_id":"836d396acb6d7","details":[{"issue":"CAPTURE_FULLY_REFUNDED","description":"The '
            #  'capture has already been fully '
            #  'refunded"}],"links":[{"href":"https://developer.paypal.com/docs/api/payments/v2/#error-CAPTURE_FULLY_REFUNDED","rel":"information_link"}]}')



            # # {
            # #     "name":"INVALID_REQUEST",
            # #     "message":"Request is not well-formed, syntactically incorrect, or violates schema.",
            # #     "debug_id":"41d2bc02bd2cb",
            # #     "details":[
            # #         {
            # #             "field":"/intent",
            # #             "value":"",
            # #             "location":"body",
            # #             "issue":"MISSING_REQUIRED_PARAMETER",
            # #             "description":"A required field / parameter is missing."
            # #         },
            # #         {
            # #             "field":"/purchase_units/0/amount/currency_code","value":"",
            # #             "location":"body",
            # #             "issue":"MISSING_REQUIRED_PARAMETER",
            # #             "description":"A required field / parameter is missing."}
            # #     ],
            # #     "links":[
            # #         {
            # #             "href":"https://developer.paypal.com/docs/api/orders/v2/#error-MISSING_REQUIRED_PARAMETER",
            # #             "rel":"information_link",
            # #             "encType":"application/json"
            # #         }
            # #     ]
            # # }





            zzz_print("    %-28s: %s" % ("e.status_code", e.status_code))         # ex: 400
            # raise RuntimeError("Something bad happened")

        if not self.clientexecutionfailed:
            self.__response_data = response.result.__dict__['_dict']
            self.save()

    # --------------------------------------------------------------------------
    def mpaypal_create_order(self, cart_context):
        zzz_print("    %-28s: %s" % ("mpaypal_create_order()", ""))
        order_request   = OrdersCreateRequest()
        order_request.prefer("return=representation")
        order_json      = self.generateOrderJson(cart_context)
        order_request.request_body(order_json)
        self.executeClientOrder(self.client, order_request)
        # MMH: PERFECT WORLD: perform specific validation tests on data returned for mpaypal_create_order

    # --------------------------------------------------------------------------
    def mpaypal_capture_order(self, order_id):
        zzz_print("    %-28s: %s" % ("mpaypal_capture_order()", ""))
        order_request   = OrdersCaptureRequest(order_id)
        order_request.prefer("return=representation")
        self.executeClientOrder(self.client, order_request)
        # MMH: PERFECT WORLD: perform specific validation tests on data returned for this method

    # --------------------------------------------------------------------------
    def mpaypal_payment_details(self, capture_id):
        zzz_print("    %-28s: %s" % ("mpaypal_payment_details()", ""))
        order_request   = CapturesGetRequest(capture_id)
        # Nope: CapturesGetRequest doesn't have a .prefer field so can't do the following.
        # order_request.prefer("return=representation")
        self.executeClientOrder(self.client, order_request)
        # MMH: PERFECT WORLD: perform specific validation tests on data returned ffor this method

    # --------------------------------------------------------------------------
    def mpaypal_capture_refund(self, capture_id, context):
        zzz_print("    %-28s: %s" % ("mpaypal_capture_refund()", capture_id))
        zzz_print("    %-28s: %s" % ("context['products_list']", context['products_list']))
        zzz_print("    %-28s: %s" % ("context['total_cost']",    context['total_cost']))

        order_request   = CapturesRefundRequest(capture_id)
        order_request.prefer("return=representation")
        order_json      = self.generateRefundOrderJson(context)
        zzz_print("    %-28s: %s" % ("order_json", order_json))
        order_request.request_body(order_json)
        self.executeClientOrder(self.client, order_request)
        # MMH: PERFECT WORLD: perform specific validation tests on data returned for mpaypal_capture_refund





