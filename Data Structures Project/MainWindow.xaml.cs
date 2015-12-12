using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using IronPython.Hosting;
using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;
using System.IO;

namespace Data_Structures_Project
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        ScriptEngine engine;
        dynamic ex2;
        String ex1FileAddr;
        String ex2FileAddr;
        String ex3FileAddr;
        String ex4FileAddr;
        String ex5FileAddr;
        public MainWindow()
        {
            InitializeComponent();
            engine = Python.CreateEngine();
            checkSettings();
        }

        private void ex1RunButton_Click(object sender, RoutedEventArgs e)
        {

        }
        private void ex2RunButton_Click(object sender, RoutedEventArgs e)
        {
            ex2 = engine.ExecuteFile(ex2FileAddr);
            dynamic ex2Class = ex2.Exercise2(ex2DirAddTextBox.Text);
            dynamic str = ex2.Exercise2(ex2DirAddTextBox.Text).listFiles();
//            str = ex2.Exercise2(ex2DirAddTextBox.Text).readFile();
            dynamic asdf = ex2.fileControl().datetoint(str[0]);
//            string dfdg = str[0];
            return;
        }

        private void settingsMenu_Click(object sender, RoutedEventArgs e)
        {
            Settings settingsWindows = new Settings();
            settingsWindows.Closed += SettingsWindows_Closed;
            settingsWindows.ShowDialog();
        }

        private void SettingsWindows_Closed(object sender, EventArgs e)
        {
            checkSettings();
        }

        private void checkSettings()
        {
            if (File.Exists("settings.ini") == false) MessageBox.Show("settings.ini does not exist. Please go to Settings and configure the application.", "Error", MessageBoxButton.OK, MessageBoxImage.Exclamation);
            else
            {
                ICollection<string> paths = engine.GetSearchPaths();
                StreamReader sr = new StreamReader("settings.ini");
                if (sr.ReadLine() == "[Python libraries]")
                {
                    paths.Add(sr.ReadLine());
                    engine.SetSearchPaths(paths);
                }
                sr.ReadLine();
                if (sr.ReadLine() == "[Exercise 1 Python script]")
                {
                    ex1FileAddr = sr.ReadLine();
                    ex1RunButton.IsEnabled = true;
                }
                sr.ReadLine();
                if (sr.ReadLine() == "[Exercise 2 Python script]")
                {
                    ex2FileAddr = sr.ReadLine();
                    ex2RunButton.IsEnabled = true;
                }
            }
        }

        private void ex2DirAddBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            System.Windows.Forms.FolderBrowserDialog folderBrowser = new System.Windows.Forms.FolderBrowserDialog();
            folderBrowser.ShowDialog();
            ex2DirAddTextBox.Text = folderBrowser.SelectedPath;
        }
    }
}
