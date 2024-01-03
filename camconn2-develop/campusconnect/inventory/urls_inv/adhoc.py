from django.urls import path
from django.conf.urls import url, include

app_name = "adhoc"

from inventory.views.vprod_adhoc import (
    AdhocRequestByGuest,
    AdhocRequestSubmitConf,


    AdhocHome,
    AdhocHowItWorks,
    AdhocTermsCond,
    AdhocAppChecklist,
    AdhocCompareThis,
    AdhocUseCases,
    AdhocProductDeliveryMethods,
    AdhocFAQ,

    
)


adhoc_urls = [
    # product pages 
    path("request/create", AdhocRequestByGuest.as_view(),
        name="adhoc_submit_req_now"
    ),
    path("request/submit-confirmation/<int:id>/<str:token>",
        AdhocRequestSubmitConf.as_view(),
        name="adhoc_req_sub_conf"
    ),


    # non-product pages         
    path("home",
        AdhocHome.as_view(),
        name="adhoc_home"),

    path("terms-conditions",
        AdhocTermsCond.as_view(),
        name="adhoc_terms_cond"),

    path("app-checklist",
        AdhocAppChecklist.as_view(),
        name="adhoc_checklist"),



    # prod insight
    path("how-it-works",
        AdhocHowItWorks.as_view(),
        name="adhoc_how_it_works"),
    path("product-comparison",
        AdhocCompareThis.as_view(),
        name="adhoc_compare_this"),
    path("use-cases",
        AdhocUseCases.as_view(),
        name="adhoc_use_cases"),
    path("faq",
        AdhocFAQ.as_view(),
        name="adhoc_faq"),
    path("product-delivery-methods",
        AdhocProductDeliveryMethods.as_view(),
        name="adhoc_del_meth"),
]


urlpatterns = [
    path("", include(adhoc_urls)),
]
