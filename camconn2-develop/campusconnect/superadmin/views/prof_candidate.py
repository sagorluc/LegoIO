# #!/usr/bin/env python
# # -*- coding: utf-8 -*-


# from django.contrib import admin
# from prof_candidate.models import (
#     OrderCancellationRequest,
#     CandidateInternalMsg,
#     DispCause,
#     DisputeClaim,
#     ResumeDocType,
#     ResumeFormType,
#     DeactivatedAccount,

# )


# @admin.register(OrderCancellationRequest)
# class AdminOrderCancellationRequest(admin.ModelAdmin):
#     list_display = (
#         "created_for",
#         "created_at",
#         "submitted_by"
#     )


# # customer contact us message
# @admin.register(ResumeDocType)
# class MyResAdmin(admin.ModelAdmin):
#     list_display = (
#         "user",
#         'id',
#         "document",
#         'created',
#         'updated',
#     )


# @admin.register(ResumeFormType)
# class MyResFormAdmin(admin.ModelAdmin):
#     list_display = (
#         'user',
#         'id',
#         'created',
#         'updated',
#     )


# # dispute causes
# @admin.register(DispCause)
# class DispCauseAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "reason",
#     )

# # dispute submitted
# @admin.register(DisputeClaim)
# class DisputeAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         'created_by',
#         # 'tracking_id',
#         'created_at',

#     )

# @admin.register(CandidateInternalMsg)
# class CandidateMessageAdmin(admin.ModelAdmin):
#     list_display = (
#         "subject",
#         "created_by",

#     )

# @admin.register(DeactivatedAccount)
# class DeactivatedAccountAdmin(admin.ModelAdmin):
#     list_display = (
#         "user",
#         "email",
#         "created",
#     )
