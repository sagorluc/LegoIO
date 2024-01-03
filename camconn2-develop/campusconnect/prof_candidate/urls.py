from django.conf import settings
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from general.views import PromotionalOffersView
from .views import (

    CandidateProfileHome,

    # ============= my rewards
    MyCurrentRewardOffers,
    MyEarnedCoupons,

    # ============= my orders
    OrderHistoryAll,
    OrderDetails,
    # MyInvoices,
    # InvoicePDF,
    ServiceFeedbackView,


    # ============ referral


    # ============ order cancellation
    CancelOrder_mmh,
    OrderCancellationRequestView,
    OrderCancellationConfirmationView,
    CancellationDetailsView,
    CancelOrderSuccess_mmh,
    # CancelOrderFailed_mmh,


    # ============= disputes
    SubmitDisputeView,
    DisputeHistoryView,
    DisputeDetailsView,
    DisputeResultView,


    # ============= resume profile
    ResumeDocView,
    ResumeFormView,
    ResumeFormEditView,
    ResumeFormTips,
    ResumeFormConfirm,
    delete_doc,


    # ============= cust comm
    CandidateMsg,
    MsgHistory,
    MsgDetails,
    MsgConfirm,


    # ============= my info
    UpdatePassView,
    AccountDeactivationView,
    AccDeactivateConfirmView,


    # ============= acct settings
    AcctSettingsHomeView,

)


app_name = 'prof_candidate'


home = [
    path(
        'home',
        CandidateProfileHome.as_view(),
        name="dashboard_homepage"
    ),

]


rewards = [
    path(
        'offers',
        MyCurrentRewardOffers.as_view(),
        name="my_current_offers"
        ),
    path(
        'earnings',
        MyEarnedCoupons.as_view(),
        name="my_earned_coupons"
    ),

]


cust_comm = [
    path('contact-us',
        CandidateMsg.as_view(),
        name="msg_submit"
    ),
    path('my-message-history',
        MsgHistory.as_view(),
        name="msg_history"
    ),
    path('my-message-detail/<int:pk>',
        MsgDetails.as_view(),
        name="msg_details"
    ),
    path('my-message-confirmation',
        MsgConfirm.as_view(),
        name="msg_confirm"
    ),

]


order_cancellation_links = [
    path('cancel/request/<str:tracking_id>',           
        OrderCancellationRequestView.as_view(),                
        name="mmh_cancel_order"
    ),
    path('cancel/confirm/<str:tracking_id>',           
        OrderCancellationConfirmationView.as_view(),                
        name="mmh_cancel_order_confirm"
    ),    
    path('cancel/details/<str:tracking_id>',           
        CancellationDetailsView.as_view(),                
        name="mmh_cancel_order_details"
    ),
    path('submit/request/success/<str:tracking_id>',    
        CancelOrderSuccess_mmh,         
        name="mmh_cancel_order_success"
    ),
    # path('submit/request/failed/<str:tracking_id>',     CancelOrderFailed_mmh,          name="mmh_cancel_order_failed"),

]


my_orders = [
    path('history',                                 OrderHistoryAll,                name="order_history_all"),
    path('detail/<str:tracking_id>',                OrderDetails,                   name="order_details"),
    path('order/<str:tracking_id>/submit-feedback', ServiceFeedbackView.as_view(),    name="submit_feedback_for_order"),
        
    # path('my-invoices',                             MyInvoices.as_view(),           name="order_invoice"),
    # path('invoice-pdf/<str:tracking_id>',           InvoicePDF,                     name="invoice_pdf"),

    # mmh: removed when processing merged into pending view
    # path('history_inprocessing',                    OrderHistoryInProcessing,       name="order_history_inprocessing"),

]


my_disputes = [
    path(
        'order/submit-dispute/<str:tracking_id>',
        SubmitDisputeView.as_view(),
        name="file_disp_with_tracking_id"
    ),
    path(
        'my-dispute-history',
        DisputeHistoryView.as_view(),
        name="dispute_history"
    ),
    path(
        'my-dispute-details/<pk>',
        DisputeDetailsView.as_view(),
        name="dispute_details"
    ),
    path(
        'my-dispute-results',
        DisputeResultView.as_view(),
        name="dispute_result"
    ),
    # path(
    #     'order-feedback-form',
    #     OrderFeedbackView.as_view(),
    #     name="order_feedback_form"
    # ),

]


my_resume_prof = [
    path(
        'resume-upload-url',
        ResumeDocView.as_view(),
        name="resume_doc_upload_link"
    ),
    path(
        'resume-form',
        ResumeFormView.as_view(),
        name="resume_form"
    ),
    path(
        'resume-form-edit',
        ResumeFormEditView.as_view(),
        name="resume_form_edit"
    ),
    path(
        'resume-form-submission-confirm',
        ResumeFormConfirm.as_view(),
        name="resume_form_confirm"
    ),
    path(
        'resume-form-fillup-tips',
        ResumeFormTips.as_view(),
        name="resume_form_tips"
    ),
    path(
        'resume-delete/<int:doc_id>',
        delete_doc, 
        name="resume_doc_delete"
    ),
]


acct_set = [
    path(
        'home',
        AcctSettingsHomeView.as_view(),
        name="acct_set_home"
    ),

    path(
            "account-settings/update_password/", 
            UpdatePassView.as_view(), 
            name="update_password"
        ),

    # path(
    #         "account-settings/update_password/done/", 
    #         auth_views.PasswordChangeDoneView.as_view(extra_context={"msg": "Password Updated Successfully"}), 
    #         name="password_change_done"
    #     ),


    path(
        "deactivate_account",
        AccountDeactivationView.as_view(),
        name="account_deactivate"
    ),
    path(
        "deactivate_account_done",
        AccDeactivateConfirmView.as_view(),
        name="account_deactivate_done"
    )
]


urlpatterns = [
    path("", include(home)),
    path("my-orders/dispute/", include(my_disputes)),
    path("my-orders/", include(my_orders)),
    path("my-orders/cancellation/", include(order_cancellation_links)),
    path("my-resume/", include(my_resume_prof)),
    # path("referral-request/", include(referral)),
    path("my-rewards/", include(rewards)),
    path("cust-comm/", include(cust_comm)),
    path("account-settings/", include(acct_set)),
    
]
