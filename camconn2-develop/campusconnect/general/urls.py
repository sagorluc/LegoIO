from django.conf.urls import url, include
from django.urls import path

app_name = "general"


from general.views.general_views import(
    Page404View,
    AboutUsView,
    # top news
    Covid19ResponseView,
    BLMResponseView,
    PromotionalOffersView,
    ThisIsBeta,
    UsOnlySupport,
    # help center
    HelpCenterHome,
    MemberBenefitsView,
)

# general
site_general_urls = [
    path("product-docs/all",
        AboutUsView.as_view(),
        name="about_us"
    ),
    path("page-404-view", 
        Page404View.as_view(), 
        name="page_404_view"
    ),

]


# news section
topnews_urls = [
    path("covid19-response", 
        Covid19ResponseView.as_view(), 
        name="covid19_res_url"
    ),
    path("how-we-tackle-racial-injudtice", 
        BLMResponseView.as_view(), 
        name="blm_page"
    ),
    path("promotional-offers", 
        PromotionalOffersView.as_view(), 
        name="promo_offers_page"
    ),
    path("us-only", 
        UsOnlySupport.as_view(), 
        name="us_only_support"
    ),    
    path("beta", 
        ThisIsBeta.as_view(), 
        name="this_is_beta"
    ),        
]

#help center section
footer_urls = [ 
    path("help-center/home",
        HelpCenterHome.as_view(),
        name="cust_service_home"
    ),
    path("help-center/membership-benefits",
        MemberBenefitsView.as_view(),
        name="mem_ben_url"
    ),    
]

# GENERAL STUFF
SITE_GENERAL      = [path("",                 include(site_general_urls)),]
# FOOTER            = [path("",                 include(footer_urls)),]
TOPNEWS           = [path("news/",            include(topnews_urls)),]

urlpatterns =   SITE_GENERAL
# urlpatterns +=  FOOTER
urlpatterns +=  TOPNEWS