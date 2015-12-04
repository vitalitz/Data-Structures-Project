import wpf

from System.Windows import Application, Window, DialogResultConverter
from Microsoft.Win32 import OpenFileDialog, CommonDialog

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Data_Structures_Project.xaml')
    
    def Button_Click(self, sender, e):
        openFileDialog = OpenFileDialog()
        openFileDialog.Filter = "Text Files(*.txt)|*.txt|All Files (*.*)|*.*"
        openFileDialog.ShowDialog(self)
        if (openFileDialog.FileName != ""):
            self.fileAddressTextBox.Text = openFileDialog.FileName
        del openFileDialog
        pass
    

if __name__ == '__main__':
    Application().Run(MyWindow())
