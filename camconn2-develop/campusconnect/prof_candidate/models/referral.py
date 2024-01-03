from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from base64 import b64encode, b64decode
from dirtyfields import DirtyFieldsMixin



# # ===================
# from django.contrib.auth.models import User
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from uuid import uuid4
# from base64 import b64encode, b64decode
# from dirtyfields import DirtyFieldsMixin


# JOB_SEARCH_STAGES = (
#     ('kk726', 'I am casually looking'),

# )

# INT_PREP_STAGES = (
#     ('kb226', 'I can handle my interview'),

# )

# MY_EDU_LEVEL = (
#     ('ed7261', 'I am still studying'),
#     ('ed7262', 'I am done studying'),
# )

# MY_EDU_ORG = (
#     ('ed7261', 'I have degree from USA'),
#     ('ed7262', 'I havo no degree from USA'),
# )

# EMPL_STATUS = (
#     ('emp776', 'I am currently employed'),
#     ('emp716', 'I am not employed'),
# )

# WHY_NEEDED = (
#     ('', 'Choose...'),
#     ('code403', 'I donot know many recruiters'),
#     ('code409', 'I donot know where to submit my resume'),
# )

# # ******************************************************************************
# class mprod_referral(models.Model):
#     # about the job description section
#     resume = models.FileField(
#         default='null',
#         upload_to='referral_resumes/%Y/%m/%d'
#     )
#     target_job_title1 = models.CharField(
#         max_length=500,
#         null=True,
#         blank=True
#     )
#     target_JD_1 = models.CharField(
#         max_length=2000,
#         null=True,
#         blank=True
#     )

#     target_job_title2 = models.CharField(
#         max_length=500,
#         null=True,
#         blank=True
#     )
#     target_JD_2 = models.CharField(
#         max_length=2000,
#         null=True,
#         blank=True
#     )

#     target_job_title3 = models.CharField(
#         max_length=500,
#         null=True,
#         blank=True
#     )
#     target_JD_3 = models.CharField(
#         max_length=2000,
#         null=True,
#         blank=True
#     )

#     job_search_stage = models.CharField(
#         max_length=20,
#         choices=JOB_SEARCH_STAGES,
#         default='no'
#     )
#     job_search_stage_exp = models.CharField(
#         max_length=2000,
#         null=True,
#         blank=True
#     )

#     int_prep_stage = models.CharField(
#         max_length=20,
#         choices=INT_PREP_STAGES,
#         default='no'
#     )
#     int_prep_stage_exp = models.CharField(
#         max_length=2000,
#         null=True,
#         blank=True
#     )

#     empl_status = models.CharField(
#         max_length=20,
#         choices=EMPL_STATUS,
#         default='no'
#     )
#     empl_status_exp = models.CharField(
#         max_length=2000,
#         null=True,
#         blank=True
#     )

#     edu_level = models.CharField(
#         max_length=20,
#         choices=MY_EDU_LEVEL,
#         default='no'
#     )
#     edu_origin = models.CharField(
#         max_length=20,
#         choices=MY_EDU_ORG,
#         default='no'
#     )


#     # contact with the person section
#     f_name = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True
#     )
#     l_name = models.CharField(
#         max_length=200,
#         null=True,
#         blank=True
#     )
#     email = models.CharField(
#         max_length=200,
#         null=True,
#         blank=True
#     )


#     # feedback section
#     why_needed = models.CharField(
#         max_length=20,
#         choices=WHY_NEEDED,
#         default='no'
#     )
#     msg = models.CharField(
#         max_length=2000,
#         null=True,
#         blank=True
#     )

#     # form meta info
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     consent = models.BooleanField(
#         default=False
#     )

#     class Meta:
#         verbose_name_plural = "Referral Req"


#     def __str__(self):
#         return f'{self.f_name}'

