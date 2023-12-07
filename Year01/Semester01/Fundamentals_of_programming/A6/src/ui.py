import functions
from copy import deepcopy
from colorama import Fore, Back, init
import constants

# COMMAND HANDLING

def printUIHelp():
    textToPrint = """Help menu:
    
    (A) ADD THE RESULT OF A NEW PARTICIPANT
    add - adds a participant alongside with the 3 scores of the solved problems
    USAGE: add <P1 score> <P2 score> <P3 score>
        -p1, p2 and p3 are integers between 0 and 10
        
    insert - adds a participant in a specific position alongside with the 3 scores of the solved problems
    USAGE: insert <P1 score> <P2 score> <P3 score> at <position> 
        -p1, p2 and p3 are integers between 0 and 10
        -position should be between 0 and the last existent position 
    
    (B) MODIFY  SCORES
    remove - sets the score of participants at specific positions to 0
    USAGE: remove <position>
    USAGE2: remove <start position> to <end position>
        - sets the score to 0 for all the participants from start position to end position
    USAGE3: remove [ < | = | > ] <score> 
        - sets the score with an average score less, equal or greater than a value
    
    replace - replaces the score of a participant's problem
    USAGE: replace <contestant> <P1 | P2 | P3> with <new score>
        -p1, p2 and p3 are integers between 0 and 10
 
    (C) DISPLAY PARTICIPANTS
    list - displays participants according to the arguments
    USAGE1: list 
        - displays all participants
    USAGE 2: list sorted
        - displays all participants in decreasing order
    USAGE3: list [ < | = | > ] <score>
        - displays all participants with an average score less, equal or greater than a value  
 
    (D) ESTABLISH THE PODIUM
    top - displays the top
    USAGE: top <number> 
    ALTERNATIVE USAGE: top <number> <P1 | P2 | P3>
    
    (E) UNDO
    undo - undo the last operation (can be called repeatedly)
    """
    print(Back.CYAN + Fore.BLACK + textToPrint)


def add_command_CommandHandler(commandName: str, commandArguments: list, definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    try:
        firstProblemScore = int(commandArguments[constants.INDEX_OF_FIRST_PROBLEM_SCORE])
        secondProblemScore = int(commandArguments[constants.INDEX_OF_SECOND_PROBLEM_SCORE])
        thirdProblemScore = int(commandArguments[constants.INDEX_OF_THIRD_PROBLEM_SCORE])
        functions.checkIfValidValues(firstProblemScore, secondProblemScore, thirdProblemScore)
        stackedHistoryOfListOfContestants = definedFunctions[str(commandName.lower())](firstProblemScore, secondProblemScore, thirdProblemScore, stackedHistoryOfListOfContestants)
        print(f"Added values {firstProblemScore}, {secondProblemScore} and {thirdProblemScore}")
    except (ValueError, IndexError):
        commandErrorHandler(commandName, constants.INVALID_ARGUMENTS_ERROR_CODE)
    return stackedHistoryOfListOfContestants


def insert_command_CommandHandler(commandName: str, commandArguments: list, definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    ARGUMENT_INDEX_FOR_AT_KEYWORD = 3
    ARGUMENT_INDEX_FOR_PLACE_TO_INSERT_IN = 4
    try:
        if commandArguments[ARGUMENT_INDEX_FOR_AT_KEYWORD].lower() != "at":
            raise ValueError
        firstProblemScore = int(commandArguments[constants.INDEX_OF_FIRST_PROBLEM_SCORE])
        secondProblemScore = int(commandArguments[constants.INDEX_OF_SECOND_PROBLEM_SCORE])
        thirdProblemScore = int(commandArguments[constants.INDEX_OF_THIRD_PROBLEM_SCORE])
        functions.checkIfValidValues(firstProblemScore, secondProblemScore, thirdProblemScore)
        indexToInsertIn = int(commandArguments[ARGUMENT_INDEX_FOR_PLACE_TO_INSERT_IN])
        stackedHistoryOfListOfContestants = definedFunctions[str(commandName.lower())](firstProblemScore, secondProblemScore, thirdProblemScore, indexToInsertIn, stackedHistoryOfListOfContestants)
        print(f"Added values {firstProblemScore}, {secondProblemScore} and {thirdProblemScore}")
    except (ValueError, IndexError, functions.IndexOutOfListError) as e:
        if type(e) == functions.IndexOutOfListError:
            commandErrorHandler(commandName, constants.INSERT_REMOVE_INDEX_OUT_OF_BOUNDS_ERROR_CODE)
        else:
            commandErrorHandler(commandName, constants.INVALID_ARGUMENTS_ERROR_CODE)
    return stackedHistoryOfListOfContestants

def remove_command_CommandHandler(commandName: str, commandArguments: list, definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    MINIMUM_NUMBER_OF_COMMAND_ARGUMENTS = 1
    try:
        INDEX_OF_THE_OPERATOR = 0
        INDEX_OF_THE_AVERAGE_SCORE = 1
        if ("<" in commandArguments[INDEX_OF_THE_OPERATOR] or "=" in commandArguments[INDEX_OF_THE_OPERATOR]
                or ">" in commandArguments[INDEX_OF_THE_OPERATOR]):
            comparisonOperator = commandArguments[INDEX_OF_THE_OPERATOR]
            averageScoreToCompare = int(commandArguments[INDEX_OF_THE_AVERAGE_SCORE])
            intervalOfContestantsToRemove = (comparisonOperator, averageScoreToCompare)
            stackedHistoryOfListOfContestants = definedFunctions[str(commandName.lower())](intervalOfContestantsToRemove, stackedHistoryOfListOfContestants)
            print(f"Removed all contestants that have the average score {comparisonOperator} {averageScoreToCompare}")

        else:
            INDEX_OF_THE_KEYWORD_TO = 1
            INDEX_OF_THE_FIRST_POSITION_INDEX = 0
            INDEX_OF_THE_SECOND_POSITION_INDEX = 2
            if len(commandArguments) > MINIMUM_NUMBER_OF_COMMAND_ARGUMENTS and commandArguments[INDEX_OF_THE_KEYWORD_TO].lower() == "to":
                firstPositionIndex = int(commandArguments[INDEX_OF_THE_FIRST_POSITION_INDEX])
                secondPositionIndex = int(commandArguments[INDEX_OF_THE_SECOND_POSITION_INDEX])
            else:
                firstPositionIndex = int(commandArguments[INDEX_OF_THE_FIRST_POSITION_INDEX])
                secondPositionIndex = firstPositionIndex
            intervalOfContestantsToRemove = (firstPositionIndex, secondPositionIndex)
            stackedHistoryOfListOfContestants = definedFunctions[str(commandName.lower())](intervalOfContestantsToRemove, stackedHistoryOfListOfContestants)
            if firstPositionIndex == secondPositionIndex:
                print(f"Removed contestant {firstPositionIndex}")
            else:
                print(f"Removed contestants from {firstPositionIndex} to {secondPositionIndex}")
    except (ValueError, IndexError, functions.IndexOutOfListError) as e:
        if type(e) == functions.IndexOutOfListError:
            commandErrorHandler(commandName, constants.INSERT_REMOVE_INDEX_OUT_OF_BOUNDS_ERROR_CODE)
        else:
            commandErrorHandler(commandName, constants.INVALID_ARGUMENTS_ERROR_CODE)
    return stackedHistoryOfListOfContestants

def replace_command_CommandHandler(commandName: str, commandArguments: list, definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    ARGUMENT_INDEX_FOR_PARTICIPANT_NUMBER = 0
    ARGUMENT_INDEX_FOR_PROBLEM_NUMBER = 1
    ARGUMENT_INDEX_FOR_KEYWORD_WITH = 2
    ARGUMENT_INDEX_FOR_NEW_PROBLEM_SCORE = 3
    try:
        indexOfParticipant = int(commandArguments[ARGUMENT_INDEX_FOR_PARTICIPANT_NUMBER])
        problemNumber = str(commandArguments[ARGUMENT_INDEX_FOR_PROBLEM_NUMBER])
        if (commandArguments[ARGUMENT_INDEX_FOR_KEYWORD_WITH].lower() != "with"
                or (problemNumber.upper() != "P1" and problemNumber.upper() != "P2" and problemNumber.upper() != "P3")):
            raise ValueError
        newProblemScore = int(commandArguments[ARGUMENT_INDEX_FOR_NEW_PROBLEM_SCORE])
        stackedHistoryOfListOfContestants = definedFunctions[str(commandName.lower())](indexOfParticipant, problemNumber, newProblemScore, stackedHistoryOfListOfContestants)
        print(f"Changed the {problemNumber} problem score of contestant number {indexOfParticipant} to {newProblemScore}")
    except (ValueError, IndexError, functions.IndexOutOfListError) as e:
        if type(e) == functions.IndexOutOfListError:
            commandErrorHandler(commandName, constants.INSERT_REMOVE_INDEX_OUT_OF_BOUNDS_ERROR_CODE)
        else:
            commandErrorHandler(commandName, constants.INVALID_ARGUMENTS_ERROR_CODE)
    return stackedHistoryOfListOfContestants


def displayContestants(currentListOfContestants: list):
    FIRST_ELEMENT_OF_LIST = 0
    didItPrintAnyContestant = False
    textToPrint = "\n"
    lengthOfCurrentListOfContestants = len(currentListOfContestants)
    try:
        for contestantPosition in range(FIRST_ELEMENT_OF_LIST, lengthOfCurrentListOfContestants):
            contestantScores = currentListOfContestants[contestantPosition]
            firstScore = contestantScores[constants.INDEX_OF_FIRST_PROBLEM_SCORE]
            secondScore = contestantScores[constants.INDEX_OF_SECOND_PROBLEM_SCORE]
            thirdScore = contestantScores[constants.INDEX_OF_THIRD_PROBLEM_SCORE]
            contestantNumber = contestantScores[constants.INDEX_OF_CONTESTANT_POSITION]
            if (firstScore != constants.IMPOSSIBLE_SCORE
                    and secondScore != constants.IMPOSSIBLE_SCORE
                    and thirdScore != constants.IMPOSSIBLE_SCORE):
                textToPrint += f"Contestant {contestantNumber}'s scores: {firstScore}, {secondScore}, {thirdScore}\n"
                didItPrintAnyContestant = True
        if not didItPrintAnyContestant:
            textToPrint = "There is no contestant to display"
        print(textToPrint)
    except (ValueError, IndexError):
        commandName = "display"
        commandErrorHandler(commandName, constants.CANNOT_DISPLAY_BLANK_ERROR_CODE)


def list_command_CommandHandler(commandName: str, commandArguments: list, definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    LENGTH_OF_LIST_IF_NO_MORE_ARGUMENTS = 0

    currentListOfContestants = deepcopy(functions.getCurrentListOfContestants(stackedHistoryOfListOfContestants))
    try:
        ARGUMENT_INDEX_FOR_KEYWORD_SORTED = 0
        ARGUMENT_INDEX_FOR_OPERATOR = 0
        ARGUMENT_INDEX_FOR_AVERAGE_SCORE = 1
        if len(commandArguments) == LENGTH_OF_LIST_IF_NO_MORE_ARGUMENTS:
            listOfContestantsToPrint = deepcopy(currentListOfContestants)
            listOfContestantsToPrint = functions.rememberPositionsOfContestants(listOfContestantsToPrint)

            definedFunctions[commandName.lower()](listOfContestantsToPrint)
        elif commandArguments[ARGUMENT_INDEX_FOR_KEYWORD_SORTED].lower() == "sorted":
            listOfContestantsToPrint = deepcopy(currentListOfContestants)
            listOfContestantsToPrint = functions.rememberPositionsOfContestants(listOfContestantsToPrint)
            listOfContestantsToPrint = functions.getSortedListOfContestants(listOfContestantsToPrint, "AVERAGE")
            definedFunctions[commandName.lower()](listOfContestantsToPrint)
        elif ("<" in commandArguments[ARGUMENT_INDEX_FOR_OPERATOR]
              or "=" in commandArguments[ARGUMENT_INDEX_FOR_OPERATOR]
              or ">" in commandArguments[ARGUMENT_INDEX_FOR_OPERATOR]):
            comparisonOperator = commandArguments[ARGUMENT_INDEX_FOR_OPERATOR]
            averageScoreToCompare = int(commandArguments[ARGUMENT_INDEX_FOR_AVERAGE_SCORE])
            listOfContestantsToPrint = deepcopy(currentListOfContestants)
            listOfContestantsToPrint = functions.rememberPositionsOfContestants(listOfContestantsToPrint)
            listOfContestantsToPrint = functions.listOfContestantsWithAnAverageScoreOf(comparisonOperator, averageScoreToCompare, listOfContestantsToPrint)
            definedFunctions[commandName.lower()](listOfContestantsToPrint)
        else:
            raise ValueError
    except (ValueError, IndexError):
        commandErrorHandler(commandName, constants.INVALID_ARGUMENTS_ERROR_CODE)
    return stackedHistoryOfListOfContestants


def top_command_CommandHandler(commandName: str, commandArguments: list, definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    LENGTH_OF_LIST_IF_MORE_THAN_ONE_ARGUMENT = 1
    INDEX_OF_TOP_LENGTH = 0
    INDEX_OF_PROBLEM_NUMBER = 1
    currentListOfContestants = deepcopy(functions.getCurrentListOfContestants(stackedHistoryOfListOfContestants))
    listOfContestantsToPrint = []
    try:
        numberOfContestantsInTop = int(commandArguments[INDEX_OF_TOP_LENGTH])
        if len(commandArguments) > LENGTH_OF_LIST_IF_MORE_THAN_ONE_ARGUMENT:
            problemScoreKeyToRankBy = commandArguments[INDEX_OF_PROBLEM_NUMBER]
            if problemScoreKeyToRankBy.upper() != "P1" and problemScoreKeyToRankBy.upper() != "P2" and problemScoreKeyToRankBy.upper() != "P3":
                raise ValueError
        else:
            problemScoreKeyToRankBy = "AVERAGE"

        listOfContestantsToPrint = deepcopy(currentListOfContestants)
        listOfContestantsToPrint = functions.rememberPositionsOfContestants(listOfContestantsToPrint)
        listOfContestantsToPrint = functions.getSortedListOfContestants(listOfContestantsToPrint, problemScoreKeyToRankBy)
        listOfContestantsToPrint = listOfContestantsToPrint[:numberOfContestantsInTop]
        print(f"\nTOP {numberOfContestantsInTop} CONTESTANTS, ranked by {problemScoreKeyToRankBy.lower()}")
        displayContestants(listOfContestantsToPrint)
    except (ValueError, IndexError):
        commandErrorHandler(commandName, constants.INVALID_ARGUMENTS_ERROR_CODE)

    stackedHistoryOfListOfContestants = functions.addChangesToHistoryListOfContestants(stackedHistoryOfListOfContestants, currentListOfContestants)
    return stackedHistoryOfListOfContestants



def undo_command_CommandHandler(commandName: str, definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    try:
        stackedHistoryOfListOfContestants = definedFunctions[commandName.lower()](stackedHistoryOfListOfContestants)
        print("Undid last change")
    except IndexError:
        commandErrorHandler(commandName, constants.CANNOT_UNDO_ANYMORE_ERROR)
    return stackedHistoryOfListOfContestants


def generalCommandHandler(commandName: str, commandArguments: list, definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    if str(commandName.lower()) == "help":
        definedFunctions[commandName.lower()]()
    elif str(commandName.lower()) == "add":
        stackedHistoryOfListOfContestants = add_command_CommandHandler(commandName, commandArguments, definedFunctions, stackedHistoryOfListOfContestants)
    elif str(commandName.lower()) == "insert":
        stackedHistoryOfListOfContestants = insert_command_CommandHandler(commandName, commandArguments, definedFunctions, stackedHistoryOfListOfContestants)
    elif str(commandName.lower()) == "remove":
        stackedHistoryOfListOfContestants = remove_command_CommandHandler(commandName, commandArguments, definedFunctions, stackedHistoryOfListOfContestants)
    elif str(commandName.lower()) == "replace":
        stackedHistoryOfListOfContestants = replace_command_CommandHandler(commandName, commandArguments, definedFunctions, stackedHistoryOfListOfContestants)
    elif str(commandName.lower()) == "list":
        stackedHistoryOfListOfContestants = list_command_CommandHandler(commandName, commandArguments, definedFunctions, stackedHistoryOfListOfContestants)
    elif str(commandName.lower()) == "top":
        stackedHistoryOfListOfContestants = top_command_CommandHandler(commandName, commandArguments, definedFunctions, stackedHistoryOfListOfContestants)
    elif str(commandName.lower()) == "undo":
        stackedHistoryOfListOfContestants = undo_command_CommandHandler(commandName, definedFunctions, stackedHistoryOfListOfContestants)

# TERMINAL HANDLING

def commandErrorHandler(commandUsed: str, commandErrorCode: int):
    if commandErrorCode == constants.COMMAND_DOESNT_EXIST_ERROR_CODE:
        print(Fore.RED + f"The command {commandUsed} does not exist")
    elif commandErrorCode == constants.INVALID_ARGUMENTS_ERROR_CODE:
        print(Fore.RED + f"Invalid arguments for command {commandUsed}. Check \"help\" for the syntax")
    elif commandErrorCode == constants.INSERT_REMOVE_INDEX_OUT_OF_BOUNDS_ERROR_CODE:
        print(Fore.RED + f"Invalid index for command {commandUsed}. Use a position between 0 and the last position in the contestants list. Check \"help\" for the syntax")
    elif commandErrorCode == constants.CANNOT_DISPLAY_BLANK_ERROR_CODE:
        print(Fore.RED + f"Cannot display a blank list of contestants.")
    elif commandErrorCode == constants.CANNOT_UNDO_ANYMORE_ERROR:
        print(Fore.RED + f"Cannot undo anymore.")


def checkIfCommandExists(commandName: str, definedFunctions: dict):
    for definedCommand in definedFunctions.keys():
        if str(commandName.lower()) == str(definedCommand):
            return True
    return False


def parseInputCommand(command: str):
    INDEX_OF_COMMAND_NAME = 0
    INDEX_WHERE_COMMAND_ARGUMENTS_START = 1
    commandWordList = command.split(" ")
    commandName = commandWordList[INDEX_OF_COMMAND_NAME]
    commandArguments = commandWordList[INDEX_WHERE_COMMAND_ARGUMENTS_START:]
    return commandName, commandArguments

def startTerminal(definedFunctions: dict, stackedHistoryOfListOfContestants: list):
    init(autoreset=True)
    stillInTheMenu = True
    while stillInTheMenu:
        inputText = waitForInput()
        commandName, commandArguments = parseInputCommand(inputText)
        if not checkIfCommandExists(commandName, definedFunctions):
            commandErrorHandler(commandName, constants.COMMAND_DOESNT_EXIST_ERROR_CODE)
        else:
            generalCommandHandler(commandName, commandArguments, definedFunctions, stackedHistoryOfListOfContestants)


def waitForInput() -> str:
    inputText = str(input(Fore.GREEN + "> "))
    return inputText
