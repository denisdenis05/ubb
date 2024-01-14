from src.repository.repository import RepositoryMemory
from src.repository.repository import RepositoryError
import pickle


class RepositoryBinary(RepositoryMemory):
    def __init__(self, typeOfRepository, file_name):
        self.__typeOfRepository = typeOfRepository
        self.__file_name = file_name
        self.__data = self.__loadFile()
        super().__init__(typeOfRepository, self.__data)


    def addToRepository(self, instanceToAdd, instanceIdentifier):
        statusOfCommand = super().addToRepository(instanceToAdd, instanceIdentifier)
        self.__data = super().getAllItems()
        self.__save_file()
        return statusOfCommand

    def addAsMultipleItemsToRepository(self, instancesToAdd, instanceIdentifier):
        statusOfCommand = super().addAsMultipleItemsToRepository(instancesToAdd, instanceIdentifier)
        self.__data = super().getAllItems()
        self.__save_file()
        return statusOfCommand

    def removeFromRepository(self, instanceIdentifier):
        statusOfCommand = super().removeFromRepository(instanceIdentifier)
        self.__data = super().getAllItems()
        self.__save_file()
        return statusOfCommand

    def updateItem(self, instanceIdentifier, newItem):
        statusOfCommand = super().updateItem(instanceIdentifier, newItem)
        self.__data = super().getAllItems()
        self.__save_file()
        return statusOfCommand


    def __loadFile(self):
        try:
            with open(self.__file_name, "rb") as fileToRead:
                try:
                    savedDictionaryOfSavedComplexNumbers = pickle.load(fileToRead)
                    return savedDictionaryOfSavedComplexNumbers
                except EOFError:
                    savedDictionaryOfSavedComplexNumbers = {}
        except FileNotFoundError:
            emptyDictionary = {}
            return emptyDictionary

    def __save_file(self):
        with open(self.__file_name, "wb+") as fileToWrite:
            pickle.dump(self.__data, fileToWrite)