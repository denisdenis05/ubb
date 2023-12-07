
def Naive_findMaximumValueByOptimalRodCuttingWithGivenRodLengthAndPrices(currentRodLength:int, remainingRodLength:int, rodValues:list):
    lengthsThatWerePutInSum = []
    firstPositionInAnyList = 0

    if currentRodLength == 0:
        for rodLength in range(1, remainingRodLength):
            lengthsThatWerePutInSum = lengthsThatWerePutInSum+[(firstPositionInAnyList+1, rodValues[firstPositionInAnyList])]
        return remainingRodLength * rodValues[firstPositionInAnyList], lengthsThatWerePutInSum


    firstRodLengthSumToCompare, firstLengthsThatWerePutInSum = Naive_findMaximumValueByOptimalRodCuttingWithGivenRodLengthAndPrices(currentRodLength-1, remainingRodLength, rodValues)

    secondRodLengthSumToCompare=0
    if currentRodLength < remainingRodLength:
        secondRodLengthSumToCompare, secondLengthsThatWerePutInSum = Naive_findMaximumValueByOptimalRodCuttingWithGivenRodLengthAndPrices(currentRodLength, remainingRodLength - currentRodLength - 1, rodValues)
        secondRodLengthSumToCompare=rodValues[currentRodLength]+secondRodLengthSumToCompare
        lengthsThatWerePutInSum = lengthsThatWerePutInSum + secondLengthsThatWerePutInSum
        lengthsThatWerePutInSum = lengthsThatWerePutInSum + [(currentRodLength+1,rodValues[currentRodLength])]


    if firstRodLengthSumToCompare>secondRodLengthSumToCompare:
        return firstRodLengthSumToCompare, firstLengthsThatWerePutInSum
    else:
        return secondRodLengthSumToCompare, lengthsThatWerePutInSum


def Dynamic_findMaximumValueByOptimalRodCuttingWithGivenRodLengthAndPrices(currentRodLength:int, remainingRodLength:int, rodValues:list, alreadyComputedValues:dict):
    lengthsThatWerePutInSum=[]
    firstPositionInAnyList = 0

    if currentRodLength == 0:
        for rodLength in range(1, remainingRodLength):
            lengthsThatWerePutInSum=lengthsThatWerePutInSum+[(firstPositionInAnyList+1, rodValues[firstPositionInAnyList])]
        alreadyComputedValues[(currentRodLength, remainingRodLength)]=(remainingRodLength * rodValues[0], lengthsThatWerePutInSum)
        return remainingRodLength * rodValues[0], lengthsThatWerePutInSum, alreadyComputedValues

    if (currentRodLength-1, remainingRodLength) in alreadyComputedValues.keys():
        firstRodLengthSumToCompare = alreadyComputedValues[(currentRodLength-1, remainingRodLength)][firstPositionInAnyList]
        firstLengthsThatWerePutInSum = alreadyComputedValues[(currentRodLength-1, remainingRodLength)][firstPositionInAnyList+1]
        print(f"\nGOT ALREADY CHECKED VALUE:\nFor the remaining length of {remainingRodLength} we already stored the sum {firstRodLengthSumToCompare}, made up by adding {firstLengthsThatWerePutInSum}")

    else:
        firstRodLengthSumToCompare, firstLengthsThatWerePutInSum, alreadyComputedValues = Dynamic_findMaximumValueByOptimalRodCuttingWithGivenRodLengthAndPrices(currentRodLength-1, remainingRodLength, rodValues, alreadyComputedValues)


    secondRodLengthSumToCompare=0
    secondLengthsThatWerePutInSum=[]
    if currentRodLength < remainingRodLength:

        if (currentRodLength, remainingRodLength - currentRodLength - 1) in alreadyComputedValues.keys():
            print(f"\nGOT ALREADY CHECKED VALUE:\nFor the remaining length of {remainingRodLength} we already stored the sum {firstRodLengthSumToCompare}, made up by adding {firstLengthsThatWerePutInSum}")

            secondRodLengthSumToCompare = alreadyComputedValues[(currentRodLength, remainingRodLength - currentRodLength - 1)][firstPositionInAnyList]
            secondLengthsThatWerePutInSum = alreadyComputedValues[(currentRodLength, remainingRodLength - currentRodLength - 1)][firstPositionInAnyList+1]
        else:
            secondRodLengthSumToCompare, secondLengthsThatWerePutInSum, alreadyComputedValues = Dynamic_findMaximumValueByOptimalRodCuttingWithGivenRodLengthAndPrices(currentRodLength, remainingRodLength - currentRodLength - 1, rodValues, alreadyComputedValues)

        secondRodLengthSumToCompare = secondRodLengthSumToCompare + rodValues[currentRodLength]

        secondLengthsThatWerePutInSum = secondLengthsThatWerePutInSum + [(currentRodLength + 1, rodValues[currentRodLength])]



    if firstRodLengthSumToCompare > secondRodLengthSumToCompare:
        lengthsThatWerePutInSum = lengthsThatWerePutInSum + firstLengthsThatWerePutInSum

        alreadyComputedValues[(currentRodLength, remainingRodLength)] = (
        firstRodLengthSumToCompare, lengthsThatWerePutInSum)

        return firstRodLengthSumToCompare, firstLengthsThatWerePutInSum, alreadyComputedValues
    else:
        lengthsThatWerePutInSum = lengthsThatWerePutInSum + secondLengthsThatWerePutInSum

        alreadyComputedValues[(currentRodLength, remainingRodLength)] = (
        secondRodLengthSumToCompare, lengthsThatWerePutInSum)

        return secondRodLengthSumToCompare, lengthsThatWerePutInSum, alreadyComputedValues



def main():
    stillInTheMenu = True
    while stillInTheMenu:
        print("> Choose an option:\n1.Naive implementation\n2.Dynamic implementation\n3.Exit")
        selectedOption = int(input("> "))
        if selectedOption == 1:
            givenRodLength = int(input("Insert the length of the rod: "))
            givenRodValueText = input("Insert the values of the rod separated by spaces: ")
            givenRodValues = list(map(int, givenRodValueText.split()))

            resultedRodLength, valuesTaken = Naive_findMaximumValueByOptimalRodCuttingWithGivenRodLengthAndPrices(givenRodLength-1, givenRodLength, givenRodValues)

            print(f"\nThe max profit is {resultedRodLength}, by adding the following pieces: (piece length, piece value):\n {valuesTaken}")

        elif selectedOption == 2:
            givenRodLength = int(input("Insert the length of the rod: "))
            givenRodValueText = input("Insert the values of the rod separated by spaces: ")
            givenRodValues = list(map(int, givenRodValueText.split()))

            someRandomEmptyDictionary = {}
            resultedRodLength, valuesTaken, alreadyComputedValues = Dynamic_findMaximumValueByOptimalRodCuttingWithGivenRodLengthAndPrices(givenRodLength - 1, givenRodLength, givenRodValues, someRandomEmptyDictionary)

            print(f"\nThe max profit is {resultedRodLength}, by adding the following pieces: (piece length, piece value):\n {valuesTaken}")

        elif selectedOption == 3:
            stillInTheMenu = False
            print("Bye!")

main()