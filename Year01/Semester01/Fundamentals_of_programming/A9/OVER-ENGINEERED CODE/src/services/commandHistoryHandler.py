from src.services.undoRedoSystem import UndoRedo

class commandHistoryHandler(UndoRedo):
    def __init__(self, constants, studentsRepository, disciplinesRepository, facultyDataRepository):
        super().__init__()
        self.__constants = constants
        self.__studentsRepository = studentsRepository
        self.__disciplinesRepository = disciplinesRepository
        self.__facultyDataRepository = facultyDataRepository


    def parseCommands(self, operations, commandsToUndoOrRedo):
        inverseCommands = {}
        for commandToParse in commandsToUndoOrRedo:
            if commandToParse == self.__constants.ADD_STUDENT_OPTION:
                inversedCommandArguments = []
                addStudentCommand = self.__constants.menuFunctions[self.__constants.ADD_STUDENT_OPTION]
                for studentsToAdd in commandsToUndoOrRedo[commandToParse]:
                    studentId = studentsToAdd.getStudentId()
                    studentName = studentsToAdd.getStudentName()
                    addStudentCommand(operations, studentId, studentName)
                    inversedCommandArguments.append(studentId)
                inverseCommands[self.__constants.REMOVE_STUDENT_OPTION] = inversedCommandArguments
            elif commandToParse == self.__constants.ADD_DISCIPLINE_OPTION:
                inversedCommandArguments = []
                addDisciplineCommand = self.__constants.menuFunctions[self.__constants.ADD_DISCIPLINE_OPTION]
                for disciplinesToAdd in commandsToUndoOrRedo[commandToParse]:
                    disciplineId = disciplinesToAdd.getDisciplineId()
                    disciplineName = disciplinesToAdd.getDisciplineName()
                    addDisciplineCommand(operations, disciplineId, disciplineName)
                    inversedCommandArguments.append(disciplineId)
                inverseCommands[self.__constants.REMOVE_DISCIPLINE_OPTION] = inversedCommandArguments
            elif commandToParse == self.__constants.REMOVE_STUDENT_OPTION:
                inversedCommandArguments = []
                removeStudentCommand = self.__constants.menuFunctions[self.__constants.REMOVE_STUDENT_OPTION]
                for studentsToRemove in commandsToUndoOrRedo[commandToParse]:
                    removedStudent = self.__studentsRepository.getItem(studentsToRemove)
                    inversedCommandArguments.append(removedStudent)
                    removeStudentCommand(operations, studentsToRemove)
                inverseCommands[self.__constants.ADD_STUDENT_OPTION] = inversedCommandArguments
            elif commandToParse == self.__constants.REMOVE_DISCIPLINE_OPTION:
                inversedCommandArguments = []
                removeDisciplineCommand = self.__constants.menuFunctions[self.__constants.REMOVE_DISCIPLINE_OPTION]
                for disciplinesToRemove in commandsToUndoOrRedo[commandToParse]:
                    removedDiscipline = self.__studentsRepository.getItem(disciplinesToRemove)
                    inversedCommandArguments.append(removedDiscipline)
                    removeDisciplineCommand(operations, disciplinesToRemove)
                inverseCommands[self.__constants.ADD_DISCIPLINE_OPTION] = inversedCommandArguments
            elif commandToParse == self.__constants.UPDATE_STUDENT_OPTION:
                updateStudentCommand = self.__constants.menuFunctions[self.__constants.UPDATE_STUDENT_OPTION]
                for studentInformationToUpdate in commandsToUndoOrRedo[commandToParse]:
                    studentId = studentInformationToUpdate[self.__constants.INDEX_OF_ID_IN_UNDO_REDO_STACK_OPTION]
                    studentName = studentInformationToUpdate[self.__constants.INDEX_OF_NAME_IN_UNDO_REDO_STACK_OPTION]
                    updateStudentCommand(operations, studentId, studentName)
                inverseCommands[self.__constants.UPDATE_STUDENT_OPTION] = commandsToUndoOrRedo[commandToParse]
            elif commandToParse == self.__constants.UPDATE_DISCIPLINE_OPTION:
                updateDisciplineCommand = self.__constants.menuFunctions[self.__constants.UPDATE_DISCIPLINE_OPTION]
                for disciplineInformationToUpdate in commandsToUndoOrRedo[commandToParse]:
                    disciplineId = disciplineInformationToUpdate[self.__constants.INDEX_OF_ID_IN_UNDO_REDO_STACK_OPTION]
                    disciplineName = disciplineInformationToUpdate[self.__constants.INDEX_OF_NAME_IN_UNDO_REDO_STACK_OPTION]
                    updateDisciplineCommand(operations, disciplineId, disciplineName)
                inverseCommands[self.__constants.UPDATE_DISCIPLINE_OPTION] = commandsToUndoOrRedo[commandToParse]
            elif commandToParse == self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION:
                gradeStudentAtADisciplineCommand = self.__constants.menuFunctions[self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION]
                gradeInformationToUndo = commandsToUndoOrRedo[commandToParse]
                inverseCommandArguments = []
                for gradeIdentifier in gradeInformationToUndo:
                    inverseCommandArguments.append(gradeIdentifier)
                    studentId = gradeIdentifier[self.__constants.INDEX_OF_STUDENT_ID_IN_UNDO_REDO_STACK_GRADE_OPTION]
                    disciplineId = gradeIdentifier[self.__constants.INDEX_OF_DISCIPLINE_ID_IN_UNDO_REDO_STACK_GRADE_OPTION]
                    gradesToUndo = gradeInformationToUndo[gradeIdentifier]
                    for grade in gradesToUndo:
                        gradeValue = grade.getGrade()
                        gradeStudentAtADisciplineCommand(operations, studentId, disciplineId, gradeValue)
                inverseCommands[self.__constants.REMOVE_GRADE_STUDENT_AT_A_DISCIPLINE_OPTION] = inverseCommandArguments
            elif commandToParse == self.__constants.REMOVE_GRADE_STUDENT_AT_A_DISCIPLINE_OPTION:
                removeGradeStudentAtADisciplineCommand = self.__constants.menuFunctions[self.__constants.REMOVE_GRADE_STUDENT_AT_A_DISCIPLINE_OPTION]
                gradeInformationToUndo = commandsToUndoOrRedo[commandToParse]
                inverseCommandArguments = {}
                for gradeIdentifier in gradeInformationToUndo:
                    removedGrade = removeGradeStudentAtADisciplineCommand(operations, gradeIdentifier)
                    if gradeIdentifier in inverseCommandArguments:
                        inverseCommandArguments[gradeIdentifier].append(removedGrade)
                    else:
                        inverseCommandArguments[gradeIdentifier] = [removedGrade]
                inverseCommands[self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION] = inverseCommandArguments
            return inverseCommands

    def Undo(self, operations):
        undoCommands = self.getOperationFromUndoStack()
        redoCommands = self.parseCommands(operations, undoCommands)
        self.addRedoOperationToHistory(redoCommands)

    def Redo(self, operations):
        redoCommands = self.getOperationFromRedoStack()
        undoCommands = self.parseCommands(operations, redoCommands)
        self.addUndoOperationToHistory(undoCommands)


