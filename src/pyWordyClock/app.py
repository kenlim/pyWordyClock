import sys
from time import localtime
from pyWordyClock.WordyClockConverter import convertToWords, roundToClosest5Minutes, roundToClosest5Minutes

baseClock = """ITLISASTIME
ACQUARTERDC
TWENTYFIVEX
HALFBTENFTO
PASTERUNINE
ONESIXTHREE
FOURFIVETWO
EIGHTELEVEN
SEVENTWELVE
TENSEOCLOCK"""

def main():
    clock = localtime()
    hour, minutes = roundToClosest5Minutes(clock.tm_hour, clock.tm_min)
    print convertToWords(hour, minutes)
    return 0

if __name__ =='__main__':
    sys.exit(main())