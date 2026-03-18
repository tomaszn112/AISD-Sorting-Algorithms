def selectionSort(lst):
    for i in range(len(lst)):
        minIndex = i
        for j in range(i + 1, len(lst)):
            if lst[minIndex] > lst[j]:
                minIndex = j
        lst[i], lst[minIndex] = lst[minIndex], lst[i]
    return lst