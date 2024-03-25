#pragma once
#include <stdlib.h>
#include "domain.h"

typedef struct{
    Country* listOfCountries;
    int lengthOfRepository;
}DynamicArray;

typedef struct{
    DynamicArray** undoLists;
    int lengthOfUndoList;
    DynamicArray** redoLists;
    int lengthOfRedoList;
}UndoRedo;

typedef struct{
    DynamicArray* repositoryData;
    UndoRedo undoRedo;
}CountryRepository;

CountryRepository* CreateCountryRepository();
void AddCountryToRepository(CountryRepository* repository, Country country);
void RemoveCountryFromRepository(CountryRepository* repository, int positionOfCountry);
Country getCountryOnRepositoryPosition(CountryRepository* repository, int position);
Country* getCountryPointerOnRepoPosition(CountryRepository* repository, int position);
void setCountryOnPosition(CountryRepository* repository, int position, Country* country);
int getRepositoryDataLength(CountryRepository* repository);
void DestroyRepository(CountryRepository* repository);
DynamicArray* CopyDynamicArray(DynamicArray* dynamicArray);
void AddToUndo(CountryRepository* repository, DynamicArray* dynamicArray);
void Undo(CountryRepository* repository);
void RefreshRedo(CountryRepository* repository);
void Redo(CountryRepository* repository);