def PrimeCheck(n:int): #used for problem 1 and 5
    if n<2:
        return 0
    if n==2:
        return 1
    for i in range(2, int(n/2)):
        if n%i == 0:
            return 0
    return 1

def Goldbach(n:int): #used for problem 2
    if PrimeCheck(n-2) == 1:
        return 2,n-2
    for i in range(3,n):
        if(PrimeCheck(i) and PrimeCheck(n-i)):
            return i,n-i

def GetLowestNumber(n:int): #used for number 3
    m=0
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n > 0:
        list[n % 10] = list[n % 10] + 1
        n = int(n / 10)
    if list[0] > 0:
        i = 1
        for x in list[1:]:
            if x > 0:
                m = m * 10 + i
                x = x - 1
                break
            i = i + 1
    else:
        i = 1
        for x in list[1:]:
            while x > 0:
                m = m * 10 + i
                x = x - 1
            i = i + 1
    return m

def GetHighestNumber(n:int):
    m=0
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n > 0:
        list[9 - (n % 10) + 1] = list[9 - (n % 10) + 1] + 1
        n = int(n / 10)
    i = 0
    for x in list:
        while x > 0:
            m = m * 10 + (9 - i + 1)
            x = x - 1
        i = i + 1
    return m

def problem(nr:int):
    # 1
    if nr==1:
        n=int(input("Insert n: "))
        while (True):
            n = n + 1
            if PrimeCheck(n):
                print("The first prime number larger than the given natural number is "+str(n)+'\n')
                break

    #2
    elif nr==2:
        n=int(input("Insert n: "))
        x,y=Goldbach(n)
        print(str(x) +' and '+ str(y) + ' are 2 prime numbers, adding them results into the given number \n')

    #3
    elif nr==3:
        n=int(input("Insert n: "))
        m=GetLowestNumber(n)
        print(str(m) +"is the minimal number that can be created using given number's digits\n")

    #4
    elif nr==4:
        n=int(input("Insert n: "))
        m=GetHighestNumber(n)
        print(str(m) +"is the largest number that can be created using given number's digits\n")


    #5
    elif nr==5:
        n=int(input("Insert n: "))
        while (True):
            n = n - 1
            if PrimeCheck(n):
                print("The largest prime number smaller than the given natural number is "+str(n)+'\n')
                break
    else:
        print("Couldn't find problem nr." + str(nr) + '\n')

def main():
    nr = int(input("Select problem nr: "))
    problem(nr)

main()