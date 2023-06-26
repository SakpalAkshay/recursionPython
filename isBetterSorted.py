def isSorted(mylist, startIndex = 0):
    l = len(mylist)

    if startIndex == l or startIndex == l -1:
        return True

    if mylist[startIndex] > mylist[startIndex + 1]:
        return False

    output = isSorted(mylist, startIndex + 1)
    return output

print(isSorted([1,2,3,1,4,5]))
        