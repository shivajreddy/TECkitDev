import os
import clr
import myfile

from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')
clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')


from pyrevit import UI
from pyrevit import script
from pyrevit import framework
from pyrevit.framework import wpf, Controls, Imaging


__title__ = "Windows info \n (under constr.)"
__author__ = "ShivaReddy"
doc = __revit__.ActiveUIDocument.Document

xamlfilepath = script.get_bundle_file('myui3.xaml')
teclogopath = script.get_bundle_file('teclogo.png')
# teclogo = os.path.abspath(__file__) + "\\teclogo.png"


from System import Windows
from System.Windows import Media
import System.Windows.Controls as controls


mylist = []

###### Let the Hacking Begin! ######
maincollector = FilteredElementCollector(doc)

windows_collector = maincollector.OfCategory(BuiltInCategory.OST_Windows)

all_windows_list = list(windows_collector)

doc_window_instances = []

for i in range(len(all_windows_list)):
    if str(type(all_windows_list[i])) == "<type 'FamilyInstance'>":
        doc_window_instances.append(all_windows_list[i])
        # i = (all_windows_list[i].GetParameters("Width"))
        # print(all_windows_list[i].LookupParameter("Width"))


# This function basically return the parameters with name and value
def get_param_name_value(obj):
    obj_params = list(obj.Parameters)
    all_param_names = []
    all_param_values = []
    indeces = []
    my_param_names = []
    my_param_values = []
    for i in range(len(obj_params)):
        this_name = obj_params[i].Definition.Name
        this_value = obj_params[i].AsValueString()
        all_param_names.append(this_name)
        all_param_values.append(this_value)
        if this_name == "Family Name" or this_name == "Width" or this_name == "Height" :
            my_param_names.append(this_name)
            my_param_values.append(this_value)
        
    
    # for x in range(len(all_param_names)):
    #     if all_param_names[x] == "Family Name" or all_param_names[x] == "Width":
    #         indeces.append(all_param_names.index(all_param_names[x]))
    
    return my_param_names, my_param_values
    
        # print ("param number", i, obj_params[i].Definition.Name, obj_params[i].AsValueString())
        # if obj_params[i].Definition.Name == "Width":
            # print (obj_params[i].Definition.Name, obj_params[i].AsValueString())
        # if obj_params[i].Definition.Name == "Family Name":
        #     print (obj_params[i].AsValueString())



for i in range(0, len(doc_window_instances)):
    p = doc_window_instances[i]
    p_type = doc.GetElement(p.GetTypeId())
    # print("item number ", i)
    print(get_param_name_value(p_type))
