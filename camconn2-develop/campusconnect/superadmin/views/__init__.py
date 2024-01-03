from .cart import *

# """ from .coupon import (
# 	admin_mcoupon,
# ) """

from .login import (
	MyLoginView,
)

from .others import (
	admin_GuestResumeFiles,
	AdminSiteSurvey,
	Adminmsendmail,
    AdminAmar_pay,
    AdminSSL_commerz,
    Adminmsendmail_failure,
)



from .users import (
	AdminVerifiedUsers
)

# product lines 
# ------------------------------------------------
from .prod_adhoc import (
	AdminAdhocRequests
)



# from .prod_dialect import (
# 	admin_mprod_proglang_catlist,
# 	AdminProglangServlist,
# 	AdminProglangServiceoption,
# 	admin_mprod_prei20_deliveryoption,

# )

from superadmin.views.prod_visaassist import (
	AdminVisaassistServList,
	AdminVisaassistServiceoption,
	admin_mprod_visaassist_deliveryoption,
    admin_mprod_visaassist_catlist
)

from superadmin.views.prod_prei20 import (
	AdminPrei20ServList,
	AdminPrei20Serviceoption,
	admin_mprod_prei20_deliveryoption,

 )

from superadmin.views.prod_posti20 import (
    PostI20CatListAdmin,
    PostI20ServlistAdmin,
    PostI20DeliveryOptionAdmin,
    PostI20ServiceOptionAdmin
)

# from .prod_identity import (
# 	AdminTechRoleCatList,
# 	AdminTechRoleServList,
# 	AdminTechRoleServiceoption,
# 	AdminTechRoleDelivOption,

# )

from .prod_univcom import (
	admin_mprod_univcom_catlist,
	AdminUnivcomServlist,
	AdminUnivcomServiceoption,
	admin_mprod_univcom_deliveryoption,

)

from .prod_strategy import (
	AdminStrategyCatList,
	AdminStrategyServList,
	AdminStrategyServiceoption,
	admin_mprod_strategy_deliveryoption,

)

# from .prof_candidate import (
# 	AdminOrderCancellationRequest,
# 	MyResAdmin,
# 	MyResFormAdmin,
# 	DispCauseAdmin,
# 	DisputeAdmin,
# 	CandidateMessageAdmin,
# 	DeactivatedAccountAdmin,

# )


