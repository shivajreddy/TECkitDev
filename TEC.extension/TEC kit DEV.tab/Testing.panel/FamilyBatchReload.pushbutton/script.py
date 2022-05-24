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
from pyrevit import forms, revit, DB, script


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

# demo_door_family = "C:\Users\sreddy\Desktop\FamilBatchUpgrader\Door_Hinged_Single_Solid Flush.rfa"
demo_door_family1 = "C:\Users\sreddy\Desktop\FamilBatchUpgrader\otest\Door_Hinged_Single_Solid Flush_testv2.rfa"
demo_door_family2 = "C:\Users\sreddy\Desktop\FamilBatchUpgrader\otest\Door_Hinged_Single_Solid Flush_testv3.rfa"


# Getting all the Door Families in the project
doorFamilies = []

for fam in all_families_in_project:
    # print(fam.Name, fam.FamilyCategory.Name)
    if (fam.FamilyCategory.Name) == "Doors":
        doorFamilies.append(fam)


# famdoc = app.OpenDocumentFile(demo_door_family)

# familyManager = doc.FamilyManager
# print(familyManager.Types)

class FamilyLoaderOptionsHandler(DB.IFamilyLoadOptions):
    # t.Start("Modifying family")
    print("started from here")
    def OnFamilyFound(self, familyInUse, overwriteParameterValues):
        print("reached here")
        # This overwriteParameterValues if set to True, it will overwrite the family
        overwriteParameterValues = True
        return True
    def OnSharedFamilyFound(self,
                            sharedFamily, #pylint: disable=W0613
                            familyInUse, #pylint: disable=W0613
                            source, #pylint: disable=W0613
                            overwriteParameterValues): #pylint: disable=W0613
        source = DB.FamilySource.Family
        overwriteParameterValues = True
        print("reached here too")
        return True
    # t.Commit()
    print("ended here")

# Working
famloadhandler = FamilyLoaderOptionsHandler()
ret_ref = clr.Reference[DB.Family]()


# revit.doc.LoadFamily('path\family.rfa') ->Works
p = revit.doc.LoadFamily(demo_door_family1, famloadhandler)
print("result of second p", p)


logger = script.get_logger()

class myFamilyLoader():
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path).replace(".rfa", "")

    @property
    def is_loaded(self):
        collector = DB.FilteredElementCollector(revit.doc).OfClass(DB.Family)
        condition = (x for x in collector if x.Name == self.name)
        return next(condition, None) is not None

    def load_all(self):
        """ Loads family and all its symbols. """
        with revit.Transaction('Loaded {}'.format(self.name)):
            try:
                revit.doc.LoadFamily(self.path)
                logger.debug(
                    'Successfully loaded family: {}'.format(self.name))
            except Exception as load_err:
                logger.error(
                    'Error loading family symbol from {} | {}'
                    .format(self.path, load_err))
                raise load_err


# THIS WORKS, cause it uses LoadFamily Symbol to load
t.Start("v3.1Load all types of test fam")
revit.doc.LoadFamily(demo_door_family2, famloadhandler, ret_ref)
t.Commit()

family = myFamilyLoader(demo_door_family1)
print(family)
print(type(family))
# family.load_selective()
# family.load_all()


# temp_family_symbols = family.get_symbols
# print(temp_family_symbols)
# print(type(temp_family_symbols))
# family_symbols = list(temp_family_symbols)
# for fs in family_symbols:
#     print(fs)

# Loads all types of this family
# x = family.load_all()
# print("result of x", x)

# Testing
def load_family(family_file, doc=None):
    mlogger.debug('Loading family from: %s', family_file)
    ret_ref = clr.Reference[DB.Family]()
    return doc.LoadFamily(family_file, famloadhandler, ret_ref)
    # return doc.LoadFamily(family_file, FamilyLoaderOptionsHandler(), ret_ref)

# y = load_family(demo_door_family, doc)
# print("result of y", y)
