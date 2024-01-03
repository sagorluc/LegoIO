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


CONST_MPAYPAL_CLIENT_ID     = os.environ.get('PAYPAL_CLIENT_ID')
CONST_MPAYPAL_SECRET_ID     = os.environ.get('PAYPAL_SECRET_ID')


# ------------------------------------------------------------------------------
# EXAMPLE OF CAPTURED ORDER DATA from ->>> mpaypal_capture_order()
#    when setting: order_request.prefer("return=representation")
#
# {
#     "id": "04G855938N1629536",
#     "links": [{"rel": "self", "href": "https://api.sandbox.paypal.com/v2/checkout/orders/04G855938N1629536", "method": "GET"}],
#     "payer": {"name": {"surname": "Name", "given_name": "Fake"}, "address": {"country_code": "US"}, "payer_id": "E4A4VPZPHB49W", "email_address": "sb-zsic26037323@personal.example.com"},
#     "intent": "CAPTURE",
#     "status": "COMPLETED",
#     "create_time": "2021-07-06T14:31:30Z",
#     "update_time": "2021-07-06T14:33:14Z",
#     "purchase_units": [
#         {
#             "payee": {"merchant_id": "HTX7ME4UECR5A", "email_address": "arifulhaque2010-facilitator@yahoo.com"},
#             "amount": {"value": "15.99", "currency_code": "USD"},
#             "payments": {
#                 "captures": [{
#                     "id": "1EG83155DW1420437",  # mmh: saved as capture id
#                     "links": [{"rel": "self", "href": "https://api.sandbox.paypal.com/v2/payments/captures/1EG83155DW1420437", "method": "GET"}, {"rel": "refund", "href": "https://api.sandbox.paypal.com/v2/payments/captures/1EG83155DW1420437/refund", "method": "POST"}, {"rel": "up", "href": "https://api.sandbox.paypal.com/v2/checkout/orders/04G855938N1629536", "method": "GET"}],
#                     "amount": {"value": "15.99", "currency_code": "USD"},
#                     "status": "COMPLETED",
#                     "create_time": "2021-07-06T14:33:14Z",
#                     "update_time": "2021-07-06T14:33:14Z",
#                     "final_capture": true,
#                     "seller_protection": {"status": "ELIGIBLE", "dispute_categories": ["ITEM_NOT_RECEIVED", "UNAUTHORIZED_TRANSACTION"]},
#                     "seller_receivable_breakdown": {"net_amount": {"value": "15.23", "currency_code": "USD"}, "paypal_fee": {"value": "0.76", "currency_code": "USD"}, "gross_amount": {"value": "15.99", "currency_code": "USD"}}
#                     }]
#                 },
#             "shipping": {"name": {"full_name": "Fake Name"}, "address": {"postal_code": "90210", "admin_area_1": "KS", "admin_area_2": "Bolgna", "country_code": "US", "address_line_1": "1 Mainstreet"}},
#             "reference_id": "default",
#             "soft_descriptor": "PAYPAL *TESTACCOUNT"
#         }
#     ]
# }
# ------------------------------------------------------------------------------
