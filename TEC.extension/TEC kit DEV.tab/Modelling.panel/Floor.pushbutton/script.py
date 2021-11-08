# Floor from Rooms- V1 - </ShivaReddy>
import os
import clr

from pyrevit.framework import List, wpf, Controls, Imaging
from pyrevit.revit.ui import *
from pyrevit import revit, DB, UI, forms
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
# from Autodesk.Revit.DB import FilteredElementCollector, Transaction, Level, Element, SpatialElement, FloorType
# from Autodesk.Revit import UI
# from Autodesk.Revit import DB
from rpw.ui.forms import CommandLink, TaskDialog, Alert


__title__ = "Floor from Room"
__author__ = "Shiva Reddy"

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
t = Transaction(doc)

###### LET THE HACKING BEGIN ######

def createFloor(thisRoom, floorTypeId, currentLevelId,isStructural):
    thisRoomId = thisRoom.Id
    thisRoomName = Element.Name.__get__(thisRoom)

    spatialElementBoundaryOptions = SpatialElementBoundaryOptions()

    myBoundaries = []
    myCurves = []
    myCurveArray = CurveArray()
    myCurveLoop = CurveLoop()

    myBoundaryList = thisRoom.GetBoundarySegments(spatialElementBoundaryOptions)
    for boundary in myBoundaryList[0]:
    	myBoundaries.append(boundary)
    	myCurve = boundary.GetCurve()
    	myCurves.append(myCurve)
    	myCurveArray.Append(myCurve)
        myCurveLoop.Append(myCurve)
    
    # Floor.Create(doc, myCurveLoop, floorTypeId, currentLevelId)
    floor = doc.Create.NewFloor(myCurveArray, floorTypeId,currentLevelId,isStructural)
    return floor

def getRoomsCreateFloors():

    active = doc.ActiveView
    level = active.LookupParameter("Associated Level")

# Checking if the current view is anything other than FloorPlan
    if level == None:
        Alert("Open FloorPlanView and select the button again", title="That is why you fail",header ="Only Jedi's can draw Floor's in any View", exit= True)

# If Its not a FloorPlan (Because 'Assosiated Level' parameter is only there in FloorPlan view)
    else:
        lvlCollector = FilteredElementCollector(doc).OfClass(Level).ToElements()
        for lvl in lvlCollector:
            if lvl.Name == level.AsString():
                #Giving this variable the element itself, becuase CreateFloor() function needs the element itself
                presentLevel = lvl
                # presentId = lvl.Id

        roomCollector = FilteredElementCollector(doc).WhereElementIsNotElementType().OfClass(SpatialElement)
        currentViewRooms = []

        for room in roomCollector:
            #Checks |>| Location (checking if it is present in the active Design Option) |>| Type is a Room |>| Room's LevelId is the Current Level's Id
            if (room.Location != None) and (str(room.GetType()) == "Autodesk.Revit.DB.Architecture.Room") and (room.LevelId == presentLevel.Id):
                currentViewRooms.append(room)
            
        
        finalCurrentViewRooms = forms.SelectFromList.show([Element.Name.__get__(i) for i in currentViewRooms], title ="Select the Rooms to create Floors for", button_name = "OK", multiselect = True)

        floorTypes = FilteredElementCollector(doc).OfClass(FloorType).ToElements()
        floorTypeNames = []

        for i in floorTypes:
            typeName = Element.Name.__get__(i)
            if typeName not in floorTypeNames:
                floorTypeNames.append(typeName)

        nameOfChosenFloorType = forms.CommandSwitchWindow.show(floorTypeNames, message = "Pick Type of Floor")
        
        for i in floorTypes:
            if (Element.Name.__get__(i) == nameOfChosenFloorType):
                #Giving this variable the element itself, becuase CreateFloor() function needs the element itself
                chosenFloorType = i

                chosenFloorTypeThickness = chosenFloorType.LookupParameter("Default Thickness").AsDouble()
                # print(chosenFloorTypeThickness)
                # chosenFloorTypeId = i.Id

# Reporting the Final Rooms after filtering out, and the FloorType chosen to apply to these Rooms
        print("{}->{}. The Chosen floor type is->{}".format("The total rooms found are",len(currentViewRooms), nameOfChosenFloorType))
        for i in finalCurrentViewRooms:
            print(finalCurrentViewRooms.index(i)+1, i)
            # print(finalCurrentViewRooms.index(i)+1, Element.Name.__get__(i))

#TaskDialog to get Yes or No, on continuing to create Floor's based off of Rooms Boundaries

        if chosenFloorType != None:
            # This is the start of creatign Floor's
            t.Start("Create Floors Using Rooms")
            for room in currentViewRooms:
                thisFloor = createFloor(room,floorTypeId= chosenFloorType,currentLevelId=presentLevel, isStructural=False)
                ((thisFloor.GetParameters("Height Offset From Level"))[0]).Set(chosenFloorTypeThickness)
            t.Commit()

        print("Successfully Created all Floors at these Rooms, with {} ".format(nameOfChosenFloorType))

getRoomsCreateFloors()
