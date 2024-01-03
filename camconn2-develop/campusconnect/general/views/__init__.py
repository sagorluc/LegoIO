#!/usr/bin/env python
# -*- coding: utf-8 -*-

## cart
from inventory.views.shopcart.rw_cart_views import (
    mmh_CartHome,
    mmh_CartFileUpload,
    # mmh_CartUserLogin,
    mmh_CartGuestLogin,
    mmh_CartLoginPage,
    mmh_CartLoginOrGuestSuccess,
    mmh_CartPurchaseSuccess,
    rwCartAjaxView_contents,
    rwCartAjaxView_carticon,
    rwCartAjaxView_emptycart,
    rwCartAjaxView_removebymodelnameandid,
    rwCartAjaxView_addproductver2,
    rwCartAjaxView_removeproductver2,
    # rwCartAjaxView_applycoupontocart,
    # rwCartAjaxView_unapplycoupontocart,
    # rwCartAjaxView_applycoupon,
)

## payment 
""" from .vpaypal import (
    vcreate,
    vcapture,
)
 """
from .general_views import (
    Covid19ResponseView,
    BLMResponseView,
    PromotionalOffersView,
    Page404View,
    ThisIsBeta,
    UsOnlySupport,
    MemberBenefitsView,

    # about us
    AboutUsView,

    # help center
    HelpCenterHome,
)

from .homepage import HomePageView

from .vusergroup import (
    vug_failed_test,
)
