def factorial(n):

    if n == 0:
        return 1 #base case or trivial  case
    return n * factorial(n-1)


n = int(input("Give a Number : "))
fact = factorial(n)
print("Factorial is : ", fact )