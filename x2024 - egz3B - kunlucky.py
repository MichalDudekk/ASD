# egzamin 2024 termin 3 zadanie 2 - kunlucky
from egz3btesty import runtests

# O(n)
def kunlucky(T, k):
    n = len(T)
    x = k
    itr = 1
    unlucky = {}
    max_T = max(T)
    while x <= max_T:
        unlucky[x] = True
        x = x + (x % itr) + 7
        itr += 1

    F = [[-1 for kol in range(n)] for w in range(3)]
    # F[w][k] - maksymalna długość spójnego ciągu z liczb od T[0] do T[k] zawierającego dokładnie w k-pechowych liczb

    for kol in range(n):
        if T[kol] in unlucky:
            F[1][kol] = 1
        else:
            F[0][kol] = 1

    res = 0
    for kol in range(n-1):
        for w in range(3):
            if F[w][kol] == -1:
                continue
            if T[kol+1] in unlucky:
                if w < 2:
                    F[w+1][kol+1] = max( F[w+1][kol+1] , F[w][kol] + 1 )
                    res = max(res, F[w+1][kol+1])
                continue
            F[w][kol+1] = max( F[w][kol+1] , F[w][kol] + 1 )
            res = max(res, F[w][kol+1])

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kunlucky, all_tests=True)

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 3.21 sek.
# Status testów: A A A A A A A A A A