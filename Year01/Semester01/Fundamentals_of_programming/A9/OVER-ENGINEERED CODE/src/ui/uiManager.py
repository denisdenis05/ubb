from src.ui.inputOutput import Input
from src.ui.inputOutput import Output
from src.ui.textsToDisplay import errorTexts
from src.ui.textsToDisplay import menuTexts

class UiManager(Input, Output):
    def __init__(self, constants):
        super().__init__()
        self.__constants = constants


    def checkIfChosenOptionIsASubMenu(self, menuOption):
        if menuOption in self.__constants.NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE.keys():
            return True
        return False

    def checkIfMenuOptionExists(self, currentMenuPage, menuOption):
        if menuOption > self.__constants.NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE[currentMenuPage] or menuOption < self.__constants.MINIMUM_NUMBER_OF_OPTION_IN_A_MENU:
            self.displayErrorMessage(errorTexts.INVALID_MENU_OPTION_MESSAGE)
            return False
        return True


    def getActualMenuPageIndex(self, currentMenuPage, selectedMenuPage):
        actualMenuPageIndex = 0
        for menuPageNumber in self.__constants.NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE:
            if menuPageNumber < currentMenuPage:
                actualMenuPageIndex += self.__constants.NUMBER_OF_MENU_CHOICES_ON_EACH_MENU_PAGE[menuPageNumber]
        actualMenuPageIndex += selectedMenuPage
        return actualMenuPageIndex


    def displayMenu(self, menuPage):
        currentPageMenuText = menuTexts.MENU_TEXTS_FOR_PAGE[menuPage]
        self.displayMessage(currentPageMenuText)

    def getUserMenuChoice(self, currentMenuPage):
        self.displayMenu(currentMenuPage)
        if self.checkIfChosenOptionIsASubMenu(currentMenuPage):
            selectedMenuPage = self.getUserOptionInput()
            if self.checkIfMenuOptionExists(currentMenuPage, selectedMenuPage) is False:
                generalMenuIndex = self.__constants.GENERAL_MENU
                functionToCall = self.getUserMenuChoice(generalMenuIndex)
            else:
                actualMenuChoice = self.getActualMenuPageIndex(currentMenuPage, selectedMenuPage)
                if self.checkIfChosenOptionIsASubMenu(actualMenuChoice):
                    functionToCall = self.getUserMenuChoice(actualMenuChoice)
                else:
                    functionToCall = actualMenuChoice
        else:
            functionToCall = currentMenuPage
        return functionToCall
