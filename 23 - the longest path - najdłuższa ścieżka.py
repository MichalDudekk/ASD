# 23 - the longest path - najdłuższa ścieżka
# Dana jest tablica (m x n) wypełniona wartościami. Znajdź najdłuższą ścieżkę w tej tablicy (możemy
# poruszać się tylko na pola sąsiadujące krawędziami), gdzie wartości na ścieżce są rosnące
# (z pola o wartości 3 możemy przejść tylko na pola o wartości większej lub równej 4).
# Podany jest punkt startowy.
# Opis algorytmu na dole.

# top down - O(n*m)
def longest_path(T,start_w,start_k):
    m = len(T)      # m - liczba wierszy
    n = len(T[0])   # n - liczba kolumn

    F = [[-1 for k in range(n)] for w in range(m)]
    # F[w][k] - długość najdłuższej ścieżki wychodzącej z punktu (w,k)

    def recur(w,k):
        if F[w][k] != -1:
            return F[w][k]
        F[w][k] = 0
        if w-1 >= 0 and T[w][k] < T[w-1][k]:
            F[w][k] = max( F[w][k] , recur(w-1,k) + 1)
        if w+1 < m and T[w][k] < T[w+1][k]:
            F[w][k] = max( F[w][k] , recur(w+1,k) + 1)
        if k-1 >= 0 and T[w][k] < T[w][k-1]:
            F[w][k] = max( F[w][k] , recur(w,k-1) + 1)
        if k+1 < n and T[w][k] < T[w][k+1]:
            F[w][k] = max( F[w][k] , recur(w,k+1) + 1)
        return F[w][k]

    return recur(start_w,start_k)

# Przykładowy test - oczekiwana wartość: 2
T = [[3, 4, 5, 2, 1],
     [10, 2, 13, 14, 8],
     [11, 1, 4, 9, 5],
     [9, 8, 11, 7, 3],
     [6, 2, 1, 6, 9]]
print(longest_path(T,2,4))
# Przykładowy test - oczekiwana wartość: 4
T = [[3, 4, 5, 2, 1],
     [10, 2, 13, 14, 8],
     [11, 1, 4, 9, 5],
     [9, 8, 11, 7, 3],
     [6, 2, 1, 6, 9]]
print(longest_path(T,0,0))
# Przykładowy test - oczekiwana wartość: 24
T = [[ (5*w) + k if w%2==0 else (5*w) + 4 - k for k in range(5)] for w in range(5)]
print(longest_path(T,0,0))

# Opis algorytmu - longest_path(T,start_w,start_k) - O(n*m)
# recur(w,k) - długość najdłuższej ścieżki wychodzącej z punktu (w,k)
# Dla każdego wywołania recur(w,k) algorytm rozważa kontynuacje ścieżki w 4 strony,
# o ile spełniają one wymogi zadania.
