#include "services.h"
#include <stdio.h>


void backupHistoryToUndo(CountryRepository* repository){
    DynamicArray* copyOfCurrentList = CopyDynamicArray(repository->repositoryData);
    AddToUndo(repository, copyOfCurrentList);
    RefreshRedo(repository);
}


void transformToUppercase(char* text)
{
    for(int iterator=0; text[iterator]; iterator++)
        if(isalpha(text[iterator]))
            text[iterator] = toupper(text[iterator]);
}

char* checkIfSubstringInString(char* string, char* substring){
    char firstCountryName[101], secondCountryName[101];
    strcpy(firstCountryName, string);
    strcpy(secondCountryName, substring);

    transformToUppercase(firstCountryName);
    transformToUppercase(secondCountryName);

    return strstr(firstCountryName, secondCountryName);
}

int checkIfStringAreEqual(char* string1, char* string2){
    char firstCountryName[101], secondCountryName[101];
    strcpy(firstCountryName, string1);
    strcpy(secondCountryName, string2);

    transformToUppercase(firstCountryName);
    transformToUppercase(secondCountryName);

    return strcmp(firstCountryName, secondCountryName);
}

int checkIfCountryHasPopulationEqualOrLowerTo(Country* country, int population)
{
    if (getCountryPopulation(country) <= population)
        return 1;
    return 0;
}
int checkIfCountryHasPopulationEqualOrGreaterTo(Country* country, int population)
{
    if (getCountryPopulation(country) >= population)
        return 1;
    return 0;
}

int compareNames(char* firstName, char* secondName){
    char firstCountryName[101], secondCountryName[101];
    strcpy(firstCountryName, firstName);
    strcpy(secondCountryName, secondName);

    transformToUppercase(firstCountryName);
    transformToUppercase(secondCountryName);

    return strcmp(firstCountryName, secondCountryName);
}

int compareNamesBetweenCountries(Country* firstCountry, Country* secondCountry){
    return compareNames(getCountryName(firstCountry), getCountryName(secondCountry));
}

int compareNamesBetweenCountryAndText(Country* firstCountry, char* name){
    return compareNames(getCountryName(firstCountry), name);
}


char* checkIfSubstringInCountryName(Country* firstCountry, char* name){
    return checkIfSubstringInString(getCountryName(firstCountry), name);
}

int checkIfCountryNamesAreEqual(Country* firstCountry, char* name){
    return checkIfStringAreEqual(getCountryName(firstCountry), name);
}

int checkIfContinentIsValid(char* continentName){
    char listOfValidContinents[6][15];
    strcpy(listOfValidContinents[0], "Europe");
    strcpy(listOfValidContinents[1], "Asia");
    strcpy(listOfValidContinents[2], "Africa");
    strcpy(listOfValidContinents[3], "Australia");
    strcpy(listOfValidContinents[4], "America");

    for (int i=0; i<=4; i++)
        if (compareNames(listOfValidContinents[i], continentName) == 0)
            return 1;
    return 0;
}


void normalizeCountryName(char* countryName){
    if (countryName[0] >= 'a' && countryName[0] <= 'z')
        countryName[0] = toupper(countryName[0]);
    for (int i=1; countryName[i]; i++)
        if (countryName[i - 1] == ' ' && (countryName[i] >= 'a' && countryName[i] <= 'z'))
            countryName[i] = toupper(countryName[i]);
        else if (countryName[i - 1] != ' ' && countryName[i] >= 'A' && countryName[i] <= 'Z')
            countryName[i] = tolower(countryName[i]);
}

int searchCountryByName(CountryRepository* repository, char* countryName){
    for (int i=0; i < getRepositoryDataLength(repository); i++) {
        if (checkIfCountryNamesAreEqual(getCountryPointerOnRepoPosition(repository, i), countryName) == 0) {
            return i;
        }
    }
    return -1;
}

int addCountry(CountryRepository* repository, char* countryName, char* continentName, int population, int shouldBackup){
    if (searchCountryByName(repository, countryName) != -1)
        return 4;
    if (checkIfContinentIsValid(continentName) == 0)
        return 2;
    if (population < 0)
        population = population * (-1);
    normalizeCountryName(countryName);
    normalizeCountryName(continentName);
    Country countryToAdd = createCountry(countryName, continentName, population);

    if (shouldBackup == 1)
        backupHistoryToUndo(repository);

    AddCountryToRepository(repository, countryToAdd);
    return 0;
}

void searchAllCountriesByName(CountryRepository* repository, int* lengthOfListToPrint, char** listToPrint, char* countryName){
    *lengthOfListToPrint = 0;
    for (int i=0; i < getRepositoryDataLength(repository); i++) {
        if (checkIfSubstringInCountryName(getCountryPointerOnRepoPosition(repository, i), countryName) != NULL) {

            int lengthOfCountryName = strlen(getCountryName(getCountryPointerOnRepoPosition(repository, i)));
            int lengthOfContinentName = strlen(getCountryName(getCountryPointerOnRepoPosition(repository, i)));
            int maximumPopulationLength = 5;
            int spaceRequiredForSeparator = 2;
            int otherWordsLength = strlen("population: ");
            char* textToPrint = (char*) malloc ((lengthOfCountryName + lengthOfContinentName + otherWordsLength + maximumPopulationLength + 3*spaceRequiredForSeparator) * sizeof(char));

            sprintf(textToPrint, "%s; %s; population: %dM", getCountryName(
                            getCountryPointerOnRepoPosition(repository, i)),
                    getContinentName(getCountryPointerOnRepoPosition(repository, i)),
                    getCountryPopulation(getCountryPointerOnRepoPosition(repository, i)));

            listToPrint[*lengthOfListToPrint] = textToPrint;
            *lengthOfListToPrint = *lengthOfListToPrint + 1;
        }
    }
}


void searchAllCountriesByPopulation(CountryRepository* repository, int* lengthOfListToPrint, char** listToPrint, int population, int filterOption)
{
    int equalOrLowerOption = 1, equalOrGreaterOption = 2;
    *lengthOfListToPrint = 0;
    for (int i=0; i < getRepositoryDataLength(repository); i++) {
        int shouldDisplayCountry = 0;
        if (filterOption == equalOrLowerOption && checkIfCountryHasPopulationEqualOrLowerTo(
                getCountryPointerOnRepoPosition(repository, i), population))
            shouldDisplayCountry = 1;
        else if (filterOption == equalOrGreaterOption && checkIfCountryHasPopulationEqualOrGreaterTo(
                getCountryPointerOnRepoPosition(repository, i), population))
            shouldDisplayCountry = 1;
        if (shouldDisplayCountry)
        {
            int lengthOfCountryName = strlen(getCountryName(getCountryPointerOnRepoPosition(repository, i)));
            int lengthOfContinentName = strlen(getContinentName(getCountryPointerOnRepoPosition(repository, i)));
            int maximumPopulationLength = 5;
            int spaceRequiredForSeparator = 2;
            int otherWordsLength = strlen("population: ");
            char* textToPrint = (char*) malloc ((lengthOfCountryName + lengthOfContinentName + otherWordsLength + maximumPopulationLength + 3*spaceRequiredForSeparator) * sizeof(char));

            sprintf(textToPrint, "%s; %s; population: %dM",
                    getCountryName(getCountryPointerOnRepoPosition(repository, i)),
                    getContinentName(getCountryPointerOnRepoPosition(repository, i)),
                    getCountryPopulation(getCountryPointerOnRepoPosition(repository, i)));

            listToPrint[*lengthOfListToPrint] = textToPrint;
            *lengthOfListToPrint = *lengthOfListToPrint + 1;
        }
    }
}


int executeUndo(CountryRepository* repository){
    if (repository->undoRedo.lengthOfUndoList == 0)
        return 5;
    Undo(repository);
    return 0;
}

int executeRedo(CountryRepository* repository){
    if (repository->undoRedo.lengthOfRedoList == 0)
        return 6;
    Redo(repository);
    return 0;
}


int checkIfPopulationDecreaseIsPossible(CountryRepository* repository, int positionOfCountry, int populationChange){
    Country* countryToUpdate = getCountryPointerOnRepoPosition(repository, positionOfCountry);
    if (getCountryPopulation(countryToUpdate) < populationChange * (-1))
        return getCountryPopulation(countryToUpdate);
    return populationChange;

}

int checkMaximumPopulationDecrease(CountryRepository* repository, int positionOfCountry)
{
    Country* countryToCheck = getCountryPointerOnRepoPosition(repository, positionOfCountry);
    return (-1) * getCountryPopulation(countryToCheck);
}

void updateCountryPopulation(CountryRepository* repository, int positionOfCountry, int populationChange)
{
    Country* countryToUpdate = getCountryPointerOnRepoPosition(repository, positionOfCountry);

    int newPopulation = getCountryPopulation(countryToUpdate) + populationChange;

    setCountryPopulation(countryToUpdate, newPopulation);
}

void updateCountryName(CountryRepository* repository, int positionOfCountry, char* newName, int shouldBackup)
{
    Country* countryToUpdate = getCountryPointerOnRepoPosition(repository, positionOfCountry);

    if (shouldBackup == 1)
        backupHistoryToUndo(repository);


    setCountryName(countryToUpdate, newName);
}

int handleUpdateCountryName(CountryRepository* repository, char* oldName, char* newName, int shouldBackup)
{
    int positionOfCountry = searchCountryByName(repository, oldName);
    if (positionOfCountry == -1)
        return 1;
    normalizeCountryName(newName);
    updateCountryName(repository, positionOfCountry, newName, shouldBackup);

    return 0;
}

int handleUpdateCountryPopulation(CountryRepository* repository, char* countryName, int populationChange, int shouldBackup)
{
    int positionOfCountry = searchCountryByName(repository, countryName);
    if (positionOfCountry == -1)
        return 1;
    if (populationChange < 0) {
        int maximumPopulationDecrease = checkMaximumPopulationDecrease(repository, positionOfCountry);
        if (populationChange < maximumPopulationDecrease)
            populationChange = maximumPopulationDecrease;
    }

    if (shouldBackup == 1)
        backupHistoryToUndo(repository);


    updateCountryPopulation(repository, positionOfCountry, populationChange);

    return 0;
}

int handleUpdateCountryMigration(CountryRepository* repository, char* countryName1, char* countryName2, int populationChange, int shouldBackup)
{
    int positionOfCountry1 = searchCountryByName(repository, countryName1);
    int positionOfCountry2 = searchCountryByName(repository, countryName2);
    if (positionOfCountry1 == -1 || positionOfCountry2 == -1)
        return 1;

    if (populationChange < 0)
        populationChange = populationChange * (-1);

    int maximumPopulationDecrease = (-1) * checkMaximumPopulationDecrease(repository, positionOfCountry1);
    if (populationChange > maximumPopulationDecrease)
        populationChange = maximumPopulationDecrease;


    if (shouldBackup == 1)
        backupHistoryToUndo(repository);

    updateCountryPopulation(repository, positionOfCountry1, populationChange * (-1));
    updateCountryPopulation(repository, positionOfCountry2, populationChange);

    return 0;
}

int handleRemoveCountry(CountryRepository* repository, char* countryName, int shouldBackup)
{
    int positionOfCountry = searchCountryByName(repository, countryName);
    if (positionOfCountry == -1)
        return 1;

    if (shouldBackup == 1)
        backupHistoryToUndo(repository);


    deleteCountry(getCountryPointerOnRepoPosition(repository, positionOfCountry));
    RemoveCountryFromRepository(repository, positionOfCountry);

    return 0;
}


void partiallySortByPopulation(CountryRepository* repository, int* listOfCountriesToSort, int numberOfElementsToSort, int ascendingOrDescending){
    int isListSorted = 0;
    while (isListSorted == 0) {
        isListSorted = 1;
        for (int i = 0; i < numberOfElementsToSort - 1; i++) {
            int currentPosition = listOfCountriesToSort[i];
            int nextPosition = listOfCountriesToSort[i + 1];
            int firstCountryPopulation = getCountryPopulation(
                    getCountryPointerOnRepoPosition(repository, currentPosition));
            int secondCountryPopulation = getCountryPopulation(getCountryPointerOnRepoPosition(repository, nextPosition));
            if (ascendingOrDescending == 0 && firstCountryPopulation > secondCountryPopulation)
            {
                listOfCountriesToSort[i] = nextPosition;
                listOfCountriesToSort[i + 1] = currentPosition;
                isListSorted = 0;
            }
            else if(ascendingOrDescending == 1 && firstCountryPopulation < secondCountryPopulation)
            {
                listOfCountriesToSort[i] = nextPosition;
                listOfCountriesToSort[i + 1] = currentPosition;
                isListSorted = 0;
            }
        }
    }
}

void findAllCountriesInAContinentOverAPopulation(CountryRepository* repository, char* continentName, int population, int* listOfCountries, int* lengthOfList)
{
    *lengthOfList = 0;
    for (int i=0; i < getRepositoryDataLength(repository); i++) {
        if (continentName[0] == '\0' || checkIfStringAreEqual(getContinentName(
                getCountryPointerOnRepoPosition(repository, i)), continentName) == 0){
            if(getCountryPopulation(getCountryPointerOnRepoPosition(repository, i)) >= population) {
                listOfCountries[*lengthOfList] = i;
                *lengthOfList = *lengthOfList + 1;
            }
        }
    }
}


void handleDisplayCountriesByContinent(CountryRepository* repository, char* continentName, int population, char** listToPrint, int* lengthOfListToPrint, int ascendingOrDescending)
{
    int* listOfCountries = (int*) malloc (getRepositoryDataLength(repository) * sizeof (int));
    *lengthOfListToPrint = 0;
    int lengthOfList = 0;
    findAllCountriesInAContinentOverAPopulation(repository, continentName, population, listOfCountries, &lengthOfList);
    printf("Length of list %d", lengthOfList);
    partiallySortByPopulation(repository, listOfCountries, lengthOfList, ascendingOrDescending);
    for (int i=0; i< lengthOfList; i++)
    {
        printf("%d", listOfCountries[i]);
        int countryPosition = listOfCountries[i];
        int lengthOfCountryName = strlen(getCountryName(getCountryPointerOnRepoPosition(repository, countryPosition)));
        int lengthOfContinentName = strlen(getCountryName(getCountryPointerOnRepoPosition(repository, countryPosition)));
        int maximumPopulationLength = 5;
        int spaceRequiredForSeparator = 2;
        int otherWordsLength = strlen("population: ");
        char* textToPrint = (char*) malloc ((lengthOfCountryName + lengthOfContinentName + otherWordsLength + maximumPopulationLength + 3*spaceRequiredForSeparator) * sizeof(char));

        sprintf(textToPrint, "%s; %s; population: %dM",
                getCountryName(getCountryPointerOnRepoPosition(repository, countryPosition)),
                getContinentName(getCountryPointerOnRepoPosition(repository, countryPosition)),
                getCountryPopulation(getCountryPointerOnRepoPosition(repository, countryPosition)));
        listToPrint[*lengthOfListToPrint] = textToPrint;
        *lengthOfListToPrint = *lengthOfListToPrint + 1;
    }
    free(listOfCountries);
}