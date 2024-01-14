from services.services import Services
from src.repository.binaryRepository import RepositoryBinary
from src.repository.repository import RepositoryMemory
from src.repository.textFileRepository import RepositoryTextFile
from src.undoRedo.commandHistoryHandler import commandHistoryHandler
from ui.uiManager import UiManager
import constants
import configparser


def getProperties():
    configParserInstance = configparser.RawConfigParser()
    configParserInstance.read('src/settings.properties')
    typeOfRepository = str(configParserInstance.get('settings', 'typeOfRepository'))
    if typeOfRepository == "binary":
        studentsSaveFileName = str(configParserInstance.get('settings', 'studentsBinaryFileName'))
        disciplinesSaveFileName = str(configParserInstance.get('settings', 'disciplinesBinaryFileName'))
        facultyDataSaveFileName = str(configParserInstance.get('settings', 'gradesBinaryFileName'))
    elif typeOfRepository == "textFile":
        studentsSaveFileName = str(configParserInstance.get('settings', 'studentsTextFileName'))
        disciplinesSaveFileName = str(configParserInstance.get('settings', 'disciplinesTextFileName'))
        facultyDataSaveFileName = str(configParserInstance.get('settings', 'gradesTextFileName'))
    else:
        studentsSaveFileName = "unknownFile"
        disciplinesSaveFileName = "unknownFile"
        facultyDataSaveFileName = "unknownFile"
    return typeOfRepository, studentsSaveFileName, disciplinesSaveFileName, facultyDataSaveFileName


def createRepositories(typeOfRepository, studentsSaveFileName, disciplinesSaveFileName, facultyDataSaveFileName):
    if typeOfRepository == "memory":
        studentsRepository = RepositoryMemory("students")
        disciplinesRepository = RepositoryMemory("disciplines")
        facultyDataRepository = RepositoryMemory("grades")
    elif typeOfRepository == "binary":
        studentsRepository = RepositoryBinary("students", studentsSaveFileName)
        disciplinesRepository = RepositoryBinary("disciplines", disciplinesSaveFileName)
        facultyDataRepository = RepositoryBinary("grades", facultyDataSaveFileName)
    else:
        studentsRepository = RepositoryTextFile("students", studentsSaveFileName)
        disciplinesRepository = RepositoryTextFile("disciplines", disciplinesSaveFileName)
        facultyDataRepository = RepositoryTextFile("grades", facultyDataSaveFileName)
    return studentsRepository, disciplinesRepository, facultyDataRepository

def populateRepositories(services):
    services.addStudent(1, "Andrei")
    services.addStudent(2, "Andreea")
    services.addStudent(3, "Marian")
    services.addStudent(4, "Constantin")
    services.addStudent(5, "Laura")
    services.addStudent(6, "Paul")
    services.addStudent(7, "Maria")
    services.addStudent(8, "Alex")
    services.addStudent(9, "Diana")
    services.addStudent(10, "Cristina")

    services.addDiscipline(1, "Math")
    services.addDiscipline(2, "English")
    services.addDiscipline(3, "French")
    services.addDiscipline(4, "German")
    services.addDiscipline(5, "History")
    services.addDiscipline(6, "Geography")
    services.addDiscipline(7, "Physics")
    services.addDiscipline(8, "Chemistry")
    services.addDiscipline(9, "Biology")
    services.addDiscipline(10, "Computer Science")

    services.gradeStudentAtADiscipline(1, 1, 10)
    services.gradeStudentAtADiscipline(1, 2, 6)
    services.gradeStudentAtADiscipline(1, 3, 3)
    services.gradeStudentAtADiscipline(2, 4, 3)
    services.gradeStudentAtADiscipline(3, 5, 3)
    services.gradeStudentAtADiscipline(2, 6, 1)
    services.gradeStudentAtADiscipline(2, 7, 5)
    services.gradeStudentAtADiscipline(3, 8, 7)
    services.gradeStudentAtADiscipline(1, 9, 10)
    services.gradeStudentAtADiscipline(2, 10, 6)
    services.gradeStudentAtADiscipline(3, 1, 8)
    services.gradeStudentAtADiscipline(3, 2, 7)
    services.gradeStudentAtADiscipline(3, 3, 2)


def main():
    typeOfRepository, studentsSaveFileName, disciplinesSaveFileName, facultyDataSaveFileName = getProperties()
    studentsRepository, disciplinesRepository, facultyDataRepository = createRepositories(typeOfRepository, studentsSaveFileName, disciplinesSaveFileName, facultyDataSaveFileName)


    serviceFunctions = Services(studentsRepository, disciplinesRepository, facultyDataRepository, constants)
    undoRedoService = commandHistoryHandler(studentsRepository, disciplinesRepository, facultyDataRepository, serviceFunctions, constants)
    uiManager = UiManager(serviceFunctions, undoRedoService, constants)

    if typeOfRepository == "memory":
        populateRepositories(serviceFunctions)

    uiManager.startMenu()


main()
