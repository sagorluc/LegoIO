#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print

from ..models.muniqueid import muniqueid

# ******************************************************************************
class mw_mmhUserUniqueid:

    # --------------------------------------------------------------------------
    def __init__(self, get_response):
        self.get_response = get_response
        # zzz_print("    %-28s: %s" % ("mw_mmhUserUniqueid", "__init__"))

    # --------------------------------------------------------------------------
    def __call__(self, request):
        response = self.get_response(request)
        # zzz_print("    %-28s: %s" % ("__call__", request.path))
        return response

    # --------------------------------------------------------------------------
    def process_view(self, request, view_func, view_args, view_kwargs):
        zzz_print("    %-28s: %s" % ("process_view", request.path))
        # zzz_print("    %-28s: %s" % ("process_view", view_func.__name__))

        # MMH: Cannot call
        #      response = self.get_response(request)
        #      here as that generates infiniate recursive loop

        if request.user.is_authenticated:
            # zzz_print("    %-28s: (view = %s)" % ("process_view", view_func.__name__))
            muniqueid.objects.muniqueid_add(request)
        return None



















