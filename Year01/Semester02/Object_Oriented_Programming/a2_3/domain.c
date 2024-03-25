#include "domain.h"


Country createCountry(char* name, char* continent, int populationInMillions){
    Country createdCountry;
    createdCountry.nameOfCountry = (char*) malloc(100 * sizeof(char));
    createdCountry.nameOfContinent = (char*) malloc(100 * sizeof(char));

    strcpy(createdCountry.nameOfContinent, continent);
    strcpy(createdCountry.nameOfCountry, name);
    createdCountry.populationInMillions = populationInMillions;
    return createdCountry;
}

Country copyCountry(Country countryToCopy){
    Country copyOfCountry = createCountry(countryToCopy.nameOfCountry, countryToCopy.nameOfContinent, countryToCopy.populationInMillions);
    return copyOfCountry;
}

void setCountryPopulation(Country* countryToUpdate, int newPopulation){
    countryToUpdate->populationInMillions = newPopulation;
}
void setCountryName(Country* countryToUpdate, char* newName){
    strcpy(countryToUpdate->nameOfCountry, newName);
}

void deleteCountry(Country* countryToDelete){
    free(countryToDelete->nameOfContinent);
    free(countryToDelete->nameOfCountry);
    countryToDelete->populationInMillions = 0;
}

char* getCountryName(Country* country){
    return country->nameOfCountry;
}
char* getContinentName(Country* country){
    return country->nameOfContinent;
}
int getCountryPopulation(Country* country){
    return country->populationInMillions;
}