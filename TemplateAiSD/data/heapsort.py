def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def siftDown(lst, i, upper):
    while(True):
        leftChild = i * 2 + 1
        rightChild = i * 2 + 2
        if max(leftChild, rightChild) < upper:
            if lst[i] >= max(lst[leftChild], lst[rightChild]): 
                break
            elif lst[leftChild] > lst[rightChild]:
                swap(lst, i, leftChild)
                i = leftChild
            else:
                swap(lst, i, rightChild)
        elif leftChild < upper:
            if lst[leftChild] > lst[i]:
                swap(lst, i, leftChild)
                i = leftChild
            else:
                break
        elif rightChild < upper:
            if lst[rightChild] > lst[i]:
                swap(lst, i, r)
                i = rightChild
            else:
                break
        else:
            break

def heapsort(lst):
    for i in range((len(lst)-2)//2, -1, -1):
        siftDown(lst, i, len(lst))

    for i in range(len(lst) - 1, 0, -1):
        swap(lst, 0, i)
        siftDown(lst, 0, i)
    
    return lst