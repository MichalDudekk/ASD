# egzamin 2021 termin 1 zadanie 1 - chaos_index

from zad1testy import runtests

def merge_sort(T,a,b):
    if a == b:
        return [T[a]]
    mid = (a+b)//2

    left = merge_sort(T,a,mid)
    right = merge_sort(T,mid+1,b)
    l = len(left)
    r = len(right)
    ctr_l = 0
    ctr_r = 0

    res = [0 for _ in range(l+r)]
    for i in range(l+r):
        if ctr_l >= l:
            res[i] = right[ctr_r]
            ctr_r += 1
            continue
        if ctr_r >= r:
            res[i] = left[ctr_l]
            ctr_l += 1
            continue
        if left[ctr_l] < right[ctr_r]:
            res[i] = left[ctr_l]
            ctr_l += 1
            continue
        res[i] = right[ctr_r]
        ctr_r += 1
    return res

# O(n*log(n))
def chaos_index(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i],i)

    #T.sort()
    T = merge_sort(T,0,n-1)

    k = 0
    for j in range(n):
        k = max(k, abs(j - T[j][1]))
    return k

runtests( chaos_index )
