from django.urls import path
from django.conf.urls import url, include


# strategy >>> mprod_strategy
from inventory.views.vprod_strategy import (
    StrategyHomePg,
    StrategyServiceAll,
    StratSolProdDetails_ajax,
    StratSolProdDetails,
    StratSolServiceByCat,

    StrategyHowItWorks,
    StrategyOurspeciality,
    StrategyUseCases,
    StrategyCompareThis,
    StrategyFAQs,
    StrategyProductDeliveryMethods,

)


# strategy >>> mprod_strategy
strat_sol_urls = [
    path("home", 
        StrategyHomePg.as_view(), 
        name="strategy_home"
    ),
    
    path("all-services", 
        StrategyServiceAll.as_view(), 
        name="strategy_all_serv"
    ),

    path("service-details/<int:id>", 
        StratSolProdDetails, 
        name="strategy_prod_details"
    ),

    path("category/<str:tagname>",
        StratSolServiceByCat.as_view(),
        name='strategy_bycat'
    ),








    path("how-we-diff", 
        StrategyOurspeciality.as_view(), 
        name="stratsol_special"
    ),
    

    path("how-it-works", 
        StrategyHowItWorks.as_view(), 
        name="stratsol_how_it_works"
    ),
    
    path("service-comparison",
        StrategyCompareThis.as_view(), 
        name="stratsol_compare_this"
    ),
    
    path("use-cases", 
        StrategyUseCases.as_view(), 
        name="stratsol_use_cases"
    ),
    
    path("faq", 
        StrategyFAQs.as_view(), 
        name="stratsol_faq"
    ),
    
    path("product-delivery-methods", 
        StrategyProductDeliveryMethods.as_view(), 
        name="stratsol_del_meth"
    ),

]
