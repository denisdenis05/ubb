#pragma once

#include <string.h>
#include <stdlib.h>

typedef struct{
    char* nameOfCountry;
    char* nameOfContinent;
    int populationInMillions;
}Country;

Country createCountry(char* name, char* continent, int populationInMillions);
Country copyCountry(Country countryToCopy);
void setCountryPopulation(Country* countryToUpdate, int newPopulation);
void setCountryName(Country* countryToUpdate, char* newName);
void deleteCountry(Country* countryToDelete);

char* getCountryName(Country* country);
char* getContinentName(Country* country);
int getCountryPopulation(Country* country);
