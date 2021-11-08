import clr

import Autodesk.Revit.ApplicationServices
import Autodesk.Revit.Attributes
import Autodesk.Revit.DB
import Autodesk.Revit.UI
import System
import System.Transactions
import System.Collections.Generic
import System.Reflection
import System.Windows.Media.Imaging
import System.Drawing


list1 = []
list1.append ("shiva")
print(list1)

from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB import BuiltInCategory



from pyrevit import coreutils


from Autodesk.Revit import DB
from Autodesk.Revit import UI

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import Filtere

from Autodesk.Revit.UI import *

main_collector = FilteredElementCollector()

walls = main_collector.ofcategory




