def lastIndexOf(myList, elem):
    l = len(myList)
    if l == 0:
        return -1
    
    newList = myList[1:]
    output = lastIndexOf(newList, elem)

    if output!=-1:
        return output + 1
    if myList[0]==elem:
        return 0
    else:
        return -1 
   
    

   
