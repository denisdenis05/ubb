
def CheckIfLeapYear(year:int):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def GetDaysInPartialYear(startingMonth, endingMonth, startingDay, endingDay, year):
    days=0
    monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if CheckIfLeapYear(year):
        monthsDays[1]=29
    for month in range(startingMonth+1,endingMonth):
        days=days+monthsDays[month-1]
    days=days+(monthsDays[startingMonth-1]-startingDay)
    days=days+(monthsDays[endingMonth-1]-(monthsDays[endingMonth-1]-endingDay))
    return days

def ConvertAgeInDays(birthDay:int,birthMonth:int,birthYear:int,day:int,month:int,year:int):
    totalDays=0
    for yr in range(birthYear+1,year):
        if CheckIfLeapYear(yr):
            totalDays=totalDays+366
        else:
            totalDays=totalDays+365
    if birthYear==year:
        totalDays = totalDays + GetDaysInPartialYear(birthMonth, month, birthDay, day, birthYear)
    else:
        totalDays=totalDays+GetDaysInPartialYear(birthMonth,12,birthDay,31,birthYear)
        totalDays=totalDays+GetDaysInPartialYear(1,month,1,day,year)
        totalDays=totalDays+1
    return totalDays

def GetNumberOfPrimeFactors(n:int): #used for problem 13
    d=2
    nr=0
    while n>1:
        if n%d==0:
            nr=nr+1
        while n%d==0:
            n=n/d
        d=d+1
    return nr

def GetNthPrimeFactor(number:int, nth:int): #used for problem 13
    if nth==0:
        nth=1
    d = 2
    nr = 0
    while number > 1:
        if number % d == 0:
            nr = nr + 1
        if nr==nth:
            return d
        while number % d == 0:
            number = number / d
        d=d+1

def FindNumberInRange(n:int): #used for problem 13
    if n == 1:
        return 1
    number=2
    nrofelements=1
    while nrofelements<n:
        nrofelements=nrofelements+GetNumberOfPrimeFactors(number)
        number=number+1
    number=number-1
    return GetNthPrimeFactor(number,nrofelements-n)


def GetNumberOfPrimeFactorsIncludingComposed(n:int): #used for problem 14
    d=2
    nr=0
    nrIfComposed=0
    isComposed=False
    while n>1:
        if n%d==0:
            if (n/d)%d==0:
                isComposed=True
            nr=nr+1
            nrIfComposed=nrIfComposed+d
        while n%d==0:
            n=n/d
        d=d+1
    if isComposed is True or nr>1:
        return nrIfComposed
    else:
        return nr

def GetNthPrimeFactorIncludingComposed(number:int, nth:int): #used for problem 14
    if nth==0:
        nth=1
    d = 2
    nr = 0
    while number > 1:
        if number % d == 0:
            nr = nr + d
        if nr>=nth:
            return d
        while number % d == 0:
            number = number / d
        d=d+1

def FindNumberInRangeIncludingComposed(n:int): #used for problem 14
    if n==1:
        return 1
    number=2
    nrofelements=1
    while nrofelements<n:
        nrofelements=nrofelements+GetNumberOfPrimeFactorsIncludingComposed(number)
        number=number+1
    number=number-1
    return GetNthPrimeFactorIncludingComposed(number,nrofelements-n+1)

def GetSumOfDivisors(n:int):
    sum = 1
    for div in range(2, int(n / 2) + 1):
        if n % div == 0:
            sum = sum + div
    return sum

def GetPerfectNumberSmallerThan(n:int):
    if n<=6:
        return -1
    while True:
        n=n-1
        if GetSumOfDivisors(n)==n:
            return n

def problem(nr:int):
    # 12
    if nr==12:
        birthdate=input("Insert birthday (dd/mm/yyyy): ")
        birthDay,birthMonth,birthYear=map(int, birthdate.split("/"))
        currentdate=input("Insert current date (dd/mm/yyyy): ")
        day,month,year=map(int, currentdate.split("/"))
        days=ConvertAgeInDays(birthDay,birthMonth,birthYear,day,month,year)
        print("The age of the given person is " + str(days) + ' days \n')
    elif nr==13:
        n=int(input("Insert n: "))
        nth=FindNumberInRange(n)
        print("The given nth element of the sequence is " + str(nth) + '\n')
    elif nr==14:
        n = int(input("Insert n: "))
        nth = FindNumberInRangeIncludingComposed(n)
        print("The given nth element of the sequence is " + str(nth) + '\n')
    elif nr==15:
        n = int(input("Insert n: "))
        perfNr=GetPerfectNumberSmallerThan(n)
        if perfNr==-1:
            print("The largest perfect number smaller than the given natural number doesn't exist " + '\n')
        else:
            print("The largest perfect number smaller than the given natural number is " + str(perfNr) + '\n')
    else:
        print("Couldn't find problem nr." + str(nr) + '\n')


def main():
    nr = int(input("Select problem nr: "))
    problem(nr)

main()
