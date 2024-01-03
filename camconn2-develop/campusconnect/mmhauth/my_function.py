from prof_candidate.models.acc_sett import DeactivatedAccount
import logging
logger = logging.getLogger(__name__)
from django.views.decorators.cache import cache_page


def user_is_deactivated(email):
    # query through Deactivateacc model & pass email
    # model = DeactivatedAccount
    # model_email = DeactivatedAccount.objects.filter(email=formemail).first()
    mmk = DeactivatedAccount.objects.filter(email=email).exists()
    
    if mmk:
        logger.warning("calling user_is_deactivated ")
        return True
    else: 
    	return False

