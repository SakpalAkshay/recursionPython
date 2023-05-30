def isListSorted(myList):

    if len(myList) == 1:
        return True
    
    if myList[0] > myList[1]:
        return False
    
    updatedList = myList[1:]
    output = isListSorted(updatedList)
    return output

print(isListSorted([1,2,3]))
print(isListSorted([1,2,7,3]))