#pragma once

#include "domain.h"
#include "repository.h"
#include <string.h>
#include <ctype.h>

int addCountry(CountryRepository* repository, char* countryName, char* continentName, int population, int shouldBackup);
void searchAllCountriesByName(CountryRepository* repository, int* lengthOfListToPrint, char** listToPrint, char* filterOption2);
void searchAllCountriesByPopulation(CountryRepository* repository, int* lengthOfListToPrint, char** listToPrint, int population, int filterOption);
int handleUpdateCountryPopulation(CountryRepository* repository, char* countryName, int populationChange, int shouldBackup);
int handleUpdateCountryMigration(CountryRepository* repository, char* countryName1, char* countryName2, int populationChange, int shouldBackup);
int handleUpdateCountryName(CountryRepository* repository, char* oldName, char* newName, int shouldBackup);
int handleRemoveCountry(CountryRepository* repository, char* countryName, int shouldBackup);
void handleDisplayCountriesByContinent(CountryRepository* repository, char* continentName, int population, char** listToPrint, int* lengthOfListToPrint, int ascendingOrDescending);
int executeUndo(CountryRepository* repository);
int executeRedo(CountryRepository* repository);
