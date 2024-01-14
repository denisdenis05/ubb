from src.domain.domain import Student
from src.domain.domain import Discipline
from src.domain.domain import FacultyGrades
from src.ui.textsToDisplay import menuTexts

class Operations:
    def __init__(self, studentsRepository, disciplinesRepository, facultyDataRepository, constants):
        self.__constants = constants
        self.__studentsRepository = studentsRepository
        self.__disciplinesRepository = disciplinesRepository
        self.__facultyDataRepository = facultyDataRepository

    def addStudent(self, studentId: int, studentName: str):
        try:
            studentToAdd = Student(studentId, studentName)
            self.__studentsRepository.addToRepository(studentToAdd, studentId)
            return studentToAdd
        except:
            return None

    def addDiscipline(self, disciplineId: int, disciplineName: str):
        try:
            disciplineToAdd = Discipline(disciplineId, disciplineName)
            self.__disciplinesRepository.addToRepository(disciplineToAdd, disciplineId)
            return disciplineToAdd
        except:
            return None

    def removeStudent(self, studentId: int):
        try:
            studentRemoved = self.__studentsRepository.getItem(studentId)
            self.__studentsRepository.removeFromRepository(studentId)
            return studentRemoved
        except:
            return None

    def removeDiscipline(self, disciplineId: int):
        try:
            disciplineRemoved = self.__disciplinesRepository.getItem(disciplineId)
            self.__disciplinesRepository.removeFromRepository(disciplineId)
            return disciplineRemoved
        except:
            return None

    def updateStudent(self, studentId: int, newStudentName: str):
        if self.__studentsRepository.getItem(studentId) is not None:
            try:
                studentToUpdate = self.__facultyDataRepository.getItem(studentId)
                newStudent = Student(studentId, newStudentName)
                self.__studentsRepository.updateItem(studentId, newStudent)
                return newStudent
            except:
                return None
        return None

    def updateDiscipline(self, disciplineId: int, newDisciplineName: str):
        if self.__disciplinesRepository.getItem(disciplineId) is not None:
            try:
                disciplineToUpdate = self.__facultyDataRepository.getItem(disciplineId)
                newDiscipline = Discipline(disciplineId, newDisciplineName)
                return self.__disciplinesRepository.updateItem(disciplineId, newDiscipline)
            except:
                return None
        return None

    def gradeStudentAtADiscipline(self, studentId: int, disciplineId: int, gradeScore: int):
        gradeIdentifier = (studentId, disciplineId)
        gradeToAddToFaculty = FacultyGrades(studentId, disciplineId, gradeScore)
        self.__facultyDataRepository.addAsMultipleItemsToRepository(gradeToAddToFaculty, gradeIdentifier)
        return gradeIdentifier

    def removeLatestStudentGradesAtDiscipline(self, gradeIdentifier):
        grades = self.__facultyDataRepository.removeFromRepository(gradeIdentifier)
        removedGrade = grades.pop(self.__constants.LATEST_ADDED_ELEMENT_POSITION_IN_GRADE_LIST)
        for grade in grades:
            self.__facultyDataRepository.addAsMultipleItemsToRepository(grade, gradeIdentifier)
        return removedGrade

    def removeStudentsGradesAtADiscipline(self, gradeIdentifier):
        return self.__facultyDataRepository.removeFromRepository(gradeIdentifier)


    def getDictionaryOfAllStudentGrades(self, studentId: int):
        dictionaryOfGrades = {}
        for disciplineIdentifier in self.__disciplinesRepository.getAllItems():
            discipline = self.__disciplinesRepository.getItem(disciplineIdentifier)
            gradeIdentifier = (studentId, discipline.getDisciplineId())
            dictionaryOfGrades[gradeIdentifier] = self.__facultyDataRepository.getItem(gradeIdentifier)
        return dictionaryOfGrades

    def getDictionaryOfAllDisciplineGrades(self, disciplineId: int):
        dictionaryOfGrades = {}
        for studentIdentifier in self.__studentsRepository.getAllItems():
            student = self.__studentsRepository.getItem(studentIdentifier)
            gradeIdentifier = (student.getStudentId(), disciplineId)
            dictionaryOfGrades[gradeIdentifier] = self.__facultyDataRepository.getItem(gradeIdentifier)
        return dictionaryOfGrades

    def getAllStudentGrades(self, studentId):
        textOfAllGrades = ""
        allDisciplines = self.__disciplinesRepository.getAllItems()
        allStudents = self.__studentsRepository.getAllItems()
        if len(allDisciplines) == self.__constants.EMPTY_LIST_LENGTH or len(allStudents) == self.__constants.EMPTY_LIST_LENGTH:
            textOfAllGrades = menuTexts.noGradesInFacultyText
            return textOfAllGrades
        for student in allStudents:
            studentName = student.getStudentName()
            studentId = student.getStudentId()
            textOfAllGrades += f"\n[ Student {studentName} nr {studentId} ]\n"
            for discipline in allDisciplines:
                disciplineId = discipline.getDisciplineId()
                disciplineName = discipline.getDisciplineName()
                disciplineGradesIdentifier = (studentId, disciplineId)
                allStudentGradesAtDiscipline = self.__facultyDataRepository.getItem(disciplineGradesIdentifier)
                if allStudentGradesAtDiscipline is None:
                    textOfAllGrades += f"Student has no grades at discipline {disciplineName}\n"
                else:
                    gradesText = ""
                    for gradeIdentifier in allStudentGradesAtDiscipline:
                        grade = allStudentGradesAtDiscipline[gradeIdentifier]
                        gradesText += f"{grade} "
                    textOfAllGrades += f"Student's grades at discipline {disciplineName}:  {gradesText}\n"
        return textOfAllGrades


    def searchForStudents(self, studentNameToSearchFor: str):
        listOfAllStudents = self.__studentsRepository.getAllItems()
        listOfStudentsFound = []
        for studentIdentifier in listOfAllStudents:
            student = listOfAllStudents[studentIdentifier]
            studentNameToCheck = student.getStudentName()
            if studentNameToSearchFor.lower() in studentNameToCheck.lower():
                listOfStudentsFound.append(student)
        textOfMatchingStudents = menuTexts.matchingStudentsHeaderText
        for matchingStudent in listOfStudentsFound:
            matchingStudentId = matchingStudent.getStudentId()
            matchingStudentName = matchingStudent.getStudentName()
            textOfMatchingStudents += f"\nStudent nr {matchingStudentId}: {matchingStudentName}"
        if textOfMatchingStudents == menuTexts.matchingStudentsHeaderText:
            textOfMatchingStudents = menuTexts.noStudentsFoundText
        return textOfMatchingStudents

    def searchForDisciplines(self, disciplineNameToSearchFor: str):
        listOfAllDisciplines = self.__disciplinesRepository.getAllItems()
        listOfDisciplinesFound = []
        for disciplineIdentifier in listOfAllDisciplines:
            discipline = listOfAllDisciplines[disciplineIdentifier]
            disciplineNameToCheck = discipline.getDisciplineName()
            if disciplineNameToSearchFor.lower() in disciplineNameToCheck.lower():
                listOfDisciplinesFound.append(discipline)
        textOfMatchingDisciplines = menuTexts.matchingDisciplinesHeaderText
        for matchingDiscipline in listOfDisciplinesFound:
            matchingDisciplineId = matchingDiscipline.getDisciplineId()
            matchingDisciplineName = matchingDiscipline.getDisciplineName()
            textOfMatchingDisciplines += f"\nDiscipline nr {matchingDisciplineId}: {matchingDisciplineName}"
        if textOfMatchingDisciplines == "Matching disciplines:":
            textOfMatchingDisciplines = menuTexts.noDisciplinesFoundText
        return textOfMatchingDisciplines

    def listAllGrades(self):
        textOfAllGrades = ""
        allDisciplines = self.__disciplinesRepository.getAllItems()
        allStudents = self.__studentsRepository.getAllItems()
        if len(allDisciplines) == self.__constants.EMPTY_LIST_LENGTH or len(allStudents) == self.__constants.EMPTY_LIST_LENGTH:
            textOfAllGrades = menuTexts.noGradesInFacultyText
            return textOfAllGrades
        for studentIdentifier in allStudents:
            studentToCheckGrades = allStudents[studentIdentifier]
            studentName = studentToCheckGrades.getStudentName()
            studentId = studentToCheckGrades.getStudentId()
            textOfAllGrades += f"\n[ Student {studentName} nr {studentId} ]\n"
            for discipline in allDisciplines:
                discipline = allDisciplines[discipline]
                disciplineId = discipline.getDisciplineId()
                disciplineName = discipline.getDisciplineName()
                studentAndDisciplineIdentifier = (studentId, disciplineId)
                grades = self.__facultyDataRepository.getItem(studentAndDisciplineIdentifier)
                if grades is None or grades == []:
                    textOfAllGrades += f"Student has no grades at discipline {disciplineName}\n"
                else:
                    gradesText = ""
                    for gradeObject in grades:
                        grade = gradeObject.getGrade()
                        gradesText += f"{grade} "
                    textOfAllGrades += f"Student's grades at discipline {disciplineName}:  {gradesText}\n"
        return textOfAllGrades


    def getTextOfAllStudents(self):
        textContainingAllStudents = ""
        for studentIdentifier in self.__studentsRepository.getAllItems():
            studentToDisplay = self.__studentsRepository.getItem(studentIdentifier)
            textContainingAllStudents += str(studentToDisplay) + "\n"
        if textContainingAllStudents == "":
            textContainingAllStudents = menuTexts.noStudentsInFacultyText
        return textContainingAllStudents


    def getTextOfAllDisciplines(self):
        textContainingAllDisciplines = ""
        for disciplineIdentifier in self.__disciplinesRepository.getAllItems():
            disciplineToDisplay = self.__disciplinesRepository.getItem(disciplineIdentifier)
            textContainingAllDisciplines += str(disciplineToDisplay) + "\n"
        if textContainingAllDisciplines == "":
            textContainingAllDisciplines = menuTexts.noDisciplinesInFacultyText
        return textContainingAllDisciplines


    def getAverageGradeAtADiscipline(self, disciplineGrades: list):
        if disciplineGrades is None:
            return self.__constants.MINIMUM_GRADE
        gradesSum = 0
        numberOfGrades = 0
        for grade in disciplineGrades:
            gradesSum += grade.getGrade()
            numberOfGrades += self.__constants.COUNT_BY_ONE
        return gradesSum / numberOfGrades

    def getStudentAverageGrade(self, studentGrades: dict):
        if studentGrades is None:
            return self.__constants.MINIMUM_GRADE
        gradesSum = 0
        numberOfDisciplines = 0
        for gradeIdentifier in studentGrades:
            allDisciplineGrades = studentGrades[gradeIdentifier]
            gradesSum += self.getAverageGradeAtADiscipline(allDisciplineGrades)
            numberOfDisciplines += self.__constants.COUNT_BY_ONE
        return gradesSum / numberOfDisciplines

    def getListOfStudentsWithTheBestSchoolSituation(self, allDisciplineGrades):
        studentsWithTheBestSchoolSituation = {}
        for studentIdentifier in allDisciplineGrades:
            studentGrades = allDisciplineGrades[studentIdentifier]
            averageGrade = self.getStudentAverageGrade(studentGrades)
            if averageGrade > self.__constants.MINIMUM_GRADE_TO_BE_CONSIDERED_TOP_STUDENT:
                studentToAppend = self.__studentsRepository.getItem(studentIdentifier)
                if studentToAppend not in studentsWithTheBestSchoolSituation:
                    studentsWithTheBestSchoolSituation[studentToAppend] = averageGrade
        listOfStudentsWithTheBestSchoolSituation = sorted(studentsWithTheBestSchoolSituation, key=lambda studentToCheck: studentsWithTheBestSchoolSituation[studentToCheck], reverse=True)
        sortedStudentsWithTheBestSchoolSituation = {}
        for student in listOfStudentsWithTheBestSchoolSituation:
            averageGrade = studentsWithTheBestSchoolSituation[student]
            sortedStudentsWithTheBestSchoolSituation[student] = averageGrade
        return sortedStudentsWithTheBestSchoolSituation

    def getTextOfStudentsWithTheBestSchoolSituation(self, allDisciplineGrades):
        studentsWithTheBestSchoolSituation = self.getListOfStudentsWithTheBestSchoolSituation(allDisciplineGrades)
        textOfStudentsWithTheBestSchoolSituation = menuTexts.studentsWithTheBestSchoolSituationHeaderText
        for student in studentsWithTheBestSchoolSituation:
            studentId = student.getStudentId()
            studentName = student.getStudentName()
            averageGrade = studentsWithTheBestSchoolSituation[student]
            textOfStudentsWithTheBestSchoolSituation += f"\nStudent nr {studentId}: {studentName}; grade {averageGrade}"
        return textOfStudentsWithTheBestSchoolSituation

    def getListOfDisciplinesAtWhichThereIsAtLeastOneGrade(self, allDisciplineGrades):
        disciplinesWithAtLeastOneGrade = {}
        for disciplineId in allDisciplineGrades:
            disciplineGrades = allDisciplineGrades[disciplineId]
            currentDisciplineGrades = []
            for gradeIdentifier in disciplineGrades:
                grades = disciplineGrades[gradeIdentifier]
                if grades is not None:
                    currentDisciplineGrades += grades
            averageGrade = self.getAverageGradeAtADiscipline(currentDisciplineGrades)
            disciplineToAppend = self.__disciplinesRepository.getItem(disciplineId)
            if disciplineToAppend not in disciplinesWithAtLeastOneGrade:
                disciplinesWithAtLeastOneGrade[disciplineToAppend] = averageGrade
        listOfDisciplinesWithAtLeastOneGrade = sorted(disciplinesWithAtLeastOneGrade, key=lambda disciplineToCheck: disciplinesWithAtLeastOneGrade[disciplineToCheck], reverse=True)
        sortedDisciplinesWithAtLeastOneGrade = {}
        for discipline in listOfDisciplinesWithAtLeastOneGrade:
            averageGrade = disciplinesWithAtLeastOneGrade[discipline]
            sortedDisciplinesWithAtLeastOneGrade[discipline] = averageGrade
        return sortedDisciplinesWithAtLeastOneGrade

    def getTextOfDisciplinesAtWhichThereIsAtLeastOneGrade(self, allDisciplineGrades):
        disciplinesAtWhichThereIsAtLeastOneGrade = self.getListOfDisciplinesAtWhichThereIsAtLeastOneGrade(allDisciplineGrades)
        textOfDisciplinesAtWhichThereIsAtLeastOneGrade = menuTexts.disciplinesAtWhichThereIsAtLeastOneGradeHeaderText
        for discipline in disciplinesAtWhichThereIsAtLeastOneGrade:
            disciplineId = discipline.getDisciplineId()
            disciplineName = discipline.getDisciplineName()
            disciplineAverageGrade = disciplinesAtWhichThereIsAtLeastOneGrade[discipline]
            textOfDisciplinesAtWhichThereIsAtLeastOneGrade += f"\nDiscipline nr {disciplineId}: {disciplineName}; average grade {disciplineAverageGrade}"
        return textOfDisciplinesAtWhichThereIsAtLeastOneGrade

    def getAllStudentsFailing(self, allDisciplineGrades):
        allStudentsFailing = []
        for studentIdentifier in allDisciplineGrades:
            studentGrades = allDisciplineGrades[studentIdentifier]
            for disciplineIdentifier in studentGrades:
                disciplineGrades = studentGrades[disciplineIdentifier]
                if self.getAverageGradeAtADiscipline(disciplineGrades) < 5:
                    studentToAppend = self.__studentsRepository.getItem(studentIdentifier)
                    if studentToAppend not in allStudentsFailing:
                        allStudentsFailing.append(studentToAppend)
        return allStudentsFailing

    def getTextOfAllStudentsFailing(self, allDisciplineGrades):
        allStudentsFailing = self.getAllStudentsFailing(allDisciplineGrades)
        textOfAllStudentsFailing = menuTexts.allStudentsFailingHeaderText
        for student in allStudentsFailing:
            studentId = student.getStudentId()
            studentName = student.getStudentName()
            textOfAllStudentsFailing += f"\nStudent nr {studentId}: {studentName}"
        return textOfAllStudentsFailing

    def Undo(self, historyHandler):
        historyHandler.Undo(self)

    def Redo(self, historyHandler):
        historyHandler.Redo(self)


