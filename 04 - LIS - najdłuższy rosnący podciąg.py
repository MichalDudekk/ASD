# 04 - LIS - najdłuższy rosnący podciąg
# Znajdź długość najdłuższego podciągu rosnącego w danym ciągu takiego,
# że wszystkie elementy podciągu są posortowane w kolejności rosnącej.
# Dodatkowo wypisz ten podciąg.
# Przykład:
# Wejście: [10, 22, 9, 33, 21, 50, 41, 60, 80]
# Najdłuższy podciąg rosnący: [10, 22, 33, 50, 60, 80]
# Opis algorytmu na dole.

# bottom up
def lis(T):
    n = len(T)

    F = [1 for k in range(n)]   # każda liczba napewno tworzy rosnący podciąg długości 1
    # F(i) = najdłuższy rosnący podciąg z liczb z przedziału od T[0] do T[i] KOŃCZĄCY się dokładnie na i-tej liczbie
    parent = [[T[k]] for k in range(n)]

    for k in range(n):
        for i in range(0,k):
            if T[k] <= T[i]:
                continue
            if F[k] < F[i] + 1:
                F[k] = F[i] + 1
                parent[k] = parent[i] + [T[k]]
    return F[n-1] , parent[n-1]

# top down
def lis_recursive(T):
    n = len(T)
    F = [-1 for k in range(n)]
    parent = [[T[k]] for k in range(n)]

    def recur(k):
        if F[k] != -1:
            return F[k]
        F[k] = 1
        for i in range(0,k):
            if T[i] >= T[k]:
                continue
            val = recur(i)
            if val + 1 > F[k]:
                F[k] = val + 1
                parent[k] = parent[i] + [T[k]]
        return F[k]
    recur(n-1)
    return F[n-1] , parent[n-1]




# Przykładowy test - oczekiwana wartość: 6, [10, 22, 33, 50, 60, 80]
T = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(T))
print(lis_recursive(T))

# Opis algorytmu - lis(T) - O(n^2)
# F(i) = najdłuższy rosnący podciąg z liczb z przedziału od T[0] do T[i] KOŃCZĄCY się dokładnie na i-tej liczbie
# Dla każdego k-tego wywołania pętli algorytm wybiera takie i z przedziału <0,k), że:
# 1) T[i] < T[k]
# 2) F[i] + 1 > F[k]