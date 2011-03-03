from unittest import TestCase
from pyWordyClock.WordyClockConverter import roundToClosest5Minutes, convertToWords


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
        self.assertEquals("it is  ten o' clock", convertToWords(10, 0))
        self.assertEquals("it is ten past ten o' clock", convertToWords(10, 10))

    def testShouldDisplayTimeToNextHourIfPast30Minutes(self):
        self.assertEquals("it is ten to ten o' clock", convertToWords(9, 50))
        self.assertEquals("it is quarter to ten o' clock", convertToWords(9, 45))


