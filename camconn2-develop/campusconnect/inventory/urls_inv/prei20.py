from django.urls import path
from django.conf.urls import url, include


# PreI20
from inventory.views.vprod_prei20 import (
    Prei20Home,
    Prei20DetailView_ajax,
    Prei20DetailView,
    Prei20ServiceAll,
    Prei20ServiceBycat,

    Prei20HowItWorks,
    Prei20CompareThis,
    Prei20UseCases,
    Prei20ProductDeliveryMethods,
    Prei20FAQ,
)


url_list_prei20 = [
    path("home",
        Prei20Home.as_view(),
        name="prei20_homepg_url"
    ),
    path("all-services",
        Prei20ServiceAll.as_view(),
        name="prei20_services_all"
    ),
    path("category/<str:category>",
        Prei20ServiceBycat.as_view(),
        name="prei20_services_bycat"
    ),    
    path("service-details/<int:id>",
        Prei20DetailView,
        name="prei20_detail_view_link"
    ),




    path("how-it-works",
        Prei20HowItWorks.as_view(),
        name="prei20_how_it_works"
    ),
    path("service-comparison",
        Prei20CompareThis.as_view(),
        name="prei20_compare_this"
    ),
    path("use-cases",
        Prei20UseCases.as_view(),
        name="prei20_use_cases"
    ),
    path("faq",
        Prei20FAQ.as_view(),
        name="prei20_faq"
    ),
    path("product-delivery-methods",
        Prei20ProductDeliveryMethods.as_view(),
        name="prei20_del_meth"
    ),

]
