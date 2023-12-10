import mysql.connector
from mysql.connector import Error

from src.domain import Complex
from src.repository import ComplexRepositoryMemory

class ComplexRepositorySQL(ComplexRepositoryMemory):

    def connectToSqlDatabase(self):
        try:
            SqlConnection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin',
                database='complexNumbers'
            )

            if SqlConnection.is_connected():
                return SqlConnection
        except Error as mysqlError:
            print(mysqlError)

    def __init__(self):
        self.__SqlConnection = self.connectToSqlDatabase()
        self.__data = self.__loadDataFromTable()
        super().__init__(self.__data)

    def updateLocalDataDictionary(self):
        self.__data = super().getAllSavedDictionaryValues()

    def addToRepository(self, newComplexNumber: Complex):
        self.__addDataToTable(newComplexNumber)
        super().addToRepository(newComplexNumber)
        self.updateLocalDataDictionary()

    def removeFromRepository(self, complexNumberToRemove: Complex):
        super().removeFromRepository(complexNumberToRemove)
        self.updateLocalDataDictionary()
        self.__removeDataFromTable(complexNumberToRemove)
        return complexNumberToRemove

    def getAllSavedDictionaryValues(self) -> dict:
        return super().getAllSavedDictionaryValues()

    def getAllSavedListValues(self) -> list:
        return super().getAllSavedListValues()

    def __loadDataFromTable(self):
        try:
            mySqlTerminal = self.__SqlConnection.cursor()
            queryToExecute = "SELECT * FROM complex_numbers"
            mySqlTerminal.execute(queryToExecute)
            rows = mySqlTerminal.fetchall()

            dictionaryOfSavedComplexNumbers = {}
            for row in rows:
                INDEX_OF_REAL_PART = 0
                INDEX_OF_IMAGINARY_PART = 1
                realPart = row[INDEX_OF_REAL_PART]
                imaginaryPart = row[INDEX_OF_IMAGINARY_PART]

                complexNumberToAdd = Complex(realPart, imaginaryPart)
                complexNumberIndices = (realPart, imaginaryPart)
                dictionaryOfSavedComplexNumbers[complexNumberIndices] = complexNumberToAdd

            return dictionaryOfSavedComplexNumbers
        except Error as mysqlError:
            print(mysqlError)

    def __addDataToTable(self, complexNumberToAdd):
        try:
            mySqlTerminal = self.__SqlConnection.cursor()
            queryToExecute = "INSERT INTO complex_numbers VALUES (%s, %s)"
            realPart = complexNumberToAdd.getRealPart()
            imaginaryPart = complexNumberToAdd.getImaginaryPart()
            mySqlTerminal.execute(queryToExecute, (realPart, imaginaryPart))
            self.__SqlConnection.commit()
        except Error as mysqlError:
            print(mysqlError)

    def __removeDataFromTable(self, complexNumberToRemove):
        try:
            mySqlTerminal = self.__SqlConnection.cursor()
            queryToExecute = "DELETE FROM complex_numbers WHERE realpart = %s AND imaginarypart = %s"
            realPart = complexNumberToRemove.getRealPart()
            imaginaryPart = complexNumberToRemove.getImaginaryPart()
            mySqlTerminal.execute(queryToExecute, (realPart, imaginaryPart))
            self.__SqlConnection.commit()
        except Error as mysqlError:
            print(mysqlError)

    def deleteAllElementsFromRepository(self):
        self.__data = {}

        try:
            mySqlTerminal = self.__SqlConnection.cursor()
            queryToExecute = "DELETE FROM complex_numbers"
            mySqlTerminal.execute(queryToExecute)
            self.__SqlConnection.commit()
        except Error as mysqlError:
            print(mysqlError)