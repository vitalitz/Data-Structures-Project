#!/usr/bin/python
""" Exercise 2 """
import glob
from System import Array

def listFiles(dirAddr):
    print "Directory path: " + dirAddr
    files = glob.glob(dirAddr + "//*.txt")
    print "Files list:"
    for file in Array[str](files):
        print file
    print("")
    return Array[str](files)

def readFileDate(fileAddr):
    f = open(fileAddr, 'r')
    print fileAddr
    date = f.readline()
    f.close()
    print "Date:"
    print date
    strDate = date.Substring(6, 10)
    year = int(strDate.Substring(6, 4))
    month = int(strDate.Substring(3, 2))
    day = int(strDate.Substring(0, 2))
    dateStruct = [year, month, day]
    print "Date:"
    print dateStruct
    return Array[int](dateStruct)

def readFileLanguage(fileAddr):
    f = open(fileAddr, 'r')
    f.readline()
    lang = f.readline()
    endIndex = lang.find("</language>")
    lang = lang.Substring(10, endIndex - 10)
    print lang
    print("")
    return lang

def example(file):
    print file
    return