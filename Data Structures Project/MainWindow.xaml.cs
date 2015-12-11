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

namespace Data_Structures_Project
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        String script_ex1; // TODO - get Iron Python script
        ScriptEngine engine;
        ScriptScope scope;
        ScriptSource source;
        CompiledCode compiled;
        dynamic result;
        public MainWindow()
        {
            InitializeComponent();
            return;
        }

        private void ex1FileBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog fileDialog = new Microsoft.Win32.OpenFileDialog();
            fileDialog.Filter = "Text Files(*.txt)|*.txt|All Files (*.*)|*.*";
            fileDialog.ShowDialog();
            if ((fileDialog.FileName != "") && (fileDialog.CheckFileExists == true)) ex1FileAddTextBox.Text = fileDialog.FileName;
        }

        private void ex1SciprtBrowseButton_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog fileDialog = new Microsoft.Win32.OpenFileDialog();
            fileDialog.Filter = "Python Script Files(*.py)|*.py|All Files (*.*)|*.*";
            fileDialog.ShowDialog();
            if ((fileDialog.FileName != "") && (fileDialog.CheckFileExists == true)) ex1ScriptAddTextBox.Text = fileDialog.FileName;
        }

        private void ex1RunButton_Click(object sender, RoutedEventArgs e)
        {
            if (ex1ScriptAddTextBox.Text != "") script_ex1 = ex1ScriptAddTextBox.Text;
            engine = Python.CreateEngine();
            scope = engine.CreateScope();
            source = engine.CreateScriptSourceFromString(script_ex1, SourceCodeKind.Statements);
            compiled = source.Compile();
            result = compiled.Execute(scope);
        }
    }
}
