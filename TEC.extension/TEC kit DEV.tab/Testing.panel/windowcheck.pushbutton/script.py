#Automate FLoor Boundaries - V1 - </ShivaReddy>
import os
import clr

from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI import Selection

from pyrevit import UI
from pyrevit import revit, DB
from pyrevit.revit.ui import *
from pyrevit.framework import List, wpf, Controls, Imaging

__title__ = "Check \n Window Location"
__author__ = "Shiva Reddy"

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()


for the_phase in doc.Phases:
	if the_phase.Name == "New Construction":
		newConstructionPhase = the_phase
	if the_phase.Name == "Existing":
		existingPhase = the_phase


###### LET THE HACKING BEGIN ######

# this_window = doc.GetElement(ElementId(6537909))

window_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType()
door_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType()

def window_from_room(window, phase):
	from_room = window.FromRoom[phase]
	if from_room != None :
		from_room_name = (from_room.get_Parameter(BuiltInParameter.ROOM_NAME)).AsString()
		return from_room_name


def window_to_room(window, phase):
	to_room = window.ToRoom[phase]
	if to_room != None:
		to_room_name = (to_room.get_Parameter(BuiltInParameter.ROOM_NAME)).AsString()
		return to_room_name


###### Getting all the FROM and TO rooms of any window
# print("the total number of windows are", window_collector.GetElementCount())
# w_count = 0
# for w in window_collector:
# 	print("{0} FromRoom: {0}, ToRoom: {1}".format(w_count, (window_from_room(w,newConstructionPhase)), (window_to_room(w,newConstructionPhase))))
# 	y = ("{0} FromRoom: {0}, ToRoom: {1}".format(w_count, (window_from_room(w,newConstructionPhase)), (window_to_room(w,newConstructionPhase))))
# 	w_count += 1


# print("the total doors are", door_collector.GetElementCount())
# d_count = 0
# for w in door_collector:
# 	print("{0} FromRoom: {1}, ToRoom: {2}".format(d_count, (window_from_room(w,newConstructionPhase)), (window_to_room(w,newConstructionPhase))))
# 	d_count += 1



##### Switch for all windows - DOES NOT TOGGLE, JUST ON or OFF
def switch_all_windows_temp_param(yes1orno0):
	t.Start("Toggle Tempered Style of all Windows")
	for w in window_collector:
		this_w_params = w.Parameters
		
		for param in this_w_params:
			if param.Definition.Name == "TemperedWindow":
				temp_window_param = param
		
		temp_window_param.Set(yes1orno0)
	t.Commit()
# switch_all_windows_temp_param(0)

def on_temp_window(window_group):
	t.Start("Toggle specific windows to temp")
	for window in window_group:
		this_params = window.Parameters

		for param in this_params:
			if param.Definition.Name == "TemperedWindow":
				temp_window_param = param
		
		temp_window_param.Set(1)
	t.Commit()


test_window = doc.GetElement(ElementId(6514155))
group_of_windows = [test_window]
on_temp_window(group_of_windows)

# print("The Test window's Level: {0}".format((doc.GetElement(test_window.LevelId).Name)))



# TaskDialog.Show("The level is ",(doc.GetElement(test_window.LevelId).Name))


