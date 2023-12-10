from src.domain import Complex
from src.repository import ComplexRepositoryMemory
import pickle

class ComplexRepositoryBinary(ComplexRepositoryMemory):
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
            with open(self.__file_name, "rb") as fileToRead:
                try:
                    savedDictionaryOfSavedComplexNumbers = pickle.load(fileToRead)
                except EOFError:
                    savedDictionaryOfSavedComplexNumbers = {}

                dictionaryOfSavedComplexNumbers = {}
                for complexNumber in savedDictionaryOfSavedComplexNumbers:
                    INDEX_OF_REAL_PART = 0
                    INDEX_OF_IMAGINARY_PART = 1
                    realPart = complexNumber[INDEX_OF_REAL_PART]
                    imaginaryPart = complexNumber[INDEX_OF_IMAGINARY_PART]
                    complexNumberToAdd = Complex(realPart, imaginaryPart)
                    dictionaryOfSavedComplexNumbers[complexNumber] = complexNumberToAdd
                return dictionaryOfSavedComplexNumbers
        except FileNotFoundError:
            emptyDictionary = {}
            return emptyDictionary

    def __save_file(self):
        with open(self.__file_name, "wb+") as fileToWrite:
            pickle.dump(self.__data, fileToWrite)
