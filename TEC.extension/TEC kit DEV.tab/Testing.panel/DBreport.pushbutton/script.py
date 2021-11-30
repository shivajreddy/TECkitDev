#Automate FLoor Boundaries - V2.2 - </ShivaReddy>
import os
import clr

from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI import Selection

from pyrevit import UI
from pyrevit import revit, DB
from pyrevit import forms
# from pyrevit.form import WPFWindow
from pyrevit.revit.ui import *
from pyrevit.framework import List, wpf, Controls, Imaging

__title__ = "DB report"
__author__ = "Shiva Reddy"

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
filePath = doc.PathName
fileTitle = doc.Title
head, split, tail = filePath.partition(fileTitle)
fileLocation = head
t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()

###### LET THE HACKING BEGIN ######

# Project Information
project_path = filePath
project_title = fileTitle
project_location = fileLocation
project_active_view = doc.ActiveView.Name
shared_param_location = doc.Application.SharedParametersFilename
# project_template =
project_user = doc.Application.Username
project_version = "{0}, {1}".format(doc.Application.VersionName,doc.Application.VersionBuild)

def getProjectInformation():
    print("Project Path: {0}".format(project_path))
    print("Project Title: {0}".format(project_title))
    print("Project Location: {0}".format(project_location))
    print("Project Active View Name: {0}".format(project_active_view))
    print("Shared Parameter Location: {0}".format(shared_param_location))
    print("Project User: {0}".format(project_user))
    print("Project Version: {0}".format(project_version))



docCollector = FilteredElementCollector(doc)

print("total elements in the doc", docCollector.GetElementCount())

allCategories = doc.Settings.Categories


def getAllCategories():
    for cat in allCategories:
        print("Name -> {0} | {1}".format(cat.Name, cat.CategoryType))


# getProjectInformation()

g_p = GlobalParametersManager.GetAllGlobalParameters(doc)

global_parameters = []
for g in g_p:
    e = doc.GetElement(g)
    global_parameters.append(e)
    
def get_global_param_id(param_name):
    for g in global_parameters:
        if g.Name == param_name:
            return g.Id

def get_global_param_value(param_name):
    for g in global_parameters:
        if g.Name == param_name:
            return g.GetValue().Value

print(get_global_param_value("NEIGHBORHOOD"))


def get_sheet(sheet_name):
    for s in sheet_collector:
        if (sheet_name) == (str(s.Name)):
            return s


# allFamilies = FilteredElementCollector(doc).OfClass(type(Family))
allFamilies = FilteredElementCollector(doc).OfClass((Family))


print(allFamilies, allFamilies.GetElementCount())
for famiy in allFamilies:
    print((famiy.Name),(famiy.Id))
    




# cover_page =  get_sheet("COVER PAGE")

# for c in cover_page.Parameters:

#         if c.Definition.Name == "SF - AS DESIGNED - BASEMENT":
#             g_id = get_global_param_id("SF - AS DESIGNED - BASEMENT")
#             c.AssociateWithGlobalParameter(g_id)
