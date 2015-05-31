#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-30 23:44:31
# @Last Modified 2015-05-31
# @Last Modified time: 2015-05-31 10:37:26

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
                colname=colname+"1"
            self.csvfile['colsbyname'][colname]=colloc
        for row in thisreader:
            self.csvfile['rowsbynumber'][thisreader.line_num]=row

    def writefile(self):
        with open(self.csvfile['pathtocsvfile'], 'wb') as f:
            thiswriter=csv.DictWriter(f, self.csvfile['colsbyname'].keys())
            thiswriter.writeheader()
            for eachrowunmber in sorted(self.csvfile['rowsbynumber'].keys()):
                thiswriter.writerow(self.csvfile['rowsbynumber'][eachrowunmber])

    def __repr__(self):
        return json.dumps(self.__dict__)



class csvheadings(object):
    def __init__(self,name):
        self.name=name.lower()
        # self.heading["name"]={}
    #     self.heading['name']['namefromfile']=name
    #     self.heading['stats']={}
    #     #self.heading['stats']={}
    def __repr__(self):
        return json.dumps(self.__dict__)


class csvrow(object):

    def __init__(self, dictofrowdata):
        self.row={}
        self.row['originaldict']=dict(dictofrowdata)
    def __repr__(self):
        return json.dumps(self.__dict__)


