import random
def quickSortLeft(lst):
    def _quick_sort(low, high):
        if low < high:
            pivot_idx = _partition_left(low, high)
            _quick_sort(low, pivot_idx - 1)
            _quick_sort(pivot_idx + 1, high)
    def _partition_left(low, high):
        pivot = lst[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[low], lst[i - 1] = lst[i - 1], lst[low]
        return i - 1
    _quick_sort(0, len(lst) - 1)
    return lst

def quickSortRandom(lst):
    def _quick_sort(low, high):
        if low < high:
            pivot_idx = _partition_random(low, high)
            _quick_sort(low, pivot_idx - 1)
            _quick_sort(pivot_idx + 1, high)
    def _partition_random(low, high):
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
    _quick_sort(0, len(lst) - 1)
    return lst