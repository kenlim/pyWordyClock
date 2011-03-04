import re
from unittest import TestCase
from pyWordyClock.WordyClock import *


class AcceptanceTest(TestCase):

    def testShouldRoundTimeToClosest5MinuteBlock(self):
        self.assertEquals((1,0), roundToClosest5Minutes(1, 0))
        self.assertEquals((1,0), roundToClosest5Minutes(1, 1))
        self.assertEquals((1,0), roundToClosest5Minutes(1, 2))
        self.assertEquals((1, 5), roundToClosest5Minutes(1, 3))
        self.assertEquals((1, 5), roundToClosest5Minutes(1, 4))
        self.assertEquals((1, 5), roundToClosest5Minutes(1, 5))

        self.assertEquals((1, 15), roundToClosest5Minutes(1, 17))
        self.assertEquals((1, 30), roundToClosest5Minutes(1, 29))
        self.assertEquals((1, 45), roundToClosest5Minutes(1, 44))
        self.assertEquals((1, 45), roundToClosest5Minutes(1, 46))

    def testShouldRoundToNextHourIfWithin2AndAHalfMinutes(self):
        self.assertEquals((2,0), roundToClosest5Minutes(1, 58))

    def testShouldConvertTimeToWordsCorrectly(self):
        self.assertEquals("it is ten", convertToWords(10, 0))
        self.assertEquals("it is ten past ten", convertToWords(10, 10))

    def testShouldDisplayTimeToNextHourIfPast30Minutes(self):
        self.assertEquals("it is ten to ten", convertToWords(9, 50))
        self.assertEquals("it is a quarter to ten", convertToWords(9, 45))

    def testShouldRecognizeMidnight(self):
        self.assertEquals("it is midnight", convertToWords(0,0))
        self.assertEquals("it is five to midnight", convertToWords(23, 55))

    def testShouldRecognizeNoon(self):
        self.assertEquals("it is noon", convertToWords(12, 0))
        self.assertEquals("it is ten past noon", convertToWords(12, 10))

    def testShouldConvertTargetStringIntoRegularExpression(self):
        targetString  = "it is ten to ten"
        self.assertEquals(".*(it).*(is).*(ten).*(to).*(ten).*", convertToRegex(targetString))
        
    def testShouldBlankOutCharsThatDoNotMatchStrings(self):
        baseString = "xxxxxtargetxxxlockedxxx"
        self.assertEquals("     target   locked   ", blankOutTargetFromBase("target locked", baseString))

    def testShouldWorkWithNewLines(self):
        baseString = "xxxxxtarget\nlockedxxx"
        self.assertEquals("     target\nlocked   ", blankOutTargetFromBase("target locked", baseString))

    def testActualUseCase(self):
        expectedResult = "IT IS      \n           \n           \n     TEN TO\n           \n           \n           \n           \nTEN        \n           "

        self.assertEquals(expectedResult, blankOutTargetFromBase("it is ten to ten".upper(), clockFace))