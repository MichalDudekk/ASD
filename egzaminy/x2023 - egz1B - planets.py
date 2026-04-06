# egzamin 2023 termin 1 zadanie 2 - planets
from egz1btesty import runtests
from math import inf

# O(n*E)
def planets( D, C, T, E ):
    n = len(D)

    F = [[inf for k in range(n)] for w in range(E+1)]
    # F[w][k] - minimalny koszt dostania się na planetę k mając dokładnie w paliwa
    F[0][0] = 0

    for k in range(n-1):
        for w in range(E+1):
            if F[w][k] == inf:
                continue
            if w == 0:      # teleportacja
                j,p = T[k]
                if k != j:
                    F[0][j] = min( F[0][j], F[0][k] + p )
            if w != E:      # tankowanie
                F[w+1][k] = min( F[w+1][k], F[w][k] + C[k] )

            dist = D[k+1] - D[k]
            if dist <= w:   # lot
                F[w - dist][k+1] = min( F[w - dist][k+1] , F[w][k] )
    res = inf
    for w in range(E+1):
        res = min(res,F[w][n-1])
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 0.73 sek.
# Status testów: A A A A A A A A A A