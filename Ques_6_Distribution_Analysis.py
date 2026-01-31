numbers = [3, 1, 2, 3, 4, 2]

numbers = [3, 1, 2, 3, 4, 2]


def distributionAnalysis(numberList):
    # Dictionary to store the percentage for each unique number
    distributionDictionary = {}

    # Total number of elements in the list
    totalElements = len(numberList)

    # Sort the list so values are in order
    numberList.sort()

    # Loop through each number in the list
    for currentKey in numberList:
        # Only process each unique number once
        if currentKey not in distributionDictionary:

            countLessOrEqual = 0

            # Count how many values are less than or equal to currentKey
            for currentValue in numberList:
                if currentValue <= currentKey:
                    countLessOrEqual += 1

            # Calculate percentage of values <= currentKey
            percentage = (countLessOrEqual / totalElements) * 100
            distributionDictionary[currentKey] = percentage

    return distributionDictionary


print(distributionAnalysis(numbers))
