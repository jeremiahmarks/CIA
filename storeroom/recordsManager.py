#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-24 14:59:00
# @Last Modified 2015-05-24
# @Last Modified time: 2015-05-24 18:13:12
import os
import sqlite3
import datetime
import shutil
import CIA.tools.CSVToolBox as csvTools
import random
import string

def timeStamp():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')



pathToFile=__file__
pathToFolder=os.path.abspath(pathToFile)

class Worker(object):
    def __init__(self, assignedProject):
        self.project=assignedProject
        self.projectDBPath=os.path.join(os.path.dirname(pathToFolder),  assignedProject)
        self.projectDBFile=os.path.join(self.projectDBPath, assignedProject + ".sqlite")
        self.lastFile=self.projectDBFile
        if not os.path.exists(self.projectDBPath):
            os.makedirs(self.projectDBPath)
        if not os.path.exists(self.projectDBFile):
            # offer to create common tables for project
            pass

    def getDBPath(self):
        return self.projectDBPath

    def moveFileToStorage(self,pathToFile):
        # example:
            # the pathToFile should probably come from 
            # os.path.abspath or similar
            # input = "/home/jlmarks/file.csv"
            # os.path.basename(input))
            # 'file.csv'
            # os.path.dirname(input)
            # '/home/jlmarks'

        ts=timeStamp()
        filename=os.path.basename(pathToFile)
        if filename.rfind('.')>0:
            newName=filename[:filename.rfind('.')] + ts + filename[filename.rfind('.'):]
        else:
            newName=ts+filename
        destinationFileLocation=os.path.join(self.projectDBPath,newName)
        shutil.copyfile(pathToFile, destinationFileLocation)
        self.lastFile=destinationFileLocation
        return self.lastFile

    def addNumberingColumnToCSV(self, pathToFile):
        self.lastFile=csvTools.numberRows.addRowNumAsCol(pathToFile)
        return self.lastFile

    def getRandomID(self,size=6, chars=string.ascii_uppercase + string.digits):
        # This is a slight mod of this thread on SO: 
        #  http://stackoverflow.com/a/2257449
        global uniques
        if 'uniques' not in globals():
            uniques = set()
        while True:
            potentialID=''.join(random.choice(chars) for _ in range(size))
            if potentialID not in uniques:
                uniques.add(potentialID)
                break
        return potentialID
