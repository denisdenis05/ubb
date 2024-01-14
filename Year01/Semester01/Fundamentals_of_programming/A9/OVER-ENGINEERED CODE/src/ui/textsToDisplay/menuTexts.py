
generalMenuText = """
1.Manage students and disciplines.
2.Grade students at a given discipline.
3.Search for disciplines/students.
4.Create statistics
5.Undo
6.Redo
"""

manageStudentsMenuText = """
1.Add students/disciplines.
2.Remove students/disciplines.
3.Update students/disciplines.
4.List students/disciplines.
"""

gradeStudentsMenuText = """
1.Grade a student at a discipline.
2.List grades.
"""

searchMenuText = """
1.Search for students.
2.Search for disciplines.
"""

createStatisticsMenuText = """
1.All students failing.
2.Students with the best school situation.
3.Disciplines at which there is at least one grade.
"""

addStudentsDisciplinesMenuText = """
1.Add student.
2.Add discipline.
"""

removeStudentsDisciplinesMenuText = """
1.Remove student.
2.Remove discipline.
"""

updateStudentsDisciplinesMenuText = """
1.Update student.
2.Update discipline.
"""


listStudentsDisciplinesMenuText = """
1.List students.
2.List disciplines.
"""

MENU_TEXTS_FOR_PAGE = {0: generalMenuText,
                       1: manageStudentsMenuText,
                       2: gradeStudentsMenuText,
                       3: searchMenuText,
                       4: createStatisticsMenuText,
                       7: addStudentsDisciplinesMenuText,
                       8: removeStudentsDisciplinesMenuText,
                       9: updateStudentsDisciplinesMenuText,
                       10: listStudentsDisciplinesMenuText}



studentAddedSuccessfullyText = "Student added successfully in the faculty!"
studentRemovedSuccessfullyText = "Student removed successfully from the faculty!"
studentUpdatedSuccessfullyText = "Student updated successfully in the faculty!"

disciplineAddedSuccessfullyText = "Discipline added successfully in the faculty!"
disciplineRemovedSuccessfullyText = "Discipline removed successfully from the faculty!"
disciplineUpdatedSuccessfullyText = "Discipline updated successfully in the faculty!"

gradeAddedSuccessfullyText = "Grade added successfully in the faculty!"

insertStudentIdText = "Insert the student's id: "
insertStudentNameText = "Insert the student's name: "
insertNewStudentNameText = "Insert the new student's name: "
insertGradeText = "Insert the grade: "

insertDisciplineIdText = "Insert the discipline's id: "
insertDisciplineNameText = "Insert the discipline's name: "
insertNewDisciplineNameText = "Insert the new discipline's name: "

noStudentsInFacultyText = "There are no students in the faculty!"
noDisciplinesInFacultyText = "There are no disciplines in the faculty!"
noGradesInFacultyText = "There are no grades in the faculty!"

matchingStudentsHeaderText = "Matching students:"
noStudentsFoundText = "No students found!"
matchingDisciplinesHeaderText = "Matching disciplines:"
noDisciplinesFoundText = "No disciplines found!"

allStudentsFailingHeaderText = "All students failing:"
studentsWithTheBestSchoolSituationHeaderText = "Students with the best school situation:"
disciplinesAtWhichThereIsAtLeastOneGradeHeaderText = "Disciplines at which there is at least one grade:"

undoSuccessfullyText = "Undo successfully!"
redoSuccessfullyText = "Redo successfully!"
