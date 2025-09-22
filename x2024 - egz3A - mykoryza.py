# egzamin 2024 termin 3 zadanie 1 - mykoryza

from egz3atesty import runtests
from collections import deque

# O(V+E)
def mykoryza( G,T,d ):
    n = len(G)
    res = 0
    visited = [False]*n
    q = deque()

    for i in range(len(T)):
        q.append( (T[i],i) )

    while q:
        v,shroom = q.popleft()
        if visited[v]:
            continue
        if shroom == d:
            res += 1
        visited[v] = True
        for u in G[v]:
            if visited[u]:
                continue
            q.append( (u,shroom) )
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 2.11 sek.
# Status testów: A A A A A A A A A A