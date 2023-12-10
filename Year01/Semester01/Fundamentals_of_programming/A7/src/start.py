from src.domain import Complex
from src.services import Services
from src.repository import ComplexRepositoryMemory
from src.repository.binary_save import ComplexRepositoryBinary
from src.repository.text_file_save import ComplexRepositoryTextFile
from src.repository.json_file_save import ComplexRepositoryJSONFile
from src.repository.sql_save import ComplexRepositorySQL
import configparser


def getProperties():
    configParserInstance = configparser.RawConfigParser()
    configParserInstance.read('settings.properties')
    binaryFileName = configParserInstance.get('settings', 'binaryFileName')
    textFileName = configParserInstance.get('settings', 'textFileName')
    JsonFileName = configParserInstance.get('settings', 'JsonFileName')
    typeOfRepository = configParserInstance.get('settings', 'typeOfRepository')
    return binaryFileName, textFileName, JsonFileName, typeOfRepository


def createRepository(binaryFileName, textFileName, JsonFileName, typeOfRepository):
    if str(typeOfRepository) == "binary":
        complexNumbersRepository = ComplexRepositoryBinary(str(binaryFileName))
    elif str(typeOfRepository) == "text":
        complexNumbersRepository = ComplexRepositoryTextFile(str(textFileName))
    elif str(typeOfRepository) == "json":
        complexNumbersRepository = ComplexRepositoryJSONFile(str(JsonFileName))
    elif str(typeOfRepository) == "sql":
        complexNumbersRepository = ComplexRepositorySQL()
    else:
        initialComplexNumbersList = {(1, 2): Complex(1, 2),
                                     (3, 4): Complex(3, 4),
                                     (5, 6): Complex(5, 6),
                                     (7, 8): Complex(7, 8),
                                     (9, 10): Complex(9, 10),
                                     (11, 12): Complex(11, 12),
                                     (13, 14): Complex(13, 14),
                                     (15, 16): Complex(15, 16),
                                     (17, 18): Complex(17, 18),
                                     (19, 20): Complex(19, 20),
                                     (21, 22): Complex(21, 22)}
        complexNumbersRepository = ComplexRepositoryMemory(initialComplexNumbersList)
    return complexNumbersRepository

def main():
    binaryFileName, textFileName, JsonFileName, typeOfRepository = getProperties()
    complexNumbersRepository = createRepository(binaryFileName, textFileName, JsonFileName, typeOfRepository)

    serviceFunctions = Services(complexNumbersRepository, typeOfRepository)
    serviceFunctions.startMenu()


main()
