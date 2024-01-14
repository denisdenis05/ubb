from src.repository.repository import RepositoryMemory
from src.repository.repository import RepositoryError
from src.domain.domain import Student
from src.domain.domain import Discipline
from src.domain.domain import FacultyGrades


class RepositoryTextFile(RepositoryMemory):
    def __init__(self, typeOfRepository, file_name):
        self.__file_name = file_name
        self.__typeOfRepository = typeOfRepository
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
            with open(self.__file_name, "r+") as fileToRead:
                dictionaryOfSavedComplexNumbers = {}
                linesToParse = fileToRead.readlines()
                for lineToParse in linesToParse:
                    if self.__typeOfRepository == "grades":
                        studentId, disciplineId, grades = lineToParse.split(":")
                        grades = grades[:-1]
                        studentId = int(studentId)
                        disciplineId = int(disciplineId)
                        gradeIdentifier = (studentId, disciplineId)
                        allGradesList = grades.split(" ")
                        listOfGradesToInput = []
                        for grade in allGradesList:
                            if grade != "":
                                gradeObject = FacultyGrades(studentId, disciplineId, int(grade))
                                listOfGradesToInput.append(gradeObject)
                        dictionaryOfSavedComplexNumbers[gradeIdentifier] = listOfGradesToInput
                    elif self.__typeOfRepository == "students":
                        studentId, studentName = lineToParse.split(":")
                        studentId = int(studentId)
                        studentName = studentName[:-1]
                        studentToAdd = Student(studentId, studentName)
                        dictionaryOfSavedComplexNumbers[studentId] = studentToAdd
                    elif self.__typeOfRepository == "disciplines":
                        disciplineId, disciplineName = lineToParse.split(":")
                        disciplineId = int(disciplineId)
                        disciplineName = disciplineName[:-1]
                        disciplineToAdd = Discipline(disciplineId, disciplineName)
                        dictionaryOfSavedComplexNumbers[disciplineId] = disciplineToAdd
                return dictionaryOfSavedComplexNumbers
        except FileNotFoundError:
            emptyDictionary = {}
            return emptyDictionary


    def __save_file(self):
        textToWrite = ""
        if self.__typeOfRepository == "grades":
            for gradeIdentifier in self.__data:
                studentId, disciplineId = gradeIdentifier
                grades = self.__data[gradeIdentifier]
                gradesToAdd = ""
                for grade in grades:
                    gradesToAdd += str(int(grade.getGrade())) + " "
                textToWrite += f"{studentId}:{disciplineId}:{gradesToAdd}\n"
        elif self.__typeOfRepository == "students":
            for instanceIdentifier in self.__data:
                instance = self.__data[instanceIdentifier].getStudentName()
                textToWrite += f"{instanceIdentifier}:{instance}\n"
        elif self.__typeOfRepository == "disciplines":
            for instanceIdentifier in self.__data:
                instance = self.__data[instanceIdentifier].getDisciplineName()
                textToWrite += f"{instanceIdentifier}:{instance}\n"
        with open(self.__file_name, "w+") as fileToWrite:
            fileToWrite.write(textToWrite)
