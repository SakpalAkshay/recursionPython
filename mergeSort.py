def mergeTwoSortedList(a1, a2, a):

    i, j, k = 0, 0, 0
    while (i < len(a1) and j < len(a2)):

        if (a1[i] < a2[j]):
            a[k] = a1[i]
            i = i + 1
            k = k + 1
        else:
            a[k] = a2[j]
            j = j + 1
            k = k + 1
    while (i < len(a1)):
        a[k] = a1[i]
        i = i + 1
        k = k + 1

    while (j < len(a2)):
        a[k] = a2[j]
        j = j + 1
        k = k + 1


def mergeSort(a):
    # base case
    if len(a) == 0 or len(a) == 1:
        return

    mid = len(a)//2
    a1 = a[:mid]
    a2 = a[mid:]
    mergeSort(a1)
    mergeSort(a2)

    mergeTwoSortedList(a1, a2, a)


ls = [2, 1, 4, 5, 6, 7, 0]
mergeSort(ls)
print(ls)
