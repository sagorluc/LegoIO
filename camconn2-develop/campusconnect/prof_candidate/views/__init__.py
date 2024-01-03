from .home import (
    CandidateProfileHome,
)

from .my_orders import (
    OrderHistoryAll,
    OrderDetails,
    # MyInvoices,
    # InvoicePDF,
    # mmh: removed when processing merged into pending view
    # OrderHistoryInProcessing,
    resume_download_view,
)

from .order_cancellation import (
    CancelOrder_mmh,
    CancelOrderSuccess_mmh,
    CancellationDetailsView,
    # CancelOrderFailed_mmh,
    OrderCancellationRequestView,
    OrderCancellationConfirmationView,

)

from .dispute import (
    SubmitDisputeView,
    DisputeHistoryView,
    DisputeDetailsView,
    DisputeResultView,
    # DisputeConfirmation,
    # SubmitDisputeFromOrderDetails,

)

from .service_feedback import ServiceFeedbackView

from .my_resume import (
    ResumeDocView,
    ResumeFormView,
    ResumeFormEditView,
    ResumeFormTips,
    ResumeFormConfirm,
    delete_doc,
    
)


from .cust_comm import (
    CandidateMsg,
    MsgHistory,
    MsgDetails,
    MsgConfirm,
)


from .rewards import (
    MyCurrentRewardOffers,
    MyEarnedCoupons,

)


from .acct_set import (
    AcctSettingsHomeView,
    UpdatePassView,
    AccountDeactivationView,
    AccDeactivateConfirmView,
    
)
