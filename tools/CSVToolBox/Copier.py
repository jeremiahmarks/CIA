#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-24 16:10:08
# @Last Modified 2015-05-26
# @Last Modified time: 2015-05-26 01:51:43

import os
import csv
import CIA.tools.credentials

class Copier(object):
    """Extensible class (Perhaps should be a imaginary 
    object, whatever those are called.) As a standalone,
    will accept the path to a csv file. It will then open
    the file and copy it to the specified location. In the
    transition, child classes will either manipulate of 
    process the information on the way.
    """
    def __init__(self, pathtocsv, destination):
        """Accepts the path to a csv file and a destination
        path. It will then open the csv file as a dictionary
        It will then call the act function
        """
        self.origcsv=os.path.abspath(pathtocsv)
        self.destination=os.path.abspath(destination)


        self.act()

    def act(self):
        """This will have the operating system make the path
        to the destination, if it does not exist
        """
        self.createdestination()
        self.openfiles()
        self.getmanipulators()
        self.outputwriter.writeheader()
        for row in self.inputreader:
            self.outputwriter.writerow(row)
        self.closefiles()

    def createdestination(self):
        """Checks if the path exists to the destination 
        folder. If it does not, it creates it. 
        """
        destFolder=os.path.dirname(os.path.abspath(self.destination))
        if not os.path.isdir(destFolder):
            os.makedirs(destFolder)

    def closefiles(self):
        self.inputcsv.close()
        self.outputcsv.close()

    def openfiles(self):
        self.inputcsv=open(self.origcsv)
        self.outputcsv=open(os.path.abspath(self.destination),'wb+')

    def getmanipulators(self):
        self.inputreader=csv.DictReader(self.inputcsv)
        self.outputwriter=csv.DictWriter(self.outputcsv,self.inputreader.fieldnames)

class addrow(Copier):
    def act(self):
        self.createdestination()
        self.openinputfile()
        self.getinputmanipulator()
        self.inputrows=[]
        for row in self.inputreader:
            row["LOCALID"]=CIA.tools.credentials.getRandomID()
            self.inputrows.append(row)
        self.closeinputfile()
        self.openoutputfile()
        self.newfieldnames=self.inputrows[0].keys()
        self.getoutputmanipulator()
        self.outputwriter.writeheader()
        for eachRow in self.inputrows:
            self.outputwriter.writerow(eachRow)
        self.closeoutputfile()





    def openinputfile(self):
        self.inputcsv=open(self.origcsv)
    def closeinputfile(self):
        self.inputcsv.close()


    def openoutputfile(self):
        self.outputcsv=open(os.path.abspath(self.destination),'wb+')
    def closeoutputfile(self):
        self.outputcsv.close()


    def getinputmanipulator(self):
        self.inputreader=csv.DictReader(self.inputcsv)
    def getoutputmanipulator(self):
        self.outputwriter=csv.DictWriter(self.outputcsv,self.newfieldnames)


# def addRowNumAsCol(pathToCSV, pathtostorage=None):
#     """Accepts the absolute path to a csvFile
#     """
#     if not os.path.exists(pathToCSV):
#         return False
#     filename=os.path.basename(pathToCSV)
#     newFile=os.path.join(os.path.dirname(os.path.abspath(pathToCSV)), "updatedWithRowCounter"+filename)
#     outFile=open(newFile,'wb+')
#     csvFile=open(pathToCSV,'rb+')
#     reader=csv.DictReader(csvFile)
#     allRows=[]
#     for rowNum,row in enumerate(reader):
#         while None in row.keys():
#             garbage=row.pop(None)
#         row["rowNum"]=rowNum
#         allRows.append(row)
#     csvFile.close()
#     allH=set()
#     for eachRow in allRows:
#         now=len(allH)
#         allH.union(set(eachRow.keys()))
#         later=len(allH)
#         if later>now:
#             print allH
#     print allRows[0].keys()
#     writer=csv.DictWriter(outFile, allRows[0].keys())
#     writer.writeheader()
#     for eachRow in allRows:
#         writer.writerow(eachRow)
#     outFile.close()
#     return newFile
