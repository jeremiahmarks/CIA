#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-24 17:16:12
# @Last Modified 2015-05-24
# @Last Modified time: 2015-05-24 18:14:16
from CIA.storeroom import recordsManager
import os
import datetime
import csv
import parseMagic
import uglyObjects

class fileWorker(recordsManager.Worker):
    def prepare(self, filePath):
        timeStamp=datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
        self.files={}
        self.files['originalCSV']=filePath
        filename=os.path.basename(os.path.abspath(filePath))
        foldername=os.path.join(os.path.dirname(os.path.abspath(filePath)),'parsing')
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        workingName=self.getRandomID()+".csv"
        outFile=os.path.join(foldername,workingName)
        if 'project' in globals():
            logfilePrefix=project
        else:
            logfilePrefix=self.getRandomID()
        logFolder=os.path.join(foldername,'log')
        logFile=os.path.join(logFolder, logfilePrefix + filename)
        if not os.path.exists(logFolder):
            os.makedirs(logFolder)
        if not os.path.exists(logFile):
            open(logFile,'wb+').close()
        self.logger=open(logFile, 'a')
        self.logger.write('logger checking in\n' + timeStamp + '\n' + __file__ + "\n" + filePath + "\n" )

    def parseCSV(self):
        parser=parseMagic.uglyStyle()
        rowHolder={}
        self.files["parsed"]={}
        reader=csv.DictReader(open(self.files['originalCSV'], 'rb'))
        for rownum, row in enumerate(reader):
            rowType=parser.getRowType(row)
            if rowType not in rowHolder.keys():
                rowHolder[rowType]={}
            rowHolder[rowType][rownum]=row

            if rowType=="product":
                thisProduct=parser.parseProductRow(row)

            if rowType=="skuPricing":
                thisSku=parser.parseSkuRow(row,thisProduct.options)

            if rowType=="pricingRule":
                thisPricing=parser.parsePricingRow(row, thisProduct.options)

            if rowType=="option":
                thisOption=parser.parseOptionRow(row, thisProduct.options)

        if rowHolder:
            for eachType in rowHolder.keys():
                if eachType not in self.files["parsed"].keys():
                    self.files["parsed"][eachType]=''
                if len(rowHolder[eachType])>0:
                    timestamp=datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
                    self.files["parsed"][eachType]=os.path.join(self.folPath, eachType+".csv")
                    headers=rowHolder[eachType][rowHolder[eachType].keys()[0]].keys()
                    print headers
                    quickWriterFile=open(self.files["parsed"][eachType], 'wb+')
                    quickWriter=csv.DictWriter(quickWriterFile,['rowNumber'] + headers)
                    print quickWriter.fieldnames
                    quickWriter.writeheader()
                    for eachRowNum in rowHolder[eachType].keys():
                        rowHolder[eachType][eachRowNum]['rowNumber']=eachRowNum
                        print rowHolder[eachType][eachRowNum]
                        quickWriter.writerow(rowHolder[eachType][eachRowNum])
                    quickWriterFile.close()
        return rowHolder


