def firstIndexSearch(myList, elem, startIndex):
    #base case is if list is empty or we dont find the elem

    l = len(myList)
    if startIndex == l:
        return -1

    if myList[startIndex] == elem:
        return startIndex
    
    output = firstIndexSearch(myList, elem, startIndex + 1)
    
    return output


print(firstIndexSearch([1,2,3],5,0))
