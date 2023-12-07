def RetrieveDate(FullDay,year): #used for problem 6
    months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
              'September': 30, 'October': 31, 'November': 30, 'December': 31}

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        months['February'] = 29

    for month in months:
        if(months[month]>=FullDay):
            return month,FullDay
        else:
            FullDay=FullDay-months[month]

def DisplayDate(year: int, month: int, date: int): #used for problem 6
    if date == 1 or date == 21:
        print("The full date is: " + str(month) + " " + str(date) + "st " + str(year) + '\n')
    elif date == 2 or date == 22:
        print("The full date is: " + str(month) + " " + str(date) + "nd " + str(year) + '\n')
    elif date == 3 or date == 23:
        print("The full date is: " + str(month) + " " + str(date) + "rd " + str(year) + '\n')
    else:
        print("The full date is: " + str(month) + " " + str(date) + "th " + str(year) + '\n')


def PrimeCheck(n): #used for problem 7
    if n<2:
        return 0
    if n==2:
        return 1
    for i in range(2, int(n/2)):
        if n%i == 0:
            return 0
    return 1


def P(n1,n2): #used for problem 11
    list1=[0,0,0,0,0,0,0,0,0,0]
    list2=[0,0,0,0,0,0,0,0,0,0]
    while n1>0:
        list1[n1%10] = list1[n1%10] + 1
        n1 = int(n1/10)
    while n2>0:
        list2[n2%10] = list2[n2%10] + 1
        n2 = int(n2/10)
    for i in range(0,9):
        if (list1[i]>0 and list2[i]==0) or (list1[i]==0 and list2[i]>0):
            return False
    return True

def Fib(n:int):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        x = 2
        y = 3
        m = y
        while (m <= n):
            m = x + y
            x = y
            y = m
        return m

def GetProductOfDivisors(n:int):
    prod = 1
    for div in range(2, int(n / 2) + 1):
        if n % div == 0:
            prod = prod * div
    return prod

def Palindrome(n:int):
    pal = 0
    while n > 0:
        pal = pal * 10 + (n % 10)
        n = int(n / 10)
    return pal

def problem(nr:int):

    #6
    if nr==6:
        year=int(input("Insert year: "))
        day=int(input("Insert day: "))

        month,date=RetrieveDate(day, year)
        DisplayDate(year,month,date)

    #7
    elif nr==7:
        n=int(input("Insert n: "))
        p=n+1
        while True:
            if PrimeCheck(p) == 1 and PrimeCheck(p+2) == 1:
                print("The twin prime numbers immediately larger than the given number are "+str(p)+" and "+str(p+2)+'\n')
                break
            elif PrimeCheck(p+1) == 1 and PrimeCheck(p+3) == 1:
                print("The twin prime numbers immediately larger than the given number are "+str(p+1)+" and "+str(p+3)+'\n')
                break
            p=p+4

    #8
    elif nr==8:
        n=int(input("Insert n: "))
        m=Fib(n)
        print("The smallest number m from the Fibonacci sequence larger than the given natural number is " + str(m) +'\n')


    #9
    elif nr==9:
        n=int(input("Insert n: "))
        p=GetProductOfDivisors(n)
        print("The product of all the proper factors of the given number is "+str(p)+'\n')

    #10
    elif nr==10:
        n=int(input("Insert n: "))
        pal=Palindrome(n)
        print("The palindrome of the given number is "+str(pal)+'\n')


    #11
    elif nr==11:
        n1=int(input("Insert n1: "))
        n2=int(input("Insert n2: "))
        if P(n1,n2):
            print("11) The given numbers do have the P property" + '\n')
        else:
            print("11) The given numbers DO NOT have the P property" + '\n')
    else:
        print("Couldn't find problem nr." + str(nr) + '\n')

def main():
    nr = int(input("Select problem nr: "))
    problem(nr)

main()
