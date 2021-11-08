import os
import clr
import myfile
clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')
clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')


from pyrevit import UI
from pyrevit import script
from pyrevit import framework
from pyrevit.framework import wpf, Controls, Imaging


xamlfilepath = script.get_bundle_file('myui3.xaml')
teclogopath = script.get_bundle_file('teclogo.png')
# teclogo = os.path.abspath(__file__) + "\\teclogo.png"


import wpf
from System import Windows
from System.Windows import Media
import System.IO
import System.Windows
import Microsoft.Win32
import System.Windows.Controls as controls
import System.Windows.Media.Imaging


###### Let the Hacking Begin! ######
class MyWindow(Windows.Window):

    # bitimg = Imaging.BitmapImage()
    # bitimg
    # bitimg.UriSource = Uri("C:\Users\sreddy\AppData\Roaming\pyRevit-Master\extensions\TEC.extension\TEC kit.tab\panel2.panel\uitest.pushbutton\icon.png")


    def __init__(self):
        wpf.LoadComponent(self, xamlfilepath)
        # self.Width = 0.3 * System.Windows.SystemParameters.PrimaryScreenWidth
        self.Topmost = True
        self.Top = 0
        self.Left = 0

        self.teclogomain.Source = Imaging.BitmapImage(System.Uri(teclogopath, System.UriKind.RelativeOrAbsolute))


    def dragcommand(self, sender, e):
        self.DragMove()



    def window_properties(self):
        self.windowkey.Width = 100


    def myfunc(self, sender, args):
        Windows.Window.Close(self)


    def BrowseButtonClick(self, sender, args):
        openFileDlg = Microsoft.Win32.OpenFileDialog()
        result = openFileDlg.ShowDialog()
        self.filepath_1.Text = openFileDlg.FileName

    def RunEstimateReportButtonClick(self, sender, args):
        myfile.foo()
        # print(excel_template_location[0])


MyWindow().ShowDialog()

