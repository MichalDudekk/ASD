# egzamin 2022 termin 3 zadanie 1 - snow

from egz3atesty import runtests

# O(n*log(n))
def snow( T, I ):
    n = len(I)
    tab = []
    for s,t in I:
        tab.append( (s,0) )
        tab.append( (t,1) )
    tab.sort()

    res = 0
    current = 0
    for s,typ in tab:
        if typ == 0:
            current += 1
        else:
            current -= 1
        res = max(res,current)
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 2.00 sek.
# Status testów: A A A A A A A A A A