from django.conf import settings
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "guestactions"

from .views import (
    ContactUsGuestView,
    CheckOrderStatusView,
    ProductReviewGuestView,
    feedback_submit_confirmation_view,
    ProductSearchResultsView,
    InviteFriendsView,
    InviteFriendsThankyou,
    SiteSurveyView,
    SurveyThankyouView,
)

urls_sitesurvey = [ 
    path("help-center/action/site-survey",      
        SiteSurveyView.as_view(),       
        name="submit_site_survey_as_guest"
    ),
    path("help-center/action/site-survey/thankyou",  
        SurveyThankyouView.as_view(),   
        name="site_survey_thankyou"
    ),
]

urls_productsearch = [    
    path("", ProductSearchResultsView.as_view(), name="product_search_link"),   
]

urls_orderstatuscheck = [
    path("check-order-status", 
        CheckOrderStatusView.as_view(), 
        name="check_my_order_status"
    ),
]

urls_contactus = [
    path("help-center/action/contact-us", 
        ContactUsGuestView.as_view(), 
        name="contact_us_guest"
    ),
]

urls_invitefriends = [
    path("help-center/action/invite-friends",           
        InviteFriendsView,      
        name="invite_friends_link"
    ),
    path("help-center/action/invite-friends/thankyou",  
        InviteFriendsThankyou,  
        name="invite_friends_thankyou"
    ),
]

urls_productreview = [
    path("help-center/action/product-review",           
        ProductReviewGuestView, 
        name="product_review_by_guest_link"
    ),
    path("help-center/action/product-review/thankyou",  
        feedback_submit_confirmation_view, 
        name="feedback_submit_confirmation_view"
    ),

]

urlpatterns = [
    path("",            include(urls_productsearch)),
    path("",            include(urls_orderstatuscheck)),
    path("",            include(urls_contactus)),
    path("",            include(urls_invitefriends)),
    path("",            include(urls_productreview)),
    path("",            include(urls_sitesurvey)),

]
