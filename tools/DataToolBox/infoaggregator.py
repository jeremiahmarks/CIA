#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-05-26 13:48:24
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-05-26 18:03:20
import csv

def countuniquevalues(pathtofile):
    """This method accepts the path to a file. From there
    it creates a dictionary, named colvals to hold the
    values for each column.
    It then opens the file and assigns a dictreader to the
    file.
    It will then read each row. On each row it gets a list
    of the column names.  It will make sure that each column
    name is a key in colvals and create and assign an empty
    dict to the column name
    After it has checked the column name, it will then see
    if the cell value has a record in the dictionary.
    If the dict does not, it will create the appropriate key
    and assign it an empty list.
    It will then append the row number to the list.
    """
    colvals={}
    inputfile=open(pathtofile)
    reader=csv.DictReader(inputfile)
    rowCounter=0
    for row in reader:
        rowCounter+=1
        for eachcolumnname in row.keys():
            if eachcolumnname and len(eachcolumnname.strip())>0:
                if eachcolumnname not in colvals.keys():
                    colvals[eachcolumnname]={}
                if len(row[eachcolumnname].strip())>0:
                    if row[eachcolumnname] not in colvals[eachcolumnname].keys():
                        colvals[eachcolumnname][row[eachcolumnname]]=[]
                    colvals[eachcolumnname][row[eachcolumnname]].append(rowCounter)
    inputfile.close()
    # now we have a data structure that looks like this:
        # colvals = {
            # rowheader1: {
                # val1: [1,3,4,7]
                # val2: [2,5,6]
            # }
            # rowheader2: {
                # val3: [1,2,3]
                # val4: [4, 5, 6, 7]
            # }
        # }
    # general stats:
    # len(rowheader1.keys()) will tell you how many unique
    # values there were in the column named rowheader1
    # len(rowheader1[val1]) will tell you how many records
    # have that value in the column
    # Lets find and print that
    colstats={}
    # colstats['colname']=''
    # colstats['uniqval']=int(number of unique values)
    for eachcolumnname in colvals.keys():
        if eachcolumnname not in colstats.keys():
            colstats[eachcolumnname]={}
        for eachvalue in colvals[eachcolumnname].keys():
            colstats[eachcolumnname][eachvalue]=len(colvals[eachcolumnname][eachvalue])
    tabledata=[]
    for eachcol in colstats.keys():
        tabledata.append([eachcol, sorted(colstats[eachcol].items(), key=lambda x: x[1])])
    return tabledata



