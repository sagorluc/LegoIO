from guestactions.models import mcoupon, mcoupon_given
from zzz_lib.zzz_log import zzz_print
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import requests

import logging
logger = logging.getLogger(__name__)


def generate_coupon_code():
    # Find best active mcoupon instance for product liked
    imcoupon = mcoupon.objects.filter(active=True).order_by('-discount_percent').first()

    if settings.DEBUG:
        print('value of imcoupon>>>{}'.format(imcoupon))
        logger.warning("line20>>>'value of imcoupon>>>{}'".format(imcoupon))

    if not imcoupon:
        zzz_print("   %s " % ("ACTIVE MCOUPON NOT FOUND"))
        return None
    else:
        # zzz_print("   %s " % ("ACTIVE MCOUPON FOUND"))

        # generate a coupon code
        imcoupon_given = mcoupon_given.objects.mcoupon_given_add(request=requests, mcoupon=imcoupon)
        
        context = {
            'discount_percent'      :imcoupon.discount_percent,
            'hours_to_expire'       :imcoupon.hours_to_expire,
            'coupon_code'           :imcoupon_given.random_string_32,
        }

    return context
