# 87 - open intervals - otwarte przedziały
# Dany jest zbiór otwartych przedziałów. Znajdź podzbiór tego zbioru taki, że:
#    1) jego rozmiar wynosi dokładnie k,
#    2) przedziały są rozłączne,
#    3) różnica między najwcześniejszym początkiem a najdalszym końcem jest minimalna.
# Jeśli nie ma rozwiązania, algorytm powinien to stwierdzić.

def open_intervals(T,k):
    res = []
    T.sort(key=lambda x:(x[1],-1*x[0]))
    last = T[0][0]
    for start,end in T:
        if start < last:
            continue
        res.append( (start,end) )
        last = end

    if len(res) < k:
        return False

    left = 0
    right = len(res)-1
    while right-left != k-1:
        progress_left = res[left+1][0] - res[left][0]
        progress_right = res[right][1] - res[right-1][1]
        if progress_left > progress_right:
            left += 1
        else:
            right -= 1

    ans = []
    for i in range(left,right+1):
        ans.append(res[i])
    return ans

# Przykładowy test - oczekiwane wartości: [(1, 2), (3, 4), (7, 8)]
T = [(1, 7), (2, 5), (3, 4), (8, 11), (3, 6), (2, 4), (5, 9), (7, 8), (1, 5), (1, 2), (2, 5)]
print(open_intervals(T, 3))