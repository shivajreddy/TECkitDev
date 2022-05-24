#!python3 

from datetime import datetime
import shutil
import os
import xlsxwriter


def copy_file(template_path):

  # get the path from the file
  head_tail = os.path.split(template_path)
  directory_path = head_tail[0]

  now = datetime.now()
  current_time = now.strftime("%H_%M_%S")

  new_file_location = directory_path + "\\" + "EstimateReport_" +current_time + ".xlsm"

  try:
    shutil.copy(template_path, new_file_location)
    return new_file_location
  except shutil.Error:
    print('Error by shutil')



def print_data_into_excel(target_excel_file):
  print(target_excel_file)


# At the end of the file, run is used as the run function in script.py
def run(templatePath):

  # Make a copy of the template
  new_file_location = copy_file(templatePath)

  # Get the data from revit


  # Print the data in to excel
  print_data_into_excel(new_file_location)
