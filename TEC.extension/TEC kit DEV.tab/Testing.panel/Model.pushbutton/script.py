# Automate FLoor Boundaries - V1 - </ShivaReddy>
import sys
import os
from collections import namedtuple
# from typing import List
# from typing import _TC

from Autodesk.Revit.DB.Architecture import Room

import rpw
from rpw import doc, uidoc, DB, UI, db, ui

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

from pyrevit import UI
from pyrevit import revit, DB

__title__ = "Model Floors"
__author__ = "Shiva Reddy"

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()

###### LET THE HACKING BEGIN ######

# main_collector = FilteredElementCollector(doc)
# floors = main_collector.OfCategory(BuiltInCategory.OST_Floors)
# print(floors.GetElementCount())
# levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels)
# print(levels.GetElementCount())


# floor_types = []
# level_types = []


# for f in floors:
#     if type(f) == FloorType:
#         floor_types.append(f)
# print("the total no of floor types are", len(floor_types))

# for l in levels:
#     if type(l) == LevelType:
#         level_types.append(l)
# print("the total levels are", len(level_types))

# for l in level_types:
#     print(l, l.Id)
my_wall_id = ElementId(7766205)
my_wall = doc.GetElement(my_wall_id)
print(my_wall)

uid = my_wall.UniqueId
print(uid)
nines = -9999
refString = str.format("{0}:{1}:{2}", uid, nines, 1)

wall_center = Reference.ParseFromStableRepresentation(doc, refString)
print(wall_center)

refString = str.format("{0}:{1}:{2}", uid, nines, 2)
print(Reference.ParseFromStableRepresentation(doc, refString))

refString = str.format("{0}:{1}:{2}", uid, nines, 3)
print(Reference.ParseFromStableRepresentation(doc, refString))

refString = str.format("{0}:{1}:{2}", uid, nines, 4)
print(Reference.ParseFromStableRepresentation(doc, refString))

refString = str.format("{0}:{1}:{2}", uid, nines, 5)
print(Reference.ParseFromStableRepresentation(doc, refString))

refString = str.format("{0}:{1}:{2}", uid, nines, 6)
print(Reference.ParseFromStableRepresentation(doc, refString))

refString = str.format("{0}:{1}:{2}", uid, nines, 7)
print(Reference.ParseFromStableRepresentation(doc, refString))


floorid = ElementId(2552)
levelid = ElementId(8547)
# for f in floor_types:
#     print(f.FamilyName)

first = XYZ(0, -50, 0)
second = XYZ(20, 0, 0)
third = XYZ(20, 15, 0)
four = XYZ(0, 15, 0)
profile = CurveLoop()

profile.Append(Line.CreateBound(first, second))
profile.Append(Line.CreateBound(second, third))
profile.Append(Line.CreateBound(third, four))
profile.Append(Line.CreateBound(four, first))

# t = Transaction(doc)
# t.Start("create floor from API")
# floor = Floor.Create(doc, [profile], floorid, levelid)
# t.Commit()


# Main Selectin
# myselection = ui.Selection()
myselection = revit.get_selection()
selected_items = [e for e in myselection]
selected_items_ids = [item.Id for item in selected_items]

# if not selected_items:
#     TaskDialog.Show("Selection Error", "You should choose some elements to use this tool")
#     sys.exit()

selected_walls = []
selected_lines = []

for e in selected_items:
    if type(e) == ModelLine:
        selected_lines.append(e)

for element in selected_items:
    if type(element) == Wall:
        selected_walls.append(element)

for i in selected_walls:
    print("The wall name is ", i.Name, "its level id is ", i.LevelId)

for line in selected_lines:
    print(line.GeometryCurve.GetEndPoint(0), line.GeometryCurve.GetEndPoint(1))

    # print("the line is ", i)


# for id in selected_items_ids:
#     print(id)

# selection_ids = [e for e in myselection]
# selected_walls = [wall_element for wall_element in myselection if type(wall_element, Wall)]

# for id in selected_items_ids:
#     e = uidoc.Document.GetElement(id)
#     print("this is e", e)
#     if type(e) == Wall:
#         selected_walls.append(e)

# for e in selected_items:
#     print("this is from main selection element e", type(e))


# selected_rooms = [e for e in selection.elements if isinstance(e, Room)]

# for id in myselection:
    # selection_ids.append(id.IntegerValue)


# if selection_ids.Count = 0:
#     TaskDialog("Select some element, any element")


# for id in myselection:
#     element = uidoc.Document.GetElement(id)
#     if type(element) == Wall:
#         selection_wall_ids.append(id)
#         selection_walls.append(element)


# floor_types = rpw.db.Collector(of_category='OST_Floors', is_type=True).elements
# floor_type_options = {DB.Element.Name.GetValue(t): t for t in floor_types}


# floor_type = ui.forms.SelectFromList('Model Floors', selection_ids, description = "Choose your Floor Type")
# print(floor_type.id)
# floor_type_id = floor_type.id

# selected_rooms = [e for e in selection.elements if isinstance(e, Room)]
# if not selected_rooms:
#     UI.TaskDialog.Show('MakeFloors', 'You need to select at lest one Room.')
#     sys.exit()


# floor_type = ui.forms.SelectFromList('Make Floors', floor_type_options,
#                                      description='Select Floor Type')
# floor_type_id = floor_type.Id
