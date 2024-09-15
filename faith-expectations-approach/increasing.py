#lets work with Expectation, Faith and connecting expectation with faith

#print Increasing Order 1 to N

#Expectation f(n) => will print 1,2,3,4 ..... till n
#Faith f(n-1) => will print 1,2,3, .... till n - 1
#Connecting Expectation with Faith f(n) =  f(n - 1) => will print from 1 to n - 1 and then we print(n)

def increasing(n):
  if n==0:
    return
  increasing(n-1) #this will print 1 to n - 1
  print(n)


increasing(5)
