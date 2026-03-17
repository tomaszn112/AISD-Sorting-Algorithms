def steps(n):
    steps = []
    k = 0
    while True:
        s1 = 9 * (4**k - 2**k) + 1
        s2 = 4**k - 3 * 2**(k) + 1

        if s1 < n:
            steps.append(s1)
        if s2 > 0 and s2 < n:
            steps.append(s2)
            
        if s1 >= n and s2 >= n:
            break
        k += 1

    return sorted(list(set(steps)), reverse=True)

def shellSort(lst):
    gaps = steps(len(lst))
    
    for gap in gaps:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
    return lst