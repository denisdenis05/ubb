class UndoRedo:
    def __init__(self):
        self.__undoStack = []
        self.__redoStack = []

    def addUndoOperationToHistory(self, operations):
        self.__undoStack.append(operations)
        self.__redoStack = []

    def addRedoOperationToHistory(self, operations):
        self.__redoStack.append(operations)

    def getOperationFromUndoStack(self):
        if len(self.__undoStack) == 0:
            return None
        return self.__undoStack.pop()

    def getOperationFromRedoStack(self):
        if len(self.__redoStack) == 0:
            return None
        return self.__redoStack.pop()