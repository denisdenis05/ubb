from src.domain import Complex

class RepositoryError(Exception):
    @property
    def message(self) -> str:
        return self.__message

    def __init__(self, message: str = "Repository Error"):
        self.__message = message

    def __str__(self) -> str:
        return self.__message


class ComplexRepositoryMemory:
    def __init__(self, initialComplexNumbersList):
        self.__data = initialComplexNumbersList

    def addToRepository(self, newComplexNumber: Complex):
        complexNumberToAdd = (newComplexNumber.getRealPart(), newComplexNumber.getImaginaryPart())
        if complexNumberToAdd in self.__data:
            raise RepositoryError(f"Complex number {newComplexNumber} already in repository, skipped")
        else:
            self.__data[complexNumberToAdd] = newComplexNumber

    def removeFromRepository(self, complex_number: Complex) -> Complex:
        complexNumberToRemove = (complex_number.getRealPart(), complex_number.getImaginaryPart())
        if complexNumberToRemove not in self.__data:
            raise RepositoryError("Complex number not in repository")
        return self.__data.pop(complexNumberToRemove)

    def getAllSavedDictionaryValues(self):
        complexNumbersListToReturn = {}
        for complexNumber in self.__data:
            complexNumbersListToReturn[complexNumber] = self.__data[complexNumber]
        return complexNumbersListToReturn

    def getAllSavedListValues(self) -> list:
        dictionaryOfRepositoryValues = self.getAllSavedDictionaryValues()
        listOfRepositoryValues = []
        for complexNumber in dictionaryOfRepositoryValues:
            listOfRepositoryValues.append(dictionaryOfRepositoryValues[complexNumber])
        return listOfRepositoryValues

    def __len__(self):
        return len(self.__data)

