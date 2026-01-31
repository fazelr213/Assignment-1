# Example dictionary showing string length and parity
stringLengthParityDictionary = {
    "data": {"length": 4, "parity": "even"},
    "science": {"length": 7, "parity": "odd"}
}

def analyzeStringList(stringList):
    # Dictionary to store results
    resultDictionary = {}

    # Loop through each string in the list
    for currentString in stringList:
        stringLength = len(currentString)                 # length of the string
        parity = "even" if stringLength % 2 == 0 else "odd"  # check even or odd

        # Store length and parity for this string
        resultDictionary[currentString] = {
            "length": stringLength,
            "parity": parity
        }

    return resultDictionary  # return the completed dictionary
