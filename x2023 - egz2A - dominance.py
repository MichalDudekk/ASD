# egzamin 2023 termin 2 zadanie 1 - dominance

# Wartość dom jest niepoprawna (zaniżona) dla każdego punktu (a,b), takiego że istnieje taki punkt (c,d), że c > a i d > b.
# Jednak jeżeli taki punkt (c,d) istnieje to znaczy, że (a,b) i tak nie byłoby najbardziej dominującym punktem.
#
# Wartość dom jest poprawna dla każdego punktu (a,b) takiego że NIE istnieje taki punkt (c,d) że c > a i d > b.
# Wartość dom jest poprawna dla każdego punktu, który ma szanse być najbardziej dominującym, a dla puntów, które
# nie mają szans być najbardziej dominujące, ta wartość jest zaniżona.
# Z tego wynika, że biorąc maksiumum z obliczonych dom dla wszystkich punktów mamy gwarancje poprawnego wyniku.

from egz2atesty import runtests

# O(n)
def dominance(P):
    n = len(P)

    T = [0 for _ in range(n + 1)]
    F = [0 for _ in range(n + 1)]

    for x,y in P:
        T[y] += 1
        F[x] += 1

    for i in range(n-1,-1,-1):
        T[i] += T[i+1]
    for i in range(n-1,-1,-1):
        F[i] += F[i + 1]

    ans = 0
    for x,y in P:
        dom = n - T[y] - F[x] + 1
        ans = max(ans,dom)
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

# Liczba zaliczonych testów: 11/11
# Liczba testów z przekroczonym czasem: 0/11
# Liczba testów z błędnym wynikiem: 0/11
# Liczba testów zakończonych wyjątkiem: 0/11
# Orientacyjny łączny czas : 3.31 sek.
# Status testów: A A A A A A A A A A A