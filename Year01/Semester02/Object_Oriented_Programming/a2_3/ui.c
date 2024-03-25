#include "ui.h"

void displayText(char* text)
{
    printf("%s", text);
}

void displayMessage(char* message)
{
    printf("%s\n", message);
}

void getRidOfNewline(){
    scanf("%*c");
}

int waitForIntegerInput()
{
    int input;
    scanf("%100d", &input);
    getRidOfNewline();
    return input;
}

char* waitForStringInput()
{
    char temporaryInput[101] = {0};
    scanf("%100[^\n]", temporaryInput);

    int lengthOfString = strlen(temporaryInput);
    char* input = (char*) malloc((lengthOfString+1) * sizeof(char));
    strcpy(input, temporaryInput);

    getRidOfNewline();
    return input;
}

char* waitForStringInputIgnoreNewLine()
{
    char temporaryInput[101] = {0};
    scanf("%100[^\n]", temporaryInput);

    int lengthOfString = strlen(temporaryInput);
    char* input = (char*) malloc((lengthOfString+1) * sizeof(char));
    strcpy(input, temporaryInput);
    return input;
}


void handleStatus(int statusOfOperation)
{
    if (statusOfOperation == 0){
        displayMessage("Success.\n");
    }
    else if (statusOfOperation == 1){
        displayMessage("Error, please insert a valid country name\n");
    }
    else if (statusOfOperation == 2){
        displayMessage("Error, please insert a valid continent name\n");
    }
    else if (statusOfOperation == 3){
        displayMessage("Error, no such option\n");
    }
    else if (statusOfOperation == 4)
    {
        displayMessage("Error, country already exists");
    }
    else if (statusOfOperation == 5)
    {
        displayMessage("Cannot undo.");
    }
    else if (statusOfOperation == 6)
    {
        displayMessage("Cannot redo.");
    }
}


void displayListOfCountries(char** listToPrint, int lengthOfListToPrint)
{
    if (lengthOfListToPrint == 0)
        printf("\n>> THERE IS NO COUNTRY TO DISPLAY <<\n");
    else
        printf("\n>> Countries <<\n");
    for (int i=0; i<lengthOfListToPrint; i++)
        displayMessage(listToPrint[i]);
}

void displayMenu()
{
    displayMessage("\nChoose an option:");
    displayMessage("1.Add a country");
    displayMessage("2.Remove a country");
    displayMessage("3.Update country");
    displayMessage("4.Display countries");
    displayMessage("5.Undo");
    displayMessage("6.Redo");
    displayMessage("7.Exit\n");

}

void displayFilterMenu()
{
    displayMessage(">> Choose an option:");
    displayMessage(">> 1.Filter by name");
    displayMessage(">> 2.Filter by population");
    displayMessage(">> 3.Filter by continent and population\n");
}

void displayPopulationFilterMenu()
{
    displayMessage(">>>> Choose an option:");
    displayMessage(">>>> 1.Get countries with a population equal or lower that X");
    displayMessage(">>>> 2.Get countries with a population equal or greater than X\n");
}

void displayUpdateMenu()
{
    displayMessage(">> Choose an option:");
    displayMessage(">> 1.Update the name of the country");
    displayMessage(">> 2.Update the population of the country");
    displayMessage(">> 3.Migrate the population of the country to another\n");
}


void handleAddCommand(CountryRepository* repository)
{
    displayMessage("What is the name of the country?\n");
    char* countryName = waitForStringInput();
    displayMessage("What is the name of the continent?\n");
    char* continentName = waitForStringInput();
    displayMessage("What is the population of the country (in millions)?\n");
    int population = waitForIntegerInput();

    int statusOfOperation = addCountry(repository, countryName, continentName, population, 1);
    handleStatus(statusOfOperation);

    free(countryName);
    free(continentName);
}

void handleDisplayCommand(CountryRepository* repository){
    displayFilterMenu();
    int filterOption = waitForIntegerInput();
    if (filterOption == 1)
    {
        displayMessage("Insert a string to filter countries by (leave empty if you want to see all countries)\n");
        char* countryName = waitForStringInputIgnoreNewLine();
        if (countryName[0] != '\n')
            getRidOfNewline();
        else
            countryName[0] = '\0';
        char** listToPrint = (char**) malloc (getRepositoryDataLength(repository) * sizeof(char*));
        int lengthOfListToPrint;
        searchAllCountriesByName(repository, &lengthOfListToPrint, listToPrint, countryName);
        displayListOfCountries(listToPrint, lengthOfListToPrint);

        free(countryName);
        for(int i=0; i<lengthOfListToPrint; i++)
            free(listToPrint[i]);
        free(listToPrint);
    }
    else if (filterOption == 2) {
        displayPopulationFilterMenu();
        int filterOption2 = waitForIntegerInput();
        if (filterOption2 < 1 || filterOption2 > 2)
            handleStatus(3);
        else {
            displayMessage("Insert the population to filter by\n");
            int population = waitForIntegerInput();
            char **listToPrint = (char **) malloc(getRepositoryDataLength(repository) * sizeof(char *));
            int lengthOfListToPrint;
            searchAllCountriesByPopulation(repository, &lengthOfListToPrint, listToPrint, population,
                                           filterOption2);
            displayListOfCountries(listToPrint, lengthOfListToPrint);

            for(int i=0; i<lengthOfListToPrint; i++)
                free(listToPrint[i]);
            free(listToPrint);
        }
    }
    else if (filterOption == 3) {
        displayMessage("Insert the name of the continent (valid continents: Europe, Asia, Africa, Australia, America)");
        char* continentName = waitForStringInputIgnoreNewLine();
        displayMessage("Insert the population to filter by (will take only countries greater than)\n");
        int population = waitForIntegerInput();
        displayMessage("Insert the sorting order\n1.Ascending\n2.Descending");
        int ascendingOrDescending = waitForIntegerInput();
        if (ascendingOrDescending >= 1 && ascendingOrDescending <= 2) {
            ascendingOrDescending = ascendingOrDescending - 1;
            char** listToPrint = (char**) malloc (getRepositoryDataLength(repository) * sizeof(char*));
            int lengthOfListToPrint = 0;
            handleDisplayCountriesByContinent(repository, continentName, population, listToPrint, &lengthOfListToPrint, ascendingOrDescending);

            displayListOfCountries(listToPrint, lengthOfListToPrint);
            for(int i=0; i<lengthOfListToPrint; i++)
                free(listToPrint[i]);
            free(listToPrint);
        }
        else
            handleStatus(3);

        free(continentName);
    }
    else
        handleStatus(3);
}

void handleUpdateCommand(CountryRepository* repository)
{
    displayUpdateMenu();
    int filterOption = waitForIntegerInput();
    if (filterOption == 1)
    {
        displayMessage("Insert the current name of the country: \n");
        char* countryName = waitForStringInput();
        displayMessage("Insert the new name for the country: \n");
        char* newName = waitForStringInput();
        int statusOfOperation = handleUpdateCountryName(repository, countryName, newName, 1);
        free(countryName);
        free(newName);
        handleStatus(statusOfOperation);
    }
    else if(filterOption == 2)
    {
        displayMessage("Insert the name of the country: \n");
        char* countryName = waitForStringInput();
        displayMessage("Insert the population increase/decrease in millions (example: -5): \n");
        int populationChange = waitForIntegerInput();
        int statusOfOperation = handleUpdateCountryPopulation(repository, countryName, populationChange, 1);
        free(countryName);
        handleStatus(statusOfOperation);
    }
    else if(filterOption == 3)
    {
        displayMessage("Insert the name of the country people migrate from: \n");
        char* countryName1 = waitForStringInput();
        displayMessage("Insert the name of the country people migrate to: \n");
        char* countryName2 = waitForStringInput();
        displayMessage("Insert the population that migrates in millions (positive numbers, sign won't matter) \n");
        int populationChange = waitForIntegerInput();
        int statusOfOperation = handleUpdateCountryMigration(repository, countryName1, countryName2, populationChange, 1);
        free(countryName1);
        free(countryName2);
        handleStatus(statusOfOperation);
    }
    else
        handleStatus(3);
}
void handleRemoveCommand(CountryRepository* repository)
{
    displayMessage("Insert the name of the country you want to remove\n");
    char* countryName = waitForStringInput();
    int statusOfOperation = handleRemoveCountry(repository, countryName, 1);
    free(countryName);
    handleStatus(statusOfOperation);

}

void handleUndoCommand(CountryRepository* repository){
    int statusOfOperation = executeUndo(repository);
    handleStatus(statusOfOperation);
}

void handleRedoCommand(CountryRepository* repository){
    int statusOfOperation = executeRedo(repository);
    handleStatus(statusOfOperation);
}


void startMenu(CountryRepository* repository) {
    int stillInTheMenu = 1;
    while (stillInTheMenu == 1) {
        displayMenu();
        int option = waitForIntegerInput();

        if(option == 1){
            handleAddCommand(repository);
        }
        else if(option == 2)
        {
            handleRemoveCommand(repository);
        }
        else if(option == 3)
        {
            handleUpdateCommand(repository);
        }
        else if(option == 4)
        {
            handleDisplayCommand(repository);
        }
        else if(option == 5)
        {
            handleUndoCommand(repository);
        }
        else if(option == 6)
        {
            handleRedoCommand(repository);
        }

        else if(option == 7) {
            DestroyRepository(repository);
            stillInTheMenu = 0;
        }
        else
            handleStatus(3);
    }
}