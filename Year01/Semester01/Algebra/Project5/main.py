import itertools
import numpy as np


def getFirstLineZero(matrix, m, n):
    i = 0
    firstLineZero = ()
    while i < m and matrix[i][0] == 1:
        i += 1
    if i == m:
        return ()
    else:
        currentLatest0 = 0
        for j in range(n):
            if matrix[i][j] == 0:
                currentLatest0 = j
            else:
                break
    firstLineZero = (i, currentLatest0)
    return firstLineZero


def hasZerosUnderDiagonal(matrix, m, n):
    firstLineZero = getFirstLineZero(matrix, m, n)
    if firstLineZero == ():
        return False
    else:
        for i in range(m):
            for j in range(n):
                if i > firstLineZero[0] and j <= i + firstLineZero[1]:
                    if matrix[i][j] == 1:
                        return False
    return True

def checkColumnFor1sOtherThanLeading1s(matrix, m, n, positionOfLeading1, column):
    for i in range(m):
        if matrix[i][column] == 1 and i != positionOfLeading1:
            return True
    return False

def checkForLeading1s(matrix, m, n):
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if checkColumnFor1sOtherThanLeading1s(matrix, m, n, i, j):
                    return False
                break
    return True

def generateMatrices(m, n):
    allMatrices = list(itertools.product([0, 1], repeat=m*n))
    matricesWithZerosUnder = [matrix for matrix in allMatrices if hasZerosUnderDiagonal(np.array(matrix).reshape(m, n), m, n)]
    reducedEchelonMatrices = [matrix for matrix in matricesWithZerosUnder if checkForLeading1s(np.array(matrix).reshape(m, n), m, n)]
    #reduced_echelon_matrices
    return reducedEchelonMatrices




def main():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        m= int(lines[0])
        n = int(lines[1])
        resultMatrices = generateMatrices(m, n)
        textToPrint = ""
        textToPrint += f"The number of matrices M{m},{n}(Z2) in reduced echelon form is {len(resultMatrices)}\n\n"
        textToPrint += "The matrices M{m},{n}(Z2) in reduced echelon form are:\n"
        for matrix in resultMatrices:
            textToPrint += str(np.array(matrix).reshape(m, n)) + '\n'
        with open("output.txt", 'w') as file:
            file.write(textToPrint)

main()
