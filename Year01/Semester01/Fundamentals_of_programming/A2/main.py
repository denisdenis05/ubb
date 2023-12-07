import random

def generateRandomList()->list:
    listLength=int(input("Insert the length of the list: "))
    generatedList=[]
    for position in range(0,listLength):
        generatedList.append(random.randint(0,101))
    return generatedList

def listSorterByExchange(listToSort:list, numberOfStepsToPrintAt:int)->list:
    listLength=len(listToSort)
    numberOfStepsWeAreCurrentlyAt=0
    for firstIndex in range(0,listLength-1):
        if numberOfStepsWeAreCurrentlyAt==0:
            print(f"\nThe list before sorting looks like\n{listToSort}\n")
        for secondIndex in range(firstIndex+1,listLength):
            if(int(listToSort[firstIndex])>int(listToSort[secondIndex])):
                almostUselessVariableThatRetainsOneListValueInOrderToSwapTheOther=listToSort[firstIndex]
                listToSort[firstIndex]=listToSort[secondIndex]
                listToSort[secondIndex]=almostUselessVariableThatRetainsOneListValueInOrderToSwapTheOther
                numberOfStepsWeAreCurrentlyAt+=1
                if numberOfStepsWeAreCurrentlyAt % numberOfStepsToPrintAt == 0:
                    print(f"The list at step {numberOfStepsWeAreCurrentlyAt} looks like\n{listToSort}")
    print(f"\nThe sorted list looks like\n{listToSort}\n")

def mergeTheSortedLists(listToMerge1:list, listToMerge2:list, shouldPrintAtCurrentStep:bool, currentStep:int)->list:
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
    if shouldPrintAtCurrentStep:
        print(f"Got back at step {currentStep} and merged the sublist")
        print(mergedList)
    elif currentStep==0:
        print(f"In the end the list looks like")
        print(mergedList)
    return mergedList


def listSorterByStrand(listToSort:list, numberOfStepsToPrintAt:int, currentStep:int)->list:

    shouldPrintAtCurrentStep=False
    if currentStep%numberOfStepsToPrintAt==0:
            if currentStep == 0:
                print(f"\nThe list before sorting looks like\n{listToSort}\n")
            else:
                shouldPrintAtCurrentStep=True

    if shouldPrintAtCurrentStep:
        print(f"At step {currentStep} we sort the following substring\n{listToSort}")

    if len(listToSort)<=1:
        if shouldPrintAtCurrentStep:
            print('\n')
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

    if shouldPrintAtCurrentStep:
        print(f"Split the original list into the sorted {kindaSortedList} and almost sorted {stillUnsortedList}\n")

    theRestOfTheListThatIsNowSorted=listSorterByStrand(stillUnsortedList,numberOfStepsToPrintAt,currentStep+1)

    finalSortedList=mergeTheSortedLists(kindaSortedList,theRestOfTheListThatIsNowSorted,shouldPrintAtCurrentStep, currentStep)

    return finalSortedList



def main():
    stillInTheMenu=True
    listToSort=[]
    while stillInTheMenu:
        print(
            "> Choose an option:\n1.Generate a list of n random natural numbers\n2.Sort the list using the exchange method\n3.Sort the list using the strand method\n4.Exit the program\n")
        selectedOption=int(input("> "))
        if selectedOption==1:
            listToSort=generateRandomList()
            print(listToSort)
        elif selectedOption==2:
            if len(listToSort)==0:
                print("\n!!! Generate a list first !!!\n")
            else:
                numberOfSteps=int(input("Insert the number of steps you'd like to get updates at: "))
                listSorterByExchange(listToSort,numberOfSteps)
        elif selectedOption==3:
            if len(listToSort)==0:
                print("!!! Generate a list first !!!")
            else:
                numberOfSteps = int(input("Insert the number of steps you'd like to get updates at: "))
                listSorterByStrand(listToSort,numberOfSteps,0)

        elif selectedOption == 4:
            stillInTheMenu = False
            print("Bye!")

main()