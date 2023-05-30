def print1ToN(n):

    if n == 0:
        return 1 #base or trivial case
    print1ToN(n -1)
    print(n)



def printNTo1(n):

    if n == 0:
        return 1
    print(n)
    printNTo1(n-1)
    

print1ToN(4)
printNTo1(5)