from math import sqrt
import json

class Complex:
    def __init__(self, realPart, imaginaryPart):
        self.__realPart = int(realPart)
        self.__imaginaryPart = int(imaginaryPart)

    def getRealPart(self):
        return self.__realPart

    def getImaginaryPart(self):
        return self.__imaginaryPart

    def getMagnitude(self):
        realPart = self.getRealPart()
        imaginaryPart = self.getImaginaryPart()
        return sqrt(realPart * realPart + imaginaryPart * imaginaryPart)

    def __eq__(self, complexNumberToCompare):
        if type(complexNumberToCompare) != Complex:
            raise ValueError("Can't compare a complex number to a non-complex number")
        else:
            if self.getRealPart() == complexNumberToCompare.getRealPart() and self.getImaginaryPart() == complexNumberToCompare.getImaginaryPart():
                return True
        return False

    def __ne__(self, complexNumberToCompare):
        if type(complexNumberToCompare) != Complex:
            raise ValueError("Can't compare a complex number to a non-complex number")
        else:
            if self.getRealPart() != complexNumberToCompare.getRealPart() or self.getImaginaryPart() != complexNumberToCompare.getImaginaryPart():
                return True
        return False

    def __le__(self, complexNumberToCompare):
        if type(complexNumberToCompare) != Complex:
            raise ValueError("Can't compare a complex number to a non-complex number")
        else:
            if self.getMagnitude() <= complexNumberToCompare.getMagnitude():
                return True
        return False

    def __lt__(self, complexNumberToCompare):
        if type(complexNumberToCompare) != Complex:
            raise ValueError("Can't compare a complex number to a non-complex number")
        else:
            if self.getMagnitude() < complexNumberToCompare.getMagnitude():
                return True
        return False

    def __gt__(self, complexNumberToCompare):
        if type(complexNumberToCompare) != Complex:
            raise ValueError("Can't compare a complex number to a non-complex number")
        else:
            if self.getMagnitude() > complexNumberToCompare.getMagnitude():
                return True
        return False

    def __ge__(self, complexNumberToCompare):
        if type(complexNumberToCompare) != Complex:
            raise ValueError("Can't compare a complex number to a non-complex number")
        else:
            if self.getMagnitude() >= complexNumberToCompare.getMagnitude():
                return True
        return False

    def __str__(self):
        textToPrint = ""
        realPart = self.getRealPart()
        imaginaryPart = self.getImaginaryPart()
        if realPart == 0:
            textToPrint = textToPrint + str(imaginaryPart) + "i"
        elif imaginaryPart == 0:
            textToPrint = textToPrint + str(realPart)
        elif imaginaryPart >= 0:
            textToPrint = textToPrint + str(realPart) + "+" + str(imaginaryPart) + "i"
        else:
            textToPrint = textToPrint + str(realPart) + str(imaginaryPart) + "i"
        return textToPrint

    def __json__(self):
        realPart = self.getRealPart()
        imaginaryPart = self.getImaginaryPart()
        return [realPart, imaginaryPart]


