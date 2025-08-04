# 02 - rod cutting - cięcie pręta
# Mając pręt o długości n cali oraz tabelę cen T[i] dla i = [1, 2, ..., n].
# Określ maksymalny przychód r[n], który można uzyskać przez pocięcie pręta i sprzedaż
# poszczególnych kawałków.

# bottom up
def rod_cutting(T):
    n = len(T)

    F = [-1 for k in range(n+1)]
    # F[k] - maksymalny zysk z pocięcia pręta długości k

    for k in range(n+1):
        F[k] = T[k-1]
        for i in range(1,k):
            F[k] = max( F[k] , F[i] + F[k-i] )

    return F[n]

# top down
def rod_cutting_recursive(T):
    n = len(T)
    F = [-1 for k in range(n+1)]
    # F[k] - maksymalny zysk z pocięcia pręta długości k
    def recur(k):
        if F[k] != -1:
            return F[k]
        F[k] = T[k-1]
        for i in range(1,k):
            F[k] = max( F[k] , recur(i) + recur(k-i) )
        return F[k]
    return recur(n)

# bottom up ze zwracaniem cięć
def rod_cutting_parent(T):
    n = len(T)
    F = [-1 for k in range(n+1)]
    parent = [[] for k in range(n+1)]

    for k in range(n+1):
        F[k] = T[k-1]
        parent[k] = [T[k-1]]
        for i in range(1,k):
            if F[i] + F[k-i] > F[k]:
                F[k] = F[i] + F[k-i]
                parent[k] = parent[i] + parent[k-i]

    return F[n],parent[n]


T = [2, 1, 1, 2, 1, 12, 11, 11, 11, 13, 11, 19, 32, 23, 24, 19, 20] # 40
#T = [1, 5, 8, 9]    # 10
print(rod_cutting(T))
print(rod_cutting_recursive(T))
print(rod_cutting_parent(T))

# Opis algorytmu - rod_cutting(T) - O(n^2)
# F[k] - maksymalny zysk z pocięcia pręta długości k
# Dla każdego k-tego wywołania pętli algorytm znajduje najbardziej opłacalny podział na dokładnie dwa kawałki
# F[i] i F[k-i], gdzie i jest z przedziału <1,k)
