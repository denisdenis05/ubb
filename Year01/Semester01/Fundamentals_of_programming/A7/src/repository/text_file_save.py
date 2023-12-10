from src.domain import Complex
from src.repository import ComplexRepositoryMemory

class ComplexRepositoryTextFile(ComplexRepositoryMemory):
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
                dictionaryOfSavedComplexNumbers = {}
                linesToParse = fileToRead.readlines()
                for lineToParse in linesToParse:
                    realPart, imaginaryPart = lineToParse.split(" ")
                    realPart = int(realPart)
                    imaginaryPart = int(imaginaryPart)
                    complexNumberToAdd = Complex(realPart, imaginaryPart)
                    complexNumberIndices = (realPart, imaginaryPart)
                    dictionaryOfSavedComplexNumbers[complexNumberIndices] = complexNumberToAdd

                return dictionaryOfSavedComplexNumbers
        except FileNotFoundError:
            emptyDictionary = {}
            return emptyDictionary

    def __save_file(self):
        textToWrite = ""
        for complexNumberIndex in self.__data:
            complexNumber = self.__data[complexNumberIndex]
            realPart = complexNumber.getRealPart()
            imaginaryPart = complexNumber.getImaginaryPart()
            textToWrite += str(realPart) + " " + str(imaginaryPart) + "\n"
        with open(self.__file_name, "w+") as fileToWrite:
            fileToWrite.write(textToWrite)
