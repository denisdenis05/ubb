
def isElementAlreadyInTheList(numberToCheckIfInTheList:int, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)->bool:
    if len(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)==1:
        return False
    if numberToCheckIfInTheList in theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue[:-1]:
        return True
    return False

def displayNumbers(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
    textToPrint=""
    for listElementToPrint in theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue:
        textToPrint=textToPrint+f"{listElementToPrint} "
    print(textToPrint)

def absoluteDifferenceBetweenLast2ElementsIsAtLeast(absoluteDifferenceValue:int, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
    if len(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)==1:
        return True
    if abs(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue[-1]-theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue[-2])>=absoluteDifferenceValue:
        return True
    return False

def Recursive_EverySequenceGeneratorSoTheDifferenceOf2NeighboringElementsIsAtLeastAValue(positionInList:int, rangeUpperLimit:int, absoluteDifferenceValue:int, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
    if positionInList == rangeUpperLimit:
        return
    for numberToDisplay in range(1, rangeUpperLimit+1):
        if positionInList == 1:
            theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue.clear()
        elif positionInList < len(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
            theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue.pop()
        theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue.append(numberToDisplay)
        if not isElementAlreadyInTheList(numberToDisplay, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue) and absoluteDifferenceBetweenLast2ElementsIsAtLeast(absoluteDifferenceValue,theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
            if len(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)>=2:
                displayNumbers(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)
                if positionInList<rangeUpperLimit:
                    Recursive_EverySequenceGeneratorSoTheDifferenceOf2NeighboringElementsIsAtLeastAValue(positionInList + 1, rangeUpperLimit, absoluteDifferenceValue, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)
            else:
                Recursive_EverySequenceGeneratorSoTheDifferenceOf2NeighboringElementsIsAtLeastAValue(positionInList+1,rangeUpperLimit,absoluteDifferenceValue, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)
        else:
            theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue.pop()


def Iterative_EverySequenceGeneratorSoTheDifferenceOf2NeighboringElementsIsAtLeastAValue(rangeUpperLimit:int, absoluteDifferenceValue:int, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
    stackToRememberCombinations=[theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue]
    while stackToRememberCombinations:
        theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue = stackToRememberCombinations.pop()
        if len(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)!=0:
            if absoluteDifferenceBetweenLast2ElementsIsAtLeast(absoluteDifferenceValue, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
                if len(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)>=2:
                    displayNumbers(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)
        if len(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)<rangeUpperLimit:
            actualCombination=theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue
            for numberToDisplay in range(1, rangeUpperLimit + 1):
                theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue = theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue + [numberToDisplay]
                if not isElementAlreadyInTheList(numberToDisplay, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
                    if absoluteDifferenceBetweenLast2ElementsIsAtLeast(absoluteDifferenceValue,
                                                                       theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue):
                        stackToRememberCombinations.append(theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)
                theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue=actualCombination


                

def main():
    stillInTheMenu = True
    while stillInTheMenu:
        print("> Choose an option:\n1.Recursive backtracking\n2.Iterative backtracking\n3.Exit")
        selectedOption = int(input("> "))
        if selectedOption == 1:
            theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue = []
            theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue.clear()
            rangeUpperLimit = int(input("Insert the n number (length of the list): "))
            absoluteDifferenceValue = int(input("Insert the m number (smallest absolute difference between 2 neighboring elements): "))
            Recursive_EverySequenceGeneratorSoTheDifferenceOf2NeighboringElementsIsAtLeastAValue(1, rangeUpperLimit, absoluteDifferenceValue, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)
        elif selectedOption == 2:
            theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue = []
            theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue.clear()
            rangeUpperLimit = int(input("Insert the n number (length of the list): "))
            absoluteDifferenceValue = int(input("Insert the m number (smallest absolute difference between 2 neighboring elements): "))
            Iterative_EverySequenceGeneratorSoTheDifferenceOf2NeighboringElementsIsAtLeastAValue(rangeUpperLimit, absoluteDifferenceValue, theNumberCombinationsThatWillDisplaySoTheDifferenceOf2NeighboringElementsIsAtLeastAValue)
        elif selectedOption == 3:
            stillInTheMenu = False
            print("Bye!")

main()