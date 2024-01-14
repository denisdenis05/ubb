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
