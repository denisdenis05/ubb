from services.services import Services
from services.commandHistoryHandler import commandHistoryHandler
from services.operations import Operations
from src.repository.repository import RepositoryMemory
from src.repository.binaryRepository import RepositoryBinary
from src.repository.textFileRepository import RepositoryTextFile
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

def initializeConstantMenuFunctions():
    constants.menuFunctions[constants.UNDO_OPTION] = Operations.Undo
    constants.menuFunctions[constants.REDO_OPTION] = Operations.Redo

    constants.menuFunctions[constants.ADD_STUDENT_OPTION] = Operations.addStudent
    constants.menuFunctions[constants.ADD_DISCIPLINE_OPTION] = Operations.addDiscipline

    constants.menuFunctions[constants.REMOVE_STUDENT_OPTION] = Operations.removeStudent
    constants.menuFunctions[constants.REMOVE_DISCIPLINE_OPTION] = Operations.removeDiscipline

    constants.menuFunctions[constants.UPDATE_STUDENT_OPTION] = Operations.updateStudent
    constants.menuFunctions[constants.UPDATE_DISCIPLINE_OPTION] = Operations.updateDiscipline

    constants.menuFunctions[constants.LIST_STUDENTS_OPTION] = Operations.getTextOfAllStudents
    constants.menuFunctions[constants.LIST_DISCIPLINES_OPTION] = Operations.getTextOfAllDisciplines

    constants.menuFunctions[constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION] = Operations.gradeStudentAtADiscipline
    constants.menuFunctions[constants.LIST_GRADES_OPTION] = Operations.listAllGrades

    constants.menuFunctions[constants.SEARCH_FOR_STUDENTS_OPTION] = Operations.searchForStudents
    constants.menuFunctions[constants.SEARCH_FOR_DISCIPLINES_OPTION] = Operations.searchForDisciplines

    constants.menuFunctions[constants.ALL_STUDENTS_FAILING_OPTION] = Operations.getTextOfAllStudentsFailing
    constants.menuFunctions[constants.STUDENTS_WITH_THE_BEST_SCHOOL_SITUATION_OPTION] = Operations.getTextOfStudentsWithTheBestSchoolSituation
    constants.menuFunctions[constants.DISCIPLINES_AT_WHICH_THERE_IS_AT_LEAST_ONE_GRADE_OPTION] = Operations.getTextOfDisciplinesAtWhichThereIsAtLeastOneGrade

    constants.menuFunctions[constants.REMOVE_GRADE_STUDENT_AT_A_DISCIPLINE_OPTION] = Operations.removeLatestStudentGradesAtDiscipline


def initializeConstantFunctionHandlers():
    constants.menuFunctionsHandlers[constants.UNDO_OPTION] = Services.UndoHandler
    constants.menuFunctionsHandlers[constants.REDO_OPTION] = Services.RedoHandler

    constants.menuFunctionsHandlers[constants.ADD_STUDENT_OPTION] = Services.addStudentHandler
    constants.menuFunctionsHandlers[constants.ADD_DISCIPLINE_OPTION] = Services.addDisciplineHandler

    constants.menuFunctionsHandlers[constants.REMOVE_STUDENT_OPTION] = Services.removeStudentHandler
    constants.menuFunctionsHandlers[constants.REMOVE_DISCIPLINE_OPTION] = Services.removeDisciplineHandler

    constants.menuFunctionsHandlers[constants.UPDATE_STUDENT_OPTION] = Services.updateStudentHandler
    constants.menuFunctionsHandlers[constants.UPDATE_DISCIPLINE_OPTION] = Services.updateDisciplineHandler

    constants.menuFunctionsHandlers[constants.LIST_STUDENTS_OPTION] = Services.listStudentsHandler
    constants.menuFunctionsHandlers[constants.LIST_DISCIPLINES_OPTION] = Services.listDisciplinesHandler


    constants.menuFunctionsHandlers[constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION] = Services.gradeStudentAtADisciplineHandler
    constants.menuFunctionsHandlers[constants.LIST_GRADES_OPTION] = Services.listAllGradesHandler

    constants.menuFunctionsHandlers[constants.SEARCH_FOR_STUDENTS_OPTION] = Services.searchForStudentsHandler
    constants.menuFunctionsHandlers[constants.SEARCH_FOR_DISCIPLINES_OPTION] = Services.searchForDisciplinesHandler

    constants.menuFunctionsHandlers[constants.ALL_STUDENTS_FAILING_OPTION] = Services.allStudentsFailingHandler
    constants.menuFunctionsHandlers[constants.STUDENTS_WITH_THE_BEST_SCHOOL_SITUATION_OPTION] = Services.studentsWithTheBestSchoolSituationHandler
    constants.menuFunctionsHandlers[constants.DISCIPLINES_AT_WHICH_THERE_IS_AT_LEAST_ONE_GRADE_OPTION] = Services.disciplinesAtWhichThereIsAtLeastOneGradeHandler


def populateRepositories(operationsManager):
    operationsManager.addStudent(1, "Andrei")
    operationsManager.addStudent(2, "Andreea")
    operationsManager.addStudent(3, "Marian")
    operationsManager.addStudent(4, "Constantin")
    operationsManager.addStudent(5, "Laura")
    operationsManager.addStudent(6, "Paul")
    operationsManager.addStudent(7, "Maria")
    operationsManager.addStudent(8, "Alex")
    operationsManager.addStudent(9, "Diana")
    operationsManager.addStudent(10, "Cristina")

    operationsManager.addDiscipline(1, "Math")
    operationsManager.addDiscipline(2, "English")
    operationsManager.addDiscipline(3, "French")
    operationsManager.addDiscipline(4, "German")
    operationsManager.addDiscipline(5, "History")
    operationsManager.addDiscipline(6, "Geography")
    operationsManager.addDiscipline(7, "Physics")
    operationsManager.addDiscipline(8, "Chemistry")
    operationsManager.addDiscipline(9, "Biology")
    operationsManager.addDiscipline(10, "Computer Science")

    operationsManager.gradeStudentAtADiscipline(1, 1, 10)
    operationsManager.gradeStudentAtADiscipline(1, 2, 6)
    operationsManager.gradeStudentAtADiscipline(1, 3, 3)
    operationsManager.gradeStudentAtADiscipline(2, 4, 3)
    operationsManager.gradeStudentAtADiscipline(3, 5, 3)
    operationsManager.gradeStudentAtADiscipline(2, 6, 1)
    operationsManager.gradeStudentAtADiscipline(2, 7, 5)
    operationsManager.gradeStudentAtADiscipline(3, 8, 7)
    operationsManager.gradeStudentAtADiscipline(1, 9, 10)
    operationsManager.gradeStudentAtADiscipline(2, 10, 6)
    operationsManager.gradeStudentAtADiscipline(3, 1, 8)
    operationsManager.gradeStudentAtADiscipline(3, 2, 7)
    operationsManager.gradeStudentAtADiscipline(3, 3, 2)

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


def main():

    initializeConstantMenuFunctions()
    initializeConstantFunctionHandlers()

    typeOfRepository, studentsSaveFileName, disciplinesSaveFileName, facultyDataSaveFileName = getProperties()
    studentsRepository, disciplinesRepository, facultyDataRepository = createRepositories(typeOfRepository, studentsSaveFileName, disciplinesSaveFileName, facultyDataSaveFileName)
    uiManager = UiManager(constants)
    historyHandler = commandHistoryHandler(constants, studentsRepository, disciplinesRepository, facultyDataRepository)
    operationsManager = Operations(studentsRepository, disciplinesRepository, facultyDataRepository, constants)
    serviceFunctions = Services(uiManager, historyHandler, operationsManager, studentsRepository, disciplinesRepository, facultyDataRepository, constants)

    if typeOfRepository == "memory":
        populateRepositories(operationsManager)

    serviceFunctions.startMenu()


main()