from django.urls import path
from django.conf.urls import url, include


# dialect >>> mprod_posti20
from inventory.views.vprod_posti20 import (
    PostI20Home,
    PostI20ServiceAll,
    PostI20ServiceByCat,
    PostI20ServiceProdDetails_ajax,
    PostI20ServiceProdDetails,

    PostI20HowItWorks,
    PostI20CompareThis,
    PostI20UseCases,
    PostI20FAQ,
    PostI20ProductDeliveryMethods

)


# dialect >>> mprod_posti20
posti20_url = [
    path("home",
        PostI20Home.as_view(),
        name="posti20_home"
    ),
    path("all-services",
        PostI20ServiceAll.as_view(),
        name="posti20_all_services"
    ),
    path('category/<str:langname>',
        PostI20ServiceByCat.as_view(),
        name='posti20_bycat'
    ),
    path("service-details/<int:id>",
        PostI20ServiceProdDetails,
        name="posti20_prod_details"
    ),



    path("how-it-works",
        PostI20HowItWorks.as_view(),
        name="posti20_how_it_works"
    ),
    path("service-comparison",
        PostI20CompareThis.as_view(),
        name="posti20_compare_this"
    ),
    path("use-cases",
        PostI20UseCases.as_view(),
        name="posti20_use_cases"
    ),
    path("faq",
        PostI20FAQ.as_view(),
        name="posti20_faq"
    ),
    path("product-delivery-methods",
        PostI20ProductDeliveryMethods.as_view(),
        name="posti20_del_meth"
    ),
]
