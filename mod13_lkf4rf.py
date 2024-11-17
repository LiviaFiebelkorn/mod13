import unittest
from datetime import datetime

dateFormat = "%Y-%m-%d"
def testIfSymbol(symbol):
    if (symbol.isupper()) and (1<= len(symbol) <= 7):
        return True
    else:
        return False
def testChartType(chartType):
    if (chartType == 1) or (chartType == 2):
        return True
    else:
        return False
def testTimeSeries(timeSeries):
    if 1<= timeSeries <= 4:
        return True
    else:
        return False
def testStartDate(startDate):
    try:
        datetime.strptime(startDate, dateFormat)
        return True
    except Exception:
        return False
def testEndDate(endDate):
    try:
        datetime.strptime(endDate, dateFormat)
        return True
    except Exception:
        return False

class Project3aTest(unittest.TestCase):

    def testS(self):
        self.assertTrue(testIfSymbol("GOOGL"))
        self.assertFalse(testIfSymbol("googl"))
        self.assertFalse(testIfSymbol("GOOGLEEEEEEEEEEEEE"))
    def testCT(self):
        self.assertTrue(testChartType(1))
        self.assertFalse(testChartType(8))

    def testTS(self):
        self.assertTrue(testTimeSeries(3))
        self.assertFalse(testTimeSeries(20))
    def testSD(self):
        self.assertTrue(testStartDate("2024-01-01"))
        self.assertFalse(testStartDate("24-01-01"))
    def testED(self):
        self.assertTrue(testEndDate("2024-01-01"))
        self.assertFalse(testEndDate("24-01-01"))
    
        
if __name__ == "__main__":
    unittest.main()
