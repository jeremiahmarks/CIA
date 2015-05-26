#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-25 15:46:53
# @Last Modified 2015-05-25>
# @Last Modified time: 2015-05-25 16:03:41
import csv

def deleteEmptyColumns(pathToFile):
    origFile=open(pathToFile, 'rb')
    reader=csv.DictReader(origFile)
    headers=reader.headers
    stats={}
    rows=[]
    for eachHeader in headers:
        stats[eachHeader]=0
    for row in reader:
        rows.append(row)
        for col in headers:
            if len(row[col].strip(' '))>0:
                stats[col]+=1
    origFile.close()
    nrows=[]
    nheaders=[]
    for eachcol in stats.keys():
        if stats[eachcol]>0:
            nheaders.append(eachcol)
    for eachrow in rows:
        newRowData={}
        for eachnheader in nheaders:
            newRowData[eachnheader]=eachrow[eachnheader]
        nrows.append(newRowData)
    nfile=pathToFile[:-4]+'noEmptyCols' + pathToFile[-4:]
    nFile=open(nfile)
    nwriter=csv.DictWriter(nFile,nheaders)
    nwriter.writeheader()
    nwriter.writerows(nrows)
    nFile.close()