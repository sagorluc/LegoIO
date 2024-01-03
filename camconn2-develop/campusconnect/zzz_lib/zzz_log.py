#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import logging
import pprint
import sys
import time

# *****************************************************************************
class zzz_stack(object):

    # --------------------------------------------------------------------------
    # parentLevel 0: is self
    # parentLevel 1: is parents
    # parentLevel 2: is grand parents
    # etc
    def __init__(self, origParentLevel):
        self.origParentLevel        = origParentLevel
        self.stackSize              = len(inspect.stack())
        # Ensure parentLevel is valid and correct appropriately
        self.parentLevel            = self.origParentLevel
        self.correctedParentLevel   = False
        if self.parentLevel >= self.stackSize:
            self.parentLevel = self.stackSize - 1
            self.correctedParentLevel = True
        self.stack = inspect.stack()[self.parentLevel]

    # --------------------------------------------------------------------------
    # ex: <frame object at 0x7f106bf65228>
    def getFrameObject(self):
        return self.stack[0]

    # --------------------------------------------------------------------------
    def getFilePath(self):
        return self.stack[1]

    # --------------------------------------------------------------------------
    def getLineNumber(self):
        return self.stack[2]

    # --------------------------------------------------------------------------
    # ex: SELF or SOME PARENT:      zhLog_displayMethodInfo
    # ex: GREATEST PARENT:          <module>
    def getMethodName(self):
        return self.stack[3]

    # --------------------------------------------------------------------------
    def getMethodArgsAsString(self):
        returnString = ""
        args, varargs, keywords, values = inspect.getargvalues(self.getFrameObject())
        firstIteration = True
        for i in args:
            if not firstIteration:
                returnString += ", "
            returnString += "%s=%s" % (i, values[i])
            firstIteration = False
        return returnString

    # --------------------------------------------------------------------------
    def getFilenameFiletype(self):
        # right partition string by backslash and return third part of tuple
        return self.getFilePath().rpartition('/')[2]

    # --------------------------------------------------------------------------
    def getFilename(self):
        return self.getFilenameFiletype().partition('.')[0]

    # --------------------------------------------------------------------------
    def getParentName(self):
        # FilePath Example: /some/work/path/to/project/git_repo_name/backend/ParentName/PythonFile.py
        split_array = self.getFilePath().split('/')
        # print("len(split_array) = " + str(len(split_array)))
        parentName = split_array[len(split_array)-2]
        # print("parentName = " + parentName)
        return parentName

    # --------------------------------------------------------------------------
    def displayStack(self):
        print("    %-24s: %d" % ("parentLevel",                     self.parentLevel))
        print("    %-24s: %d" % ("StackSize",                       self.stackSize))
        print("    %-24s: %d" % ("origParentLevel",                 self.origParentLevel))
        print("    %-24s: %s" % ("correctedParentLevel",            self.correctedParentLevel))
        print("    %-24s: %s" % ("FrameObject",                     self.getFrameObject()))
        print("    %-24s: %s" % ("FilePath",                        self.getFilePath()))
        print("    %-24s: %d" % ("LineNumber",                      self.getLineNumber()))
        print("    %-24s: %s" % ("MethodName",                      self.getMethodName()))
        print("    %-24s: %s" % ("getFilename",                     self.getFilename()))
        print("    %-24s: %s" % ("getFilenameFiletype",             self.getFilenameFiletype()))
        print("    %-24s: %s" % ("getParentName",                   self.getParentName()))


# ------------------------------------------------------------------------------
def zzz_print_exit(original_print_string):
    zzz_print(original_print_string)
    sys.exit()



# *****************************************************************************
class zzz_print(object):

    # --------------------------------------------------------------------------
    def __init__(self, original_print_string, pretty=False):
        print_obj = original_print_string

        if pretty:
            if hasattr(print_obj, '__dict__'):  print_obj = pprint.pformat(vars(print_obj))
            else:                               print_obj = pprint.pformat(print_obj)
            print_obj = self.dumpPrettyBoundry_Start() + print_obj + self.dumpPrettyBoundry_End()

        inContext_message = self.__getInContextLogString(print_obj)
        self.dump_text(inContext_message)

    # --------------------------------------------------------------------------
    def __getInContextLogString(self, log_string):
        # Configure CONST_STACK_PARENT_LEVEL for proper context which depends on location of original call
        CONST_STACK_PARENT_LEVEL = 3
        zzz_stack_instance = zzz_stack(CONST_STACK_PARENT_LEVEL)
        # zzz_stack_instance.displayStack()

        parentName          = zzz_stack_instance.getParentName()
        filenameFiletype    = zzz_stack_instance.getFilenameFiletype()
        methodName          = zzz_stack_instance.getMethodName()
        lineNumber          = zzz_stack_instance.getLineNumber()
        src_info            = parentName + "/" + filenameFiletype + " (line " + str(lineNumber) + ")"
        t                   = time.localtime()
        time_formatted      = time.strftime("%H:%M:%S", t)
        # time_formatted      = time.strftime("%y/%m/%d %H:%M:%S", t)

        return "[%s] %-50s| %-28s| %s" % (time_formatted, src_info, methodName+"()", log_string)

    # --------------------------------------------------------------------------
    def dumpPrettyBoundry_Start(self):
        return "\n******************************************************************************************** ZZZ_PRETTY | START:\n"

    # --------------------------------------------------------------------------
    def dumpPrettyBoundry_End(self):
        return "\n******************************************************************************************** ZZZ_PRETTY | END:\n"

    # --------------------------------------------------------------------------
    def dump_text(self, text):
        # print (text)
        # logging.info(text)
        # logging.debug(text)
        logging.warning(text)






