#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-31 15:36:29
# @Last Modified 2015-05-31
# @Last Modified time: 2015-05-31 20:20:04

import cherrypy
import os
import Tkinter as tk
from tkFileDialog import askopenfilename


from tools.CSVToolBox import Copier, CSVObjects
import webviews
thisfile=__file__
thisDir=os.path.dirname(os.path.abspath(thisfile))
folderStoragePath=os.path.join(os.path.abspath(thisDir), 'folderStorage')

class WebWorkFlow(object):
    def __init__(self):
        self.project={}
        self.thisDir=thisDir
        self.folderStoragePath=folderStoragePath


    @cherrypy.expose
    def index(self):
        if 'name' not in self.project.keys():
            return webviews.projectselectionscreen(self)
        else:
            print self.project['name']
            return webviews.projectmainscreen(self)

    @cherrypy.expose
    def setprojectname(self, newprojectname=None, existingprojectname=None):
        if len(newprojectname)>0:
            self.project['name']=newprojectname
            self.project["projectFolderPath"]=os.path.abspath(os.path.join(os.path.abspath(folderStoragePath), self.project["name"]))
            if not os.path.exists(os.path.abspath(self.project["projectFolderPath"])):
                os.makedirs(os.path.abspath(self.project["projectFolderPath"]))
        else:
            self.project['name']=existingprojectname
            self.project["projectFolderPath"]=os.path.abspath(os.path.join(os.path.abspath(folderStoragePath), self.project["name"]))
            if not os.path.exists(os.path.abspath(self.project["projectFolderPath"])):
                os.makedirs(os.path.abspath(self.project["projectFolderPath"]))
        return self.index()

    @cherrypy.expose
    def projectmainmenu(self, projectaction=None):
        if projectaction is not None:
            if projectaction == "AddFile":
                newfilename=self.getnewfilename()
                desttoprojectfolder=os.path.join(os.path.abspath(self.project['projectFolderPath']), os.path.basename(os.path.abspath(newfilename)))
                thiscopier=Copier.ColCleaner(newfilename, os.path.abspath(desttoprojectfolder))
            else:
                pass
        return self.index()

    @cherrypy.expose
    def loadfile(self, filetoload):
        if filetoload is not None:
            if 'files' not in self.project.keys():
                self.project['files']={}
            self.project['files'][filetoload]=CSVObjects.csvfile(os.path.join(self.project["projectFolderPath"], filetoload))
            self.project['files'][filetoload].loadfile()
            self.project['files'][filetoload].generatecolstats()
            self.project['workingfile']=self.project['files'][filetoload]
        else:
            pass
        return self.index()

    def getnewfilename(self):
        root=tk.Tk()
        root.withdraw()
        return askopenfilename()

def main():
    cherrypy.quickstart(WebWorkFlow())

if __name__ == '__main__':
    main()