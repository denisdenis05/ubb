import itertools
import numpy as np

def isLinearlyIndependent(vectorSpaces: int) -> bool:
    matrixOfVectorSpaced = np.array(vectorSpaces).T  # transform list of vector spaces into matrix
    determinant = np.linalg.det(matrixOfVectorSpaced)  # we calculate the determinant of the matrix
    if determinant != 0:
        return True  # determinant is not zero so it is linearly independent
    else:
        return False  # determinant is zero so it is linearly dependent


def generateVectorSpaces(n: int) -> list:
    vectorSpaces = list(itertools.product([0, 1], repeat=n))  # generates all vector spaces
    print(vectorSpaces)
    return vectorSpaces


def generateAllBases(n: int) -> list:

    vectorSpaces = generateVectorSpaces(n)  # we generate the vector spaces

    allBases = []  # we create a list of bases which is empty at first

    for basisToCheck in itertools.product(vectorSpaces, repeat=n):  # we take each generated base in combinations of n vector spaces (dimension is n)
        if isLinearlyIndependent(basisToCheck):  # we check if the base is linearly independent and if so, we put it in the list
            allBases.append(basisToCheck)

    return allBases


def displayAllBases(n: int, allBases: list):
    textToPrint = f"1. the number of bases of the vector space Z^2 {n} over Z2 is {len(allBases)}\n"

    textToPrint = textToPrint + "2. the vectors of each such basis are:\n"
    for basis in allBases:
        textToPrint = textToPrint + str(basis) + "\n"
    with open("output.txt", 'w') as file:
        file.write(textToPrint)

def main():
    with open("input.txt", 'r') as file:
        n = int(file.read())

    allBases = generateAllBases(n)
    displayAllBases(n, allBases)


main()

