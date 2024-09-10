#palindrome checker using recursion
string = "madams"
n = len(string)
def palindrome(i):
  if i>=n/2:
    return True
  if string[i]!=string[n-i-1]:
    return False
  return palindrome(i+1)
ans = palindrome(0)
print(ans)


