import json

from src.domain import Complex
from src.repository import ComplexRepositoryMemory

class ComplexRepositoryJSONFile(ComplexRepositoryMemory):
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__data = self.__loadFile()
        super().__init__(self.__data)

    def updateLocalDataDictionary(self):
        self.__data = super().getAllSavedDictionaryValues()

    def addToRepository(self, newComplexNumber: Complex):
        super().addToRepository(newComplexNumber)
        self.updateLocalDataDictionary()
        self.__save_file()

    def removeFromRepository(self, complexNumberToRemove: Complex):
        super().removeFromRepository(complexNumberToRemove)
        self.updateLocalDataDictionary()
        self.__save_file()
        return complexNumberToRemove

    def getAllSavedDictionaryValues(self) -> dict:
        return super().getAllSavedDictionaryValues()

    def getAllSavedListValues(self) -> list:
        return super().getAllSavedListValues()

    def __loadFile(self):

        try:
            with open(self.__file_name, "r+") as fileToRead:
                dictionaryOfSavedComplexNumbers = json.load(fileToRead)
                complexNumbersData = {}
                for complexNumberIndex in dictionaryOfSavedComplexNumbers:
                    complexNumberToAddToRepository = dictionaryOfSavedComplexNumbers[complexNumberIndex]

                    INDEX_OF_SERIALIZED_COMPLEX_NUMBER_REAL_NUMBER = 0
                    INDEX_OF_SERIALIZED_COMPLEX_NUMBER_IMAGINARY_NUMBER = 1
                    elementsOfComplexNumberToAddToRepository = list(complexNumberToAddToRepository.keys())

                    realPartIndex = elementsOfComplexNumberToAddToRepository[INDEX_OF_SERIALIZED_COMPLEX_NUMBER_REAL_NUMBER]
                    imaginaryPartIndex = elementsOfComplexNumberToAddToRepository[INDEX_OF_SERIALIZED_COMPLEX_NUMBER_IMAGINARY_NUMBER]
                    realPart = complexNumberToAddToRepository[realPartIndex]
                    imaginaryPart = complexNumberToAddToRepository[imaginaryPartIndex]

                    complexNumberTupleRepresentation = (realPart, imaginaryPart)
                    complexNumbersData[complexNumberTupleRepresentation] = Complex(realPart, imaginaryPart)
                return complexNumbersData
        except FileNotFoundError:
            emptyDictionary = {}
            return emptyDictionary

    def __save_file(self):
        complexNumbersDataToPush = {}
        for complexNumberIndex in self.__data:
            complexNumbersDataToPush[str(complexNumberIndex)] = self.__data[complexNumberIndex]
        with open(self.__file_name, "w+") as fileToWrite:
            json.dump(complexNumbersDataToPush, fileToWrite, default=vars)

