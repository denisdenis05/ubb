MINIMUM_GRADE = 1
MAXIMUM_GRADE = 10
MINIMUM_GRADE_TO_BE_CONSIDERED_TOP_STUDENT = 2

MINIMUM_NUMBER_OF_OPTION_IN_A_MENU = 1

GENERAL_MENU = 0
MANAGE_STUDENTS_MENU = 1
GRADE_STUDENTS_MENU = 2
SEARCH_MENU = 3
CREATE_STATISTICS_MENU = 4
UNDO_OPTION = 5
REDO_OPTION = 6

ADD_STUDENT_DISCIPLINES_OPTION = 7
REMOVE_STUDENT_DISCIPLINES_OPTION = 8
UPDATE_STUDENT_DISCIPLINES_OPTION = 9
LIST_STUDENTS_DISCIPLINES_OPTION = 10

GRADE_STUDENT_AT_A_DISCIPLINE_OPTION = 11
LIST_GRADES_OPTION = 12

SEARCH_FOR_STUDENTS_OPTION = 13
SEARCH_FOR_DISCIPLINES_OPTION = 14

ALL_STUDENTS_FAILING_OPTION = 15
STUDENTS_WITH_THE_BEST_SCHOOL_SITUATION_OPTION = 16
DISCIPLINES_AT_WHICH_THERE_IS_AT_LEAST_ONE_GRADE_OPTION = 17

ADD_STUDENT_OPTION = 18
ADD_DISCIPLINE_OPTION = 19

REMOVE_STUDENT_OPTION = 20
REMOVE_DISCIPLINE_OPTION = 21

UPDATE_STUDENT_OPTION = 22
UPDATE_DISCIPLINE_OPTION = 23

LIST_STUDENTS_OPTION = 24
LIST_DISCIPLINES_OPTION = 25


OPTION_IS_A_FUNCTION_NOT_A_MENU = -1

NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE = {0: 6,  # general menu
                                            1: 4,  # manage students menu
                                            2: 2,  # grade students menu
                                            3: 2,  # search menu
                                            4: 3,  # create statistics menu
                                            7: 2,  # add students/disciplines menu
                                            8: 2,  # remove students/disciplines menu
                                            9: 2,  # update students/disciplines menu
                                            10: 2}  # list students/disciplines menu


INDEX_FROM_WHICH_THE_MENU_OPTIONS_CANT_BE_SUBMENUS = 5

INVALID_OPTION = -1

NOT_KNOWN_NAME_PLACEHOLDER = "unknownName"
NOT_KNOWN_ID_PLACEHOLDER = 1

