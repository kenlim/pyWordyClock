import sys
from time import localtime
from pyWordyClock.WordyClockConverter import convertToWords, roundToClosest5Minutes, roundToClosest5Minutes, blankOutTargetFromBase

baseClock = """ITLISABOUTE
ACQUARTERDC
TWENTYFIVEX
HALFBTENFTO
PASTERUNINE
ONESIXTHREE
FOURFIVETWO
EIGHTELEVEN
SEVENTWELVE
TENIO'CLOCK"""

def main():
    clock = localtime()
    hour, minutes = roundToClosest5Minutes(clock.tm_hour, clock.tm_min)

    wordyTime = convertToWords(hour, minutes)
    print blankOutTargetFromBase(wordyTime.upper(), baseClock)
    return 0

def othermain():
    print baseClock
    return 0