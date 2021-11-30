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

__title__ = "Fascia"
__author__ = "Shiva Reddy"

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
filePath = doc.PathName
fileTitle = doc.Title
head,split,tail = filePath.partition(fileTitle)
fileLocation = head
t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()

###### LET THE HACKING BEGIN ######

roof = doc.GetElement(ElementId(288906))

fascia = doc.GetElement(ElementId(331520))
fasciaFamilySymbol = fascia.Symbol

modelLine = doc.GetElement(ElementId(330441))

print(modelLine)

roofProfiles = roof.GetProfiles()

print(roofProfiles, fascia)

createFascia = doc.Create.NewFamilyInstance(modelLine.GeometryCurve.GetEndPoint[0], fasciaFamilySymbol, roof.LevelId, DB.Structure.StructuralType.NonStructural )
