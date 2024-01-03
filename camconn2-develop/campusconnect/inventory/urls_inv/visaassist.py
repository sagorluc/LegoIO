from django.urls import path
from django.conf.urls import url, include


# dialogue >>> mprod_intprep
from inventory.views.vprod_visaassist import (
    VisaassistHome,
    VisaassistServiceByCat,
    VisaassistServiceAll,
    VisaassistProdDetails_ajax,
    VisaassistProdDetails,
    VisaassistOurspeciality,
    VisaassistTerms,
    VisaassistHowItWorks,
    VisaassistUseCases,
    VisaassistCompareThis,
    VisaassistProductDeliveryMethods,
    VisaassistFAQ,
)


url_list_visaassist = [
    path("home",
        VisaassistHome.as_view(),
        name="visaassist_home"
    ),
    path("all-services",
        VisaassistServiceAll.as_view(),
        name="visaassist_all_services"
    ),
    path("category/<str:catname>",
        VisaassistServiceByCat.as_view(),
        name="visaassist_bycat"
    ),
    path("service-details/<int:id>",
        VisaassistProdDetails,
        name="visaassist_prod_details"
    ),




    path("terms-n-conditions",
        VisaassistTerms.as_view(),
        name="visaassist_termscond"
    ),
    path("specialization",
        VisaassistOurspeciality.as_view(),
        name="visaassist_specialization"
    ),


    path("how-it-works",
        VisaassistHowItWorks.as_view(),
        name="visaassist_how_it_works"
    ),
    path("service-comparison",
        VisaassistCompareThis.as_view(),
        name="visaassist_compare_this"
    ),
    path("use-cases",
        VisaassistUseCases.as_view(),
        name="visaassist_use_cases"
    ),
    path("faq",
        VisaassistFAQ.as_view(),
        name="visaassist_faq"
    ),    
    path("product-delivery-methods",
        VisaassistProductDeliveryMethods.as_view(),
        name="visaassist_del_meth"
    ),

]
