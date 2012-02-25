def binary_search(v, L):
    
    i = 0
    j = len(L) - 1
    
    while i != j + 1:
        m = (i + j) / 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1
    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1