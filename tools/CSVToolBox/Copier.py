#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-24 16:10:08
# @Last Modified 2015-05-26
# @Last Modified time: 2015-05-26 11:03:13

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

class ColAdder(Copier):
    """Col. Adder will add a new columd to your CSV file and
    populate it with a randomly generated string.
    Since it is an extension of Copier, when this class is
    called it is initialiaed by the Copier __init__, which
    then calls this classes act function, which behaves
    differently than the originals.
    """
    def act(self):
        self.createdestination()
        self.openinputfile()
        self.getinputmanipulator()
        self.inputrows=[]
         # Ensures that the destination is created then
         # opens the input file and gets a CSV Dictreader
         #for it.
        for row in self.inputreader:
            row["LOCALID"]=CIA.tools.credentials.getRandomID()
            self.inputrows.append(row)
            # This for loop basically adds a key and value
            # for that key to each record from the input file
        self.closeinputfile()
        self.openoutputfile()
        # Close the input, then open the output file
        # This should mean that the method can use the same
        # File.

        self.newfieldnames=self.inputrows[0].keys()
        self.getoutputmanipulator()
        self.outputwriter.writeheader()
        # Here we get new list of headers, get an output
        # writer, and have it add the headers (fieldnames)
        # to the output CSV

        for eachRow in self.inputrows:
            self.outputwriter.writerow(eachRow)
            # Writing the new CSV file to file.
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


class ColCleaner(Copier):
