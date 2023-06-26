def betterLastIndex(mylist, elem, startIndex):
    l = len(mylist)
    if startIndex == l or startIndex == l -1:
        return -1

    output = betterLastIndex(mylist,elem,startIndex + 1)

    if output !=-1:
        return output
    else:
        if mylist[startIndex]==elem:
            return startIndex
        else:
            return -1 