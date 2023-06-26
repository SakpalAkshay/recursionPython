def replaceString(s,a,b):
    #base case 
    if len(s)==0:
        return s

    smallOuput = replaceString(s[1:],a,b)
    
    if s[0] == a:
        return b + smallOuput
    else:
        return s[0] + smallOuput

a = replaceString('absd','a','c')
print(a)
str ='a'
