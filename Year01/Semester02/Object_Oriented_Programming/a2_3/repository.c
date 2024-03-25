#include "repository.h"
#include <stdio.h>

void initializeUndoRedo(CountryRepository* repository){
    repository->undoRedo.undoLists = (DynamicArray**) malloc(1 * sizeof(DynamicArray*));
    repository->undoRedo.redoLists = (DynamicArray**) malloc(1 * sizeof(DynamicArray*));
    repository->undoRedo.lengthOfRedoList = 0;
    repository->undoRedo.lengthOfUndoList = 0;
}

CountryRepository* CreateCountryRepository()
{
    CountryRepository* repository = (CountryRepository *) malloc( 1 * sizeof(CountryRepository));
    repository->repositoryData = (DynamicArray*) malloc(1 * sizeof(DynamicArray));
    repository->repositoryData->listOfCountries = (Country *) malloc(1 * sizeof(Country));
    repository->repositoryData->lengthOfRepository = 0;
    initializeUndoRedo(repository);
    return repository;
}

int getDynamicArrayLength(DynamicArray* dynamicArray) {
    return dynamicArray->lengthOfRepository;
}
int getRepositoryDataLength(CountryRepository* repository) {
    getDynamicArrayLength(repository->repositoryData);
}

Country getCountryOnDynamicArrayPosition(DynamicArray* dynamicArray, int position)
{
    return dynamicArray->listOfCountries[position];
}
Country getCountryOnRepositoryPosition(CountryRepository* repository, int position)
{
    return getCountryOnDynamicArrayPosition(repository->repositoryData, position);
}


Country* getCountryPointerOnDynamicArrayPosition(DynamicArray* dynamicArray, int position)
{
    return &(dynamicArray->listOfCountries[position]);
}
Country* getCountryPointerOnRepoPosition(CountryRepository* repository, int position)
{
    return getCountryPointerOnDynamicArrayPosition(repository->repositoryData, position);
}


void setCountryOnPositionInDynamicArray(DynamicArray* dynamicArray, int position, Country* country)
{
    dynamicArray->listOfCountries[position] = *country;
}
void setCountryOnPosition(CountryRepository* repository, int position, Country* country)
{
    setCountryOnPositionInDynamicArray(repository->repositoryData, position, country);
}


void AddCountryToDynamicArray(DynamicArray* dynamicArray, Country country) {
    dynamicArray->listOfCountries = (Country*) realloc(dynamicArray->listOfCountries, (dynamicArray->lengthOfRepository + 2) * sizeof(Country));
    dynamicArray->listOfCountries[dynamicArray->lengthOfRepository] = country;
    dynamicArray->lengthOfRepository = dynamicArray->lengthOfRepository + 1;
}
void AddCountryToRepository(CountryRepository* repository, Country country) {
    AddCountryToDynamicArray(repository->repositoryData, country);
}


void RemoveCountryFromDynamicArray(DynamicArray* dynamicArray, int positionOfCountry)
{
    memmove(dynamicArray->listOfCountries + positionOfCountry, dynamicArray->listOfCountries + positionOfCountry + 1, (dynamicArray->lengthOfRepository - positionOfCountry - 1) * sizeof(Country));
    dynamicArray->lengthOfRepository = dynamicArray->lengthOfRepository - 1;
}

void RemoveCountryFromRepository(CountryRepository* repository, int positionOfCountry)
{
    RemoveCountryFromDynamicArray(repository->repositoryData, positionOfCountry);
}
void RemoveDynamicArrayFromDynamicArray(DynamicArray** dynamicArray, int* lengthOfDynamicArray, int positionOfCountry)
{
    if (dynamicArray[positionOfCountry] == NULL)
        return;
    memmove(dynamicArray + positionOfCountry, dynamicArray + positionOfCountry + 1, (*lengthOfDynamicArray - positionOfCountry - 1) * sizeof(Country));
    *lengthOfDynamicArray = *lengthOfDynamicArray - 1;
}


void DestroyDynamicArray(DynamicArray* dynamicArray){
    while(dynamicArray->lengthOfRepository > 0)
    {
        deleteCountry(getCountryPointerOnDynamicArrayPosition(dynamicArray, 0));
        RemoveCountryFromDynamicArray(dynamicArray, 0);
    }
    free(dynamicArray->listOfCountries);
    free(dynamicArray);
}


void DestroyUndoRedo(UndoRedo* undoRedo){
    while(undoRedo->lengthOfUndoList > 0)
    {
        DestroyDynamicArray(undoRedo->undoLists[0]);
        RemoveDynamicArrayFromDynamicArray(undoRedo->undoLists, &undoRedo->lengthOfUndoList, 0);
    }
    while(undoRedo->lengthOfRedoList > 0)
    {
        DestroyDynamicArray(undoRedo->redoLists[0]);
        RemoveDynamicArrayFromDynamicArray(undoRedo->redoLists, &undoRedo->lengthOfRedoList, 0);
    }
    free(undoRedo->undoLists);
    free(undoRedo->redoLists);
}

void DestroyRepository(CountryRepository* repository){
    DestroyDynamicArray(repository->repositoryData);
    DestroyUndoRedo(&(repository->undoRedo));

    free(repository);
}

DynamicArray* CopyDynamicArray(DynamicArray* dynamicArray)
{
    int sizeOfDynamicArray = getDynamicArrayLength(dynamicArray);
    DynamicArray* copyOfDynamicArray = (DynamicArray*) malloc(1*sizeof(DynamicArray));
    copyOfDynamicArray->listOfCountries = (Country *) malloc((sizeOfDynamicArray + 1) * sizeof(Country));
    int lengthOfNewDynamicArray = 0;
    for (lengthOfNewDynamicArray=0; lengthOfNewDynamicArray<sizeOfDynamicArray; lengthOfNewDynamicArray++)
    {
        copyOfDynamicArray->listOfCountries[lengthOfNewDynamicArray] = copyCountry(getCountryOnDynamicArrayPosition(dynamicArray, lengthOfNewDynamicArray));
    }
    copyOfDynamicArray->lengthOfRepository = lengthOfNewDynamicArray;
    return copyOfDynamicArray;
}

void AddToUndo(CountryRepository* repository, DynamicArray* dynamicArray)
{
    UndoRedo* undoRedo = &repository->undoRedo;
    undoRedo->undoLists = (DynamicArray **) realloc(undoRedo->undoLists, (undoRedo->lengthOfUndoList + 2) * sizeof(DynamicArray*));
    undoRedo->undoLists[undoRedo->lengthOfUndoList] = dynamicArray;
    undoRedo->lengthOfUndoList = undoRedo->lengthOfUndoList + 1;
}

void AddToRedo(CountryRepository* repository, DynamicArray* dynamicArray)
{
    UndoRedo* undoRedo = &repository->undoRedo;
    undoRedo->redoLists = (DynamicArray **) realloc(undoRedo->redoLists, (undoRedo->lengthOfRedoList + 2) * sizeof(DynamicArray*));
    undoRedo->redoLists[undoRedo->lengthOfRedoList] = dynamicArray;
    undoRedo->lengthOfRedoList = undoRedo->lengthOfRedoList + 1;
}

void ShrinkUndo(CountryRepository* repository)
{
    UndoRedo* undoRedo = &repository->undoRedo;
    undoRedo->undoLists = (DynamicArray **) realloc(undoRedo->undoLists, (undoRedo->lengthOfUndoList) * sizeof(DynamicArray*));
    undoRedo->lengthOfUndoList = undoRedo->lengthOfUndoList - 1;
}
void ShrinkRedo(CountryRepository* repository)
{
    UndoRedo* undoRedo = &repository->undoRedo;
    undoRedo->redoLists = (DynamicArray **) realloc(undoRedo->redoLists, (undoRedo->lengthOfRedoList) * sizeof(DynamicArray*));
    undoRedo->lengthOfRedoList = undoRedo->lengthOfRedoList - 1;
}

DynamicArray* getLatestUndo(CountryRepository* repository)
{
    int latestPosition = repository->undoRedo.lengthOfUndoList;
    ShrinkUndo(repository);
    return repository->undoRedo.undoLists[latestPosition-1];
}

DynamicArray* getLatestRedo(CountryRepository* repository)
{
    int latestPosition = repository->undoRedo.lengthOfRedoList;
    ShrinkRedo(repository);
    return repository->undoRedo.redoLists[latestPosition-1];
}

void Undo(CountryRepository* repository){
    DynamicArray* currentList = repository->repositoryData;
    AddToRedo(repository, currentList);
    DynamicArray* updatedCurrentList = getLatestUndo(repository);
    repository->repositoryData = updatedCurrentList;
}

void Redo(CountryRepository* repository){
    DynamicArray* currentList = repository->repositoryData;
    AddToUndo(repository, currentList);
    DynamicArray* updatedCurrentList = getLatestRedo(repository);
    repository->repositoryData = updatedCurrentList;
}

void RefreshRedo(CountryRepository* repository){
    while(repository->undoRedo.lengthOfRedoList > 0)
    {
        DestroyDynamicArray(repository->undoRedo.redoLists[0]);
        RemoveDynamicArrayFromDynamicArray(repository->undoRedo.redoLists, &(repository->undoRedo.lengthOfRedoList), 0);
    }
}