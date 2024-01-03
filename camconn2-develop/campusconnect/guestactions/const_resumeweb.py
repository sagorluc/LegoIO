#!/usr/bin/env python
# -*- coding: utf-8 -*-

GOLIVE_STATUS = (
    ('active', 'Live'),
    ('draft', 'Draft'),
)

SERVICE_CATEGORY = (
    ('analysis', 'Analysis Service'),
    ('editing', 'Editing Service'),
    ('formatting', 'Formating Service'),
)

TRENDING = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

HOMEPAGE_SHOWUP = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

EXP180LEVEL = (
    ('adhoc_get_started', 'adhoc_get_started'),
    ('others', 'others'),
)

WHY_NEEDED = (
    ('cd01', 'Didnot Find this serv in exp180'),
    ('cd02', 'I donotk now where to search'),
    ('cd03', 'it was time consuming to search for this'),
)

ADHOC_GET_STARTED = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

PROFLEVEL_TYPES = (
    ('intern','intern'),
    ('junior','junior'),
)

PURCHASE_STATUS = (
    ('pending','Pending'),
    ('processing','Processing'),
    ('delivered','Delivered'),
    ('cancelled','Cancelled'),
    ('error','Error'),
)

CANCELLED_ORDER_REASON_CHOICES = (
    ('r01','Reason #1'),
    ('r02','Reason #2'),
    ('r03','Reason #3'),
    ('r04','Reason #4'),
    ('r05','Reason #5'),
    ('r06','Reason #6'),
)


# --------------------------------------------------------------------------
# MMH: I don't use this item.
# However it is being used in campusconnect/resumeweb/models/models_all.py
# In two classes
# CompareServices and FAQ
# TODO: Consider fully removing its use and eliminating this.
# NOTE: THIS IS A TUPLE PROBABLY BECAUSE IT IS BEING USED FOR A CHOICES FIELD
PRODUCT_LINES = (
    ('adhoc',       'mprod_adhoc'),
    ('prei20',      'mprod_prei20'),
    ('intprep',     'mprod_intprep'),
    ('proflevel',   'mprod_proflevel'),
    ('posti20',     'mprod_posti20'),
    ('rolebased',   'mprod_rolebased'),
    ('strategy',    'mprod_strategy'),
    ('visabased',   'mprod_visabased'),
)

# --------------------------------------------------------------------------
MODELNAME_BOOLEAN_DICT_PRODUCTS_THAT_WORK_IN_CART_SYSTEM_RESUME_REQUIRED = {
    'mprod_exp180':     True,
    'mprod_intprep':    True,
    'mprod_proflevel':  True,
    'mprod_posti20':   True,
    'mprod_rolebased':  True,
    'mprod_strategy':   True,
    'mprod_visabased':  True,
}

# --------------------------------------------------------------------------
# FOR PRODUCTS THAT WORK IN THE CART SYSTEM
# MODEL NAME : DISPLAY NAME dict
MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_WORK_IN_CART_SYSTEM = {
    'mprod_exp180':     "Exp180",
    'mprod_intprep':    "Dialogue",
    'mprod_proflevel':  "Staircase",
    'mprod_posti20':    "Dialect",
    'mprod_rolebased':  "Identity",
    'mprod_strategy':   "Strategy",
    'mprod_visabased':  "Bandwidth",
    'mprod_xyz':        "General",
}
# FOR PRODUCTS THAT DO NOT WORK IN THE CART SYSTEM
# MODEL NAME : DISPLAY NAME dict
MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_DO_NOT_WORK_IN_CART_SYSTEM = {
    'mprod_adhoc':      "Adhoc",
    'mprod_referral':    "Referral",
}
# FOR ALL PRODUCTS
# MODEL NAME : DISPLAY NAME dict
# MODELNAME_DISPLAYNAME_DICT_ALL_PRODUCTS = (MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_WORK_IN_CART_SYSTEM + MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_DO_NOT_WORK_IN_CART_SYSTEM)
# MERGE TWO DICTS INTO MODELNAME_DISPLAYNAME_DICT_ALL_PRODUCTS
MODELNAME_DISPLAYNAME_DICT_ALL_PRODUCTS = {**MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_WORK_IN_CART_SYSTEM , **MODELNAME_DISPLAYNAME_DICT_PRODUCTS_THAT_DO_NOT_WORK_IN_CART_SYSTEM}

# --------------------------------------------------------------------------
CATEGORYNAME_DISPLAYNAME_TUPLE_SPECIAL_NOT_RELATED_TO_CART_PRODUCTS = (
    # ('anniversarysale',  'Anniversary Sale'),
)
# ADD DICT AND TUPLE TO CREATE A TUPLE.
# BE SURE TO CONVERT DICT.items() to TUPLE SO REALLY ADDING TWO TUPLES TOGETHER.
CATEGORYNAME_DISPLAYNAME_TUPLE_ALL_COUPONS = (tuple(MODELNAME_DISPLAYNAME_DICT_ALL_PRODUCTS.items()) + CATEGORYNAME_DISPLAYNAME_TUPLE_SPECIAL_NOT_RELATED_TO_CART_PRODUCTS)













