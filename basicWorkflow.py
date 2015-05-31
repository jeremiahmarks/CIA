#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-30 21:20:58
# @Last Modified 2015-05-30
# @Last Modified time: 2015-05-30 23:26:32

import os
from tools.CSVToolBox import Copier
thisfile=__file__
thisDir=os.path.dirname(os.path.abspath(thisfile))
folderStoragePath=os.path.join(os.path.abspath(thisDir), 'folderStorage')


class ProjectWorkflow(object):
    def __init__(self):
        self.project={}
        self.project["name"]=str(raw_input("\nPlease enter project name\n").strip())
        self.project["projectFolderPath"]=os.path.join(os.path.abspath(folderStoragePath), self.project["name"])
        if not os.path.exists(os.path.abspath(self.project["projectFolderPath"])):
            os.makedirs(os.path.abspath(self.project["projectFolderPath"]))


    def menu(self):
        self.project["menu"]={}
        self.project["menu"][1] = "Load the files in the projects directory"
        self.project['menu'][2] = 'add a file to the project'

    def loadfolderintoproject(self):
        if 'files' not in self.project.keys():
            self.project['files']={}
        os.chdir(self.project["projectFolderPath"])
        csvfile=[f for f in os.listdir(self.project['projectFolderPath']) if f[-3:]=="csv"]
        for eachfile in csvfile:
            if eachfile not in self.project['files'].keys():
                self.project['files'][eachfile]={}
        for eachfile in self.project['files'].keys():
            if eachfile not in csvfile:
                self.project['files'].pop(eachfile)

    def addfiletoproject(self):
        filetoadd=str(raw_input("\nPlease enter the path to the new file\n").strip())
        desttoprojectfolder=os.path.join(os.path.abspath(self.project['projectFolderPath']), os.path.basename(os.path.abspath(filetoadd)))
        thiscopier=Copier.ColCleaner(filetoadd, desttoprojectfolder)

if __name__ == '__main__':
    a=ProjectWorkflow()
    a.addfiletoproject()


