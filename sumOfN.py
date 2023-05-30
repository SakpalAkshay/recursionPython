# sum of N natural numbers

def sumOfN(n):

    if n==1:
        return 1
    
    if n ==0:
        return 0 
    
    out = n + sumOfN(n-1)
    return out


print(sumOfN(5))