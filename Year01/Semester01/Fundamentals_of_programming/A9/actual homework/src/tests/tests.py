from unittest import TestCase

from src.domain.domain import Student
from src.domain.domain import Discipline
from src.domain.domain import FacultyGrades

from src.repository.repository import RepositoryMemory

from src.services.operations import Operations

class Tests(TestCase):

    def setUp(self):
        self.__memoryRepository = RepositoryMemory()

    def testMemoryRepositoryAddRemove(self):
        student = Student(1, "Denis")
        self.__memoryRepository.addToRepository(student, 1)
        self.assertEqual(self.__memoryRepository.removeFromRepository(1), student)

        student = Student(2, "Emanuel")
        self.__memoryRepository.addToRepository(student, 2)
        self.assertEqual(self.__memoryRepository.removeFromRepository(2), student)

        student = Student(3, "Cristi")
        self.__memoryRepository.addToRepository(student, 3)
        self.assertEqual(self.__memoryRepository.removeFromRepository(3), student)

        grade = FacultyGrades(4, 1, 10)
        self.__memoryRepository.addToRepository(grade, (4, 1))
        self.assertEqual(self.__memoryRepository.removeFromRepository((4, 1)), grade)
