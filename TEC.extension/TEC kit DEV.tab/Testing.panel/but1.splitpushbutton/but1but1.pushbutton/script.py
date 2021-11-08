# Export Estimates to Excel V_0.1
from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

import clr


__doc__ = "doc"
__title__ = "ExportEstimates"
doc = __revit__.ActiveUIDocument.Document


all_elements = []
main_collector = FilteredElementCollector(doc)


def get_view_sheet(main_filter, sheet_name):
    sheet_collector = main_filter.OfCategory(BuiltInCategory.OST_Sheets)
    for sheet in sheet_collector:
        if sheet.Name == sheet_name:
            cover_page = sheet
    return cover_page


cover_page = get_view_sheet(main_collector, "COVER PAGE")
total_params = list(cover_page.Parameters)



my_parameters_names = ["Eagle Project Name","Elevation Type","Lot Number","Lot Code","Neighborhood","County","State","E Cutsheet Revision Date","Drawn By"]
my_parameters = []
my_parameters_values = []

"""This is how you get Parameter Name, and Parameter Value"""
# for i in range(len(total_params)):
#     print(total_params[i].Definition.Name, total_params[i].AsString())


for x in range(len(total_params)):
    for y in range(len(my_parameters_names)):
        if total_params[x].Definition.Name == my_parameters_names[y]:
            my_parameters.append(total_params[x])
            my_parameters_values.append(total_params[x].AsString())

print("----")


for x in range(len(my_parameters)):
    print(my_parameters[x].Definition.Name, my_parameters_values[x])


# print(cover_page.GetParameters("Eagle Project Name"))
# cover_page.GetParameters()



# sheet_names = []
# view_schedule_names = []


# for sheet in sheet_collector:
#     sheet_names.append(sheet)


# print(sheet_names)



### Grabbing Schedules Data -- DO NOT DELETE
# schedule_collector = main_collector.OfCategory(BuiltInCategory.OST_Schedules)
# schedule_collector = list(schedule_collector)
# print(schedule_collector)

# for x in schedule_collector:
#     view_schedule_names.append(x.Name)

# filtered_schedules = []
# filtered_schedules_indices = []

# for x in view_schedule_names:
#     if 'EST' in x:
#         filtered_schedules.append(x)
#         filtered_schedules_indices.append(view_schedule_names.index(x))

# # print(filtered_schedules)
# # print(filtered_schedules_indices)

# for x in range(0, len(filtered_schedules_indices)):
#     p = filtered_schedules_indices[x]
#     # print(view_schedule_names[p])
### Grabbing Schedules Data -- 


