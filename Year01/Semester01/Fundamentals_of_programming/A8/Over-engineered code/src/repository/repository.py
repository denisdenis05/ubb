class RepositoryError(Exception):
    @property
    def message(self) -> str:
        return self.__message

    def __init__(self, message: str = "Repository Error"):
        self.__message = message

    def __str__(self) -> str:
        return self.__message


class RepositoryMemory:
    def __init__(self):
        self.__data = {}

    def addToRepository(self, instanceToAdd, instanceIdentifier):
        if instanceIdentifier in self.__data:
            raise RepositoryError(f"Item {instanceIdentifier} already in repository")
        else:
            self.__data[instanceIdentifier] = instanceToAdd

    def addAsMultipleItemsToRepository(self, instancesToAdd, instanceIdentifier):
        if instanceIdentifier in self.__data:
            self.__data[instanceIdentifier].append(instancesToAdd)
        else:
            self.__data[instanceIdentifier] = [instancesToAdd]
        return instancesToAdd

    def removeFromRepository(self, instanceIdentifier):
        print(self.__data)
        if instanceIdentifier not in self.__data.keys():
            return None
        else:
            return self.__data.pop(instanceIdentifier)

    def getItem(self, instanceIdentifier):
        for instanceToCheck in self.__data:
            if instanceToCheck == instanceIdentifier:
                return self.__data[instanceToCheck]
        return None

    def getAllItems(self):
        return self.__data

    def updateItem(self, instanceIdentifier, newItem):
        print(self.__data)
        if instanceIdentifier not in self.__data.keys():
            raise RepositoryError(f"Item {instanceIdentifier} not in repository")
        else:
            self.__data[instanceIdentifier] = newItem

    def __len__(self):
        return len(self.__data)

