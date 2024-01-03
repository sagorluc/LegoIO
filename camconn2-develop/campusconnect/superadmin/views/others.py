from zzz_lib.zzz_log import zzz_print
from django.contrib import admin

from guestactions.models import (
    GuestResumeModel,
    SiteSurveyModel,
    ContactUsModel,
)




#from guestactions.models.guest_resume_upload import GuestResumeModel

from mymailroom.models import (
    msendmail, msendmail_failure,
)

#from inventory.models import mpaypal


# @admin.register(mpaypal)
# class AdminPaypal(admin.ModelAdmin):
#     list_display = (
#         "id",

#     )

from inventory.models.mssl_commerz import mssl_commerz
from inventory.models.mamar_pay import mamar_pay

@admin.register(mssl_commerz)
class AdminSSL_commerz(admin.ModelAdmin):
    list_display = (
        "id",
    )

@admin.register(mamar_pay)
class AdminAmar_pay(admin.ModelAdmin):
    list_display = (
        "id",
    )

@admin.register(msendmail)
class Adminmsendmail(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
    )

@admin.register(msendmail_failure)
class Adminmsendmail_failure(admin.ModelAdmin):
    list_display = (
        "id",
        "created"
    )


@admin.register(GuestResumeModel)
class admin_GuestResumeFiles(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "file1",
        "upload_time",
    )


@admin.register(SiteSurveyModel)
class AdminSiteSurvey(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at"
    )

