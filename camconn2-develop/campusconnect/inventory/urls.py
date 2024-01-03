from django.conf.urls import url, include
from django.urls import path
from general.views.homepage import HomePageView

# # *********************************
# # ********** EXCEPTION **********
# # *********************************




site_homepage_url = [    
    path("", HomePageView.as_view(), name="site_homepage_link"), 
    ]

# SITE_HOMEPAGE  = [
#     path("",                 include(site_homepage_url)),
#     ]




# # product
from .urls_inv import (
    #usvisa_urls,
    posti20_url,
    url_list_prei20,
    
    # mmr_eval_urls,
    # identity_url,
    # staircase_urls,
    # strat_sol_urls,
    # adhoc_urls,
    
)
from .urls_inv.strategy import strat_sol_urls
from .urls_inv.visaassist import url_list_visaassist
from .urls_inv.adhoc import adhoc_urls

# # product details
# from inventory.views.vprod_prei20 import (
#     # USVisaProdDetails_ajax,
#     # RoleBasedServiceDetails_ajax,
#     # posti20ServiceProdDetails_ajax,
#     # IntPrepProdDetails_ajax,
#     Prei20DetailView_ajax,
#     # # EvalDetailView_ajax,
#     # ProfLevelServiceDetails_ajax,
#     #StratSolProdDetails_ajax,
# )

from inventory.views.vprod_prei20 import Prei20DetailView_ajax

from inventory.views.vprod_visaassist import VisaassistProdDetails_ajax
from inventory.views.vprod_strategy import StratSolProdDetails_ajax
from inventory.views.vprod_posti20 import PostI20ServiceProdDetails_ajax

# cart
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
    #rwCartAjaxView_applycoupontocart,
    #rwCartAjaxView_unapplycoupontocart,
    #rwCartAjaxView_applycoupon,

)

# # paypal
# from .views import (
#     vcreate,
#     vcapture,
# )

# # user permissions
# from .views import (
#     vug_failed_test,
# )


# sslcommerz
from inventory.views.shopcart.sslcommerz import(
    initiate_payment,
    payment_success,
    #purchased_complete,
    
)




# # products that use cart
all_product_urls = [
    path("prei20/",                     include(url_list_prei20)),          # mprod_prei20
    path("posti20/",                    include(posti20_url)),          # mprod_posti20
    path("visaassist/",                 include(url_list_visaassist)),         # mprod_intprep
    path("strategy/",                   include(strat_sol_urls)),       # mprod_strategy
    path("adhoc/",                      include(adhoc_urls)),          # adhoc

]

# cart urls
mmh_cart_urls = [
    path("cart/home/mmh",                                       mmh_CartHome,                               name="mmh_carthome"),
    path("cart/upload",                                         mmh_CartFileUpload,                         name="mmh_cartfileupload"),
    # path("checkout/sign-in/mmh/userlogin",                      mmh_CartUserLogin,                          name="mmh_cartuserlogin"),
    path("checkout/sign-in/mmh",                                mmh_CartLoginPage,                          name="mmh_cartcheckout"),
    path("checkout/sign-in/mmh/loginorguestsuccess",            mmh_CartLoginOrGuestSuccess,                name="mmh_cartloginorguestsuccess"),
    path("checkout/sign-in/mmh/guestlogin",                     mmh_CartGuestLogin,                         name="mmh_cartguestlogin"),
    path("checkout/success/<str:paypaltransaction_id>",         mmh_CartPurchaseSuccess,                    name="mmh_cartpurchasesuccess"),
]

# # cart AJAX urls
mmh_cart_urls_ajax = [
    path("contents",                                            rwCartAjaxView_contents,                name="rwCartAjaxView_contents"),
    path("carticon",                                            rwCartAjaxView_carticon,                name="rwCartAjaxView_carticon"),
    path("emptycart",                                           rwCartAjaxView_emptycart,               name="rwCartAjaxView_emptycart"),
    path("removebymodelnameandid",                              rwCartAjaxView_removebymodelnameandid,  name="rwCartAjaxView_removebymodelnameandid"),
    path("addproductver2",                                      rwCartAjaxView_addproductver2,          name="rwCartAjaxView_addproductver2"),
    path("removeproductver2",                                   rwCartAjaxView_removeproductver2,       name="rwCartAjaxView_removeproductver2"),
    # path("applycoupontocart/<str:string32>",                    rwCartAjaxView_applycoupontocart,       name="rwCartAjaxView_applycoupontocart"),
    # path("unapplycoupontocart/<str:string32>",                  rwCartAjaxView_unapplycoupontocart,     name="rwCartAjaxView_unapplycoupontocart"),
    # path("applycoupon",                                         rwCartAjaxView_applycoupon,             name="rwCartAjaxView_applycoupon"),
]

# # paypal_urls
# mmh_vpaypal_urls = [
#     path('vcreate', vcreate, name="vpaypal_vcreate"),
#     path('vcapture/<order_id>', vcapture, name="vpaypal_vcapture"),
# ]


#SSLCommerz_url
mmh_vsslcommerz_urls = [
    path('vcreate/', initiate_payment, name="enter_payment_getway"),
    path('payment_success/', payment_success, name='payment_success'),
]
   




# # cart ajax detail product views
mmh_cart_detail_ajax_product_views = [
    path("mprod_prei20/<int:id>",                Prei20DetailView_ajax,              name="prei20_detail_view_link_ajax"),
    path("mprod_visaassist/<int:id>",      VisaassistProdDetails_ajax,            name="visaassist_detail_view_link_ajax"),
    path("mprod_posti20/<int:id>",               PostI20ServiceProdDetails_ajax,    name="posti20_detail_view_link_ajax"),
    # path("mprod_rolebased/<int:id>",    RoleBasedServiceDetails_ajax,       name="rolebased_detail_view_link_ajax"),
    path("mprod_strategy/<int:id>",     StratSolProdDetails_ajax,           name="strategy_detail_view_link_ajax"),
    #fixed
    #path("mprod_visabased/<int:id>",    USVisaProdDetails_ajax,             name="visabased_detail_view_link_ajax"),
]


# # user permissions
# vusergroup_views = [
#     path("failedtest/<str:testname>/<str:viewname>/<str:optionalmessage>",  vug_failed_test,     name="vug_failed_test"),
#     path("failedtest/<str:testname>/<str:viewname>",                        vug_failed_test,     name="vug_failed_test"),
# ]




# ## final url declaration
# ########################
# ## CART + PayPal
MMH_CART       = [path("cart/",            include(mmh_cart_urls)),]
MMH_CART_AJAX  = [path("cart_ajax/",       include(mmh_cart_urls_ajax)),]
MMH_AJAX_DETAIL= [path("ajax_detail/",     include(mmh_cart_detail_ajax_product_views)),]
# PAYPAL         = [path("vpaypal/",         include(mmh_vpaypal_urls)),]
PRODUCT        = [path("service/",         include(all_product_urls)),]
#SSL commerze
SSLCOMMERZ     = [path ("vsslcommerz/",    include(mmh_vsslcommerz_urls)),]


from inventory.views.shopcart.amar_pay import initial_payment_amarPay, success #,payment_success_amr

mmh_amar_pay_urls = [
    path('payment/', initial_payment_amarPay, name="amar_pay"),
    path('payment_success/', success, name='payment_success'),
]
AMARPAY     = [path ("payment/",    include(mmh_amar_pay_urls)),]

# ## USER PERMISSIONS
# USERGROUP      = [path("vug/",             include(vusergroup_views)),]

urlpatterns =  site_homepage_url
urlpatterns +=  MMH_CART
urlpatterns +=  MMH_CART_AJAX
urlpatterns +=  MMH_AJAX_DETAIL
# urlpatterns +=  PAYPAL
urlpatterns +=  PRODUCT
# urlpatterns +=  USERGROUP
urlpatterns +=  SSLCOMMERZ
urlpatterns += AMARPAY

