""" Exercise 2 """
import glob
from System import Array

class Exercise2:
    def __init__(self, dirAddr):
        self.dirAddr = dirAddr
        pass
    
    def listFiles(self):
        self.files = glob.glob(self.dirAddr + "//*.txt")
        return Array[str](self.files)

    def readFile(self):
        self.files = [f for f in listdir(self.dirAddr) if isfile(join(self.dirAddr, f))]
        f = open(self.dirAddr + '\\' + self.files[0], 'r')
        return f.readline()

class fileControl:
    def datetoint(self, fileAddr):
        f = open(fileAddr, 'r')
        strLine = f.readline()
        strDate = strLine.Substring(6, 10)
        day = strDate.Substring(0, 2)
        month = strDate.Substring(3, 2)
        year = strDate.Substring(6, 4)
        daysYears = (int(year) - 1980) * 365
        monthsDays = int(month) * 30
        return daysYears + monthsDays + int(day)