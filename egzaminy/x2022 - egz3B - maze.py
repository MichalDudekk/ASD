# egzamin 2022 termin 3 zadanie 2 - maze

from egz3btesty import runtests

# O(n^2)
def maze( L ):
    n = len(L)

    F = [[-1 if L[w][k] == '.' else -2 for k in range(n)] for w in range(n)]
    # F[w][k] - maksymalna liczba komnat, które może odwiedzić wojownik kończąc na polu (w,k)
    F[0][0] = 0

    for k in range(n):
        down = [F[w][k] for w in range(n)]
        up = [F[w][k] for w in range(n)]
        # down
        for w in range(n):
            if down[w] == -1 or down[w] == -2:
                continue
            if w+1 < n:
                if down[w+1] != -2 and down[w+1] < down[w] + 1:
                    down[w+1] = down[w] + 1
        # up
        for w in range(n-1,-1,-1):
            if up[w] == -1 or up[w] == -2:
                continue
            if w-1 >= 0:
                if up[w-1] != -2 and up[w-1] < up[w] + 1:
                    up[w-1] = up[w] + 1
        # right
        for w in range(n):
            if k < n - 1:
                F[w][k] = max(down[w],up[w])
                if F[w][k] != -1 and F[w][k] != -2:
                    if k + 1 < n:
                        if F[w][k + 1] != -2:
                            F[w][k + 1] = F[w][k] + 1
            else:
                F[w][k] = max(F[w][k],down[w])

    return F[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 0.98 sek.
# Status testów: A A A A A A A A A A
