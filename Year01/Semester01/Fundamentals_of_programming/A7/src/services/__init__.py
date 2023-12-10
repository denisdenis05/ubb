from src.ui import UI
from src.domain import Complex
from copy import deepcopy
from src.repository import ComplexRepositoryMemory
from colorama import Fore, Back, init


class Services:
    def __init__(self, complexNumbersRepository, typeOfRepository: str):
        self.typeOfRepository = typeOfRepository
        self.complexNumbersRepository = complexNumbersRepository
        listOfComplexNumbers = self.complexNumbersRepository.getAllSavedListValues()
        self.uiComponent = UI()
        self.historyOfChanges = [listOfComplexNumbers]
        init(autoreset=True)



    def extractImaginaryPartNumberFromString(self, imaginaryPart: str) -> int:
        imaginaryPart = imaginaryPart.replace("i", "")
        try:
            imaginaryPart = int(imaginaryPart)
        except ValueError:
            imaginaryPart = 1
        return imaginaryPart

    def parseComplexNumberString(self, stringComplexNumber: str) -> tuple:
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
                stringComplexNumber = self.extractImaginaryPartNumberFromString(stringComplexNumber)
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
            imaginaryPart = self.extractImaginaryPartNumberFromString(imaginaryPart)
            if isImaginaryPartNegative:
                imaginaryPart = imaginaryPart * (-1)
            if isRealPartNegative:
                realPart = realPart * (-1)
        elif "i" in realPart:
            realPart, imaginaryPart = imaginaryPart, realPart
            realPart = int(realPart)
            imaginaryPart = self.extractImaginaryPartNumberFromString(imaginaryPart)
            if isImaginaryPartNegative:
                realPart = realPart * (-1)
            if isRealPartNegative:
                imaginaryPart = imaginaryPart * (-1)

        return (realPart, imaginaryPart)

    def getCurrentComplexNumbersListFromHistory(self):
        if len(self.historyOfChanges) == 0:
            emptyList = []
            return emptyList
        return deepcopy(self.historyOfChanges[-1])

    def addComplexNumbersListToHistory(self, complexNumbersList: list):
        self.historyOfChanges.append(complexNumbersList)


    def convertTupleToComplexInstance(self, complexNumberTuple: tuple) -> Complex:
        INDEX_OF_REAL_PART = 0
        INDEX_OF_IMAGINARY_PART = 1
        realPart = complexNumberTuple[INDEX_OF_REAL_PART]
        imaginaryPart = complexNumberTuple[INDEX_OF_IMAGINARY_PART]
        complexNumber = Complex(realPart, imaginaryPart)
        return complexNumber

    def addNumberToList(self):
        try:
            complexNumberList = self.getCurrentComplexNumbersListFromHistory()
            complexNumberString = self.uiComponent.inputComplexNumber()
            complexNumberTuple = self.parseComplexNumberString(complexNumberString)
            complexNumber = self.convertTupleToComplexInstance(complexNumberTuple)

            self.complexNumbersRepository.addToRepository(complexNumber)

            complexNumberList.append(complexNumber)
            self.addComplexNumbersListToHistory(complexNumberList)
        except Exception as exceptionOccurred:
            print(Fore.RED + str(exceptionOccurred))

    def displayListOfNumbers(self):
        textToPrint = "| "
        complexNumberList = self.getCurrentComplexNumbersListFromHistory()
        if len(complexNumberList) == 0:
            self.uiComponent.displayMessage("List is empty\n")
        else:
            for complexNumber in complexNumberList:
                textToPrint += str(complexNumber) + " | "
            self.uiComponent.displayMessage(textToPrint + "\n")


    def removeElementsFromListOutsideBound(self, lowerBound: Complex, upperBound: Complex):
        complexNumberIndex = 0
        complexNumberList = self.getCurrentComplexNumbersListFromHistory()
        lengthOfComplexNumbersList = len(complexNumberList)
        while complexNumberIndex < lengthOfComplexNumbersList:
            complexNumber = complexNumberList[complexNumberIndex]
            if complexNumber < lowerBound or complexNumber > upperBound:
                complexNumberList.pop(complexNumberIndex)
                lengthOfComplexNumbersList -= 1
                complexNumberIndex -= 1
                self.complexNumbersRepository.removeFromRepository(complexNumber)
            complexNumberIndex += 1
        self.addComplexNumbersListToHistory(complexNumberList)



    def filterList(self):
        self.uiComponent.displayMessage("\nInput start index")
        startIndexText = self.uiComponent.inputComplexNumber()
        self.uiComponent.displayMessage("\nInput end index")
        endIndexText = self.uiComponent.inputComplexNumber()

        startIndexTuple = self.parseComplexNumberString(startIndexText)
        startIndex = self.convertTupleToComplexInstance(startIndexTuple)

        endIndexTuple = self.parseComplexNumberString(endIndexText)
        endIndex = self.convertTupleToComplexInstance(endIndexTuple)

        self.removeElementsFromListOutsideBound(startIndex, endIndex)

    def undoOperation(self):
        if len(self.historyOfChanges) == 1:
            self.uiComponent.displayMessage("No more undos")
        else:
            self.historyOfChanges.pop(-1)
            self.uiComponent.displayMessage("Saving undo...")
            self.saveAll()

    def handleMenuOption(self, option: int):
        ADD_NUMBER = 1
        DISPLAY_NUMBERS = 2
        FILTER_LIST = 3
        UNDO = 4
        stillInTheMenu = True
        if option == ADD_NUMBER:
            self.addNumberToList()
            return stillInTheMenu
        elif option == DISPLAY_NUMBERS:
            self.displayListOfNumbers()
            return stillInTheMenu
        elif option == FILTER_LIST:
            self.filterList()
            return stillInTheMenu
        elif option == UNDO:
            self.undoOperation()
            return stillInTheMenu
        else:
            self.saveAndExit()
            stillInTheMenu = False
            return stillInTheMenu


    def startMenu(self):
        stillInTheMenu = True
        while stillInTheMenu:
            self.uiComponent.displayMenu()
            functionality = self.uiComponent.inputMenuOption()
            INVALID_OPTION = -1
            if functionality != INVALID_OPTION:
                stillInTheMenu = self.handleMenuOption(functionality)


    def saveAll(self):
        listOfComplexNumbers = self.getCurrentComplexNumbersListFromHistory()
        if self.typeOfRepository == "sql":
            self.complexNumbersRepository.deleteAllElementsFromRepository()
        for complexNumber in listOfComplexNumbers:
            try:
                self.complexNumbersRepository.addToRepository(complexNumber)
            except Exception as exceptionOccurred:
                print(Fore.RED + str(exceptionOccurred))

    def saveAndExit(self):
        self.uiComponent.displayMessage("Saving and exiting...")
        self.saveAll()
