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
using System.Windows.Shapes;
using System.IO;

namespace Data_Structures_Project
{
    /// <summary>
    /// Interaction logic for Settings.xaml
    /// </summary>
    public partial class Settings : Window
    {
        public Settings()
        {
            InitializeComponent();
            if (File.Exists("settings.ini") == true)
            {
                StreamReader sr = new StreamReader("settings.ini");
                if (sr.ReadLine() == "[Python libraries]") settingsDirAddTextBox.Text = sr.ReadLine();
                sr.ReadLine();
                if (sr.ReadLine() == "[Exercise 1 Python script]") ex1FileAddTextBox.Text = sr.ReadLine();
                sr.ReadLine();
                if (sr.ReadLine() == "[Exercise 2 Python script]") ex2FileAddTextBox.Text = sr.ReadLine();
                sr.ReadLine();
                if (sr.ReadLine() == "[Exercise 3 Python script]") ex3FileAddTextBox.Text = sr.ReadLine();
                sr.ReadLine();
                if (sr.ReadLine() == "[Exercise 4 Python script]") ex4FileAddTextBox.Text = sr.ReadLine();
                sr.ReadLine();
                if (sr.ReadLine() == "[Exercise 5 Python script]") ex5FileAddTextBox.Text = sr.ReadLine();
                sr.Close();
            }
        }

        private void settingsDirAddBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog fileDialog = new Microsoft.Win32.OpenFileDialog();
            fileDialog.Filter = "Python Script Files(*.py)|*.py|All Files (*.*)|*.*";
            fileDialog.ShowDialog();
            if ((fileDialog.FileName != "") && (fileDialog.CheckFileExists == true)) settingsDirAddTextBox.Text = new FileInfo(fileDialog.FileName).Directory.FullName;
        }

        private void saveButton_Click(object sender, RoutedEventArgs e)
        {
            TextWriter tw = new StreamWriter("settings.ini", false);
            tw.WriteLine("[Python libraries]");
            tw.WriteLine(settingsDirAddTextBox.Text);
            tw.WriteLine("");
            tw.WriteLine("[Exercise 1 Python script]");
            tw.WriteLine(ex1FileAddTextBox.Text);
            tw.WriteLine("");
            tw.WriteLine("[Exercise 2 Python script]");
            tw.WriteLine(ex2FileAddTextBox.Text);
            tw.WriteLine("");
            tw.WriteLine("[Exercise 3 Python script]");
            tw.WriteLine(ex3FileAddTextBox.Text);
            tw.WriteLine("");
            tw.WriteLine("[Exercise 4 Python script]");
            tw.WriteLine(ex4FileAddTextBox.Text);
            tw.WriteLine("");
            tw.WriteLine("[Exercise 5 Python script]");
            tw.WriteLine(ex5FileAddTextBox.Text);
            tw.Close();
            this.Close();
        }

        private void ex1FileBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog fileDialog = new Microsoft.Win32.OpenFileDialog();
            fileDialog.Filter = "Python Script Files(*.py)|*.py|All Files (*.*)|*.*";
            fileDialog.ShowDialog();
            if ((fileDialog.FileName != "") && (fileDialog.CheckFileExists == true)) ex1FileAddTextBox.Text = fileDialog.FileName;
        }

        private void ex2FileBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog fileDialog = new Microsoft.Win32.OpenFileDialog();
            fileDialog.Filter = "Python Script Files(*.py)|*.py|All Files (*.*)|*.*";
            fileDialog.ShowDialog();
            if ((fileDialog.FileName != "") && (fileDialog.CheckFileExists == true)) ex2FileAddTextBox.Text = fileDialog.FileName;
        }

        private void ex3FileBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog fileDialog = new Microsoft.Win32.OpenFileDialog();
            fileDialog.Filter = "Python Script Files(*.py)|*.py|All Files (*.*)|*.*";
            fileDialog.ShowDialog();
            if ((fileDialog.FileName != "") && (fileDialog.CheckFileExists == true)) ex3FileAddTextBox.Text = fileDialog.FileName;
        }

        private void ex4FileBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog fileDialog = new Microsoft.Win32.OpenFileDialog();
            fileDialog.Filter = "Python Script Files(*.py)|*.py|All Files (*.*)|*.*";
            fileDialog.ShowDialog();
            if ((fileDialog.FileName != "") && (fileDialog.CheckFileExists == true)) ex4FileAddTextBox.Text = fileDialog.FileName;
        }

        private void ex5FileBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog fileDialog = new Microsoft.Win32.OpenFileDialog();
            fileDialog.Filter = "Python Script Files(*.py)|*.py|All Files (*.*)|*.*";
            fileDialog.ShowDialog();
            if ((fileDialog.FileName != "") && (fileDialog.CheckFileExists == true)) ex5FileAddTextBox.Text = fileDialog.FileName;
        }
    }
}
