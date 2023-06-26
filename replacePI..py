#replace any occurence of 'pi' in a string with 3.14
def replacePi(s):
    #base case
    if len(s)==0 or len(s)==1:
        return s

    if (s[0]=='p' and s[1]=='i'):
        smallOutput = replacePi(s[2:])
        return '3.14' + smallOutput
    else:
        return s[0] + replacePi(s[1:])


st = replacePi('pipiwwwpi')
print(st)