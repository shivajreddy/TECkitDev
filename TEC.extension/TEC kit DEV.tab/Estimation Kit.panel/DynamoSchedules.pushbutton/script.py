import os
import clr
import sys
import collections

sys.path.append("C:\Program Files\IronPython 2.7\Lib")

from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

clr.AddReference('System')
clr.AddReference("RevitServices")
clr.AddReference("RevitAPI")
clr.AddReference("DynamoRevitDS")
# print(clr.References)
import Dynamo


# from pyrevit import UI
from pyrevit import api
from pyrevit.api import ApplicationServices
from pyrevit import script
from pyrevit import framework
from pyrevit.framework import wpf, Controls, Imaging

__title__ = "Dynamo Script"
__author__ = "Shiva Reddy"

doc = __revit__.ActiveUIDocument.Document
t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()
main_collector = FilteredElementCollector(doc)


commandData = UI.ExternalCommandData

journalData = {}
journalData.update({Dynamo.Applications.JournalKeys.ShowUiKey:str(False)})
journalData.update({Dynamo.Applications.JournalKeys.AutomationModeKey:str(True)})
journalData.update({Dynamo.Applications.JournalKeys.DynPathKey:""})
journalData.update({Dynamo.Applications.JournalKeys.DynPathExecuteKey:str(True)})
journalData.update({Dynamo.Applications.JournalKeys.ForceManualRunKey:str(False)})
journalData.update({Dynamo.Applications.JournalKeys.ModelShutDownKey:str(True)})
journalData.update({Dynamo.Applications.JournalKeys.ModelNodesInfo:str(False)})

print(journalData, "type of this is ", type(journalData))

dynamoRevit = Dynamo.Applications.DynamoRevit()

dynamoRevitCommandData = Dynamo.Applications.DynamoRevitCommandData()

dynamoRevitCommandData.Application = UI.UIApplication(__revit__.Application)

dynamoRevitCommandData.JournalData = journalData

dynamo_path = R"C:\Users\sreddy\Desktop\ExportEstimatesToExcelV6.2-stable.dyn"

dynamoRevit.ExecuteCommand(dynamoRevitCommandData)

# dynamoRevit.RevitDynamoModel.OpenFileFromPath(journalData, True)
# dynamoRevit.RevitDynamoModel.ForceRun()

print("END")
# connected dynamo, but no control to UI and Output Window