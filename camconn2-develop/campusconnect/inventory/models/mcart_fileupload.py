#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zzz_lib.zzz_log import zzz_print

import os

from django.conf import settings
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from inventory.models.muniqueid import muniqueid_get_users_uniquid


import logging
logger = logging.getLogger(__name__)	

# --------------------------------------------------------------------------
# tuple[0]:     id              Make sure this is unique and greater than zero
# tuple[2]:     method_name     Class method name to validate something about file, returns True if validation succeeds, false otherwise
# tuple[3]:     help text       Text user will see if validation fails for this test
FILE_VALIDATION_METHODS = (
    (1, "fm_filesize_greater_than_zero",    "FILE SIZE MUST BE GREATER THEN ZERO"),
    (2, "fm_filetype_doc_or_docx",          "WE ARE ACCEPTING ONLY .DOC OR .DOCX FILE"),
)

VALID_FILE_EXTENSION_IN_LOWERCASE_LIST = [".doc", ".docx"]




# ******************************************************************************
class mcart_fileupload_instancemanager(models.Manager):
    
    def mcart_fileupload_add_or_update(self, request, document):
        owner_uniqid = muniqueid_get_users_uniquid(request)
        add_or_update_mode = "EXISTS"
        try:
            print("owner_uniqid------------------",owner_uniqid)
            print("document----------------------",type(document))
            
            mcart_fileupload_instance = mcart_fileupload.objects.get(owner_uniqid=owner_uniqid, document=document)
            # if mcart_fileupload_instance.exists():
            #     print("File exist--------------------------")
            # else:
            #     print(" Not exsit++++++++++++++++++++++++++++++++++++++++++++")

            print("mcart_fileupload_instance type>>>",mcart_fileupload_instance)
            #print(type(mcart_fileupload_instance))
        except ObjectDoesNotExist:
            add_or_update_mode = "ADDED"
            print("mcart_fileupload_instance ObjectDoesNotExist")
            mcart_fileupload_instance = self.create(owner_uniqid=owner_uniqid, document=document)

            print("mcart_fileupload_instance==============>", mcart_fileupload_instance)   
        # Probably don't need this save as existing instance not altered and created instance has implied save to DB
        mcart_fileupload_instance.save()
        zzz_print("    %-28s: %s, %s" % ("mcart_fileupload_instancemanager", add_or_update_mode, mcart_fileupload_instance.__str__()))
        return mcart_fileupload_instance


    # def mcart_fileupload_add_or_update(self, request, document):
    #     owner_uniqid = muniqueid_get_users_uniquid(request)
    #     add_or_update_mode = "EXISTS"
    #     try:
    #         mcart_fileupload_instance = mcart_fileupload.objects.get(owner_uniqid=owner_uniqid, document="4e9d083c-6b2a-4f10-bea8-b62448b56cbc_2022-09-29_142159.0527730000_SignUp_Th_1QnpIeS.docx")
    #         print("mcart_fileupload_instance type>>>")
    #         print(type(mcart_fileupload_instance))
    #     except ObjectDoesNotExist:
    #         add_or_update_mode = "ADDED"
    #         # print("this line is hit88779")
    #         mcart_fileupload_instance = self.create(owner_uniqid=owner_uniqid, document=document)

    #     add_or_update_mode = "ADDED"
    #     mcart_fileupload_instance = self.create(owner_uniqid=owner_uniqid, document=document)
    #     # Probably don't need this save as existing instance not altered and created instance has implied save to DB
    #     mcart_fileupload_instance.save()
    #     zzz_print("    %-28s: %s, %s" % ("mcart_fileupload_instancemanager", add_or_update_mode, mcart_fileupload_instance.__str__()))

    #     return mcart_fileupload_instance


# ******************************************************************************
class mcart_uploadpath(object):
    # --------------------------------------------------------------------------
    def __init__(self):
        pass
    # --------------------------------------------------------------------------
    def deconstruct(self):
        kwargs = {}
        return 'inventory.models.mcart_uploadpath', (), kwargs
    # --------------------------------------------------------------------------
    def __call__(self, instance, filename):
        # NOTE: instance.id not available at this moment
        # return "resume-cart-018/{}_{}_{}".format(instance.owner_uniqid, instance.created, filename)
        print("Model dname**********************************************************", "{}/{}_{}_{}".format(os.environ.get('AWS_S3_MCART_RESUME_FOLDER'),instance.owner_uniqid, instance.created, filename))
        return "{}/{}_{}_{}".format(os.environ.get('AWS_S3_MCART_RESUME_FOLDER'),instance.owner_uniqid, instance.created, filename)

upload_path_migrations_callable_workaround_hack = mcart_uploadpath()


# ******************************************************************************
class mcart_fileupload(models.Model):
    objects                 = mcart_fileupload_instancemanager()
    owner_uniqid            = models.CharField      (max_length=100)
    purchased               = models.BooleanField   (default=False)
    created                 = models.DateTimeField  (auto_now_add=True, help_text="timestamp of creation")
    updated                 = models.DateTimeField  (auto_now=True, help_text="timestamp of last update")
    mcompleted_purchase     = models.ForeignKey     ('inventory.mcompleted_purchase', blank=True, null=True, on_delete=models.CASCADE)
    document                = models.FileField      (upload_to=upload_path_migrations_callable_workaround_hack)
    validation_passed       = models.BooleanField   (default=False)
    validation_failed_id    = models.IntegerField   (default=0)

    # --------------------------------------------------------------------------
    def __str__(self):
        return_string  = "ID (" + str(self.id) + ") "
        return_string += "owner_uniqid (" + self.owner_uniqid + ") "
        return_string += "document: " + str(self.document)
        return format(return_string)

    # --------------------------------------------------------------------------
    def get_validation_method_description(self, id):
        return_text = "MMH NOT FOUND. IF THIS DISPLAYS THEN SOMETHING IS WRONG WITH -> FILE_VALIDATION_METHODS"
        for tuple in FILE_VALIDATION_METHODS:
            if tuple[0] == id:
                return_text = tuple[2]
                break
        return return_text

    # --------------------------------------------------------------------------
    def get_full_media_path_and_filename(self):
        return_text = settings.MEDIA_ROOT +settings.PUBLIC_MEDIA_LOCATION+ "/" + str(self.document)
        return return_text

    # --------------------------------------------------------------------------
    # def fm_filesize_greater_than_zero(self):
    #     # zzz_print("    %-28s: %s" % ("fm_filesize_greater_than_zero", ""))
    #     if os.environ.get("SERVER_TYPE") == "local":
    #         full_path_filename  = self.get_full_media_path_and_filename()
    #         filesize            = os.path.getsize(full_path_filename)
    #         # zzz_print("    %-28s: %s" % ("filesize", filesize))

    #         if filesize > 0:    return True
    #         else:               return False
    #     else:
    #         """
    #         TODO:
    #         try to figure out how to make the following command functional for s3
    #         filesize            = os.path.getsize(full_path_filename)
    #         this filesize variable returns False because os.path cannot retrieve a file location from s3 server
    #         """
    #         return True

    # --------------------------------------------------------------------------
    def fm_filesize_greater_than_zero(self):
        # zzz_print("    %-28s: %s" % ("fm_filesize_greater_than_zero", ""))
        return True


    # --------------------------------------------------------------------------
    def fm_filetype_doc_or_docx(self):
        # zzz_print("    %-28s: %s" % ("fm_filetype_doc_or_docx", ""))
        full_path_filename       = self.get_full_media_path_and_filename()
        filename, file_extension = os.path.splitext(full_path_filename)
        # zzz_print("    %-28s: %s" % ("filename", filename))
        # zzz_print("    %-28s: %s" % ("file_extension", file_extension))

        if file_extension.lower() in VALID_FILE_EXTENSION_IN_LOWERCASE_LIST: 
            return True
        else:
            return False

    # --------------------------------------------------------------------------
    def validate_uploaded_file(self):
        self.validation_passed = True
        for tuple in FILE_VALIDATION_METHODS:
            # Get pointer to test method
            methodPtr = getattr(self, tuple[1])
            if not methodPtr(): # if test method returns False
                self.validation_failed_id = tuple[0]
                self.validation_passed = False
                break
        self.save()
        if not self.validation_passed:
            zzz_print("    %-28s: %s" % ("VALIDATION FAILED", self.get_validation_method_description(self.validation_failed_id)))
            logger.info("  %-28s: %s" % ("VALIDATION FAILED", self.get_validation_method_description(self.validation_failed_id)))






# import boto3

# # initialize S3 client
# s3 = boto3.client('s3')

# # specify bucket name and file key
# bucket_name = 'your-bucket-name'
# file_key = 'path/to/your/file'

# # get the file size
# response = s3.head_object(Bucket=bucket_name, Key=file_key)
# file_size = response['ContentLength']

# # print the file size in bytes
# print(f"The size of the file {file_key} is {file_size} bytes.")
