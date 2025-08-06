# 07 - minimum cost path - minimalna ścieżka
# Mamy macierz mxn, gdzie każda komórka ma przypisaną wartość odpowiadającą kosztowi.
# Należy znaleźć minimalny koszt dotarcia z komórki (0,0) do (m-1,n-1).
# Dozwolone ruchy: tylko w prawo lub w dół.
# UWAGA: koszt pola (0,0) również należy uwzględnić
# Opis algorytmu na dole.
from math import inf

# top down - O(m*n)
def path(T):
    m = len(T)      # m - liczba wierszy
    n = len(T[0])   # n - liczba kolumn

    F = [[inf for k in range(n)] for w in range(m)]
    # F[w][k] - koszt dotarcia do (m-1,n-1) z (w,k)
    F[0][0] = T[0][0]

    def recur(w,k):
        if w < 0 or k < 0:
            return inf
        if F[w][k] != inf:
            return F[w][k]
        up = recur(w-1,k) + T[w][k]
        left = recur(w,k-1) + T[w][k]
        F[w][k] = min(up,left)
        return F[w][k]
    recur(m-1,n-1)
    return F[m-1][n-1]

# Przykładowy test - oczekiwana wartość: 18
T = [[1, 3, 5, 8],
     [4, 2, 1, 7],
     [4, 3, 2, 8],
     [7, 2, 9, 1]]
print(path(T))

# Opis algorytmu - path(T) - O(m*n)
# rekur(w,k) - koszt dotarcia do (m-1,n-1) z (w,k)
# Algorytm pokonuje drogę "od tyłu" - rozważa opcje pójścia w górę o jeden i pójścia w lewo o jeden,
# a następnie wybiera tą, która zapewnia mniejszy wynik.
