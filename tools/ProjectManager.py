#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-05-27 14:53:28
# @Last Modified 2015-05-29
# @Last Modified time: 2015-05-29 18:31:27
import os
import sqlite3
import shutil
from CIA.tools import credentials as creds
## This module will provide the entity that manages the
## project as a whole.
##
##
## Some general "todo"
## Rather than always checking if the file exists, or checking if
## attr X exists, create a function with the try/except and use
## a with statement.
##
##  http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#eafp-vs-lbyl
##  http://stackoverflow.com/a/610923/492549
##  http://effbot.org/zone/python-with-statement.htm

projectsdbname="projects.db"
currentdirectory=os.path.dirname(__file__)
projectsdb=os.path.join(currentdirectory, projectsdbname)

createusertablestmt="""CREATE TABLE users (id  INTEGER PRIMARY KEY, username STRING UNIQUE)"""
createprojectstable="""CREATE TABLE projects (userid int, projectname str, projectpath str, FOREIGN KEY(userid) REFERENCES users(id))"""
createusersindex="""CREATE INDEX usersid ON users (id);"""
createprojectsindex="""CREATE INDEX projectowner ON projects(userid)"""
tablecreator=[createusertablestmt, createprojectstable]
indexcreator=[createusersindex, createprojectsindex]

class PM(object):
    """The PM provides a method to interact with things at
    or above the project level.  It should generally stay out
    of the business that has been relegated to sub modules.
    """
    global tablecreator
    global indexcreator
    global projectsdb
    def __init__(self):
        self.username=os.path.split(os.path.expanduser('~'))[-1]
        ## This should allow us to determine who the user is.
        ## Basically what it does is:
        # os.path.expanduser('~')
        #   expand the relative path to the absolute path
        #   to the user user directory
        # os.path.split() splits the path into multiple
        #   parts based on the value of os.path.sep
        # os.path.split()[-1]
        #   the [-1] returns the value in the last position.
        #   basically, this should be the username
        self.userid=None
        ## by setting this to none at init, I am able to
        ## ensure that it is set before displaying projects.
        self.getuserid()

    def getuserid(self):
        """This will check for the existence of a sqlite3
        file in the current director.  If there is one, it
        will connect to it.  If there is not one, this will
        create one, and then connect to it.
        """
        if not os.path.exists(projectsdb):
            self.database=sqlite3.connect(projectsdb)
            self.cursor=self.database.cursor()
            for eachtable in tablecreator:
                self.cursor.execute(eachtable)
                self.database.commit()
            for eachindex in indexcreator:
                self.cursor.execute(eachindex)
                self.database.commit()
        else:
            self.database=sqlite3.connect(projectsdb)
            self.cursor=self.database.cursor()
        self.cursor.execute("SELECT id FROM users WHERE username = ?", (self.username, ))
        matchingresults=self.cursor.fetchall()
        if len(matchingresults) == 0:
            self.cursor.execute("INSERT INTO users (username) VALUES(?)",(self.username, ))
            self.database.commit()
            self.userid = self.cursor.lastrowid
        else:
            self.userid = matchingresults[0][0]
        print self.userid

    def selectprojects(self):
        """This method will get and return all of the
        projects that the current user owns.
        """
        if not self.userid:
            self.getuserid()
        projectsSelectStatement="""SELECT projectname, projectpath FROM projects WHERE userid = ?"""
        self.cursor.execute(projectsSelectStatement, (int(self.userid), ))
        return self.cursor.fetchall()

    def createproject(self, projectname):
        projectpath = os.path.join(currentdirectory, projectname)
        projectCreateStatement="""INSERT INTO projects (userid, projectname, projectpath) VALUES(?, ?, ?)"""
        self.cursor.execute(projectCreateStatement, (int(self.userid), str(projectname), str(projectpath)))
        self.database.commit()
        print self.selectprojects()

    def loadproject(self, projectname):
        projectpathStmt="""SELECT projectpath FROM projects WHERE projectname = ?"""
        self.cursor.execute(projectpathStmt,(str(projectname), ))
        projectpath=self.cursor.fetchall()[0][0]
        return Manager(projectpath)
        # if not os.path.exists(projectpath):
        #     os.makedirs(projectpath)
        # projectdb=os.path.join(projectpath, projectname + ".db")

        # if not os.path.exists(projectdb):
        #     self.database=sqlite3.connect(projectdb)
        #     self.cursor=self.database.cursor()
        #     createfilestablestmt="""CREATE TABLE files (id  STRING, filename STRING UNIQUE)"""
        #     self.cursor.execute(createfilestablestmt)
        #     self.database.commit()
        # else:
        #     self.database=sqlite3.connect(projectdb)
        #     self.cursor=self.database.cursor()


class Manager(object):
    """This is the Manager class, it is different from the 
    ProjectManager class in that it manages the individual 
    projects while the ProjectManager manages the global set
    of projects.
    """
    def __init__(self, pathToProject):
        self.projectFolder=os.path.dirname(pathToProject)
        self.databaseFile=os.path.join(pathToProject, 
            self.projectFolder.split(os.path.sep)[-1]+'.db')
        if not os.path.exists(self.projectFolder):
            os.makedirs(self.projectFolder)
        if not os.path.exists(self.databaseFile):
            self.database=sqlite3.connect(self.databaseFile)
            self.cursor=self.database.cursor()
            createfilestablestmt="""CREATE TABLE files (id  STRING, filename STRING UNIQUE)"""
            self.cursor.execute(createfilestablestmt)
            self.database.commit()
        else:
            self.database=sqlite3.connect(self.databaseFile)
            self.cursor=self.database.cursor()

    def getfiles(self):
        setfilesstmt="""SELECT id filename FROM files"""
        self.cursor.execute(setfilesstmt)
        return self.cursor.fetchall()

    def addfile(self, pathtofile):
        fileid=creds.getRandomID()
        filename = os.path.basename(pathtofile)
        print os.path.join(os.path.abspath(self.projectFolder), filename)
        shutil.copy(pathtofile, os.path.join(os.path.abspath(self.projectFolder), filename))
        addfiletofiles="INSERT INTO files (id, filename) VALUES (?, ?)"
        self.cursor.execute(addfiletofiles, (fileid, filename))
        self.database.commit()



