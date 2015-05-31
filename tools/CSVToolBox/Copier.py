#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-24 16:10:08
# @Last Modified 2015-05-29
# @Last Modified time: 2015-05-29 14:09:41

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
        to the destina tion, if it does not exist
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

    def openfiles(self):
        self.openinputfile()
        self.openoutputfile()
    def getmanipulators():
        self.getinputmanipulator()
        self.getoutputmanipulator()
    def closefiles():
        self.closeinputfile()
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

    def readtomem(self):
        """This method opens a CSV file and then reads each
        row and stores the information in a self variable
        """
        # As I make more and more sub classes I keep seeing
        # things that can be made more separate from the
        # child classes.  This, for example.
        self.openinputfile()
        self.getinputmanipulator()
        self.inputrows={}
        for rowNum, eachRow in enumerate(self.inputreader):
            self.inputrows[rowNum]=eachRow
        self.closeinputfile()

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

        for eachrow in self.inputrows:
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
    def act(self):
        self.createdestination()
        self.readtomem()
        self.columnusecount()
        # Now that we have the number of times that each column
        # has a value, we can find all columns that do not
        # have a value and remove them from the column set.
        for columnname in self.colcount.keys():
            if self.colcount[columnname]<1:
                trash=self.colcount.pop(columnname)
        # We have now removed the columns whose count is
        # less than one
        self.newfieldnames=self.colcount.keys()
        print self.newfieldnames
        self.openoutputfile()
        self.getoutputmanipulator()
        self.outputwriter.writeheader() # I am
        for eachrow in self.inputrows.values():
            rowbuilder={}
            for eachcol in self.newfieldnames:
                rowbuilder[eachcol]=eachrow[eachcol]
            self.outputwriter.writerow(rowbuilder)
        self.closeoutputfile()

    def readtomem(self):
        """This method opens a CSV file and then reads each
        row and stores the information in a self variable
        """
        # As I make more and more sub classes I keep seeing
        # things that can be made more separate from the
        # child classes.  This, for example.
        self.openinputfile()
        self.getinputmanipulator()
        self.inputrows={}
        for rowNum, eachRow in enumerate(self.inputreader):
            self.inputrows[rowNum]=eachRow
        self.closeinputfile()

    def columnusecount(self):
        """This method will take set a class variable called
        "colcount" which is a dictionary that will store the
        number of times that each column has a value.

        It will parse through each record in the file and
        make sure that the column exists in the variable.
        If the column name is not a key in the dictionary,
        it will create a key with the same name as the column
        and set its value to zero.

        After it has ensure that the value does exists as a
        key it will check if there are any values in that
        row/column. If it finds something, it will increment
        the counter.
        """
        self.colcount={}
        for eachrow in self.inputrows.keys():
            for eachcolumn in self.inputrows[eachrow]:
                if eachcolumn not in self.colcount.keys():
                    self.colcount[eachcolumn]=0
                if len(self.inputrows[eachrow][eachcolumn].strip())>0:
                    self.colcount[eachcolumn]+=1

class CutMaxsize(Copier):
    """This will initially allow you to cut the file into
    segments with complete rows with each no larger than
    XMB. it will do that by reading each row and verifying 
    that writing it would not put it over the maximum count,
    and then either writing the line immediately, or wait
    until the file is closed and a new one opened. 

    Next iteration should allow the user to pass it a variable 
    OrderImportant(T/F) which which would allow the program
    to reorder the lines in the file to make the fewest files
    possible
    """
    def act():
        self.createdestination()
        self.readtomem()
        charsperrow=[]
        #headings=self.inputrows.keys():
        for eachline in self.inputrows:
            charsinrow=0
            for eachheading in headings:
                charsinrow+=len(eachline[eachheading])
            charsperrow.append(charsinrow)

