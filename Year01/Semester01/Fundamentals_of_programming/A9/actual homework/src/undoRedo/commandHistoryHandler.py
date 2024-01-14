from src.undoRedo.undoRedoSystem import UndoRedo

class commandHistoryHandler(UndoRedo):
    def __init__(self, studentsRepository, disciplinesRepository, facultyDataRepository, serviceFunctions, constants):
        super().__init__()
        self.__constants = constants
        self.__services = serviceFunctions
        self.__studentsRepository = studentsRepository
        self.__disciplinesRepository = disciplinesRepository
        self.__facultyDataRepository = facultyDataRepository


    def parseCommands(self, commandsToUndoOrRedo):
        inverseCommands = {}
        for commandToParse in commandsToUndoOrRedo:
            if commandToParse == self.__constants.ADD_STUDENT_OPTION:
                inverseCommandArguments = []
                for studentsToAdd in commandsToUndoOrRedo[commandToParse]:
                    studentId = studentsToAdd.getStudentId()
                    studentName = studentsToAdd.getStudentName()
                    self.__services.addStudent(studentId, studentName)
                    inverseCommandArguments.append(studentId)
                inverseCommands[self.__constants.REMOVE_STUDENT_OPTION] = inverseCommandArguments
            elif commandToParse == self.__constants.ADD_DISCIPLINE_OPTION:
                inverseCommandArguments = []
                for disciplinesToAdd in commandsToUndoOrRedo[commandToParse]:
                    disciplineId = disciplinesToAdd.getDisciplineId()
                    disciplineName = disciplinesToAdd.getDisciplineName()
                    self.__services.addDiscipline(disciplineId, disciplineName)
                    inverseCommandArguments.append(disciplineId)
                inverseCommands[self.__constants.REMOVE_DISCIPLINE_OPTION] = inverseCommandArguments
            elif commandToParse == self.__constants.REMOVE_STUDENT_OPTION:
                inverseCommandArguments = []
                for studentsToRemove in commandsToUndoOrRedo[commandToParse]:
                    removedStudent = self.__studentsRepository.getItem(studentsToRemove)
                    inverseCommandArguments.append(removedStudent)
                    self.__services.removeStudent(studentsToRemove)
                inverseCommands[self.__constants.ADD_STUDENT_OPTION] = inverseCommandArguments
            elif commandToParse == self.__constants.REMOVE_DISCIPLINE_OPTION:
                inverseCommandArguments = []
                for disciplinesToRemove in commandsToUndoOrRedo[commandToParse]:
                    removedDiscipline = self.__disciplinesRepository.getItem(disciplinesToRemove)
                    inverseCommandArguments.append(removedDiscipline)
                    self.__services.removeDiscipline(disciplinesToRemove)
                inverseCommands[self.__constants.ADD_DISCIPLINE_OPTION] = inverseCommandArguments
            elif commandToParse == self.__constants.UPDATE_STUDENT_OPTION:
                for studentInformationToUpdate in commandsToUndoOrRedo[commandToParse]:
                    studentId, studentName = studentInformationToUpdate
                    oldStudentData = commandsToUndoOrRedo[commandToParse][studentInformationToUpdate]
                    oldStudentName = oldStudentData.getStudentName()
                    student = self.__services.updateStudent(studentId, oldStudentName)
                inverseCommands[self.__constants.UPDATE_STUDENT_OPTION] = {(studentId, studentName): student}
            elif commandToParse == self.__constants.UPDATE_DISCIPLINE_OPTION:
                for disciplineInformationToUpdate in commandsToUndoOrRedo[commandToParse]:
                    disciplineId, disciplineName = disciplineInformationToUpdate
                    oldDisciplineData = commandsToUndoOrRedo[commandToParse][disciplineInformationToUpdate]
                    oldDisciplineName = oldDisciplineData.getDisciplineName()
                    discipline = self.__services.updateDiscipline(disciplineId, oldDisciplineName)
                inverseCommands[self.__constants.UPDATE_DISCIPLINE_OPTION] = {(disciplineId, disciplineName): discipline}
            elif commandToParse == self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION:
                gradeInformationToUndo = commandsToUndoOrRedo[commandToParse]
                inverseCommandArguments = []
                for gradeIdentifier in gradeInformationToUndo:
                    inverseCommandArguments.append(gradeIdentifier)
                    studentId = gradeIdentifier[self.__constants.INDEX_OF_STUDENT_ID_IN_UNDO_REDO_STACK_GRADE_OPTION]
                    disciplineId = gradeIdentifier[self.__constants.INDEX_OF_DISCIPLINE_ID_IN_UNDO_REDO_STACK_GRADE_OPTION]
                    gradesToUndo = gradeInformationToUndo[gradeIdentifier]
                    for grade in gradesToUndo:
                        gradeValue = grade.getGrade()
                        self.__services.gradeStudentAtADiscipline(studentId, disciplineId, gradeValue)
                inverseCommands[self.__constants.REMOVE_GRADE_STUDENT_AT_A_DISCIPLINE_OPTION] = inverseCommandArguments
            elif commandToParse == self.__constants.REMOVE_GRADE_STUDENT_AT_A_DISCIPLINE_OPTION:
                gradeInformationToUndo = commandsToUndoOrRedo[commandToParse]
                inverseCommandArguments = {}
                for gradeIdentifier in gradeInformationToUndo:
                    removedGrade = self.__services.removeLatestStudentGradesAtDiscipline(gradeIdentifier)
                    if gradeIdentifier in inverseCommandArguments:
                        inverseCommandArguments[gradeIdentifier].append(removedGrade)
                    else:
                        inverseCommandArguments[gradeIdentifier] = [removedGrade]
                inverseCommands[self.__constants.GRADE_STUDENT_AT_A_DISCIPLINE_OPTION] = inverseCommandArguments
        return inverseCommands

    def Undo(self):
        undoCommands = self.getOperationFromUndoStack()
        redoCommands = self.parseCommands(undoCommands)
        self.addRedoOperationToHistory(redoCommands)

    def Redo(self):
        redoCommands = self.getOperationFromRedoStack()
        undoCommands = self.parseCommands(redoCommands)
        self.addSimpleUndoOperationToHistory(undoCommands)


