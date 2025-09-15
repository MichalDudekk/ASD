# egzamin 2022 termin 2 zadanie 2 - magic

from egz2btesty import runtests

# O(n)
def magic( C ):
    n = len(C)

    F = [-1 for k in range(n)]
    # F[k] - maksymalna liczba sztabek złota z którymi można dojść do komnaty k
    F[0] = 0

    for k in range(n-1):
        if F[k] == -1:
            continue
        chest = C[k][0]
        for i in range(1,4):
            price, v = C[k][i]
            if v == -1:
                continue
            if price < chest - 10:
                continue
            if price > chest + F[k]:
                continue
            if price >= chest:
                gold = F[k] - (price - chest)
                F[v] = max(F[v],gold)
                continue
            gold = F[k] + (chest - price)
            F[v] = max(F[v],gold)

    return F[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 0.08 sek.
# Status testów: A A A A A A A A A A