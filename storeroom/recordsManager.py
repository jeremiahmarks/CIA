#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-24 14:59:00
# @Last Modified 2015-05-31
# @Last Modified time: 2015-05-31 16:03:03
import os
import sqlite3
import datetime
import shutil
try:
    import CIA.tools.CSVToolBox as csvTools
except ImportError:
    import tools.CSVToolBox as csvTools
import random
import string


# This module provides a file manager, basically a worker
# who solely exists to keep files in order and backed up.
# This will also be able to do other tasks related to data
# tracking and maintenance, however its basic purpose will
# be to manage files.

############################################################
## These store the absolute path to where ever the file is.
## The application will start by storing all data in this
## folder, however that decision will need to be examined
## again if the application is developed to support
## multiple users from the same install directory

pathtofile=__file__
projectsfolder=os.path.dirname(os.path.abspath(pathtofile))

############################################################
##
## using a timestamp seems like the easiest way to avoid
## writing over other files with the same name, in the same
## project

def timeStamp():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

class Worker(object):
    """
    This class will provide the functionality to manage
    the files that are part of individual projects. It may
    be subclassed or reused to implement a class that can
    interact with the data in the files, but that is
    currently merely an option.
    """
    def __init__(self, assignedproject):
        self.project=assignedproject

