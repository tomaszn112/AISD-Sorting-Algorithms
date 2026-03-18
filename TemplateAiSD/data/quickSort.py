import random
def quickSortLeft(lst):
    def quickSort(low, high):
        if low < high:
            pivot_idx = partitionLeft(low, high)
            quickSort(low, pivot_idx - 1)
            quickSort(pivot_idx + 1, high)
    def partitionLeft(low, high):
        pivot = lst[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[low], lst[i - 1] = lst[i - 1], lst[low]
        return i - 1
    quickSort(0, len(lst) - 1)
    return lst

def quickSortRandom(lst):
    def quickSort(low, high):
        if low < high:
            pivot_idx = partitionRandom(low, high)
            quickSort(low, pivot_idx - 1)
            quickSort(pivot_idx + 1, high)
    def partitionRandom(low, high):
        rand_pivot = random.randint(low, high)
        lst[low], lst[rand_pivot] = lst[rand_pivot], lst[low]
        pivot = lst[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[low], lst[i - 1] = lst[i - 1], lst[low]
        return i - 1
    quickSort(0, len(lst) - 1)
    return lst