import re
from time import localtime

clockFace = """\
ITLISXABOUT
ACQUARTERDC
TWENTYRFIVE
HALFBTENFTO
PASTEXSNINE
ONESIXTHREE
FOURFIVETWO
EIGHTELEVEN
TENMIDNIGHT
SEVENTYNOON"""

hourNames = {   0 : 'midnight',
                1 : 'one',
                2 : 'two',
                3 : 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7 : 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'noon',
                13 : 'one',
                14 : 'two',
                15 : 'three',
                16: 'four',
                17: 'five',
                18: 'six',
                19 : 'seven',
                20: 'eight',
                21: 'nine',
                22: 'ten',
                23: 'eleven',
                24: 'midnight'
            }

minuteNames = { 0: None,
                5: 'five past',
                10: 'ten past',
                15:'a quarter past',
                20:'twenty past',
                25: 'twenty five past',
                30: 'half past',
                35: 'twenty five to',
                40:'twenty to',
                45: 'a quarter to',
                50: 'ten to',
                55: 'five to'
            }

def roundToClosest5Minutes(hour, minutes):
    minutes = round(minutes / 5.0) * 5
    if minutes == 60:
        return (hour +1, 0)
    else:
        return (hour, minutes)

def constructString(minutesRelativeTo, hour):
    components = ["it is", minuteNames[minutesRelativeTo], hourNames[hour]]
    return " ".join([x for x in components if x != None])

def convertToWords(hour, minutes):
    if minutes > 30:
        return constructString(minutes, hour + 1)
    else:
        return constructString(minutes, hour)

def convertToRegex(string):
    return ".*" + ".*".join(["(" + x + ")" for x in string.split(" ")]) + ".*"


def blankOutTargetFromBase(target, baseString):
    targetRegex = convertToRegex(target)
    blankedString = re.sub(".", " ", baseString)

    matcher = re.match(targetRegex, baseString, re.DOTALL)
    outputArray = list(blankedString)

    for x in range(1, len(matcher.groups()) +1):
        outputArray[matcher.start(x) : matcher.end(x)] = [y for y in matcher.group(x)]

    return "".join(outputArray)



def main():
    clock = localtime()
    hour, minutes = roundToClosest5Minutes(clock.tm_hour, clock.tm_min)

    wordyTime = convertToWords(hour, minutes)
    print blankOutTargetFromBase(wordyTime.upper(), clockFace)
    return 0

def otherMain():
    print clockFace
    return 0

