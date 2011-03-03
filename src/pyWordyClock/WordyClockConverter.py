import re


hourNames = { 1 : 'one',
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
                12: 'twelve'
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
    hour = hour % 12
    minutes = round(minutes / 5.0) * 5
    if minutes == 60:
        return (hour +1, 0)
    else:
        return (hour, minutes)

def constructString(hour, minutes):
    components = ["it is", minuteNames[minutes], hourNames[hour], "o' clock"]
    return " ".join([x for x in components if x != None])

def convertToWords(hour, minutes):
    if minutes > 30:
        return constructString(hour + 1, minutes)
    else:
        return constructString(hour, minutes)

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

