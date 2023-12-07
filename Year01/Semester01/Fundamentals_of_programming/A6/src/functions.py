from copy import deepcopy
from random import randint
import constants

class IndexOutOfListError(Exception):
    pass

def checkIfValidValues(firstProblemScore: int, secondProblemScore: int, thirdProblemScore: int):
    if firstProblemScore < 0 or firstProblemScore > 10:
        raise ValueError
    if secondProblemScore < 0 or secondProblemScore > 10:
        raise ValueError
    if thirdProblemScore < 0 or thirdProblemScore > 10:
        raise ValueError

def listOfContestantsWithAnAverageScoreOf(comparisonOperator: str, averageScoreToCompare: int, currentListOfContestants: list):
    INDEX_OF_CONTESTANT_NUMBER = 0

    listOfNumbersOfContestants = findContestantsWithAnAverageScoreOf(comparisonOperator, averageScoreToCompare, currentListOfContestants)
    lengthOfCurrentListOfContestants = len(currentListOfContestants)
    modifiedListOfContestants = [[constants.IMPOSSIBLE_SCORE, constants.IMPOSSIBLE_SCORE, constants.IMPOSSIBLE_SCORE]] * lengthOfCurrentListOfContestants

    for contestantNumber in listOfNumbersOfContestants:
        contestantPosition = contestantNumber[INDEX_OF_CONTESTANT_NUMBER]
        modifiedListOfContestants[contestantPosition] = currentListOfContestants[contestantPosition]
    return modifiedListOfContestants


def averageScoreOfContestant(contestantNumber: int, listOfContestants: list):
    SCALE_OF_AVERAGE_SCORE = 10
    firstProblemScore = listOfContestants[contestantNumber][constants.INDEX_OF_FIRST_PROBLEM_SCORE] * SCALE_OF_AVERAGE_SCORE
    secondProblemScore = listOfContestants[contestantNumber][constants.INDEX_OF_SECOND_PROBLEM_SCORE] * SCALE_OF_AVERAGE_SCORE
    thirdProblemScore = listOfContestants[contestantNumber][constants.INDEX_OF_THIRD_PROBLEM_SCORE] * SCALE_OF_AVERAGE_SCORE
    averageProblemScore = int((firstProblemScore + secondProblemScore + thirdProblemScore) / 3)
    return averageProblemScore


def addContestantToList(firstProblemScore, secondProblemScore, thirdProblemScore,
                        stackedHistoryOfListOfContestants: list) -> list:
    currentListOfContestants = deepcopy(getCurrentListOfContestants(stackedHistoryOfListOfContestants))
    newContestantScores = [firstProblemScore, secondProblemScore, thirdProblemScore]
    currentListOfContestants.append(newContestantScores)
    stackedHistoryOfListOfContestants = addChangesToHistoryListOfContestants(stackedHistoryOfListOfContestants,
                                                                             currentListOfContestants)
    return stackedHistoryOfListOfContestants


def insertContestantInList(firstProblemScore: int, secondProblemScore: int, thirdProblemScore: int,
                           indexToInsertIn: int, stackedHistoryOfListOfContestants: list) -> list:
    currentListOfContestants = deepcopy(getCurrentListOfContestants(stackedHistoryOfListOfContestants))
    lengthOfCurrentListOfContestants = len(currentListOfContestants)
    if indexToInsertIn > lengthOfCurrentListOfContestants or indexToInsertIn < 0:
        raise IndexOutOfListError
    newContestantScores = [firstProblemScore, secondProblemScore, thirdProblemScore]
    firstPartOfTheCurrentListOfContestants = currentListOfContestants[:indexToInsertIn]
    lastPartOfTheCurrentListOfContestants = currentListOfContestants[indexToInsertIn:]

    firstPartOfTheCurrentListOfContestants.append(newContestantScores)
    currentListOfContestants = firstPartOfTheCurrentListOfContestants + lastPartOfTheCurrentListOfContestants
    stackedHistoryOfListOfContestants = addChangesToHistoryListOfContestants(stackedHistoryOfListOfContestants,
                                                                             currentListOfContestants)
    return stackedHistoryOfListOfContestants


def rememberPositionsOfContestants(listOfContestantsToPrint: list):
    FIRST_POSITION_IN_LIST = 0
    LENGTH_OF_LIST_IF_CONTESTANT_NUMBER_NOT_ASSIGNED = 3
    INDEX_OF_LIST_TO_PUT_CONTESTANT_NUMBER_IN = 3
    lengthOfListOfContestants = len(listOfContestantsToPrint)
    for contestantIndex in range(FIRST_POSITION_IN_LIST, lengthOfListOfContestants):
        if len(listOfContestantsToPrint[contestantIndex]) == LENGTH_OF_LIST_IF_CONTESTANT_NUMBER_NOT_ASSIGNED:
            listOfContestantsToPrint[contestantIndex].append(contestantIndex)
        else:
            listOfContestantsToPrint[contestantIndex][INDEX_OF_LIST_TO_PUT_CONTESTANT_NUMBER_IN] = contestantIndex
    return listOfContestantsToPrint


def findContestantsWithAnAverageScoreOf(operatorForCheckingAverageScore: str, numberToCompareTheAverageScore: int,
                                        currentListOfContestants: list) -> list:
    lengthOfCurrentListOfContestants = len(currentListOfContestants)
    FIRST_POSITION_IN_LIST = 0
    positionsOfContestants = []
    if str(operatorForCheckingAverageScore) == "<":
        for contestantNumber in range(FIRST_POSITION_IN_LIST, lengthOfCurrentListOfContestants):
            if averageScoreOfContestant(contestantNumber, currentListOfContestants) < numberToCompareTheAverageScore:
                positionsOfContestants = positionsOfContestants + [(contestantNumber, contestantNumber)]
    elif str(operatorForCheckingAverageScore) == "=":
        for contestantNumber in range(FIRST_POSITION_IN_LIST, lengthOfCurrentListOfContestants):
            if averageScoreOfContestant(contestantNumber, currentListOfContestants) == numberToCompareTheAverageScore:
                positionsOfContestants = positionsOfContestants + [(contestantNumber, contestantNumber)]
    elif str(operatorForCheckingAverageScore) == ">":
        for contestantNumber in range(FIRST_POSITION_IN_LIST, lengthOfCurrentListOfContestants):
            if averageScoreOfContestant(contestantNumber, currentListOfContestants) > numberToCompareTheAverageScore:
                positionsOfContestants = positionsOfContestants + [(contestantNumber, contestantNumber)]
    return positionsOfContestants


def removeContestantIntervalFromList(intervalOfContestantsToRemove: tuple, currentListOfContestants: list) -> list:
    MINIMUM_SCORE = 0
    INDEX_OF_FIRST_POSITION_TO_REMOVE = 0
    INDEX_OF_LAST_POSITION_TO_REMOVE = 1
    ADD_ONE_TO_NOT_EXCLUDE_LAST_LIST_ELEMENT = 1
    firstPositionIndex = intervalOfContestantsToRemove[INDEX_OF_FIRST_POSITION_TO_REMOVE]
    secondPositionIndex = intervalOfContestantsToRemove[INDEX_OF_LAST_POSITION_TO_REMOVE]

    lengthOfCurrentListOfContestants = len(currentListOfContestants)

    firstPartOfTheCurrentListOfContestants = currentListOfContestants[:firstPositionIndex]
    lastPartOfTheCurrentListOfContestants = currentListOfContestants[(secondPositionIndex + ADD_ONE_TO_NOT_EXCLUDE_LAST_LIST_ELEMENT):]
    currentListOfContestants = firstPartOfTheCurrentListOfContestants
    for contestantIndexThatNeedsToBeRemoved in range(firstPositionIndex, secondPositionIndex + ADD_ONE_TO_NOT_EXCLUDE_LAST_LIST_ELEMENT):
        currentListOfContestants += [[MINIMUM_SCORE, MINIMUM_SCORE, MINIMUM_SCORE, contestantIndexThatNeedsToBeRemoved]]
    currentListOfContestants += lastPartOfTheCurrentListOfContestants

    return currentListOfContestants


def removeContestantsFromList(intervalOfContestantsToRemove: tuple, stackedHistoryOfListOfContestants: list) -> list:
    INDEX_OF_FIRST_POSITION_TO_REMOVE = 0
    INDEX_OF_SECOND_POSITION_TO_REMOVE = 1

    currentListOfContestants = deepcopy(getCurrentListOfContestants(stackedHistoryOfListOfContestants))
    lengthOfCurrentListOfContestants = len(currentListOfContestants)
    if "<" in str(intervalOfContestantsToRemove[INDEX_OF_FIRST_POSITION_TO_REMOVE]) or "=" in str(
            intervalOfContestantsToRemove[INDEX_OF_FIRST_POSITION_TO_REMOVE]) or "<" in str(
            intervalOfContestantsToRemove[INDEX_OF_FIRST_POSITION_TO_REMOVE]):
        comparisonOperator = intervalOfContestantsToRemove[INDEX_OF_FIRST_POSITION_TO_REMOVE]
        averageScoreToCompare = intervalOfContestantsToRemove[INDEX_OF_SECOND_POSITION_TO_REMOVE]
        positionsOfContestantsThatNeedToBeRemoved = findContestantsWithAnAverageScoreOf(comparisonOperator,
                                                                                        averageScoreToCompare,
                                                                                        currentListOfContestants)
        for contestantPosition in positionsOfContestantsThatNeedToBeRemoved:
            currentListOfContestants = removeContestantIntervalFromList(contestantPosition, currentListOfContestants)
    else:
        firstPositionIndex = intervalOfContestantsToRemove[INDEX_OF_FIRST_POSITION_TO_REMOVE]
        secondPositionIndex = intervalOfContestantsToRemove[INDEX_OF_SECOND_POSITION_TO_REMOVE]
        if firstPositionIndex > secondPositionIndex:
            firstPositionIndex, secondPositionIndex = secondPositionIndex, firstPositionIndex
        if secondPositionIndex > lengthOfCurrentListOfContestants or firstPositionIndex < 0:
            raise IndexOutOfListError

        intervalOfContestantsToRemove = (firstPositionIndex, secondPositionIndex)
        currentListOfContestants = removeContestantIntervalFromList(intervalOfContestantsToRemove,
                                                                    currentListOfContestants)

    stackedHistoryOfListOfContestants = addChangesToHistoryListOfContestants(stackedHistoryOfListOfContestants,
                                                                             currentListOfContestants)
    return stackedHistoryOfListOfContestants


def replaceContestantsInList(indexOfParticipant: int, problemNumber: str, newProblemScore: int,
                             stackedHistoryOfListOfContestants: list) -> list:
    currentListOfContestants = deepcopy(getCurrentListOfContestants(stackedHistoryOfListOfContestants))
    lengthOfCurrentListOfContestants = len(currentListOfContestants)
    IMPOSSIBLE_INDEX_IN_LIST = 0

    if indexOfParticipant > lengthOfCurrentListOfContestants or indexOfParticipant < IMPOSSIBLE_INDEX_IN_LIST:
        raise IndexOutOfListError
    if problemNumber.upper() == "P1":
        currentListOfContestants[indexOfParticipant][constants.INDEX_OF_FIRST_PROBLEM_SCORE] = newProblemScore
    elif problemNumber.upper() == "P2":
        currentListOfContestants[indexOfParticipant][constants.INDEX_OF_SECOND_PROBLEM_SCORE] = newProblemScore
    elif problemNumber.upper() == "P3":
        currentListOfContestants[indexOfParticipant][constants.INDEX_OF_THIRD_PROBLEM_SCORE] = newProblemScore
    stackedHistoryOfListOfContestants = addChangesToHistoryListOfContestants(stackedHistoryOfListOfContestants,
                                                                             currentListOfContestants)
    return stackedHistoryOfListOfContestants


def getCurrentListOfContestants(stackedHistoryOfListOfContestants: list) -> list:
    LIST_IS_EMPTY_LENGTH = 0
    LAST_INDEX_IN_LIST = -1

    if len(stackedHistoryOfListOfContestants) == LIST_IS_EMPTY_LENGTH:
        emptyList = []
        return emptyList
    currentListOfContestants = stackedHistoryOfListOfContestants[LAST_INDEX_IN_LIST]
    return currentListOfContestants

def getSortedListOfContestants(currentListOfContestants: list, keyToSortBy: str) -> list:
    INDEX_OF_POSITION_IN_ENUMERATED_LIST = 0
    sortedDecreasingListOfContestants = []

    if keyToSortBy.upper() == "AVERAGE":
        enumeratedSortedDecreasingListOfContestants = sorted(enumerate(currentListOfContestants),
                                               key=lambda IndexOfElementAboutToSort: averageScoreOfContestant(IndexOfElementAboutToSort[INDEX_OF_POSITION_IN_ENUMERATED_LIST], currentListOfContestants),
                                                   reverse=True)

        for enumeratedElementInSortedList in enumeratedSortedDecreasingListOfContestants:
            contestantToAddToList = enumeratedElementInSortedList[INDEX_OF_POSITION_IN_ENUMERATED_LIST]
            sortedDecreasingListOfContestants.append(currentListOfContestants[contestantToAddToList])
    elif keyToSortBy.upper() == "P1":
        sortedDecreasingListOfContestants = sorted(currentListOfContestants,
                                                   key=lambda IndexOfElementAboutToSort: IndexOfElementAboutToSort[constants.INDEX_OF_FIRST_PROBLEM_SCORE], reverse = True)
    elif keyToSortBy.upper() == "P2":
        sortedDecreasingListOfContestants = sorted(currentListOfContestants,
                                                   key=lambda IndexOfElementAboutToSort: IndexOfElementAboutToSort[constants.INDEX_OF_SECOND_PROBLEM_SCORE], reverse = True)
    elif keyToSortBy.upper() == "P3":
        sortedDecreasingListOfContestants = sorted(currentListOfContestants,
                                                   key=lambda IndexOfElementAboutToSort: IndexOfElementAboutToSort[constants.INDEX_OF_THIRD_PROBLEM_SCORE], reverse = True)
    return sortedDecreasingListOfContestants

def removeLastChangesInListOfContestants(stackedHistoryOfListOfContestants: list) -> list:
    GO_ONE_POSITION_BEHIND = -1
    THE_FIRST_CHANGE_IN_HISTORY = 1
    lastIndexInHistoryOfListOfContestants = len(stackedHistoryOfListOfContestants) + GO_ONE_POSITION_BEHIND
    if lastIndexInHistoryOfListOfContestants < THE_FIRST_CHANGE_IN_HISTORY:
        raise IndexError
    stackedHistoryOfListOfContestants.pop(lastIndexInHistoryOfListOfContestants)
    return stackedHistoryOfListOfContestants


def addChangesToHistoryListOfContestants(stackedHistoryOfListOfContestants: list, currentListOfContestants: list) -> list:
    stackedHistoryOfListOfContestants.append(currentListOfContestants)
    return stackedHistoryOfListOfContestants

def generateRandomListOfContestants(currentListOfContestants: list, numberOfContestants: int) -> list:
    FIRST_CONTESTANT_NUMBER = 0
    LOWEST_SCORE_POSSIBLE = 0
    HIGHEST_SCORE_POSSIBLE = 10
    for contestantIndex in range(FIRST_CONTESTANT_NUMBER, numberOfContestants):
        scoreForProblem1 = randint(LOWEST_SCORE_POSSIBLE, HIGHEST_SCORE_POSSIBLE)
        scoreForProblem2 = randint(LOWEST_SCORE_POSSIBLE, HIGHEST_SCORE_POSSIBLE)
        scoreForProblem3 = randint(LOWEST_SCORE_POSSIBLE, HIGHEST_SCORE_POSSIBLE)
        listOfScores = [scoreForProblem1, scoreForProblem2, scoreForProblem3]
        currentListOfContestants.append(listOfScores)
    return currentListOfContestants

