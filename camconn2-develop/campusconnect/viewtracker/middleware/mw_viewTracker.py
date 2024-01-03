#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from django.core.exceptions import ObjectDoesNotExist
from ..models import mviewtracker
from ..models import mviewtracker_asseterror

from inventory.models.muniqueid import (muniqueid_FROM_SESSCOOK, muniqueid_get_users_uniquid,)
from zzz_lib.zzz_log import zzz_print

CONST_NON_STANDARD_EXCEPTION_RESPONSE_CODE = 11500
CONST_NON_STANDARD_SUCCEEDED_RESPONSE_CODE = 22200



# ******************************************************************************
class mw_viewTracker:

    # --------------------------------------------------------------------------
    def __init__(self, get_response):
        self.get_response = get_response

    # --------------------------------------------------------------------------
    def __call__(self, request):
        response = self.get_response(request)
        # p03log.ip03log.logi("    %-28s: %s" % ("request.path", request.path))
        # p03log.ip03log.logi("    %-28s: %s" % ("response.status_code", response.status_code))

        if response.status_code < 200 or response.status_code >= 300:

            # Add mviewtracker_asseterror instance only if same url isn't already in database
            # otherwise increase it's total_count
            try:
                imviewtracker_asseterror = mviewtracker_asseterror.objects.get(
                    url=request.path,
                    method=request.method,
                    http_referer=request.META.get("HTTP_REFERER"),
                    query_string=request.META.get("QUERY_STRING"),
                    remote_addr=request.META.get("REMOTE_ADDR"),
                    remote_host=request.META.get("REMOTE_HOST"),
                    http_user_agent=request.META.get("HTTP_USER_AGENT"),
                    status_code=response.status_code,
                )
                imviewtracker_asseterror.total_count += 1
                imviewtracker_asseterror.save()
            except ObjectDoesNotExist:
                create_kwargs = {
                    "url":              request.path,
                    "method":           request.method,
                    "http_referer":     request.META.get("HTTP_REFERER"),
                    "query_string":     request.META.get("QUERY_STRING"),
                    "remote_addr":      request.META.get("REMOTE_ADDR"),
                    "remote_host":      request.META.get("REMOTE_HOST"),
                    "http_user_agent":  request.META.get("HTTP_USER_AGENT"),
                    "status_code":      response.status_code,
                }
                mviewtracker_asseterror.objects.create(**create_kwargs)

        return response

    # --------------------------------------------------------------------------
    def process_exception(self, request, exception):
        exctype, value      = sys.exc_info()[:2]
        exception_name      = str(exctype.__name__) # ex: SMTPAuthenticationError
        exception_value     = str(value)
        # p03log.ip03log.logi("    %-28s: %s" % ("exception_name", exception_name))
        # p03log.ip03log.logi("    %-28s: %s" % ("exception_value", exception_value))

        # owner_uniqid = muniqueid_get_users_uniquid_FROM_SESSCOOK(request)
        owner_uniqid = muniqueid_get_users_uniquid(request)

        # p03log.ip03log.logi("    %-28s: %s" % ("owner_uniqid", owner_uniqid))

        create_kwargs = {
            "url":              request.path,
            "method":           request.method,
            "http_referer":     request.META.get("HTTP_REFERER"),
            "query_string":     request.META.get("QUERY_STRING"),
            "remote_addr":      request.META.get("REMOTE_ADDR"),
            "remote_host":      request.META.get("REMOTE_HOST"),
            "http_user_agent":  request.META.get("HTTP_USER_AGENT"),
            "status_code":      CONST_NON_STANDARD_EXCEPTION_RESPONSE_CODE,
            "exception":        exception_name + ': ' + exception_value,
            "owner_uniqid":     owner_uniqid,
        }

        if request.user.is_authenticated:
            create_kwargs['user'] = request.user

        mviewtracker.objects.create(**create_kwargs)

        return None

    # --------------------------------------------------------------------------
    def process_view(self, request, view_func, view_args, view_kwargs):
        zzz_print("    %-28s" % ("====================================================== START"))
        zzz_print("    %-28s: %s" % ("request.path", request.path))
        zzz_print("    %-28s: %s" % ("view_func.__name__", view_func.__name__))
        zzz_print("    %-28s: %s" % ("view_args", view_args))
        zzz_print("    %-28s: %s" % ("view_kwargs", view_kwargs))
        zzz_print("    %-28s" % ("====================================================== END"))

        # MMH: DO NOT CALL response = self.get_response(request)
        #      here as that generates infiniate recursive loop

        owner_uniqid = muniqueid_FROM_SESSCOOK(request)
        zzz_print("    %-28s: %s" % ("owner_uniqid", owner_uniqid))

        create_kwargs = {
            "url":              request.path,
            "method":           request.method,
            "http_referer":     request.META.get("HTTP_REFERER"),
            "query_string":     request.META.get("QUERY_STRING"),
            "remote_addr":      request.META.get("REMOTE_ADDR"),
            "remote_host":      request.META.get("REMOTE_HOST"),
            "http_user_agent":  request.META.get("HTTP_USER_AGENT"),
            "status_code":      CONST_NON_STANDARD_SUCCEEDED_RESPONSE_CODE,
            "owner_uniqid":     owner_uniqid,
        }

        if request.user.is_authenticated:
            create_kwargs['user'] = request.user

        mviewtracker.objects.create(**create_kwargs)

        return None





