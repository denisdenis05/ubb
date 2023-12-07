#
# Write the implementation for A5 in this file
#


# Complex numbers parser functions:

def addComplexNumberToTheList(listOfComplexNumbers: list, ComplexNumber) -> list:
    """
    Adds an imaginary number to the list of complex numbers
    :param listOfComplexNumbers: a list of complex numbers
    :param ComplexNumber: the complex number
    :return: updated complex numbers list
    """
    listOfComplexNumbers.append(ComplexNumber)
    return listOfComplexNumbers

def extractImaginaryPartNumberFromString(imaginaryPart: str) -> int:
    """
    Eliminates the imaginary unit out of a string
    :param imaginaryPart: string of the imaginary part
    :return: integer (imaginary part)
    """
    imaginaryPart = imaginaryPart.replace("i", "")
    try:
        imaginaryPart = int(imaginaryPart)
    except ValueError:
        imaginaryPart = 1
    return imaginaryPart



#
# Write below this comment
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#




def getImaginaryPart(complexNumber: list) -> int:
    secondPositionInAList = 1
    return complexNumber[secondPositionInAList]
def getRealPart(complexNumber: list) -> int:
    firstPositionInAList = 0
    return complexNumber[firstPositionInAList]

def parseComplexNumberString(stringComplexNumber: str) -> list:
    realPart = 0
    imaginaryPart = 0
    isRealPartNegative = False
    isImaginaryPartNegative = False
    secondPositionInAList = 1
    if stringComplexNumber.startswith("-"):
        isRealPartNegative = True
        stringComplexNumber = stringComplexNumber[secondPositionInAList:]

    if "+" not in stringComplexNumber and "-" not in stringComplexNumber:
        if "i" in stringComplexNumber:
            stringComplexNumber = extractImaginaryPartNumberFromString(stringComplexNumber)
            if isRealPartNegative:
                stringComplexNumber = stringComplexNumber * (-1)
            return [0, stringComplexNumber]
        else:
            stringComplexNumber = int(stringComplexNumber)
            if isRealPartNegative:
                stringComplexNumber = stringComplexNumber * (-1)
            return [stringComplexNumber, 0]
    if "+" in stringComplexNumber:
        realPart, imaginaryPart = stringComplexNumber.split("+")
    elif "-" in stringComplexNumber:
        realPart, imaginaryPart = stringComplexNumber.split("-")
        isImaginaryPartNegative = True

    if "i" in imaginaryPart:
        realPart = int(realPart)
        imaginaryPart = extractImaginaryPartNumberFromString(imaginaryPart)
        if isImaginaryPartNegative:
            imaginaryPart = imaginaryPart * (-1)
        if isRealPartNegative:
            realPart = realPart * (-1)
    elif "i" in realPart:
        realPart, imaginaryPart = imaginaryPart, realPart
        realPart = int(realPart)
        imaginaryPart = extractImaginaryPartNumberFromString(imaginaryPart)
        if isImaginaryPartNegative:
            realPart = realPart * (-1)
        if isRealPartNegative:
            imaginaryPart = imaginaryPart * (-1)

    return [realPart, imaginaryPart]


#
# Write below this comment
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
"""
def getImaginaryPart(complexNumber: dict) -> int:
    return complexNumber["imaginaryPart"]
def getRealPart(complexNumber: dict) -> int:
    return complexNumber["realPart"]

def parseComplexNumberString(stringComplexNumber: str) -> dict
    realPart = 0
    imaginaryPart = 0
    isRealPartNegative = False
    isImaginaryPartNegative = False

    if stringComplexNumber.startswith("-"):
        isRealPartNegative = True
        stringComplexNumber = stringComplexNumber[1:]

    if "+" not in stringComplexNumber and "-" not in stringComplexNumber:
        if "i" in stringComplexNumber:
            stringComplexNumber = extractImaginaryPartNumberFromString(stringComplexNumber)
            if isRealPartNegative:
                stringComplexNumber = stringComplexNumber * (-1)
            return {"realPart": 0, "imaginaryPart": stringComplexNumber}
        else:
            stringComplexNumber = int(stringComplexNumber)
            if isRealPartNegative:
                stringComplexNumber = stringComplexNumber * (-1)
            return {"realPart": stringComplexNumber, "imaginaryPart": 0}
    if "+" in stringComplexNumber:
        realPart, imaginaryPart = stringComplexNumber.split("+")
    elif "-" in stringComplexNumber:
        realPart, imaginaryPart = stringComplexNumber.split("-")
        isImaginaryPartNegative = True

    if "i" in imaginaryPart:
        realPart = int(realPart)
        imaginaryPart = extractImaginaryPartNumberFromString(imaginaryPart)
        if isImaginaryPartNegative:
            imaginaryPart = imaginaryPart * (-1)
        if isRealPartNegative:
            realPart = realPart * (-1)
    elif "i" in realPart:
        realPart, imaginaryPart = imaginaryPart, realPart
        realPart = int(realPart)
        imaginaryPart = extractImaginaryPartNumberFromString(imaginaryPart)
        if isImaginaryPartNegative:
            realPart = realPart * (-1)
        if isRealPartNegative:
            imaginaryPart = imaginaryPart * (-1)

    return {"realPart": realPart, "imaginaryPart": imaginaryPart}
"""
#
# Write below this comment
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def moreThan3DistinctNumbersInComplexNumberList(listOfComplexNumbers: list, startingSubSequencePoint: int, endingSubSequencePoint: int) -> bool:
    """
    Checks if the subsequence contains more than 3 distinct complex numbers
    :param listOfComplexNumbers: a list of complex numbers
    :param startingSubSequencePoint: starting point index of the subsequence
    :param endingSubSequencePoint: ending point index of the subsequence
    :return: whether the subsequence contains more than 3 distinct complex numbers (boolean)
    """
    numberOfTimesComplexNumbersAppearInList = {}
    for complexNumberListIndex in range(startingSubSequencePoint, endingSubSequencePoint+1):
        complexNumber = listOfComplexNumbers[complexNumberListIndex]
        if str(complexNumber) not in numberOfTimesComplexNumbersAppearInList:
            numberOfTimesComplexNumbersAppearInList[str(complexNumber)] = 1
        else:
            numberOfTimesComplexNumbersAppearInList[str(complexNumber)] += 1
    if len(numberOfTimesComplexNumbersAppearInList) > 3:
        return True
    return False

def getMaximumLengthSubSequenceForAtMost3DistinctNumbers(listOfComplexNumbers: list):
    """
    Naively checks the largest subsequence with at most 3 distinct complex numbers
    :param listOfComplexNumbers: a list of complex numbers
    :return: the indexes of the longest increasing subsequence (starting point, ending point) and the subsequence length
    """
    firstPositionInAList = 0

    maximumSubSequenceLength = 0
    maximumSubSequenceIndexes = (firstPositionInAList, firstPositionInAList)
    for startingSubSequencePoint in range(firstPositionInAList, len(listOfComplexNumbers)):
        for endingSubSequencePoint in range(startingSubSequencePoint+1, len(listOfComplexNumbers)):
            if not moreThan3DistinctNumbersInComplexNumberList(listOfComplexNumbers, startingSubSequencePoint, endingSubSequencePoint):
                if endingSubSequencePoint-startingSubSequencePoint+1 > maximumSubSequenceLength:
                    maximumSubSequenceLength = endingSubSequencePoint-startingSubSequencePoint+1
                    maximumSubSequenceIndexes = (startingSubSequencePoint, endingSubSequencePoint)
    return maximumSubSequenceIndexes, maximumSubSequenceLength


def getLongestSequenceWithMaximum3DistinctNumbers(listOfComplexNumbers: list):
    """
    Starts the search and prints the longest subsequence with at most 3 distinct complex numbers
    :param listOfComplexNumbers: a list of complex numbers
    :return: nothing
    """
    maximumSubSequenceIndexes, maximumSubSequenceLength = getMaximumLengthSubSequenceForAtMost3DistinctNumbers(listOfComplexNumbers)
    printLongestSequenceWithMaximum3DistinctNumbers(listOfComplexNumbers, maximumSubSequenceIndexes)

def realPartIsGreater(complexNumberThatShouldBeHigher, complexNumberThatShouldBeLower):
    """
    Checks if out of two complex numbers, the real part of the first is greater than the real part of the second
    :param complexNumberThatShouldBeHigher: the complex number that its real part should be higher
    :param complexNumberThatShouldBeLower: the complex number that its real part should be lower
    :return: whether the real part of the first is greater than the real part of the second (boolean)
    """
    firstNumberRealPart = getRealPart(complexNumberThatShouldBeHigher)
    secondNumberRealPart = getRealPart(complexNumberThatShouldBeLower)
    return firstNumberRealPart >= secondNumberRealPart

def parseAllIncreasingSubsequences(listOfComplexNumbers: list):
    """
    Dinamically creates a dictionary that contains the longest increasing subsequence at each index and the starting point of the sequence
    :param listOfComplexNumbers: a list of complex numbers
    :return: a dict that contains at each index the length and the starting point of the increasing subsequence
    """
    dictionaryOfPossibleIncreasingSubSequences = {}
    lengthOfTheComplexNumbersList = len(listOfComplexNumbers)
    firstPositionInAList = 0
    for complexNumberIndex in range(firstPositionInAList, lengthOfTheComplexNumbersList):
        dictionaryOfPossibleIncreasingSubSequences[complexNumberIndex] = (1, complexNumberIndex)
        if complexNumberIndex != 0:
            currentComplexNumber = listOfComplexNumbers[complexNumberIndex]
            previousComplexNumber = listOfComplexNumbers[complexNumberIndex - 1]
            if realPartIsGreater(currentComplexNumber, previousComplexNumber):
                subSequenceLengthAtIndex = dictionaryOfPossibleIncreasingSubSequences[complexNumberIndex-1][0]
                startingPointOfsubSequenceAtIndex = dictionaryOfPossibleIncreasingSubSequences[complexNumberIndex-1][1]

                lengthOfCurrentSubSequence = subSequenceLengthAtIndex + 1
                startOfTheCurrentSubSequence = startingPointOfsubSequenceAtIndex
                dictionaryOfPossibleIncreasingSubSequences[complexNumberIndex] = (lengthOfCurrentSubSequence, startOfTheCurrentSubSequence)
    return dictionaryOfPossibleIncreasingSubSequences

def getMaximumLengthSubSequenceForIncreasingSubSequences(dictionaryOfPossibleIncreasingSubSequences: dict):
    """
    Finds the maximum length subsequence in a dictionary of increasing subsequences
    :param dictionaryOfPossibleIncreasingSubSequences: dict that contains at each index the length and the starting point of the increasing subsequence
    :return: the indexes of the longest increasing subsequence (starting point, ending point)
    """
    firstPositionInAList = 0
    secondPositionInAList = 1
    maximumSubSequenceLength = 0
    maximumSubSequenceIndexes = (firstPositionInAList, firstPositionInAList)
    lengthOfTheComplexNumbersList = len(dictionaryOfPossibleIncreasingSubSequences)
    for currentComplexNumberIndex in range(firstPositionInAList, lengthOfTheComplexNumbersList):
        subSequenceLengthAtIndex = dictionaryOfPossibleIncreasingSubSequences[currentComplexNumberIndex][firstPositionInAList]
        startingPointOfsubSequenceAtIndex = dictionaryOfPossibleIncreasingSubSequences[currentComplexNumberIndex][secondPositionInAList]
        if maximumSubSequenceLength <= subSequenceLengthAtIndex:
            maximumSubSequenceLength = subSequenceLengthAtIndex
            maximumSubSequenceIndexes = (startingPointOfsubSequenceAtIndex, currentComplexNumberIndex)
    return maximumSubSequenceIndexes

def getLongestIncreasingSequence(listOfComplexNumbers: list):
    """
    Starts the search and prints the longest increasing subsequence in a list of complex numbers, when considering each number's real part.
    :param listOfComplexNumbers: a list of complex numbers
    :return:
    """
    dictionaryOfPossibleIncreasingSubSequences = parseAllIncreasingSubsequences(listOfComplexNumbers)
    maximumSubSequenceIndexes = getMaximumLengthSubSequenceForIncreasingSubSequences(dictionaryOfPossibleIncreasingSubSequences)
    printLongestIncreasingSequence(listOfComplexNumbers, maximumSubSequenceIndexes)


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def getMenuFunctionalityInput() -> int:
    """
    Inputs the menu functionality (options from 1 to 5)
    :return: the option chosen as integer
    """
    exitMenuOption = 5
    try:
        return int(input("> "))
    except ValueError:
        return exitMenuOption


def inputComplexNumber() -> str:
    """
    Inputs a complex number
    :return: string of complex number
    """
    stringComplexNumber = input("Insert complex number (a+bi): ")
    return stringComplexNumber


def inputListOfComplexNumbers(listOfComplexNumbers: list):
    """
    Inputs complex numbers into the list of complex numbers
    :param listOfComplexNumbers: a list of complex numbers
    :return: the updated list of complex numbers
    """
    listLength = int(input("Insert the length of the list:"))
    firstPositionInAList = 0
    for listElement in range(firstPositionInAList, listLength):
        stringComplexNumber = inputComplexNumber()
        ComplexNumber = parseComplexNumberString(stringComplexNumber)
        listOfComplexNumbers = addComplexNumberToTheList(listOfComplexNumbers, ComplexNumber)
    return listOfComplexNumbers

def printListOfComplexNumbers(listOfComplexNumbers: list, startingPoint: int, endingPoint: int):
    """
    Prints complex numbers from a list in a specified range
    :param listOfComplexNumbers: a list of complex numbers
    :param startingPoint: the index in list where the printing should start
    :param endingPoint: the index in list where the printing should stop
    :return: nothing
    """
    textToPrint = ""
    for complexNumberListIndex in range(startingPoint, endingPoint+1):
        complexNumber = listOfComplexNumbers[complexNumberListIndex]
        realPart = getRealPart(complexNumber)
        imaginaryPart = getImaginaryPart(complexNumber)
        if realPart == 0:
            textToPrint = textToPrint + str(imaginaryPart) + "i; "
        elif imaginaryPart == 0:
            textToPrint = textToPrint + str(realPart) + "; "
        elif imaginaryPart >= 0:
            textToPrint = textToPrint + str(realPart) + "+" + str(imaginaryPart) + "i; "
        else:
            textToPrint = textToPrint + str(realPart) + str(imaginaryPart) + "i; "
    print(textToPrint+"\n")


def printLongestSequenceWithMaximum3DistinctNumbers(listOfComplexNumbers: list, maximumSubSequenceIndexes: tuple):
    """
            Calls printListOfComplexNumbers() in order to print all the complex numbers in the subsequence with at most 3 distinct numbers
            :param listOfComplexNumbers: a list of complex numbers
            :param maximumSubSequenceIndexes: the indexes of the subsequence (from tuple[0] to tuple[1])
            :return: nothing
            """
    firstPositionInAList = 0
    secondPositionInAList = 1
    startingPoint = maximumSubSequenceIndexes[firstPositionInAList]
    endingPoint = maximumSubSequenceIndexes[secondPositionInAList]
    maximumSubSequenceLength = endingPoint - startingPoint + 1
    print(f"\nThe length of the longest subarray of numbers that contains at most 3 distinct values is {maximumSubSequenceLength}")
    print(f"The longest subarray that contains at most 3 distinct values:")
    printListOfComplexNumbers(listOfComplexNumbers, startingPoint, endingPoint)

def printLongestIncreasingSequence(listOfComplexNumbers: list, maximumSubSequenceIndexes: tuple):
    """
        Calls printListOfComplexNumbers() in order to print all the complex numbers in the increasing subsequence
        :param listOfComplexNumbers: a list of complex numbers
        :param maximumSubSequenceIndexes: the indexes of the subsequence (from tuple[0] to tuple[1])
        :return: nothing
        """
    firstPositionInAList = 0
    secondPositionInAList = 1
    startingPoint = maximumSubSequenceIndexes[firstPositionInAList]
    endingPoint = maximumSubSequenceIndexes[secondPositionInAList]
    maximumSubSequenceLength = endingPoint-startingPoint+1
    print(f"\nThe length of the longest increasing subarray of numbers is {maximumSubSequenceLength}")
    print(f"The longest increasing subarray:")
    printListOfComplexNumbers(listOfComplexNumbers, startingPoint, endingPoint)


def printAllComplexNumbersOfTheList(listOfComplexNumbers: list):
    """
    Calls printListOfComplexNumbers() in order to print all the complex numbers
    :param listOfComplexNumbers: a list of complex numbers
    :return: nothing
    """
    print(f"\n\nThe list of complex numbers:")
    printListOfComplexNumbers(listOfComplexNumbers, 0, len(listOfComplexNumbers)-1)

def printMenuFunctionalities():
    """
    Prints the menu
    :return: nothing
    """
    print("Choose a functionality:")
    print("1.Read a list of complex numbers (in z = a + bi form) from the console.")
    print("2.Display the entire list of numbers on the console.")
    print("3.Display length and elements of a longest subarray of numbers that contain at most 3 distinct values.")
    print("4.The length and elements of a longest increasing subsequence, when considering each number's real part.")
    print("5.Exit the application.")


def runChosenFunctionalityFromMenu(functionalityChosen: int, listOfComplexNumbers: list):
    """

    :param functionalityChosen: the functionality chosen by the user
    :param listOfComplexNumbers: a list of complex numbers
    :return: still in the menu (boolean), the list of complex numbers
    """
    stillInTheMenu = True

    insertComplexNumbersInListOption = 1
    printEntireListOption = 2
    printSubsequenceWithAtMost3DistinctValuesOption = 3
    printLongestIncreasingSubsequenceOption = 4
    exitMenuOption = 5

    if functionalityChosen == insertComplexNumbersInListOption:
        return stillInTheMenu, inputListOfComplexNumbers(listOfComplexNumbers)
    elif functionalityChosen == printEntireListOption:
        printAllComplexNumbersOfTheList(listOfComplexNumbers)
        return stillInTheMenu, listOfComplexNumbers
    elif functionalityChosen == printSubsequenceWithAtMost3DistinctValuesOption:
        getLongestSequenceWithMaximum3DistinctNumbers(listOfComplexNumbers)
        return True, listOfComplexNumbers
    elif functionalityChosen == printLongestIncreasingSubsequenceOption:
        getLongestIncreasingSequence(listOfComplexNumbers)
    elif functionalityChosen == exitMenuOption:
        print("Exited the menu.")
        stillInTheMenu = False
        return stillInTheMenu, listOfComplexNumbers
    return True, listOfComplexNumbers

def InitializeArrayWithSomeValues(listOfComplexNumbers: list) -> list:
    listOfComplexNumbers = [[1, 1], [-1, 2], [-3, -5], [0, 1], [2, 1], [3, 3], [7, 2], [9, 11], [3, 2], [3, 2], [9, 11]]
    """
    listOfComplexNumbers = [{"realPart": 1, "imaginaryPart": 1}, {"realPart": -1, "imaginaryPart": 2}, {"realPart": -3, "imaginaryPart": -5},
                            {"realPart": 0, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 1}, {"realPart": 3, "imaginaryPart": 3},
                            {"realPart": 7, "imaginaryPart": 2}, {"realPart": 9, "imaginaryPart": 11}, {"realPart": 3, "imaginaryPart": 2}, 
                            {"realPart": 3, "imaginaryPart": 2}, {"realPart": 9, "imaginaryPart": 11}]
    """
    return listOfComplexNumbers

def mainMenuManager():
    """
    The menu manager; Prints the menu as long as the user doesn't exit
    :return: nothing
    """
    stillInTheMenu = True
    listOfComplexNumbers = []
    listOfComplexNumbers = InitializeArrayWithSomeValues(listOfComplexNumbers)
    while stillInTheMenu:
        printMenuFunctionalities()
        functionality = getMenuFunctionalityInput()
        stillInTheMenu, listOfComplexNumbers = runChosenFunctionalityFromMenu(functionality, listOfComplexNumbers)


def main():
    """
    Main function
    :return: nothing
    """
    mainMenuManager()


if __name__ == "__main__":
    main()
