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
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace Data_Structures_Project
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        struct DateStruct
        {
            public int year;
            public int month;
            public int day;
        };
        struct FileStruct
        {
            public string address;
            public DateStruct date;
            public string language;
        };
        FileStruct[] files;
        ScriptEngine engine;
        dynamic ex2;
        String ex1FileAddr;
        String ex2FileAddr;
        String ex3FileAddr;
        String ex4FileAddr;
        String ex5FileAddr;
        debugConsoleWindow debugConsWindow;
        ControlWriter contrwr;
        MemoryStream streamOut;
        public MainWindow()
        {
            InitializeComponent();
            debugConsWindow = new debugConsoleWindow();
            contrwr = new ControlWriter(debugConsWindow.debugConsTextBox);
            engine = Python.CreateEngine();
            streamOut = new MemoryStream();
            engine.Runtime.IO.SetOutput(streamOut, contrwr);
            checkSettings();
        }

        private void ex1RunButton_Click(object sender, RoutedEventArgs e)
        {

        }
        private void ex2RunButton_Click(object sender, RoutedEventArgs e)
        {
            ex2 = engine.ExecuteFile(ex2FileAddr);
            string[] listFiles = ex2.listFiles(ex2DirAddTextBox.Text);
            files = new FileStruct[listFiles.Length];
            int[] dateArr = new int[3];
            for (int i = 0; i < listFiles.Length; i++)
            {
                files[i].address = listFiles[i];
                dateArr = ex2.readFileDate(files[i].address);
                files[i].date.year = dateArr[0];
                files[i].date.month = dateArr[1];
                files[i].date.day = dateArr[2];
                files[i].language = ex2.readFileLanguage(files[i].address);
            }
            ex2.example(files[0]);
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

        private void debugConsButton_Click(object sender, RoutedEventArgs e)
        {
            if (debugConsWindow.IsVisible == false)
            {
                debugConsButton.Content = "Hide debug console";
                debugConsWindow.Show();
            }
            else
            {
                debugConsButton.Content = "Show debug console";
                debugConsWindow.Hide();
            }
        }

        private void Window_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            if (debugConsWindow != null) debugConsWindow.Close();
        }
    }

    public class ControlWriter : TextWriter
    {
        private TextBox textbox;
        public ControlWriter(TextBox textbox)
        {
            this.textbox = textbox;
        }

        public override void Write(char value)
        {
            textbox.Text += value;
        }

        public override void Write(string value)
        {
            textbox.Text += value;
        }

        public override Encoding Encoding
        {
            get { return Encoding.ASCII; }
        }
    }
}
