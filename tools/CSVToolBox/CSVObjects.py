#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-30 23:44:31
# @Last Modified 2015-05-31
# @Last Modified time: 2015-05-31 15:12:22

import csv
import json

class csvfile(object):
    def __init__(self,pathtocsvfile):
        self.csvfile={}
        self.csvfile['pathtocsvfile']=pathtocsvfile
        self.csvfile['columnlocation']={}
        self.csvfile['colsbyname']={}
        self.csvfile['rowsbynumber']={}

    def loadfile(self):
        thisreader=csv.DictReader(file(self.csvfile['pathtocsvfile']))
        for colloc, colname in enumerate(thisreader.fieldnames):
            self.csvfile['columnlocation'][colloc]=csvheadings(colname)
            while colname in self.csvfile['colsbyname'].keys():
                colname=colname+'a'
            self.csvfile['colsbyname'][colname]=colloc
        for row in thisreader:
            self.csvfile['rowsbynumber'][thisreader.line_num]=row

    def writefile(self):
        print self.csvfile['colsbyname'].keys()
        with open(self.csvfile['pathtocsvfile'], 'wb') as f:
            thiswriter=csv.DictWriter(f, self.csvfile['colsbyname'].keys())
            thiswriter.writeheader()
            for eachrowunmber in sorted(self.csvfile['rowsbynumber'].keys()):
                while None in self.csvfile['rowsbynumber'][eachrowunmber].keys():
                    self.csvfile['rowsbynumber'][eachrowunmber].pop(None)
                thiswriter.writerow(self.csvfile['rowsbynumber'][eachrowunmber])

    def addcolumnaftercolumn(self, columnstoadd, columntoaddafter=None, defaultvalue=None):
        if columntoaddafter is None:
            columntoaddafter = sorted(self.csvfile['columnlocation'].keys())[-1]
        numtoadd=len(columnstoadd)
        for offset in range(numtoadd):
            columnlocation=1+offset+columntoaddafter
            colname=columnstoadd[offset]
            while colname in self.csvfile['colsbyname'].keys():
                colname=colname+'a'
            if columnlocation in self.csvfile['columnlocation'].keys():
                originalorder=sorted(self.csvfile['columnlocation'].keys())[columnlocation:]
                while len(originalorder)>0:
                    last, originalorder = originalorder[-1], originalorder[:-1]
                    self.csvfile['columnlocation'][last+1]=self.csvfile['columnlocation'][last]
                    self.csvfile['colsbyname'][self.csvfile['columnlocation'][last+1].name]=last+1
            self.csvfile['columnlocation'][columnlocation]=csvheadings(colname)
            self.csvfile['colsbyname'][colname]=columnlocation
            #Now that the columns have been added to the files column structure,
            #The rowStructure needs to be updated
            for eachrowunmber in self.csvfile['rowsbynumber'].keys():
                if defaultvalue is None:
                    thisvalue=colname
                else:
                    thisvalue=defaultvalue
                self.csvfile['rowsbynumber'][eachrowunmber][colname]=thisvalue

    def removecolumn(self, columnlocation):
        '''This method will remove a column from the csv file
        . It accepts the location of an existing column. It
        will move all later columns in the order up one position
        in the display order, and then pop the largest
        key in the appropriate dictionary, as it should no longer be needed.
        From there, it will pop the values in each row that are no 
        longer needed.
        '''
        colname=self.csvfile['columnlocation'][columnlocation].values
        print colname
        updaterows= sorted([ rownum for rownum in self.csvfile['columnlocation'].keys() if rownum>columnlocation])
        while len(updaterows)>0:
            oldrownum, updaterows = updaterows[0], updaterows[1:]
            self.csvfile['columnlocation'][oldrownum-1] = self.csvfile['columnlocation'][oldrownum]
            # self.csvfile['colsbyname'][self.csvfile['columnlocation'][oldrownum-1]]=oldrownum-1
        ##I am making a couple of assumptions here, but this should 
        ##remove the largest indexed column, which should now be a duplicate.
        self.csvfile['columnlocation'].pop(oldrownum)
        self.generatecolsbyname()
        for rownum in self.csvfile['rowsbynumber'].keys():
            self.csvfile['rowsbynumber'][rownum].pop(colname)

    def generatecolsbyname(self):
        self.csvfile['colsbyname']={}
        for eachcolumnposition in self.csvfile['columnlocation'].keys():
            self.csvfile['colsbyname'][self.csvfile['columnlocation'][eachcolumnposition].values]=eachcolumnposition

    def generatecolstats(self):
        self.csvfile['colstats']={}
        for eachcolumnposition in self.csvfile['columnlocation'].keys():
            self.csvfile['colstats'][eachcolumnposition]={}
            self.csvfile['colstats'][eachcolumnposition]['name']=self.csvfile['columnlocation'][eachcolumnposition].values
            self.csvfile['colstats'][eachcolumnposition]['emptyrows']=0
            self.csvfile['colstats'][eachcolumnposition]['longestrowlength']=0
            self.csvfile['colstats'][eachcolumnposition]['longestrowrows']=[]
            self.csvfile['colstats'][eachcolumnposition]['shortestrowlength']=10**10
            self.csvfile['colstats'][eachcolumnposition]['shortestrowrows']=[]
            self.csvfile['colstats'][eachcolumnposition]['uniquevalues']=set()
            self.csvfile['colstats'][eachcolumnposition]['uniquevaluesused']={}
        eachcolumnposition=None
        for rownum in self.csvfile['rowsbynumber'].keys():
            for eachcolumnposition in self.csvfile['colstats'].keys():
                cellvalue=self.csvfile['rowsbynumber'][rownum][self.csvfile['colstats'][eachcolumnposition]['name']]
                if len(cellvalue) is 0:
                    self.csvfile['colstats'][eachcolumnposition]['emptyrows']+=1
                else:
                    if len(cellvalue)>self.csvfile['colstats'][eachcolumnposition]['longestrowlength']:
                        self.csvfile['colstats'][eachcolumnposition]['longestrowlength']=len(cellvalue)
                        self.csvfile['colstats'][eachcolumnposition]['longestrowrows']=[]
                        self.csvfile['colstats'][eachcolumnposition]['longestrowrows'].append(rownum)
                    elif len(cellvalue)==self.csvfile['colstats'][eachcolumnposition]['longestrowlength']:
                        self.csvfile['colstats'][eachcolumnposition]['longestrowrows'].append(rownum)
                    if len(cellvalue)<self.csvfile['colstats'][eachcolumnposition]['shortestrowlength']:
                        self.csvfile['colstats'][eachcolumnposition]['shortestrowlength']=len(cellvalue)
                        self.csvfile['colstats'][eachcolumnposition]['shortestrowrows']=[]
                        self.csvfile['colstats'][eachcolumnposition]['shortestrowrows'].append(rownum)
                    elif len(cellvalue)==self.csvfile['colstats'][eachcolumnposition]['shortestrowlength']:
                        self.csvfile['colstats'][eachcolumnposition]['shortestrowrows'].append(rownum)
                    if cellvalue not in self.csvfile['colstats'][eachcolumnposition]['uniquevalues']:
                        self.csvfile['colstats'][eachcolumnposition]['uniquevalues'].add(cellvalue)
                        self.csvfile['colstats'][eachcolumnposition]['uniquevaluesused'][cellvalue]=[]
                    self.csvfile['colstats'][eachcolumnposition]['uniquevaluesused'][cellvalue].append(rownum)








class csvheadings(object):
    def __init__(self,values):
        '''changed from just the name to values so that I 
        can pass it both the column name and its location
        in one dict
        '''
        self.values=values
        # self.heading['name']={}
    #     self.heading['name']['namefromfile']=name
    #     self.heading['stats']={}
    #     #self.heading['stats']={}


class csvrow(object):

    def __init__(self, dictofrowdata):
        self.row={}
        self.row.update(dict(dictofrowdata))



