#Automate FLoor Boundaries - V2.2 - </ShivaReddy>
import os
import clr
import sys

# Adding the CommunityStandards Module
communityStandardsPath = r'T:\04 - Projects\03_Community Standards'
sys.path.insert(0, communityStandardsPath)
from CommunityStandards import ReadersBranch

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

#### Setting the Community ####
if (get_global_param_value("NEIGHBORHOOD")) == "READERS BRANCH":
    Community = ReadersBranch
print("Community -> {0}".format(get_global_param_value("NEIGHBORHOOD")))


def get_sheet(sheet_name):
    for s in sheet_collector:
        if (sheet_name) == (str(s.Name)):
            return s


allFamilies = FilteredElementCollector(doc).OfClass(Family)
allFamilyInstances = FilteredElementCollector(doc).OfClass(FamilyInstance)


all_families_in_project = []
all_family_instances_in_project = []

for f in allFamilyInstances:
    all_family_instances_in_project.append(f)
    # print(f.Name)

for family in allFamilies:
    all_families_in_project.append(family)

# Checking FasciaInstances
def FasciaInstancesCheck(family_instances):
    resultFascia = []
    resultFreize = []
    FinalResults = []

    target_fascia = ReadersBranch.fascia
    target_frieze = ReadersBranch.frieze
    index = 0
    fasciaCount = 0
    friezeCount = 0
    for item in family_instances:
       
        if "Fascia" in item.Name:
            current = item.Name
            current_Fascia = (current[((current.index('Fascia'))-4):(current.index('Fascia'))-1])
            if (current_Fascia == target_fascia):
                print("Index={0} | {1}-> {2} VS. Readers{3}".format((index), (fasciaCount), (item.Name), (ReadersBranch.fascia)))
                resultFascia.append(True)
            else:
                resultFascia.append(False)
            fasciaCount = fasciaCount + 1
        if "Frieze" in item.Name:
            current = item.Name
            current_Frieze = (current[((current.index('Frieze'))-4):(current.index('Frieze'))-1])
            if (current_Frieze == target_frieze):
                print("Index={0} | {1}-> {2} VS. Readers{3}".format((index), (friezeCount), (item.Name), (ReadersBranch.fascia)))
                resultFreize.append(True)
            else:
                resultFreize.append(False)
            friezeCount = friezeCount + 1
        index = index + 1

    if (False in resultFascia):
        FinalResults.append("Fail - Not All Fascia Boards are upto Community Standards")
    elif ((False in resultFreize)):
        FinalResults.append("Fail - Not All Frieze Boards are upto Community Standards")
    else:
        FinalResults.append("All Frieze & Frieze boards Passed Comparision Test against Community Standards")

    return FinalResults

print(FasciaInstancesCheck(all_family_instances_in_project))





temp_path = "C:\Users\sreddy\Desktop\TempFamilyFiles"

# some_family = all_families_in_project[269]
# print(some_family.Name)
# famdoc = doc.EditFamily(some_family)
# famdoc.SaveAs(temp_path)
# famdoc.Close(False)



# print(some_family.path)


file_size = os.path.getsize("C:\Users\sreddy\Desktop\SRL-Lot-011-03-RB_L3X-30_V04.rvt")

def fileSizeMB(file_path):
    file_size = os.path.getsize(file_path)
    file_size_mb = file_size / 1000000
    return file_size_mb

print("The file_size in MB -> {0} MB".format(file_size/1000000))

# cover_page =  get_sheet("COVER PAGE")

# for c in cover_page.Parameters:

#         if c.Definition.Name == "SF - AS DESIGNED - BASEMENT":
#             g_id = get_global_param_id("SF - AS DESIGNED - BASEMENT")
#             c.AssociateWithGlobalParameter(g_id)



