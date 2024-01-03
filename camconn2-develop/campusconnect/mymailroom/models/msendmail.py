#!/usr/bin/env python
# -*- coding: utf-8 -*-

import html
import sys
from threading import Thread
from zzz_lib.zzz_log import zzz_print
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from .msendmail_failure import msendmail_failure


# ******************************************************************************
def msendmail_email_link_validation_sanity_test_hack(original_email_link):
    zzz_print("    %-28s: %s" % ("original_email_link", original_email_link))

    final_email_link = original_email_link.lower()

    # if 'https://' NOT FOUND in lowercase version of original_email_link
    if final_email_link.find('https://') == -1:
        zzz_print("    %-28s: %s" % ("https not found", final_email_link))
        final_email_link = 'http://' + original_email_link
    zzz_print("    %-28s: %s" % ("final_email_link", final_email_link))
    return final_email_link


# ******************************************************************************
class msendmail_instancemanager(models.Manager):
    # --------------------------------------------------------------------------
    def add(self, subject, plain_message, html_message, from_email, to_emails, appname):
        # zzz_print("    %-28s: %s" % ("to_emails_list orig", to_emails_list))
        # Remove duplicates from to_emails_list
        to_emails = list(dict.fromkeys(to_emails))
        # zzz_print("    %-28s: %s" % ("to_emails after", to_emails))
        # convert list of emails to string
        to_emails = ','.join(to_emails)
        # zzz_print("    %-28s: %s" % ("to_emails", to_emails))

        instance = self.create(
            subject         = subject, 
            plain_message   = plain_message, 
            html_message    = html_message, 
            from_email      = from_email, 
            to_emails       = to_emails, 
            appname         = appname
        )
        return instance


# ******************************************************************************
class msendmail(models.Model):
    objects             = msendmail_instancemanager()
    subject             = models.CharField      (max_length=1000, default="")
    plain_message       = models.TextField      (blank=False, null=False)
    html_message        = models.TextField      (blank=False, null=False)
    from_email          = models.CharField      (max_length=1000, default="")
    to_emails           = models.TextField      (blank=False, null=False)
    created             = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated             = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")
    sent_successfully   = models.BooleanField   (default=False)
    appname             = models.CharField      (max_length=1000, default="")

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = "SUBJECT ("   + self.subject + ") "
        return format(return_string)

    # --------------------------------------------------------------------------
    def _send(self, recipient_string):
        recipient_list = recipient_string.split(',')

        # zzz_print("    %-28s: %s" % ("subject",         self.subject))
        # zzz_print("    %-28s: %s" % ("html_message",    self.html_message))
        # zzz_print("    %-28s: %s" % ("plain_message",   self.plain_message))
        # zzz_print("    %-28s: %s" % ("from_email",      self.from_email))
        # zzz_print("    %-28s: %s" % ("to_emails",       self.to_emails))
        # zzz_print("    %-28s: %s" % ("recipient_string",  recipient_string))
        # zzz_print("    %-28s: %s" % ("recipient_list",  recipient_list))

        fail_title          = ""
        fail_description    = ""

        try:
            self.sent_successfully = True

            if self.appname == 'AUTH':
                auth_user           = settings.EMAIL_CONFIG["AUTH"]["EMAIL_HOST_USER"]
                auth_password       = settings.EMAIL_CONFIG["AUTH"]["EMAIL_HOST_PASSWORD"]
            elif self.appname == 'SHOPCART':
                auth_user           = settings.EMAIL_CONFIG["SHOPCART"]["EMAIL_HOST_USER"]
                auth_password       = settings.EMAIL_CONFIG["SHOPCART"]["EMAIL_HOST_PASSWORD"]
            elif self.appname == 'CUSTSUPP':
                auth_user           = settings.EMAIL_CONFIG["CUSTSUPP"]["EMAIL_HOST_USER"]
                auth_password       = settings.EMAIL_CONFIG["CUSTSUPP"]["EMAIL_HOST_PASSWORD"]
            else:
                auth_user           = settings.EMAIL_CONFIG["GENERAL"]["EMAIL_HOST_USER"]
                auth_password       = settings.EMAIL_CONFIG["GENERAL"]["EMAIL_HOST_PASSWORD"]
            
            return_value = send_mail(
                self.subject,
                self.plain_message,
                self.from_email,
                recipient_list,
                html_message        = self.html_message,
                fail_silently       = False,
                auth_user           = auth_user,
                auth_password       = auth_password
            )                
        
            if return_value == 0:
                self.sent_successfully  = False
                fail_title              = "Send_mail failed."
                fail_description        = "return_value == 0"
            else:
                zzz_print("    %-28s: id = %s, %s" % ("_send SUCCEEDED", self.id, recipient_list))
        except Exception as e:
            self.sent_successfully  = False
            # fail_title              = "Exception name = " + str(sys.exc_info()[0].__name__) # ex: SMTPAuthenticationError
            # fail_description        = str(sys.exc_info()[1])                                # ex: (535, b'5.7.8 Username ...
            exctype, value          = sys.exc_info()[:2]
            fail_title              = "Exception name = " + str(exctype.__name__) # ex: SMTPAuthenticationError
            fail_description        = str(value)                                # ex: (535, b'5.7.8 Username ...

        # save msendmail instance with updated value for sent_successfully
        self.save()

        # If fail save appropriate sendmail_failure instance
        if not self.sent_successfully:
            zzz_print("    %-28s: id = %s, %s, %s, %s" % ("WARNING _send FAILED", self.id, fail_title, fail_description, recipient_list))
            imsendmail_failure = msendmail_failure.objects.add_failure(self, fail_title, fail_description, recipient_string)

    # --------------------------------------------------------------------------
    # Sent in non blocking thread
    def send_to_entire_recipient_list(self):
        thread = Thread(target = self._send, args = (self.to_emails,))
        thread.start()

    # --------------------------------------------------------------------------
    # Sent in non blocking thread
    def send_to_each_recipient_seperately(self):
        for to_email in self.to_emails.split(','):
            thread = Thread(target = self._send, args = (to_email,))
            thread.start()




# # --------------------------------------------------------------------------
# # TYPES OF EMAILS BEING SENT
#
# vdev_testemail
#     now = datetime.now()
#
# CancelOrder_mmh refund success
# and             refund failure
#
#
#
# Each of these needs specific input for the email
# AND A HTML template
# AND PROBALBY A PLAIN TEXT template IF THAT CAN'T BE GENERATED FROM HTML VERSION.
#
#
# Referral assessment Purchase with link
#
#
#
# Thanks for creating accoiunt
#
#
#
# Thansk for verifying accounts
#
#
# Thans for purchase purcharse order




