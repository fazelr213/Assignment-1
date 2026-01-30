
stringLengthParityDictionary = {
 "data": {"length": 4, "parity": "even"},
 "science": {"length": 7, "parity": "odd"}
 }

def analyzeStringList(stringList):

    resultDictionary = {}

    for currentString in stringList:
        stringLength = len(currentString)
        parity = "even" if stringLength % 2 == 0 else "odd"

        resultDictionary[currentString] = {
            "length": stringLength,
            "parity": parity
        }

    return resultDictionary

