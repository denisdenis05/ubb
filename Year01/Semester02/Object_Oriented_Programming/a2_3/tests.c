
#include "tests.h"
#include <stdio.h>

void testAdd(CountryRepository* repository){
    int oldLengthOfRepo = getRepositoryDataLength(repository);

    char countryName[] = "test";
    char continentName[] = "Asia";

    addCountry(repository, countryName, continentName, 23, 0);

    assert(getRepositoryDataLength(repository) == oldLengthOfRepo + 1);
    assert(strcmp(getCountryName(getCountryPointerOnRepoPosition(repository, oldLengthOfRepo)), countryName) == 0);
    assert(strcmp(getContinentName(getCountryPointerOnRepoPosition(repository, oldLengthOfRepo)), continentName) == 0);
}

void testModify(CountryRepository* repository) {
    char oldName[] = "test";
    char newName[] = "test2";

    int lastELementInList = getRepositoryDataLength(repository) - 1;

    handleUpdateCountryName(repository, oldName, newName, 0);
    assert(strcmp(getCountryName(getCountryPointerOnRepoPosition(repository, lastELementInList)), newName) == 0);

}

void testRemove(CountryRepository* repository){
    char countryName[] = "test2";

    int oldLengthOfRepo = getRepositoryDataLength(repository);
    handleRemoveCountry(repository, countryName, 0);

    assert(getRepositoryDataLength(repository) == oldLengthOfRepo - 1);

}

void RunALlTests(CountryRepository* repository){
    testAdd(repository);
    testModify(repository);
    testRemove(repository);
}