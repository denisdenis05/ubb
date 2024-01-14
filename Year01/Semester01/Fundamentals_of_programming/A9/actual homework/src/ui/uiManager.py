from src.ui.textsToDisplay import errorTexts
from src.ui.textsToDisplay import menuTexts
from colorama import Fore, init


class UiManager:
    def __init__(self, serviceFunctions, undoRedoService, constants):
        super().__init__()
        self.__constants = constants
        self.__undoRedoService = undoRedoService
        self.__services = serviceFunctions
        init(autoreset=True)  # colorama

    # ---------------------------------------
    # INPUT/OUTPUT DOWN HERE
    # ---------------------------------------

    @staticmethod
    def getInput():
        userInput = input("> ")
        return userInput

    def getUserOptionInput(self):
        userInput = self.getInput()
        try:
            userInput = int(userInput)
        except ValueError:
            userInput = self.__constants.INVALID_OPTION
        return userInput

    @staticmethod
    def displayMessage(message):
        print(message)

    @staticmethod
    def displayErrorMessage(errorMessage):
        print(Fore.RED + errorMessage)

    @staticmethod
    def displaySuccessMessage(successMessage):
        print(Fore.GREEN + successMessage)

    # ---------------------------------------
    # FUNCTIONS HANDLERS DOWN HERE
    # ---------------------------------------

    def addStudentHandler(self):
        self.displayMessage(menuTexts.insertStudentIdText)
        studentId = self.getInput()
        self.displayMessage(menuTexts.insertStudentNameText)
        studentName = self.getInput()
        studentId, studentName = self.__services.checkIfStudentOrDisciplineInformationIsValid(studentId, studentName)

        if studentId == self.__constants.INVALID_OPTION or studentName == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_STUDENT_INFORMATION_MESSAGE)
            return

        statusOfFunction = self.__services.addStudent(studentId, studentName)
        if statusOfFunction is not None:
            self.displaySuccessMessage(menuTexts.studentAddedSuccessfullyText)
            undoCommands = {self.__constants.REMOVE_STUDENT_OPTION: [studentId]}
            self.__undoRedoService.addUndoOperationToHistory(undoCommands)

        else:
            self.displayErrorMessage(errorTexts.CANNOT_ADD_STUDENT_MESSAGE)

    def addDisciplineHandler(self):
        self.displayMessage(menuTexts.insertDisciplineIdText)
        disciplineId = self.getInput()
        self.displayMessage(menuTexts.insertDisciplineNameText)
        disciplineName = self.getInput()
        disciplineId, disciplineName = self.__services.checkIfStudentOrDisciplineInformationIsValid(disciplineId, disciplineName)

        if disciplineId == self.__constants.INVALID_OPTION or disciplineName == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_INFORMATION_MESSAGE)
            return

        statusOfFunction = self.__services.addDiscipline(disciplineId, disciplineName)
        if statusOfFunction is not None:
            self.displaySuccessMessage(menuTexts.disciplineAddedSuccessfullyText)
            undoCommands = {self.__constants.REMOVE_DISCIPLINE_OPTION: [disciplineId]}
            self.__undoRedoService.addUndoOperationToHistory(undoCommands)
        else:
            self.displayErrorMessage(errorTexts.CANNOT_ADD_DISCIPLINE_MESSAGE)

    def removeStudentHandler(self):
        self.displayMessage(menuTexts.insertStudentIdText)
        studentId = self.getInput()
        studentId, _ = self.__services.checkIfStudentOrDisciplineInformationIsValid(studentId, self.__constants.NOT_KNOWN_NAME_PLACEHOLDER)

        if studentId == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_STUDENT_INFORMATION_MESSAGE)
            return

        statusOfFunction = self.__services.removeStudent(studentId)
        if statusOfFunction is not None:
            removedGrades = self.__services.removeAllStudentGrades(studentId)
            self.displaySuccessMessage(menuTexts.studentRemovedSuccessfullyText)
            removedStudent = statusOfFunction
            undoCommands = {self.__constants.ADD_STUDENT_OPTION: [removedStudent], self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION: removedGrades}
            self.__undoRedoService.addUndoOperationToHistory(undoCommands)
        else:
            self.displayErrorMessage(errorTexts.INVALID_STUDENT_MESSAGE)

    def removeDisciplineHandler(self):
        self.displayMessage(menuTexts.insertDisciplineIdText)
        disciplineId = self.getInput()
        disciplineId, _ = self.__services.checkIfStudentOrDisciplineInformationIsValid(disciplineId, self.__constants.NOT_KNOWN_NAME_PLACEHOLDER)

        if disciplineId == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_INFORMATION_MESSAGE)
            return

        statusOfFunction = self.__services.removeDiscipline(disciplineId)
        if statusOfFunction is not None:
            removedGrades = self.__services.removeAllDisciplineGrades(disciplineId)
            self.displaySuccessMessage(menuTexts.disciplineRemovedSuccessfullyText)
            removedDiscipline = statusOfFunction
            undoCommands = {self.__constants.ADD_DISCIPLINE_OPTION: [removedDiscipline], self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION: removedGrades}
            self.__undoRedoService.addUndoOperationToHistory(undoCommands)
        else:
            self.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_MESSAGE)


    def updateStudentHandler(self):
        self.displayMessage(menuTexts.insertStudentIdText)
        studentId = self.getInput()
        self.displayMessage(menuTexts.insertNewStudentNameText)
        newStudentName = self.getInput()
        studentId, newStudentName = self.__services.checkIfStudentOrDisciplineInformationIsValid(studentId, newStudentName)

        if studentId == self.__constants.INVALID_OPTION or newStudentName == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_STUDENT_INFORMATION_MESSAGE)
            return

        statusOfFunction = self.__services.updateStudent(studentId, newStudentName)
        if statusOfFunction is not None:
            self.displaySuccessMessage(menuTexts.studentUpdatedSuccessfullyText)
            oldStudentData = statusOfFunction
            undoCommands = {self.__constants.UPDATE_STUDENT_OPTION: {(studentId, newStudentName): oldStudentData}}
            self.__undoRedoService.addUndoOperationToHistory(undoCommands)
        else:
            self.displayErrorMessage(errorTexts.INVALID_STUDENT_MESSAGE)

    def updateDisciplineHandler(self):
        self.displayMessage(menuTexts.insertDisciplineIdText)
        disciplineId = self.getInput()
        self.displayMessage(menuTexts.insertNewDisciplineNameText)
        newDisciplineName = self.getInput()
        disciplineId, newDisciplineName = self.__services.checkIfStudentOrDisciplineInformationIsValid(disciplineId, newDisciplineName)

        if disciplineId == self.__constants.INVALID_OPTION or newDisciplineName == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_INFORMATION_MESSAGE)
            return

        statusOfFunction = self.__services.updateDiscipline(disciplineId, newDisciplineName)
        if statusOfFunction is not None:
            self.displaySuccessMessage(menuTexts.disciplineUpdatedSuccessfullyText)
            oldDisciplineData = statusOfFunction
            undoCommands = {self.__constants.UPDATE_DISCIPLINE_OPTION: {(disciplineId, newDisciplineName): oldDisciplineData}}
            self.__undoRedoService.addUndoOperationToHistory(undoCommands)
        else:
            self.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_MESSAGE)

    def listStudentsHandler(self):
        textContainingAllStudents = self.__services.getTextOfAllStudents()
        self.displayMessage(textContainingAllStudents)

    def listDisciplinesHandler(self):
        textContainingAllDisciplines = self.__services.getTextOfAllDisciplines()
        self.displayMessage(textContainingAllDisciplines)

    def gradeStudentAtADisciplineHandler(self):
        self.displayMessage(menuTexts.insertStudentIdText)
        studentId = self.getInput()
        self.displayMessage(menuTexts.insertDisciplineIdText)
        disciplineId = self.getInput()
        self.displayMessage(menuTexts.insertGradeText)
        grade = self.getInput()
        studentId, _ = self.__services.checkIfStudentOrDisciplineInformationIsValid(studentId, self.__constants.NOT_KNOWN_NAME_PLACEHOLDER)
        disciplineId, _ = self.__services.checkIfStudentOrDisciplineInformationIsValid(disciplineId, self.__constants.NOT_KNOWN_NAME_PLACEHOLDER)
        grade = self.__services.checkIfGradeIsValid(grade)
        if disciplineId == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_MESSAGE)
            return
        if studentId == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_STUDENT_MESSAGE)
            return
        if grade == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_GRADE_MESSAGE)
            return

        statusOfFunction = self.__services.gradeStudentAtADiscipline(studentId, disciplineId, grade)
        if statusOfFunction is not None:
            self.displaySuccessMessage(menuTexts.gradeAddedSuccessfullyText)
            addedGrade = statusOfFunction
            undoCommands = {self.__constants.REMOVE_GRADE_STUDENT_AT_A_DISCIPLINE_OPTION: {(studentId, disciplineId): addedGrade}}
            self.__undoRedoService.addUndoOperationToHistory(undoCommands)
        else:
            self.displayErrorMessage(errorTexts.INVALID_GRADE_OR_OTHER_INFORMATION_MESSAGE)

    def listAllGradesHandler(self):
        textContainingAllGrades = self.__services.listAllGrades()
        self.displayMessage(textContainingAllGrades)

    def searchForStudentsHandler(self):
        self.displayMessage(menuTexts.insertStudentNameText)
        studentName = self.getInput()
        _, studentName = self.__services.checkIfStudentOrDisciplineInformationIsValid(self.__constants.NOT_KNOWN_ID_PLACEHOLDER, studentName)
        if studentName == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_STUDENT_INFORMATION_MESSAGE)
            return

        textContainingAllStudents = self.__services.searchForStudents(studentName)
        self.displayMessage(textContainingAllStudents)

    def searchForDisciplinesHandler(self):
        self.displayMessage(menuTexts.insertDisciplineNameText)
        disciplineName = self.getInput()
        _, disciplineName = self.__services.checkIfStudentOrDisciplineInformationIsValid(self.__constants.NOT_KNOWN_ID_PLACEHOLDER, disciplineName)
        if disciplineName == self.__constants.INVALID_OPTION:
            self.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_INFORMATION_MESSAGE)
            return

        textContainingAllDisciplines = self.__services.searchForDisciplines(disciplineName)
        self.displayMessage(textContainingAllDisciplines)

    def allStudentsFailingHandler(self):
        textContainingAllStudents = self.__services.getTextOfAllStudentsFailing()
        self.displayMessage(textContainingAllStudents)

    def studentsWithTheBestSchoolSituationHandler(self):
        textContainingAllStudents = self.__services.getTextOfStudentsWithTheBestSchoolSituation()
        self.displayMessage(textContainingAllStudents)

    def disciplinesAtWhichThereIsAtLeastOneGradeHandler(self):
        textContainingAllDisciplines = self.__services.getTextOfDisciplinesAtWhichThereIsAtLeastOneGrade()
        self.displayMessage(textContainingAllDisciplines)

    def undoHandler(self):
        try:
            self.__undoRedoService.Undo()
            self.displaySuccessMessage(menuTexts.undoSuccessfullyText)
        except:
            self.displayErrorMessage(errorTexts.CANNOT_UNDO_MESSAGE)

    def redoHandler(self):
        try:
            self.__undoRedoService.Redo()
            self.displaySuccessMessage(menuTexts.redoSuccessfullyText)
        except:
            self.displayErrorMessage(errorTexts.CANNOT_REDO_MESSAGE)

    # ---------------------------------------
    # MENU LOGIC DOWN HERE
    # ---------------------------------------


    def displayMenu(self, menuPage):
        currentPageMenuText = menuTexts.MENU_TEXTS_FOR_PAGE[menuPage]
        self.displayMessage(currentPageMenuText)

    def getUserMenuChoice(self, currentMenuPage):
        self.displayMenu(currentMenuPage)
        if self.__services.checkIfChosenOptionIsASubMenu(currentMenuPage):
            selectedMenuPage = self.getUserOptionInput()
            if self.__services.checkIfMenuOptionExists(currentMenuPage, selectedMenuPage) is False:
                self.displayErrorMessage(errorTexts.INVALID_MENU_OPTION_MESSAGE)
                generalMenuIndex = self.__constants.GENERAL_MENU
                functionToCallNumber = self.getUserMenuChoice(generalMenuIndex)
            else:
                actualMenuChoice = self.__services.getActualMenuPageIndex(currentMenuPage, selectedMenuPage)
                if self.__services.checkIfChosenOptionIsASubMenu(actualMenuChoice):
                    functionToCallNumber = self.getUserMenuChoice(actualMenuChoice)
                else:
                    functionToCallNumber = actualMenuChoice
        else:
            functionToCallNumber = currentMenuPage
        return functionToCallNumber

    def startMenu(self):
        stillInTheMenu = True
        while stillInTheMenu:
            startingPage = self.__constants.GENERAL_MENU
            selectedMenuOption = self.getUserMenuChoice(startingPage)
            self.handleCallFunction(selectedMenuOption)

    def handleCallFunction(self, selectedMenuOption):
        if selectedMenuOption == self.__constants.ADD_STUDENT_OPTION:
            self.addStudentHandler()
        elif selectedMenuOption == self.__constants.ADD_DISCIPLINE_OPTION:
            self.addDisciplineHandler()
        elif selectedMenuOption == self.__constants.REMOVE_STUDENT_OPTION:
            self.removeStudentHandler()
        elif selectedMenuOption == self.__constants.REMOVE_DISCIPLINE_OPTION:
            self.removeDisciplineHandler()
        elif selectedMenuOption == self.__constants.UPDATE_STUDENT_OPTION:
            self.updateStudentHandler()
        elif selectedMenuOption == self.__constants.UPDATE_DISCIPLINE_OPTION:
            self.updateDisciplineHandler()
        elif selectedMenuOption == self.__constants.LIST_STUDENTS_OPTION:
            self.listStudentsHandler()
        elif selectedMenuOption == self.__constants.LIST_DISCIPLINES_OPTION:
            self.listDisciplinesHandler()

        elif selectedMenuOption == self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION:
            self.gradeStudentAtADisciplineHandler()
        elif selectedMenuOption == self.__constants.LIST_GRADES_OPTION:
            self.listAllGradesHandler()
        elif selectedMenuOption == self.__constants.SEARCH_FOR_STUDENTS_OPTION:
            self.searchForStudentsHandler()
        elif selectedMenuOption == self.__constants.SEARCH_FOR_DISCIPLINES_OPTION:
            self.searchForDisciplinesHandler()

        elif selectedMenuOption == self.__constants.ALL_STUDENTS_FAILING_OPTION:
            self.allStudentsFailingHandler()
        elif selectedMenuOption == self.__constants.STUDENTS_WITH_THE_BEST_SCHOOL_SITUATION_OPTION:
            self.studentsWithTheBestSchoolSituationHandler()
        elif selectedMenuOption == self.__constants.DISCIPLINES_AT_WHICH_THERE_IS_AT_LEAST_ONE_GRADE_OPTION:
            self.disciplinesAtWhichThereIsAtLeastOneGradeHandler()

        elif selectedMenuOption == self.__constants.UNDO_OPTION:
            self.undoHandler()
        elif selectedMenuOption == self.__constants.REDO_OPTION:
            self.redoHandler()
