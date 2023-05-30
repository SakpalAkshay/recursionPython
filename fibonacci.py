# recursive code for Fibonacci series 
# here need to give series of SUM of previous two

def fibo(n):

    #here we will have two base or trivial case as our logic requires sum to Two previous digits

    if n == 1:
        return 1
    if n == 2:
        return 2
    out = fibo(n-1) + fibo(n - 2)
    return out
 

print(fibo(5))