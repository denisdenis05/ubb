from src.ui.textsToDisplay import menuTexts
from src.ui.textsToDisplay import errorTexts

class Services:
    def __init__(self, uiManager, historyHandler, operationsManager, studentsRepository, disciplinesRepository, facultyDataRepository, constants):
        self.__uiManager = uiManager
        self.__historyHandler = historyHandler
        self.__studentsRepository = studentsRepository
        self.__disciplinesRepository = disciplinesRepository
        self.__facultyDataRepository = facultyDataRepository
        self.__operationsManager = operationsManager
        self.__constants = constants


    def checkIfGradeIsValid(self, grade):
        try:
            grade = int(grade)
        except ValueError:
            grade = self.__constants.INVALID_OPTION
        if grade < self.__constants.MINIMUM_GRADE or grade > self.__constants.MAXIMUM_GRADE:
            grade = self.__constants.INVALID_OPTION
        return grade

    def checkIfStudentOrDisciplineInformationIsValid(self, studentId, studentName):
        try:
            studentId = int(studentId)
        except ValueError:
            studentId = self.__constants.INVALID_OPTION
        if any(nameCharacter.isdigit() for nameCharacter in studentName):
            studentName = self.__constants.INVALID_OPTION
        return studentId, studentName


    def addStudentHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertStudentIdText)
        studentId = self.__uiManager.getInput()
        self.__uiManager.displayMessage(menuTexts.insertStudentNameText)
        studentName = self.__uiManager.getInput()
        studentId, studentName = self.checkIfStudentOrDisciplineInformationIsValid(studentId, studentName)

        if studentId == self.__constants.INVALID_OPTION or studentName == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_STUDENT_INFORMATION_MESSAGE)
            return
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        statusOfFunction = selectedOptionFunction(self.__operationsManager, studentId, studentName)
        if statusOfFunction is not None:
            inverseOperations = {self.__constants.REMOVE_STUDENT_OPTION: [studentId]}
            self.__historyHandler.addUndoOperationToHistory(inverseOperations)
            self.__uiManager.displaySuccessMessage(menuTexts.studentAddedSuccessfullyText)
        else:
            self.__uiManager.displayErrorMessage(errorTexts.CANNOT_ADD_STUDENT_MESSAGE)

    def addDisciplineHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertDisciplineIdText)
        disciplineId = self.__uiManager.getInput()
        self.__uiManager.displayMessage(menuTexts.insertDisciplineNameText)
        disciplineName = self.__uiManager.getInput()
        disciplineId, disciplineName = self.checkIfStudentOrDisciplineInformationIsValid(disciplineId, disciplineName)

        if disciplineId == self.__constants.INVALID_OPTION or disciplineName == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_INFORMATION_MESSAGE)
            return
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        statusOfFunction = selectedOptionFunction(self.__operationsManager, disciplineId, disciplineName)
        if statusOfFunction is not None:
            inverseOperations = {self.__constants.REMOVE_DISCIPLINE_OPTION: [disciplineId]}
            self.__historyHandler.addUndoOperationToHistory(inverseOperations)
            self.__uiManager.displaySuccessMessage(menuTexts.disciplineAddedSuccessfullyText)
        else:
            self.__uiManager.displayErrorMessage(errorTexts.CANNOT_ADD_DISCIPLINE_MESSAGE)


    def removeStudentHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertStudentIdText)
        studentId = self.__uiManager.getInput()
        studentId, _ = self.checkIfStudentOrDisciplineInformationIsValid(studentId, self.__constants.NOT_KNOWN_NAME_PLACEHOLDER)

        if studentId == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_STUDENT_INFORMATION_MESSAGE)
            return
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        statusOfFunction = selectedOptionFunction(self.__operationsManager, studentId)
        if statusOfFunction is not None:
            removedStudent = statusOfFunction
            allStudentGrades = self.__operationsManager.getDictionaryOfAllStudentGrades(studentId)
            dictionaryOfIdentifierAndGrade = {}
            for gradeIdentifier in allStudentGrades:
                statusOfRemove = self.__operationsManager.removeStudentsGradesAtADiscipline(gradeIdentifier)
                if statusOfRemove is not None:
                    dictionaryOfIdentifierAndGrade = {gradeIdentifier: allStudentGrades[gradeIdentifier]}
                inverseOperations = {self.__constants.ADD_STUDENT_OPTION: [removedStudent],
                                     self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION: dictionaryOfIdentifierAndGrade}
                self.__historyHandler.addUndoOperationToHistory(inverseOperations)
            self.__uiManager.displaySuccessMessage(menuTexts.studentRemovedSuccessfullyText)
        else:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_STUDENT_MESSAGE)


    def removeDisciplineHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertDisciplineIdText)
        disciplineId = self.__uiManager.getInput()
        disciplineId, _ = self.checkIfStudentOrDisciplineInformationIsValid(disciplineId, self.__constants.NOT_KNOWN_NAME_PLACEHOLDER)

        if disciplineId == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_INFORMATION_MESSAGE)
            return
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        statusOfFunction = selectedOptionFunction(self.__operationsManager, disciplineId)
        removedDiscipline = statusOfFunction
        if statusOfFunction is not None:
            allDisciplineGrades = self.__operationsManager.getDictionaryOfAllDisciplineGrades(disciplineId)
            dictionaryOfIdentifierAndGrade = {}
            for gradeIdentifier in allDisciplineGrades:
                statusOfRemove = self.__operationsManager.removeStudentsGradesAtADiscipline(gradeIdentifier)
                if statusOfRemove is not None:
                    dictionaryOfIdentifierAndGrade = {gradeIdentifier: allDisciplineGrades[gradeIdentifier]}
                inverseOperations = {self.__constants.ADD_DISCIPLINE_OPTION: [removedDiscipline],
                                     self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION: dictionaryOfIdentifierAndGrade}
                self.__historyHandler.addUndoOperationToHistory(inverseOperations)
            self.__uiManager.displaySuccessMessage(menuTexts.disciplineRemovedSuccessfullyText)
        else:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_MESSAGE)

    def allStudentsFailingHandler(self, menuOption: int):
        allDisciplineGrades = {}
        for studentId in self.__studentsRepository.getAllItems():
            allDisciplineGrades[studentId] = self.__operationsManager.getDictionaryOfAllStudentGrades(studentId)
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        textContainingAllStudents = selectedOptionFunction(self.__operationsManager, allDisciplineGrades)
        self.__uiManager.displayMessage(textContainingAllStudents)

    def studentsWithTheBestSchoolSituationHandler(self, menuOption: int):
        allDisciplineGrades = {}
        for studentId in self.__studentsRepository.getAllItems():
            allDisciplineGrades[studentId] = self.__operationsManager.getDictionaryOfAllStudentGrades(studentId)
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        textContainingAllStudents = selectedOptionFunction(self.__operationsManager, allDisciplineGrades)
        self.__uiManager.displayMessage(textContainingAllStudents)

    def disciplinesAtWhichThereIsAtLeastOneGradeHandler(self, menuOption: int):
        allDisciplineGrades = {}
        for disciplineId in self.__disciplinesRepository.getAllItems():
            allDisciplineGrades[disciplineId] = self.__operationsManager.getDictionaryOfAllDisciplineGrades(disciplineId)
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        textContainingAllDisciplines = selectedOptionFunction(self.__operationsManager, allDisciplineGrades)
        self.__uiManager.displayMessage(textContainingAllDisciplines)


    def updateStudentHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertStudentIdText)
        studentId = self.__uiManager.getInput()
        self.__uiManager.displayMessage(menuTexts.insertNewStudentNameText)
        newStudentName = self.__uiManager.getInput()
        studentId, newStudentName = self.checkIfStudentOrDisciplineInformationIsValid(studentId, newStudentName)

        if studentId == self.__constants.INVALID_OPTION or newStudentName == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_STUDENT_INFORMATION_MESSAGE)
            return
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        oldStudentName = self.__studentsRepository.getItem(studentId).getName()
        statusOfFunction = selectedOptionFunction(self.__operationsManager, studentId, newStudentName)
        if statusOfFunction is not None:

            self.__uiManager.displaySuccessMessage(menuTexts.studentUpdatedSuccessfullyText)
            inverseOperations = {self.__constants.UPDATE_STUDENT_OPTION: [{studentId: oldStudentName}]}
            self.__historyHandler.addUndoOperationToHistory(inverseOperations)
        else:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_STUDENT_MESSAGE)

    def updateDisciplineHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertDisciplineIdText)
        disciplineId = self.__uiManager.getInput()
        self.__uiManager.displayMessage(menuTexts.insertNewDisciplineNameText)
        newDisciplineName = self.__uiManager.getInput()
        disciplineId, newDisciplineName = self.checkIfStudentOrDisciplineInformationIsValid(disciplineId, newDisciplineName)

        if disciplineId == self.__constants.INVALID_OPTION or newDisciplineName == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_INFORMATION_MESSAGE)
            return
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        oldDisciplineName = self.__disciplinesRepository.getItem(disciplineId).getName()
        statusOfFunction = selectedOptionFunction(self.__operationsManager, disciplineId, newDisciplineName)
        if statusOfFunction is not None:
            self.__uiManager.displaySuccessMessage(menuTexts.disciplineUpdatedSuccessfullyText)
            inverseOperations = {self.__constants.UPDATE_DISCIPLINE_OPTION: [{disciplineId: oldDisciplineName}]}
            self.__historyHandler.addUndoOperationToHistory(inverseOperations)
        else:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_MESSAGE)


    def listStudentsHandler(self, menuOption: int):
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        textContainingAllStudents = selectedOptionFunction(self.__operationsManager)
        self.__uiManager.displayMessage(textContainingAllStudents)

    def listDisciplinesHandler(self, menuOption: int):
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        textContainingAllDisciplines = selectedOptionFunction(self.__operationsManager)
        self.__uiManager.displaySuccessMessage(textContainingAllDisciplines)

    def gradeStudentAtADisciplineHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertStudentIdText)
        studentId = self.__uiManager.getInput()
        self.__uiManager.displayMessage(menuTexts.insertDisciplineIdText)
        disciplineId = self.__uiManager.getInput()
        self.__uiManager.displayMessage(menuTexts.insertGradeText)
        grade = self.__uiManager.getInput()
        studentId, _ = self.checkIfStudentOrDisciplineInformationIsValid(studentId, self.__constants.NOT_KNOWN_NAME_PLACEHOLDER)
        disciplineId, _ = self.checkIfStudentOrDisciplineInformationIsValid(disciplineId, self.__constants.NOT_KNOWN_NAME_PLACEHOLDER)
        grade = self.checkIfGradeIsValid(grade)
        if disciplineId == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_MESSAGE)
            return
        if studentId == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_STUDENT_MESSAGE)
            return
        if grade == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_GRADE_MESSAGE)
            return

        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        statusOfFunction = selectedOptionFunction(self.__operationsManager, studentId, disciplineId, grade)
        if statusOfFunction is not None:
            self.__uiManager.displaySuccessMessage(menuTexts.gradeAddedSuccessfullyText)
            gradeIdentifier = (studentId, disciplineId)
            dictionaryOfIdentifierAndGrade = {gradeIdentifier: grade}
            inverseOperations = {self.__constants.REMOVE_GRADE_STUDENT_AT_A_DISCIPLINE_OPTION: dictionaryOfIdentifierAndGrade}
            self.__historyHandler.addUndoOperationToHistory(inverseOperations)
        else:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_GRADE_OR_OTHER_INFORMATION_MESSAGE)

    def searchForStudentsHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertStudentNameText)
        studentName = self.__uiManager.getInput()
        _, studentName = self.checkIfStudentOrDisciplineInformationIsValid(self.__constants.NOT_KNOWN_ID_PLACEHOLDER, studentName)
        if studentName == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_STUDENT_INFORMATION_MESSAGE)
            return
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        textContainingAllStudents = selectedOptionFunction(self.__operationsManager, studentName)
        self.__uiManager.displayMessage(textContainingAllStudents)

    def searchForDisciplinesHandler(self, menuOption: int):
        self.__uiManager.displayMessage(menuTexts.insertDisciplineNameText)
        disciplineName = self.__uiManager.getInput()
        _, disciplineName = self.checkIfStudentOrDisciplineInformationIsValid(self.__constants.NOT_KNOWN_ID_PLACEHOLDER, disciplineName)
        if disciplineName == self.__constants.INVALID_OPTION:
            self.__uiManager.displayErrorMessage(errorTexts.INVALID_DISCIPLINE_INFORMATION_MESSAGE)
            return
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        textContainingAllDisciplines = selectedOptionFunction(self.__operationsManager, disciplineName)
        self.__uiManager.displayMessage(textContainingAllDisciplines)

    def listAllGradesHandler(self, menuOption: int):
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        textContainingAllGrades = selectedOptionFunction(self.__operationsManager)
        self.__uiManager.displayMessage(textContainingAllGrades)

    def UndoHandler(self, menuOption: int):
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        try:
            statusOfFunction = self.__historyHandler.Undo(self.__operationsManager)
            self.__uiManager.displaySuccessMessage(menuTexts.undoSuccessfullyText)
        except:
            self.__uiManager.displayErrorMessage(errorTexts.CANNOT_UNDO_MESSAGE)

    def RedoHandler(self, menuOption: int):
        selectedOptionFunction = self.__constants.menuFunctions[menuOption]
        try:
            statusOfFunction = self.__historyHandler.Redo(self.__operationsManager)
            self.__uiManager.displaySuccessMessage(menuTexts.redoSuccessfullyText)
        except:
            self.__uiManager.displayErrorMessage(errorTexts.CANNOT_REDO_MESSAGE)

    def startMenu(self):
        stillInTheMenu = True
        while stillInTheMenu:
            startingPage = self.__constants.GENERAL_MENU
            selectedMenuOption = self.__uiManager.getUserMenuChoice(startingPage)
            selectedOptionFunctionHandler = self.__constants.menuFunctionsHandlers[selectedMenuOption]
            selectedOptionFunctionHandler(self, selectedMenuOption)