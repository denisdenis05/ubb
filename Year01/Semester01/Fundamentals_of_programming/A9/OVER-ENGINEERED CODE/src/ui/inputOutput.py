from src import constants
from colorama import Fore, init

class Input:

    @staticmethod
    def getInput():
        userInput = input("> ")
        return userInput

    def getUserOptionInput(self):
        userInput = self.getInput()
        try:
            userInput = int(userInput)
        except ValueError:
            userInput = constants.INVALID_OPTION
        return userInput


class Output:
    def __init__(self):
        init(autoreset=True)  # colorama

    @staticmethod
    def displayMessage(message):
        print(message)

    @staticmethod
    def displayErrorMessage(errorMessage):
        print(Fore.RED + errorMessage)

    @staticmethod
    def displaySuccessMessage(successMessage):
        print(Fore.GREEN + successMessage)
