#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-31 17:03:35
# @Last Modified 2015-05-31
# @Last Modified time: 2015-05-31 20:24:37
import os
def getexistingprojects(workflowobject):
    workflowobject.currentprojects=[name for name in os.listdir(os.path.abspath(workflowobject.folderStoragePath)) if os.path.isdir(os.path.join(os.path.abspath(workflowobject.folderStoragePath), name))]
    htmlelement="""<select name="existingprojectname" size='7'>"""
    for eachproject in workflowobject.currentprojects:
        htmlelement=htmlelement+"\n"+"""<option value="%s">%s</option>"""%(eachproject,eachproject) + "\n"
    htmlelement=htmlelement+"</select>\n"
    return htmlelement

def projectselectionscreen(workflowobject):
    existingprojectsashtmlelement=getexistingprojects(workflowobject)
    returnval= """<html>
      <head></head>
      <body>
        <form method="post" action="setprojectname">"""
    returnval=returnval+existingprojectsashtmlelement
    returnval=returnval+"""
          <input type="text" name="newprojectname" />
          <button type="submit">Set Project Name</button>
        </form>
      </body>
    </html>"""
    return returnval

def projectmainmenu():
    return"""
    <div id='projectmainmenu', class='buttonmenu'>
        <form method="post" action="projectmainmenu">
            <input type="submit" name="projectaction" value="AddFile">
        </form
    </div>
        """

def getallprojectfiles(workflowobject):
    csvfiles=[name for name in os.listdir(os.path.abspath(workflowobject.project["projectFolderPath"])) if os.path.isfile(os.path.join(os.path.abspath(workflowobject.project["projectFolderPath"]), name)) and name[-3:].lower() == 'csv']
    jsonfiles=[name for name in os.listdir(os.path.abspath(workflowobject.project["projectFolderPath"])) if os.path.isfile(os.path.join(os.path.abspath(workflowobject.project["projectFolderPath"]), name)) and name[-4:].lower() == 'json']
    htmlelement="""<form method="post" action="loadfile">
        <select name="filetoload" size='7'>"""
    htmlelement+="""\n<optgroup label="CSV">"""
    for eachcsv in csvfiles:
        htmlelement+="""<option value="%s">%s</option>\n"""%(eachcsv,eachcsv)
    htmlelement+="""</optgroup></select>"""
    htmlelement+="""<button type="submit">LoadFile</button></form>\n"""
    return htmlelement

def generatecsvmenu():
    returnval="""<div><form method="post" action="csvmenu">
    <input type="submit" name="csvaction" value="update"
    </form></div>"""
    return returnval

def generatecsvdefaultview(acsvfile):
    returnval="""<div class="csvviewer">"""
    returnval+=generatecsvmenu()
    for eachposition in sorted(acsvfile.csvfile['colstats'].keys()):
        colbuilder="""<div class="csvcolstats">"""
        colbuilder+="""<div class="colpos">ColOrder: %s</div>"""%(str(eachposition))
        colbuilder+="""<div class="colname">ColName: %s</div>"""%(str(acsvfile.csvfile['colstats'][eachposition]['name']))
        colbuilder+="""<div class="emptyrows">MTRows: %s</div>"""%(str(acsvfile.csvfile['colstats'][eachposition]['emptyrows']))
        colbuilder+="""<div class="longestcell">longestVal: %s</div>"""%(str(acsvfile.csvfile['colstats'][eachposition]['longestrowlength']))
        colbuilder+="""</div>"""
        returnval+=colbuilder
    returnval+="</div>"
    return returnval

def projectmainscreen(workflowobject):
    returnval="""<html>
      <head></head>
      <body>"""
    returnval=returnval+projectmainmenu()
    returnval+="""<form method="post" action="loadfile">"""
    returnval+=getallprojectfiles(workflowobject)
    returnval+="</form>"
    if 'workingfile' in workflowobject.project.keys():
         returnval+=generatecsvdefaultview(workflowobject.project['workingfile'])
    returnval+="</body></html>"
    return returnval

