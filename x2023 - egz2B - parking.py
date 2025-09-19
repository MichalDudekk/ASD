# egzamin 2023 termin 2 zadanie 2 - parking

from egz2btesty import runtests
from math import inf

# O(m^3)
def parking_(X,Y):
    n = len(X)
    m = len(Y)

    F = [[-1 for k in range(n)] for w in range(m)]
    # F[w][k] - minimalna suma odległości biurowców z pozycji X[0], . . . , X[k] do przydzielonych
    # im działek, przy założeniu że biurowiec z pozycji X[k] ma przydzieloną działkę z pozycji Y[w]

    def recur(w,k):
        if F[w][k] != -1:
            return F[w][k]
        dist = abs(X[k] - Y[w])
        F[w][k] = inf
        if k == 0:
            F[w][k] = dist
            return F[w][k]
        for i in range(w-1,k-2,-1):
            F[w][k] = min( F[w][k] , dist + recur(i,k-1) )
        return F[w][k]

    res = inf
    for i in range(m-1,n-2,-1):
        res = min(res,recur(i,n-1))
    return res

# O(m*n) - top down
def parking(X,Y):
    n = len(X)
    m = len(Y)

    F = [[-1 for k in range(n)] for w in range(m)]
    # F[w][k] - minimalna suma odległości biurowców z pozycji X[0], . . . , X[k] do przydzielonych
    # im działek, przy założeniu że biurowiec z pozycji X[k] ma przydzieloną działkę z pozycji Y[w] LUB WCZEŚNIEJSZĄ.
    F[0][0] = abs(X[0] - Y[0])

    def recur(w,k):
        if F[w][k] != -1:
            return F[w][k]

        dist = abs(X[k] - Y[w])
        F[w][k] = dist
        if k != 0:
            F[w][k] = dist + recur(w-1, k-1)

        if w == k:
            return F[w][k]
        F[w][k] = min(F[w][k], recur(w-1,k) )
        return F[w][k]

    res = recur(m-1,n-1)
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
