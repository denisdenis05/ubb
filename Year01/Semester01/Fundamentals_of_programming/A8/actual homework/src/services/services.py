from src.domain.domain import Student
from src.domain.domain import Discipline
from src.domain.domain import FacultyGrades
from src.ui.textsToDisplay import menuTexts

class Services:
    def __init__(self, studentsRepository, disciplinesRepository, facultyDataRepository, constants):
        self.__studentsRepository = studentsRepository
        self.__disciplinesRepository = disciplinesRepository
        self.__facultyDataRepository = facultyDataRepository
        self.__constants = constants


    def checkIfChosenOptionIsASubMenu(self, menuOption):
        if menuOption in self.__constants.NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE.keys():
            return True
        return False

    def checkIfMenuOptionExists(self, currentMenuPage, menuOption):
        if menuOption > self.__constants.NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE[currentMenuPage] or menuOption < self.__constants.MINIMUM_NUMBER_OF_OPTION_IN_A_MENU:
            return False
        return True


    def getActualMenuPageIndex(self, currentMenuPage, selectedMenuPage):
        actualMenuPageIndex = 0
        for menuPageNumber in self.__constants.NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE:
            if menuPageNumber < currentMenuPage:
                actualMenuPageIndex += self.__constants.NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE[menuPageNumber]
        actualMenuPageIndex += selectedMenuPage
        return actualMenuPageIndex


    def checkIfGradeIsValid(self, grade):
        try:
            grade = float(grade)
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



    # ---------------------------------------
    # FUNCTIONS DOWN HERE
    # ---------------------------------------

        # ----
        # Functions working with repositories
        # ----


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
            return self.__studentsRepository.removeFromRepository(studentId)
        except:
            return None

    def removeDiscipline(self, disciplineId: int):
        try:
            return self.__disciplinesRepository.removeFromRepository(disciplineId)
        except:
            return None

    def removeAllStudentGrades(self, studentId):
        allStudentGrades = self.getDictionaryOfAllStudentGrades(studentId)
        for gradeIdentifier in allStudentGrades:
            self.removeStudentsGradesAtADiscipline(gradeIdentifier)
        return True

    def removeAllDisciplineGrades(self, disciplineId):
        allDisciplineGrades = self.getDictionaryOfAllDisciplineGrades(disciplineId)
        for gradeIdentifier in allDisciplineGrades:
            statusOfRemove = self.removeStudentsGradesAtADiscipline(gradeIdentifier)
            if statusOfRemove is None:
                allDisciplineGrades.pop(gradeIdentifier)
        return True

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
        return self.__facultyDataRepository.addAsMultipleItemsToRepository(gradeToAddToFaculty, gradeIdentifier)

    def removeStudentsGradesAtADiscipline(self, gradeIdentifier):
        return self.__facultyDataRepository.removeFromRepository(gradeIdentifier)


        # ----
        # Search functions
        # ----


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

        # ----
        # Functions that build text
        # ----

    def listAllGrades(self):
        textOfAllGrades = ""
        allDisciplines = self.__disciplinesRepository.getAllItems()
        allStudents = self.__studentsRepository.getAllItems()
        if len(allDisciplines) == 0 or len(allStudents) == 0:
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

    def getAllStudentGrades(self, studentId):
        textOfAllGrades = ""
        allDisciplines = self.__disciplinesRepository.getAllItems()
        allStudents = self.__studentsRepository.getAllItems()
        if len(allDisciplines) == 0 or len(allStudents) == 0:
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


        # ----
        # Functions that build text - Stats
        # ----


    def getTextOfStudentsWithTheBestSchoolSituation(self):
        studentsWithTheBestSchoolSituation = self.getListOfStudentsWithTheBestSchoolSituation()
        textOfStudentsWithTheBestSchoolSituation = menuTexts.studentsWithTheBestSchoolSituationHeaderText
        for student in studentsWithTheBestSchoolSituation:
            studentId = student.getStudentId()
            studentName = student.getStudentName()
            averageGrade = studentsWithTheBestSchoolSituation[student]
            textOfStudentsWithTheBestSchoolSituation += f"\nStudent nr {studentId}: {studentName}; grade {averageGrade}"
        return textOfStudentsWithTheBestSchoolSituation



    def getTextOfDisciplinesAtWhichThereIsAtLeastOneGrade(self):
        disciplinesAtWhichThereIsAtLeastOneGrade = self.getListOfDisciplinesAtWhichThereIsAtLeastOneGrade()
        textOfDisciplinesAtWhichThereIsAtLeastOneGrade = menuTexts.disciplinesAtWhichThereIsAtLeastOneGradeHeaderText
        for discipline in disciplinesAtWhichThereIsAtLeastOneGrade:
            disciplineId = discipline.getDisciplineId()
            disciplineName = discipline.getDisciplineName()
            disciplineAverageGrade = disciplinesAtWhichThereIsAtLeastOneGrade[discipline]
            textOfDisciplinesAtWhichThereIsAtLeastOneGrade += f"\nDiscipline nr {disciplineId}: {disciplineName}; average grade {disciplineAverageGrade}"
        return textOfDisciplinesAtWhichThereIsAtLeastOneGrade

    def getTextOfAllStudentsFailing(self):
        allStudentsFailing = self.getAllStudentsFailing()
        textOfAllStudentsFailing = menuTexts.allStudentsFailingHeaderText
        for student in allStudentsFailing:
            studentId = student.getStudentId()
            studentName = student.getStudentName()
            textOfAllStudentsFailing += f"\nStudent nr {studentId}: {studentName}"
        return textOfAllStudentsFailing


        # ----
        # Other workers
        # ----

    def getAverageGradeAtADiscipline(self, disciplineGrades: list):
        if disciplineGrades is None:
            return self.__constants.MINIMUM_GRADE
        gradesSum = 0
        numberOfGrades = 0
        for grade in disciplineGrades:
            gradesSum += grade.getGrade()
            numberOfGrades += 1
        return gradesSum / numberOfGrades

    def getStudentAverageGrade(self, studentGrades: dict):
        if studentGrades is None:
            return self.__constants.MINIMUM_GRADE
        gradesSum = 0
        numberOfDisciplines = 0
        for gradeIdentifier in studentGrades:
            allDisciplineGrades = studentGrades[gradeIdentifier]
            gradesSum += self.getAverageGradeAtADiscipline(allDisciplineGrades)
            numberOfDisciplines += 1
        return gradesSum / numberOfDisciplines

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

    def getAllStudentsFailing(self):
        allDisciplineGrades = {}
        for studentId in self.__studentsRepository.getAllItems():
            allDisciplineGrades[studentId] = self.getDictionaryOfAllStudentGrades(studentId)
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

    def getListOfDisciplinesAtWhichThereIsAtLeastOneGrade(self):
        allDisciplineGrades = {}
        for disciplineId in self.__disciplinesRepository.getAllItems():
            allDisciplineGrades[disciplineId] = self.getDictionaryOfAllDisciplineGrades(disciplineId)
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
        listOfDisciplinesWithAtLeastOneGrade = sorted(disciplinesWithAtLeastOneGrade,
                                                      key=lambda disciplineToCheck: disciplinesWithAtLeastOneGrade[
                                                          disciplineToCheck], reverse=True)
        sortedDisciplinesWithAtLeastOneGrade = {}
        for discipline in listOfDisciplinesWithAtLeastOneGrade:
            averageGrade = disciplinesWithAtLeastOneGrade[discipline]
            sortedDisciplinesWithAtLeastOneGrade[discipline] = averageGrade
        return sortedDisciplinesWithAtLeastOneGrade


    def getListOfStudentsWithTheBestSchoolSituation(self):
        allDisciplineGrades = {}
        for studentId in self.__studentsRepository.getAllItems():
            allDisciplineGrades[studentId] = self.getDictionaryOfAllStudentGrades(studentId)
        studentsWithTheBestSchoolSituation = {}
        for studentIdentifier in allDisciplineGrades:
            studentGrades = allDisciplineGrades[studentIdentifier]
            averageGrade = self.getStudentAverageGrade(studentGrades)
            if averageGrade > self.__constants.MINIMUM_GRADE_TO_BE_CONSIDERED_TOP_STUDENT:
                studentToAppend = self.__studentsRepository.getItem(studentIdentifier)
                if studentToAppend not in studentsWithTheBestSchoolSituation:
                    studentsWithTheBestSchoolSituation[studentToAppend] = averageGrade
        listOfStudentsWithTheBestSchoolSituation = sorted(studentsWithTheBestSchoolSituation,
                                                          key=lambda studentToCheck:
                                                          studentsWithTheBestSchoolSituation[studentToCheck],
                                                          reverse=True)
        sortedStudentsWithTheBestSchoolSituation = {}
        for student in listOfStudentsWithTheBestSchoolSituation:
            averageGrade = studentsWithTheBestSchoolSituation[student]
            sortedStudentsWithTheBestSchoolSituation[student] = averageGrade
        return sortedStudentsWithTheBestSchoolSituation



