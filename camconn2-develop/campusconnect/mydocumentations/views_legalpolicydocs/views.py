from django.views.generic.base import TemplateView
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from django.views.generic import (
    ListView,
    UpdateView,
    DetailView
)


TEMPLATE_BASE_FOOTNOTES = 'mydocumentations/legalpolicydocs/base-legal-docs.html'



# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# class CacheMixin(object):
    

#     def get_cache_timeout(self):
#         return self.cache_timeout

#     def dispatch(self, *args, **kwargs):
#         return cache_page(self.get_cache_timeout())(super(self).dispatch)(*args, **kwargs)






# ************************************
class LegalPolicyBaseClass(TemplateView):
    eff_dt = '07/30/2022'




# ************************************
class PrivacyPolicy(LegalPolicyBaseClass):
    
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': "Privacy Policy",
            'privacypolicy_notice': "Privacy Policy",
        }

        return context


# ************************************
class TermsofUse(LegalPolicyBaseClass):
    
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'Terms of Use',            
            'termsofuse_notice': "Terms of Use"
        }

        return context




#2

# donot sell my info
class DoNotSellMyInfo(LegalPolicyBaseClass):
    
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'Donot Sell My Information (California Rights)',            
            'donotsellmyinfo_notice': "Donot sell my info"
        }

        return context

#3
# general refund policy 
'''class RefundPolicyGeneral(LegalPolicyBaseClass):
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'General Refund Policy',            
            'refund_policy_gen': "General Refund Policy"
        }

        return context'''

#4
# general cancellation policy 
class RefundPolicyCancel(LegalPolicyBaseClass):
    
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'Cancellation & Refund Policy',
            'cancel_refund_gen': "General Cancellaiton Policy"
        }

        return context

#5
class RefundPolicyDispute(LegalPolicyBaseClass):
    
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'Dispute & Refund Policy',
            'dispute_refund_gen': "General Dispute Policy"
        }

        return context

# 6

class CookiePolicy(LegalPolicyBaseClass):
    
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'Cookie Policy',
            'cookie_policy_notes': "Cookie Policy"
        }

        return context


#7

class LegalPolicy(LegalPolicyBaseClass):
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'Legal Policy',
            'legal_policy_gen': "Legal Policy"
        }

        return context

#8

class PaymentPolicy(LegalPolicyBaseClass):
    
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'Payment Policy',
            'payment_policy_gen': "Payment Policy"
        }

        return context


#9

class SecurityPolicy(LegalPolicyBaseClass):
    
    template_name = TEMPLATE_BASE_FOOTNOTES

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'eff_dt': self.eff_dt,
            'section_title': 'Security Policy',
            'security_policy_gen': "Security Policy"
        }

        return context
        