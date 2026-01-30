
numbers = [3, 1, 2, 3, 4, 2]

def distributionAnalysis(numberList):

    distributionDictionary = {}
    totalElements = len(numberList)

    numberList.sort()

    for currentKey in numberList:
        if currentKey not in distributionDictionary:

            countLessOrEqual = 0
            for currentValue in numberList:
                if currentValue <= currentKey:
                    countLessOrEqual += 1

            percentage = (countLessOrEqual / totalElements) * 100
            distributionDictionary[currentKey] = percentage

    return distributionDictionary

print(distributionAnalysis(numbers))
