import random
import time
import sys
sys.setrecursionlimit(30000000)
def generateRandomList(listLength)->list:
    generatedList=[]
    for position in range(0,listLength):
        generatedList.append(random.randint(0,101))
    return generatedList

def listSorterByExchange(listToSort:list)->list:
    listLength=len(listToSort)
    for firstIndex in range(0,listLength-1):
        for secondIndex in range(firstIndex+1,listLength):
            if(int(listToSort[firstIndex])>int(listToSort[secondIndex])):
                almostUselessVariableThatRetainsOneListValueInOrderToSwapTheOther=listToSort[firstIndex]
                listToSort[firstIndex]=listToSort[secondIndex]
                listToSort[secondIndex]=almostUselessVariableThatRetainsOneListValueInOrderToSwapTheOther


def mergeTheSortedLists(listToMerge1:list, listToMerge2:list)->list:
    mergedList=[]
    indexForList1=0
    indexForList2=0
    while indexForList1<len(listToMerge1) and indexForList2<len(listToMerge2):
        if listToMerge1[indexForList1]<listToMerge2[indexForList2]:
            mergedList.append(listToMerge1[indexForList1])
            indexForList1+=1
        else:
            mergedList.append(listToMerge2[indexForList2])
            indexForList2 += 1
    while indexForList1<len(listToMerge1):
        mergedList.append(listToMerge1[indexForList1])
        indexForList1 += 1
    while indexForList2<len(listToMerge2):
        mergedList.append(listToMerge2[indexForList2])
        indexForList2 += 1
    return mergedList
def listSorterByStrand(listToSort:list)->list:

    if len(listToSort)<=1:
        return listToSort

    kindaSortedList=[]
    kindaSortedList.append(listToSort[0])
    stillUnsortedList=listToSort[1:]

    i=0
    while i<len(stillUnsortedList):
        if kindaSortedList[-1] <= stillUnsortedList[i]:
            kindaSortedList.append(stillUnsortedList[i])
            stillUnsortedList.pop(i)
            i-=1
        i+=1

    theRestOfTheListThatIsNowSorted=listSorterByStrand(stillUnsortedList)

    finalSortedList=mergeTheSortedLists(kindaSortedList,theRestOfTheListThatIsNowSorted)

    return finalSortedList

def generateListInReverseOrder(listLength:int)->list:
    generatedList=[]
    firstElementOfTheList=listLength
    generatedList.append(firstElementOfTheList)
    for generatedListIndex in range(1, listLength):
        generatedListElement=generatedList[generatedListIndex-1]-1
        generatedList.append(generatedListElement)
    return generatedList

def generateListInOrder(listLength:int)->list:
    generatedList=[]
    firstElementOfTheList=1
    generatedList.append(firstElementOfTheList)
    for generatedListIndex in range(1, listLength):
        generatedListElement=generatedList[generatedListIndex-1]+1
        generatedList.append(generatedListElement)
    return generatedList


def sortingAlgorithmsRuntimeCounter(listOfElementsToSort:dict, sortingAlgorithmType):
    for listLengthKey in listOfElementsToSort.keys():

        SortStartingTime=time.time()

        sortingAlgorithmType(listOfElementsToSort[listLengthKey])

        SortEndingTime=time.time()
        timeItTookToSort=SortEndingTime-SortStartingTime

        print(f"For a list of {listLengthKey} elements, it took {timeItTookToSort} seconds for {sortingAlgorithmType.__name__} sort")


def calculateWorstCase(sortingAlgorithmType):
    listOfElementsToSort={}
    listOfElementsToSort["100"] = generateListInReverseOrder(100)
    listOfElementsToSort["500"] = generateListInReverseOrder(500)
    listOfElementsToSort["1000"] = generateListInReverseOrder(1000)
    listOfElementsToSort["2000"] = generateListInReverseOrder(2000)
    listOfElementsToSort["3000"] = generateListInReverseOrder(3000)

    print(f"CHECKING WORST CASE SCENARIO FOR {sortingAlgorithmType} SORT")

    sortingAlgorithmsRuntimeCounter(listOfElementsToSort, sortingAlgorithmType)


def calculateBestCase(sortingAlgorithmType):
    listOfElementsToSort={}
    listOfElementsToSort["100"] = generateListInOrder(100)
    listOfElementsToSort["500"] = generateListInOrder(500)
    listOfElementsToSort["1000"] = generateListInOrder(1000)
    listOfElementsToSort["2000"] = generateListInOrder(2000)
    listOfElementsToSort["3000"] = generateListInOrder(3000)

    print(f"CHECKING BEST CASE SCENARIO FOR {sortingAlgorithmType} SORT")

    sortingAlgorithmsRuntimeCounter(listOfElementsToSort, sortingAlgorithmType)


def isTheListSorted(theListThatWeCheckIfSorted):
    for elementIndexOfTheList in range(1,len(theListThatWeCheckIfSorted)):
        if theListThatWeCheckIfSorted[elementIndexOfTheList-1]>theListThatWeCheckIfSorted[elementIndexOfTheList]:
            return False
    return True

def calculateAverageCase(sortingAlgorithmType):
    listOfElementsToSort={}
    listOfElementsToSort["100"] = generateRandomList(100)
    while isTheListSorted(listOfElementsToSort["100"]):
        listOfElementsToSort["100"] = generateRandomList(100)
    listOfElementsToSort["500"] = generateRandomList(500)
    while isTheListSorted(listOfElementsToSort["500"]):
        listOfElementsToSort["500"] = generateRandomList(500)
    listOfElementsToSort["1000"] = generateRandomList(1000)
    while isTheListSorted(listOfElementsToSort["1000"]):
        listOfElementsToSort["1000"] = generateRandomList(1000)
    listOfElementsToSort["2000"] = generateRandomList(2000)
    while isTheListSorted(listOfElementsToSort["2000"]):
        listOfElementsToSort["2000"] = generateRandomList(2000)
    listOfElementsToSort["3000"] = generateRandomList(3000)
    while isTheListSorted(listOfElementsToSort["3000"]):
        listOfElementsToSort["3000"] = generateRandomList(3000)

    print(f"CHECKING AVERAGE CASE SCENARIO FOR {sortingAlgorithmType} SORT")

    sortingAlgorithmsRuntimeCounter(listOfElementsToSort,sortingAlgorithmType)


def main():
    stillInTheMenu = True
    listToSort = []
    while stillInTheMenu:
        print(
            "> Choose an option:\n1.Generate a list of n random natural numbers\n2.Sort the list using the exchange method\n3.Sort the list using the strand method\n4.Calculate the worst case scenario for exchange sort\n5.Calculate the worst case scenario for strand sort\n6.Calculate the average case for exchange sort\n7.Calculate the average case for strand sort\n8.Calculate the best case for exchange sort\n9.Calculate the best case for strand sort\n10.Exit the program\n")
        selectedOption = int(input("> "))
        if selectedOption == 1:
            listLength = int(input("Insert the length of the list: "))
            listToSort = generateRandomList(listLength)
            print(listToSort)
        elif selectedOption == 2:
            if len(listToSort) == 0:
                print("\n!!! Generate a list first !!!\n")
            else:
                listSorterByExchange(listToSort)
        elif selectedOption == 3:
            if len(listToSort) == 0:
                print("!!! Generate a list first !!!")
            else:
                listSorterByStrand(listToSort)

        elif selectedOption == 4:
            calculateWorstCase(listSorterByExchange)

        elif selectedOption == 5:
            calculateWorstCase(listSorterByStrand)

        elif selectedOption == 6:
            calculateAverageCase(listSorterByExchange)

        elif selectedOption == 7:
            calculateAverageCase(listSorterByStrand)

        elif selectedOption == 8:
            calculateBestCase(listSorterByExchange)

        elif selectedOption == 9:
            calculateBestCase(listSorterByStrand)

        elif selectedOption == 7:
            stillInTheMenu = False
            print("Bye!")

main()