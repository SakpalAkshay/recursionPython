def firstIndex(mylist, elem):
    if len(mylist) == 0:
        return -1
    
    if mylist[0] == elem:
        return 0
    
    shortList = mylist[1:]
    output = firstIndex(shortList,elem)

    if output != -1:
        return output + 1
    else:
        return -1
print(firstIndex([1,2,3,4,5,6],3))