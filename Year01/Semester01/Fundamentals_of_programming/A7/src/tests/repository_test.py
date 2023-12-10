from unittest import TestCase

from src.domain import Complex
from src.repository import ComplexRepositoryMemory
from src.repository.binary_save import ComplexRepositoryBinary
from src.repository.text_file_save import ComplexRepositoryTextFile

class TestRepository(TestCase):

    def setUp(self):
        self.__memoryRepository = ComplexRepositoryMemory({})
        self.__binaryRepository = ComplexRepositoryBinary("test_complex_numbers.bin")
        self.__textRepository = ComplexRepositoryTextFile("test_complex_numbers.txt")



    def testMemoryRepositoryAddRemove(self):
        self.__memoryRepository.addToRepository(Complex(1, 2))
        self.assertEqual(self.__memoryRepository.removeFromRepository(Complex(1, 2)), Complex(1, 2))
        self.__memoryRepository.addToRepository(Complex(3, 4))
        self.assertEqual(self.__memoryRepository.removeFromRepository(Complex(3, 4)), Complex(3, 4))
        self.__memoryRepository.addToRepository(Complex(5, 6))
        self.assertEqual(self.__memoryRepository.removeFromRepository(Complex(5, 6)), Complex(5, 6))
        self.__memoryRepository.addToRepository(Complex(11, -8))
        self.assertEqual(self.__memoryRepository.removeFromRepository(Complex(11, -8)), Complex(11, -8))
        self.__memoryRepository.addToRepository(Complex(0, 0))
        self.assertEqual(self.__memoryRepository.removeFromRepository(Complex(0, 0)), Complex(0, 0))
        self.__memoryRepository.addToRepository(Complex(-1, -2))
        self.assertEqual(self.__memoryRepository.removeFromRepository(Complex(-1, -2)), Complex(-1, -2))
        self.__memoryRepository.addToRepository(Complex(-3, -4))
        self.assertEqual(self.__memoryRepository.removeFromRepository(Complex(-3, -4)), Complex(-3, -4))

    def testBinaryRepositoryAddRemove(self):
        self.__binaryRepository.addToRepository(Complex(1, 2))
        self.assertEqual(self.__binaryRepository.removeFromRepository(Complex(1, 2)), Complex(1, 2))
        self.__binaryRepository.addToRepository(Complex(3, 4))
        self.assertEqual(self.__binaryRepository.removeFromRepository(Complex(3, 4)), Complex(3, 4))
        self.__binaryRepository.addToRepository(Complex(5, 6))
        self.assertEqual(self.__binaryRepository.removeFromRepository(Complex(5, 6)), Complex(5, 6))
        self.__binaryRepository.addToRepository(Complex(11, -8))
        self.assertEqual(self.__binaryRepository.removeFromRepository(Complex(11, -8)), Complex(11, -8))
        self.__binaryRepository.addToRepository(Complex(0, 0))
        self.assertEqual(self.__binaryRepository.removeFromRepository(Complex(0, 0)), Complex(0, 0))
        self.__binaryRepository.addToRepository(Complex(-1, -2))
        self.assertEqual(self.__binaryRepository.removeFromRepository(Complex(-1, -2)), Complex(-1, -2))
        self.__binaryRepository.addToRepository(Complex(-3, -4))
        self.assertEqual(self.__binaryRepository.removeFromRepository(Complex(-3, -4)), Complex(-3, -4))

    def testTextRepositoryAddRemove(self):
        self.__textRepository.addToRepository(Complex(1, 2))
        self.assertEqual(self.__textRepository.removeFromRepository(Complex(1, 2)), Complex(1, 2))
        self.__textRepository.addToRepository(Complex(3, 4))
        self.assertEqual(self.__textRepository.removeFromRepository(Complex(3, 4)), Complex(3, 4))
        self.__textRepository.addToRepository(Complex(5, 6))
        self.assertEqual(self.__textRepository.removeFromRepository(Complex(5, 6)), Complex(5, 6))
        self.__textRepository.addToRepository(Complex(11, -8))
        self.assertEqual(self.__textRepository.removeFromRepository(Complex(11, -8)), Complex(11, -8))
        self.__textRepository.addToRepository(Complex(0, 0))
        self.assertEqual(self.__textRepository.removeFromRepository(Complex(0, 0)), Complex(0, 0))
        self.__textRepository.addToRepository(Complex(-1, -2))
        self.assertEqual(self.__textRepository.removeFromRepository(Complex(-1, -2)), Complex(-1, -2))
        self.__textRepository.addToRepository(Complex(-3, -4))
        self.assertEqual(self.__textRepository.removeFromRepository(Complex(-3, -4)), Complex(-3, -4))

