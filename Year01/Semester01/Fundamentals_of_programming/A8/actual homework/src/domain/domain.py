class Student:
    def __init__(self, studentId, studentName):
        self.__studentId = studentId
        self.__studentName = studentName


    def getStudentName(self):
        return self.__studentName

    def getStudentId(self):
        return self.__studentId

    def setStudentName(self, newStudentName):
        self.__studentName = newStudentName

    def __str__(self):
        return f"{self.__studentId} : {self.__studentName}"

class Discipline:
    def __init__(self, disciplineId, disciplineName):
        self.__disciplineId = disciplineId
        self.__disciplineName = disciplineName

    def getDisciplineId(self):
        return self.__disciplineId

    def getDisciplineName(self):
        return self.__disciplineName

    def setDisciplineName(self, newDisciplineName):
        self.__disciplineName = newDisciplineName

    def __str__(self):
        return f"{self.__disciplineId} : {self.__disciplineName}"


class FacultyGrades:
    def __init__(self, studentId, disciplineId, grade):
        self.__studentId = studentId
        self.__disciplineId = disciplineId
        self.__grade = grade

    def getStudentId(self):
        return self.__studentId

    def getDisciplineId(self):
        return self.__disciplineId

    def getGrade(self):
        return self.__grade

    def __str__(self):
        return f"Student nr {self.__studentId} at discipline {self.__disciplineId} has grade {self.__grade}"

# class Faculty:
#     def __init__(self):
#         self.students = []
#         self.disciplines = []
#         self.grades = {}
#
#     def addStudent(self, studentToAdd: Student):
#         self.students.append(studentToAdd)
#
#     def removeStudent(self, studentIdToRemove):
#         numberOfStudentsInFaculty = len(self.students)
#         for studentIndex in range(numberOfStudentsInFaculty):
#             studentToCheckIfShouldBeRemoved = self.students[studentIndex]
#             if studentToCheckIfShouldBeRemoved.getStudentId() == studentIdToRemove:
#                 return self.students.pop(studentIndex)
#
#     def addDiscipline(self, disciplineToAdd: Discipline):
#         self.disciplines.append(disciplineToAdd)
#
#     def removeDiscipline(self, disciplineIdToRemove):
#         numberOfDisciplinesInFaculty = len(self.disciplines)
#         for disciplineIndex in range(numberOfDisciplinesInFaculty):
#             disciplineToCheckIfShouldBeRemoved = self.disciplines[disciplineIndex]
#             if disciplineToCheckIfShouldBeRemoved.getDisciplineId() == disciplineIdToRemove:
#                 return self.disciplines.pop(disciplineIndex)
#
#     def refreshStudent(self, oldStudent, newStudent):
#         numberOfStudentsInFaculty = len(self.students)
#         for studentIndex in range(numberOfStudentsInFaculty):
#             studentToCheckIfShouldBeUpdated = self.students[studentIndex]
#             if studentToCheckIfShouldBeUpdated.getStudentId() == oldStudent.getStudentId():
#                 self.students[studentIndex] = newStudent
#                 return self.students[studentIndex]
#
#     def refreshDiscipline(self, oldDiscipline, newDiscipline):
#         numberOfDisciplinesInFaculty = len(self.disciplines)
#         for disciplineIndex in range(numberOfDisciplinesInFaculty):
#             disciplineToCheckIfShouldBeUpdated = self.disciplines[disciplineIndex]
#             if disciplineToCheckIfShouldBeUpdated.getDisciplineId() == oldDiscipline.getDisciplineId():
#                 self.disciplines[disciplineIndex] = newDiscipline
#                 return self.disciplines[disciplineIndex]
#
#     def addGrade(self, studentId, disciplineId, grade):
#         if (studentId, disciplineId) not in self.grades:
#             self.grades[(studentId, disciplineId)] = [grade]
#         else:
#             self.grades[(studentId, disciplineId)].append(grade)
#
#     def findGrades(self, studentId, disciplineId):
#         if (studentId, disciplineId) in self.grades:
#             return self.grades[(studentId, disciplineId)]
#         else:
#             return []
#
#
#     def findStudent(self, studentId):
#         for student in self.students:
#             if student.getStudentId() == studentId:
#                 return student
#         return None
#
#     def findDiscipline(self, disciplineId):
#         for discipline in self.disciplines:
#             if discipline.getDisciplineId() == disciplineId:
#                 return discipline
#         return None
