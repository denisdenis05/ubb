import ui
import functions

def getListOfDefinedFunction():
    definedFunctions = {}
    definedFunctions["help"] = ui.printUIHelp
    definedFunctions["add"] = functions.addContestantToList
    definedFunctions["insert"] = functions.insertContestantInList
    definedFunctions["remove"] = functions.removeContestantsFromList
    definedFunctions["replace"] = functions.replaceContestantsInList
    definedFunctions["list"] = ui.displayContestants
    definedFunctions["top"] = ui.displayContestants
    definedFunctions["undo"] = functions.removeLastChangesInListOfContestants
    return definedFunctions


def main():
    definedFunctions = getListOfDefinedFunction()
    stackedHistoryOfListOfContestants = []
    emptyList = []
    numberOfContestantsToRandomlyGenerate = 5
    randomlyGeneratedListOfContestants = functions.generateRandomListOfContestants(emptyList, numberOfContestantsToRandomlyGenerate)
    stackedHistoryOfListOfContestants.append(randomlyGeneratedListOfContestants)
    ui.startTerminal(definedFunctions, stackedHistoryOfListOfContestants)


main()
