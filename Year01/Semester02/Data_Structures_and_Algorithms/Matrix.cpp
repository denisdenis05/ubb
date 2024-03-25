#include "Matrix.h"
#include <exception>
#include <stdexcept>
#include <iostream>

using namespace std;


void Matrix::printAll(){
    cout<<"The nr of lines is "<<this->nrLins<<"\n";
    cout<<"The nr of columns is "<<this->nrCols<<"\n";
    cout<<"\n\nThe columns are:\n";
    for (int i=0; i<= this->nrCols + 1; i++)
        cout<<this->columns[i]<<" ";
    cout<<"\n\nThe lines are:\n";
    for (int i = 0; i <= this->columns[this->nrCols+1]; i++)
        cout<<this->lines[i]<<" ";
    cout<<"\n\nThe values are:\n";
    for (int i = 0; i <= this->columns[this->nrCols+1]; i++)
        cout<<this->values[i]<<" ";
    cout<<"\n";

}


Matrix::Matrix(int nrLines, int nrCols) {
	   
	this->nrLins = nrLines;
    this->nrCols = nrCols;
    this->columns = new int[nrCols+2];
    for(int i = 0; i <= nrCols + 1; i++)
        this->columns[i] = 0;
    this->lines = new int[2];
    this->values = new TElem[2];

}


int Matrix::nrLines() const {
	return this->nrLins;
}


int Matrix::nrColumns() const {
	return this->nrCols;
}

int findElementInArray(int* array, int startingPointOfArray, int lengthOfArray, int element){
    for (int i = startingPointOfArray; i < lengthOfArray; i++)
        if (array[i] == element)
            return i;
    return -1;
}


TElem Matrix::element(int i, int j) const { // probably finished

	if (i > this->nrLins or j > this->nrCols or i < 0 or j <0)
        throw runtime_error("Bad position");
    if (this->columns[j+1] - this->columns[j] <= 0)
        return NULL_TELEM;

    int positionMinOnLine = this->columns[j];
    int positionMaxOnLine = this->columns[j+1];

    int positionOfElement = findElementInArray(this->lines, positionMinOnLine, positionMaxOnLine, i);
    if (positionOfElement != -1)
        return this->values[positionOfElement];
    return NULL_TELEM;
}

TElem Matrix::modify(int i, int j, TElem e) {
    if (i > this->nrLins or j > this->nrCols or i < 0 or j < 0)
        throw runtime_error("Bad position");
    int positionMinOnLine = this->columns[j];
    int positionMaxOnLine = this->columns[j+1];
    int linePosition = findElementInArray(this->lines, positionMinOnLine, positionMaxOnLine, i);



    if (e != NULL_TELEM) { // add or update
        if (positionMaxOnLine - positionMinOnLine == 0 or linePosition == -1) { // inexistent, so add

            int currentLastPositionInLinesArray = this->columns[this->nrCols + 1];

            int *newArrayOfLines = new int[currentLastPositionInLinesArray + 2];
            TElem *newArrayOfValues = new TElem[currentLastPositionInLinesArray + 2];
            for (int iterator = 0; iterator <= currentLastPositionInLinesArray; iterator++) {
                if (iterator < positionMaxOnLine) {
                    newArrayOfLines[iterator] = this->lines[iterator];
                    newArrayOfValues[iterator] = this->values[iterator];
                } else if (iterator == positionMaxOnLine) {
                    newArrayOfLines[iterator] = i;
                    newArrayOfValues[iterator] = e;
                } else {
                    newArrayOfLines[iterator] = this->lines[iterator - 1];
                    newArrayOfValues[iterator] = this->values[iterator - 1];
                }
            }
            delete[] this->lines;
            delete[] this->values;

            this->lines = newArrayOfLines;
            this->values = newArrayOfValues;

            for (int iterator = j + 1; iterator <= this->nrCols + 1; iterator++)
                this->columns[iterator]++;
        }
        else{ // update
            TElem oldValue = this->values[linePosition];
            this->values[linePosition] = e;
            return oldValue;
        }
    }
    else { //remove
        if (positionMaxOnLine - positionMinOnLine != 0 and linePosition != -1) {
            TElem oldValue = this->values[linePosition];
            int currentLastPositionInLinesArray = this->columns[this->nrCols + 1];

            int *newArrayOfLines;
            TElem *newArrayOfValues;
            if (currentLastPositionInLinesArray >= 2) {
                newArrayOfLines = new int[currentLastPositionInLinesArray + 1];
                newArrayOfValues = new TElem[currentLastPositionInLinesArray + 1];
            }
            else{
                newArrayOfLines = new int[2];
                newArrayOfValues = new TElem[2];
            }
            for (int iterator = 0; iterator <= currentLastPositionInLinesArray; iterator++) {
                if (iterator < linePosition) {
                    newArrayOfLines[iterator] = this->lines[iterator];
                    newArrayOfValues[iterator] = this->values[iterator];
                } else if (iterator >= linePosition) {
                    newArrayOfLines[iterator] = this->lines[iterator + 1];
                    newArrayOfValues[iterator] = this->values[iterator + 1];
                }
            }
            delete[] this->lines;
            delete[] this->values;

            this->lines = newArrayOfLines;
            this->values = newArrayOfValues;

            for(int iterator = j + 1; iterator <= this->nrCols + 1; iterator++)
                this->columns[iterator]--;
            return oldValue;
        }

    }

	return NULL_TELEM;
}


