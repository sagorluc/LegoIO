from django.conf import settings
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name='mydocumentations'

from .views import (
    CompareAllServices,
    AllServices,
    AllPrimeServices,
    AllSeconServices,
    GeneralFaq,
)

urls_productdocs = [

    path("product-docs/all",
        AllServices.as_view(),
        name="all_services_link"
    ),
    path("product-docs/universal",
        AllPrimeServices.as_view(),
        name="all_prime_services_link"
    ),
    path("product-docs/proficiency",
        AllSeconServices.as_view(),
        name="all_secon_services_link"
    ),
    path("product-docs/product-feature-matrix",
        CompareAllServices.as_view(),
        name="compare_all_services_link"
    ),
    path("product-docs/faq/general",
        GeneralFaq.as_view(),
        name="faq_gen"
    ),

]

from .views import (
    TermsofUse,
    PrivacyPolicy,
    DoNotSellMyInfo,
    RefundPolicyCancel,
    RefundPolicyDispute,
    CookiePolicy,
    LegalPolicy,
    PaymentPolicy,
    SecurityPolicy, 

)

urls_legalpolicydocs = [

    path("cookie-policy",
        CookiePolicy.as_view(),
        name="cookie_policy"
    ),    
    path("donot-sell-info",
        DoNotSellMyInfo.as_view(),
        name="dont_sell_info"
    ),

    path("terms-of-use",
        TermsofUse.as_view(),
        name="terms_of_use"
    ),
    path("privacy-policy",
        PrivacyPolicy.as_view(),
        name="privacy_policy"
    ),

    path("cancel-and-refund-policy",
        RefundPolicyCancel.as_view(),
        name="cancel_policy"
    ),
    
    path("dispute-and-refund-policy",
        RefundPolicyDispute.as_view(),
        name="dispute_policy"
    ),
    path("payment-policy",
        PaymentPolicy.as_view(),
        name="payment_policy"
    ),

    path("security-policy",
        SecurityPolicy.as_view(),
        name="security_policy"
    ),

]

urlpatterns = [
    path("productdocs/", include(urls_productdocs)),
    path("legaldocs/",   include(urls_legalpolicydocs)),
]
