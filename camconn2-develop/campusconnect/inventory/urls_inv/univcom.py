# from django.urls import path
# from django.conf.urls import url, include


# # Univcom
# from inventory.views.vprod_prei20  import (
#     UnivcomHome,
#     UnivcomServiceAll,
#     UnivcomServiceByCat,
#     UnivcomServiceDetails_ajax,
#     UnivcomServiceDetails,
#     UnivcomHowItWorks,
#     UnivcomCompareThis,
#     UnivcomUseCases,
#     UnivcomFaq,
#     UnivcomProductDeliveryMethods,

# )

# url_list_univcom = [
#     path("home",
#         UnivcomHome.as_view(),
#         name="univcom_home"
#     ),
#     path("all-services",
#         UnivcomServiceAll.as_view(),
#         name="univcom_all_services"
#     ),
#     path("category/<str:levelname>",
#         UnivcomServiceByCat.as_view(),
#         name='univcom_bycat'
#     ),
#     path("prod-details/<int:id>",
#         UnivcomServiceDetails,
#         name="univcom_prod_details"
#     ),


#     path("how-it-works",
#         UnivcomHowItWorks.as_view(),
#         name="univcom_how_it_works"
#     ),
#     path("service-comparison",
#         UnivcomCompareThis.as_view(),
#         name="univcom_compare_this"
#     ),
#     path("use-cases",
#         UnivcomUseCases.as_view(),
#         name="univcom_use_cases"
#     ),
#     path("faq",
#         UnivcomFaq.as_view(),
#         name="univcom_faq"
#     ),
#     path("product-delivery-methods",
#         UnivcomProductDeliveryMethods.as_view(),
#         name="univcom_del_meth"
#     ),

# ]
