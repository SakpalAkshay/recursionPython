arr = [1,2,4,5,6,7,8,0,11,23,1,43,11]
#first is the bruteforce approach => Sort the array and give the last element
arr.sort()
print(f'largets through brute force {arr[-1]}')  #NLOGN complexity

# using a loop and more optimized approach
maxi  = 0
for i in arr:
    maxi = max(i,maxi)
print("Max thorugh for loop is :", maxi)


#Now lets solve it thorugh recursion

def findMax(arr):
    if len(arr)==0:
        return 0

    maxi = arr[0]
    newMax = findMax(arr[1:])
    return max(newMax,maxi)

maximus = findMax(arr)
print("Max Through Recursion is :", maximus)
