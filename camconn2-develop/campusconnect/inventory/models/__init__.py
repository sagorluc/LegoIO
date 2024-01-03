#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inventory.models.mcart import mcart
from inventory.models import mcart_deliveryoptions
from inventory.models import mcart_serviceoptions

from inventory.models.mcart_fileupload import mcart_fileupload, mcart_uploadpath
#from inventory.models.mcart_serviceoptions import mcart_serviceoptions
from inventory.models.mcompleted_purchase import mcompleted_purchase
from inventory.models.mcompleted_refund import mcompleted_refund, form_mcompleted_refund
#from .mpaypal import mpaypal
from general.models.buyer_list import BuyerListGuest

from mymailroom.models.msendmail import msendmail
from mymailroom.models.msendmail_failure import msendmail_failure

#preI20 Models
from inventory.models.mprod_prei20_catlist import mprod_prei20_catlist
from inventory.models.mprod_prei20 import mprod_prei20
from inventory.models.mprod_prei20_serviceoption import mprod_prei20_serviceoption
from inventory.models.mprod_prei20_deliveryoption import mprod_prei20_deliveryoption

# PostI20 Models 
from .posti20.mprod_posti20 import mprod_posti20
from .posti20.mprod_posti20_catlist import mprod_posti20_catlist
from .posti20.mprod_posti20_deliveryoption import mprod_posti20_deliveryoption
from .posti20.mprod_posti20_serviceoption import mprod_posti20_serviceoption



#Univcom Models
from .univcom.mprod_univcom import mprod_univcom
from .univcom.mprod_univcom_deliveryoption import mprod_univcom_deliveryoption
from.univcom.mprod_univcom_list import mprod_univcom_list
from .univcom.mprod_univcom_serviceoption import mprod_univcom_serviceoption

#Strategy
from .strategy.mprod_strategy import mprod_strategy
from .strategy.mprod_strategy_deliveryoption import mprod_strategy_deliveryoption
from .strategy.mprod_strategy_serviceoption import mprod_strategy_serviceoption
from .strategy.mprod_strategy_taglist import mprod_strategy_taglist

#visa
from inventory.models.visaassist.mprod_visaassist import mprod_visaassist
from inventory.models.visaassist.mprod_visaassist_catlist import mprod_visaassist_catlist
from inventory.models.visaassist.mprod_visaassist_deliveryoption import mprod_visaassist_deliveryoption
from inventory.models.visaassist.mprod_visaassist_serviceoption import mprod_visaassist_serviceoption




from .msku import msku
from .muniqueid import muniqueid, muniqueid_get_users_uniquid

from general.models.mcoupon import mcoupon
from general.models.mcoupon_given import mcoupon_given
from inventory.models.mcart_coupons import mcart_coupons

from inventory.models.mssl_commerz import mssl_commerz
from inventory.models.mamar_pay import mamar_pay
