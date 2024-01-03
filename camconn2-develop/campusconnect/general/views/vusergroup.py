#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from django.http import HttpResponse #, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy

# PROBLEM:      @user_passes_test(test_is_superuser, login_url=reverse_lazy("vug_failed_test", kwargs={'testname': "test_is_superuser"}))
# MMH: CAN I ABSTRACT THIS CALL to user_passes_test with theste specific parameters
#      TO AVOID HAVING ALL OF THIS PLACED EVERYWERE.
#      IS THERE WAY TO SHORTCUT THIS LIKE I WOULD DO IN C++

# ******************************************************************************
# logged in users with no additional priviledges
def test_is_default_group(user):
    if user.is_active and user.is_authenticated: return True
    else:                                        return False

# ******************************************************************************
# logged in users with priviledged access to prof-analyst views
# Manually create 'analyst' group in admin
# Manually add users to this group in admin.
def test_is_analyst_group(user):
    if user.is_active: return user.groups.filter(name='analyst').exists()
    else:              return False

# ******************************************************************************
# logged in users with priviledged access to admin
def test_is_admin_group(user):
    if user.is_active and user.is_staff: return True
    else:                                return False

# ******************************************************************************
# logged in users with superuser access
def test_is_superuser(user):
    if user.is_active and user.is_superuser: return True
    else:                                    return False

# ******************************************************************************
def vug_failed_test(request, testname, viewname, optionalmessage=""):
    zzz_print("    %-28s: %s" % ("vug_failed_test", "********************"))
    zzz_print("    %-28s: %s" % ("    testname",          testname))
    zzz_print("    %-28s: %s" % ("    viewname",          viewname))
    if optionalmessage:
        zzz_print("    %-28s: %s" % ("    optionalmessage",   optionalmessage))

    template = loader.get_template('resumeweb/layout/404.html')
    context = {
        "title"             : "vug_failed_test " + testname,
        "testfailed_name"   : testname,
        "viewfailed_name"   : viewname,
        "optionalmessage"   : optionalmessage,
    }
    return HttpResponse(template.render(context, request))






# Need mechanism to test if groups we need exist and if not automatically create them.
# To facilitate avoiding having to do this manually each time and possibly screw it up when doing it manually.
# creating of groups.
# assignment of permissions to each group.
#
# ensure this automatically propogates to new views/etc as they are added. Hoping someone adds this later as
# new stuff is created is problematic

# Create a set of defauilt users for testing who belong to the various groups.
#
# May need to extend this to auto populate other kinds of data such as default
# product lines, etc.
# If so this would be a view available only to an admin user that is ideally run/done/viewed
# Once for a new database but if done again is properly handled and not done twice.

# Admin form to promote users to other groups.
# when promoting user log date, time, and admin user id doing the promotion

# view to list all grlup members

# Probably enfrcing access to views with permission decorators
# Because we have a mix of regular django views and class based views we will
# need a regular permission and a permissionrequiredMixin.
#
# OR INSTEAD USE user_passes_test decorator which is similar to permission decorator
# but allows more flexibility.

# Probably need a organizational way to organize views by their required permissions.
# Hunting through various views files setting it on and off per view in location is
# problmatic. confusing and error prone.

# Probably need an organizational way to control the url parameters for permission decorators
# redirecting users if they fail to have the proper permissions.

# WRINKLES TO HANDLE/USE

# Django.user.object    active boolean    enable/disable this instead of deleting accounts
#     test how this flag affects all other permissions validation.
#     i assume when disabled everything else will fail but not sure until test
#
# Django.user.object staff status
#     Designates whether the user can log into this admin site.
#     IS THIS ENOUGH TO SPECIFY SOMEONE AS IN THE ADMIN GROUP ABOVE.
#     IT MIGHT BE.
#   THIS ISN'T QUITE ENOUGH, YOU CAN HAVE THIS BOOLEAN SET TO TRUE AND HAVE ACCESS TO THE ADMIN BUT
#   NOT HAVE ANY PERMISSIONS TO VIEW ANY OF THE MODELS AND CHANGE THEM.
#   looks like if you're using this to give user admin access you have to set this boolean
#    and
#   set the permissions they have (or group they belong to with those permissions)
#
# Django.user.object Superuser status
#     Designates that this user has all permissions without explicitly assigning them.
#     Dangerous and special permissions. NOt to be handed out lightly. Don't rely on this.


# Register django app.model classes specifying their permissions,etc.
# HERE'S WHERE THEY COULD BE PROGRAMICALLY ADDED TO THE ADMIN SYSTEM.
# HERE'S WHERE THEIR ATUAL NAMES AND DISPLAY NAMES COULD BE ORGANIZED
#
# Method to iterate through all model classes in django system.
# Compare these to ones registered to specific group permissions.
# Display ones that fall through. I.e. Might be new and not added to registration system.


# programmable method to find all view urls and then permissions for each.














# code tidbits:


# # add user to group
# from django.contrib.auth.models import Group
# group = Group.objects.get(name='groupname')
# user.groups.add(group)







