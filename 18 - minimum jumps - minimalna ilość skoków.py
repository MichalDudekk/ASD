# 18 - minimum jumps - minimalna ilość skoków
# Dana jest tablica kroków, które można wykonać do przodu z danego elementu.
# Znajdź minimalną liczbę skoków potrzebną do przejścia od początku tablicy do jej końca.
# Opis algorytmu na dole.
from math import inf

# bottom up - O(n^2)
def minimum_jumps(T):
    n = len(T)
    F = [inf for k in range(n)]
    # F[i] - minimalna liczba skoków, aby znaleźć się na polu i
    F[0] = 0
    for k in range(n):
        for step in range(1,T[k]+1):
            if k + step >= n:
                break
            F[k+step] = min(F[k+step] , F[k] + 1)
    return F[n-1]

# Przykładowy test - oczekiwana wartość: 4
T = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
print(minimum_jumps(T))

# Opis algorytmu - minimum_jumps(T) - O(n^2)
# Dla każdego k-tego wywołania pętli algorytm przechodzi po wszystkich możliwych krokach (step).
# Następnie, jeśli F[i+step] > F[i] + 1 to nadpisuje tą wartość.