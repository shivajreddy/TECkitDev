#Automate FLoor Boundaries - V2.2 - </ShivaReddy>
import os
import clr
import sys

# from Autodesk.Revit import DB
# from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI import Selection

from pyrevit import UI
from pyrevit import DB
from pyrevit import revit
from pyrevit import forms


# Modeule to import Families
from family_utils import FamilyLoader
from pyrevit.coreutils.logger import get_logger
mlogger = get_logger(__name__)

# from pyrevit.form import WPFWindow
from pyrevit.revit.ui import *
from pyrevit.framework import List, wpf, Controls, Imaging

__title__ = "Family Batch Reload"
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



docCollector = FilteredElementCollector(doc)

print("total elements in the doc", docCollector.GetElementCount())

allCategories = doc.Settings.Categories

def getAllCategories():
    for cat in allCategories:
        print("Name -> {0} | {1}".format(cat.Name, cat.CategoryType))



allFamilies = FilteredElementCollector(doc).OfClass(Family)
allFamilyInstances = FilteredElementCollector(doc).OfClass(FamilyInstance)


all_families_in_project = []
all_family_instances_in_project = []

for f in allFamilyInstances:
    all_family_instances_in_project.append(f)
    # print(f.Name)

for family in allFamilies:
    all_families_in_project.append(family)



# temp_path = "C:\Users\sreddy\Desktop\TempFamilyFiles"
DoorFamiliesPath = "C:\Users\sreddy\Desktop\FamilBatchUpgrader\Doors"
DoorFamilyList = []
index = []

for file in os.listdir(DoorFamiliesPath):
    if len(file) > 9:
        if (file.endswith(".rfa") and (file[-9] != ".")):
            DoorFamilyList.append(file)
            # DoorFamilyList.append(os.path.join(root, file))
            # print(file)

demo_door_family = "C:\Users\sreddy\Desktop\FamilBatchUpgrader\DoorsTest\Door_Hinged_Single_Solid Flush.rfa"


# Getting all the Door Families in the project
doorFamilies = []

for fam in all_families_in_project:
    # print(fam.Name, fam.FamilyCategory.Name)
    if (fam.FamilyCategory.Name) == "Doors":
        doorFamilies.append(fam)

for i in doorFamilies:
    print(i.Name)
    



# famdoc = app.OpenDocumentFile(demo_door_family)

# familyManager = doc.FamilyManager
# print(familyManager.Types)

class FamilyLoaderOptionsHandler(DB.IFamilyLoadOptions):
    def OnFamilyFound(self, familyInUse, overwriteParameterValues): #pylint: disable=W0613
        """A method called when the family was found in the target document."""
        # overwriteParameterValues = True
        return True

    def OnSharedFamilyFound(self,
                            sharedFamily, #pylint: disable=W0613
                            familyInUse, #pylint: disable=W0613
                            source, #pylint: disable=W0613
                            overwriteParameterValues): #pylint: disable=W0613
        source = DB.FamilySource.Family
        overwriteParameterValues = True
        return True

# Working
famloadhandler = FamilyLoaderOptionsHandler()

print("this is result yp")
# revit.doc.LoadFamily('path/family.rfa') ->Works
print(revit.doc.LoadFamily(demo_door_family, famloadhandler))
family = FamilyLoader(demo_door_family)
x = family.load_all()
print(x)

# Testing
def load_family(family_file, doc=None):
    mlogger.debug('Loading family from: %s', family_file)
    ret_ref = clr.Reference[DB.Family]()
    return doc.LoadFamily(family_file, FamilyLoaderOptionsHandler(), ret_ref)






# family.doc.LoadFamily(doc)


# fam_doc = revit.doc.EditFamily()


# model = revit.RevitModelFile(demo_door_family)
# print(model)
# print(doc.LoadFamily(demo_door_family, famloadhandler))



# hostapp = pyrevit._HostApplication(__revit__)
# uiapp = DocumentManager.Instance.CurrentUIApplication

# family = uidoc.OpenDocumentFile(demo_door_family)
# family = doc.OpenDocumentFile(demo_door_family)
# doc.LoadFamily(demo_door_family, family)


# doc.LoadFamily(demo_door_family, )

# demo_family = doc.EditFamily(demo_door_family)
# loadStatus = doc.LoadFamily(demo_door_family, famloadhandler)
# print(loadStatus)









# t.Commit()