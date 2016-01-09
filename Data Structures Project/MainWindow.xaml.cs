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
using System.Windows.Interop;
using System.Threading;

namespace Data_Structures_Project
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        ScriptEngine engine;
        dynamic ex2;
        dynamic database;
        String ex1FileAddr;
        String ex2FileAddr;
        String ex3FileAddr;
        String ex4FileAddr;
        String ex5FileAddr;
        ControlWriter contrwr;
        MemoryStream streamOut;
        ProgressWindow progWindow;
        private const int GWL_STYLE = -16;
        private const int WS_SYSMENU = 0x80000;
        [DllImport("user32.dll", SetLastError = true)]
        private static extern int GetWindowLong(IntPtr hWnd, int nIndex);
        [DllImport("user32.dll")]
        private static extern int SetWindowLong(IntPtr hWnd, int nIndex, int dwNewLong);
        public MainWindow()
        {
            InitializeComponent();
            contrwr = new ControlWriter(debugConsTextBox);
            engine = Python.CreateEngine();
            streamOut = new MemoryStream();
            engine.Runtime.IO.SetOutput(streamOut, contrwr);
            checkSettings();
        }

        private void ex1RunButton_Click(object sender, RoutedEventArgs e)
        {

        }
        private void sortByLanguageMergeButton_Click(object sender, RoutedEventArgs e)
        {
            Thread progressThread = new Thread(new ThreadStart(progressTh));
            progressThread.SetApartmentState(ApartmentState.STA);
            progressThread.IsBackground = true;
            progressThread.Start();
            ex2 = engine.ExecuteFile(ex2FileAddr);
            database = ex2.sortByLangMergeSort(ex2DirAddTextBox.Text);
            System.Windows.Threading.Dispatcher.FromThread(progressThread).BeginInvoke(new Action(() =>
                {
                    progWindow.Close();
                    progWindow = null;
                }
            ));
            System.Windows.Threading.Dispatcher.FromThread(progressThread).InvokeShutdown();
        }

        private void progressTh()
        {
            progWindow = new ProgressWindow();
            progWindow.Show();
            System.Windows.Threading.Dispatcher.Run();

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
                }
                sr.ReadLine();
                if (sr.ReadLine() == "[Exercise 2 Python script]")
                {
                    ex2FileAddr = sr.ReadLine();
                    sortByLanguageMergeButton.IsEnabled = true;
                    sortByLanguageQuickButton.IsEnabled = true;
                    sortByDateButton.IsEnabled = true;
                    compareSortButton.IsEnabled = true;
                }
            }
        }

        private void ex2DirAddBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            System.Windows.Forms.FolderBrowserDialog folderBrowser = new System.Windows.Forms.FolderBrowserDialog();
            folderBrowser.ShowDialog();
            ex2DirAddTextBox.Text = folderBrowser.SelectedPath;
        }

        private void debugConsTextBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            TextBox textbox = (TextBox)sender;
            textbox.ScrollToEnd();
        }

        private void clearOutputButton_Click(object sender, RoutedEventArgs e)
        {
            debugConsTextBox.Clear();
        }

        private void sortByDateButton_Click(object sender, RoutedEventArgs e)
        {
            Thread progressThread = new Thread(new ThreadStart(progressTh));
            progressThread.SetApartmentState(ApartmentState.STA);
            progressThread.IsBackground = true;
            progressThread.Start();
            ex2 = engine.ExecuteFile(ex2FileAddr);
            database = ex2.sortByDate(ex2DirAddTextBox.Text);
            System.Windows.Threading.Dispatcher.FromThread(progressThread).BeginInvoke(new Action(() =>
            {
                progWindow.Close();
                progWindow = null;
            }
            ));
            System.Windows.Threading.Dispatcher.FromThread(progressThread).InvokeShutdown();
        }

        private void sortByLanguageQuickButton_Click(object sender, RoutedEventArgs e)
        {
            Thread progressThread = new Thread(new ThreadStart(progressTh));
            progressThread.SetApartmentState(ApartmentState.STA);
            progressThread.IsBackground = true;
            progressThread.Start();
            ex2 = engine.ExecuteFile(ex2FileAddr);
            database = ex2.sortByLangQuickSort(ex2DirAddTextBox.Text);
            System.Windows.Threading.Dispatcher.FromThread(progressThread).BeginInvoke(new Action(() =>
            {
                progWindow.Close();
                progWindow = null;
            }
            ));
            System.Windows.Threading.Dispatcher.FromThread(progressThread).InvokeShutdown();
        }

        private void compareSortButton_Click(object sender, RoutedEventArgs e)
        {
            Thread progressThread = new Thread(new ThreadStart(progressTh));
            progressThread.SetApartmentState(ApartmentState.STA);
            progressThread.IsBackground = true;
            progressThread.Start();
            ex2 = engine.ExecuteFile(ex2FileAddr);
            ex2.compareSortsByLang(ex2DirAddTextBox.Text);
            System.Windows.Threading.Dispatcher.FromThread(progressThread).BeginInvoke(new Action(() =>
            {
                progWindow.Close();
                progWindow = null;
            }
            ));
            System.Windows.Threading.Dispatcher.FromThread(progressThread).InvokeShutdown();
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
