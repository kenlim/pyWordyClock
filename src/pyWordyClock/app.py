import sys
from time import localtime

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
    print "Current time is: ", localtime()

    print baseClock
    return 0

if __name__ =='__main__':
    sys.exit(main())