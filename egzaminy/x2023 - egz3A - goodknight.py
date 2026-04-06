# egzamin 2024 termin 3 zadanie 1 - goodknight

from egz3atesty import runtests
from collections import deque
from math import inf

# O(n^2)
def goodknight(G, s, t):
    n = len(G)
    visited = [[False for _ in range(17)] for i in range(n)]
    d = [[inf for _ in range(17)] for i in range(n)]
    q = deque()

    d[s][0] = 0
    q.append( (s,0,0) )

    while q:
        v , state , delay = q.popleft()
        if visited[v][state]:
            continue
        if delay > 0:
            q.append( (v,state,delay-1) )
            continue
        visited[v][state] = True
        for u in range(n):
            if G[v][u] == -1:
                continue
            cost = G[v][u]
            new_state = state + cost

            if new_state <= 16:
                if d[u][new_state] > d[v][state] + cost:
                    d[u][new_state] = d[v][state] + cost
                    q.append( (u, new_state, cost - 1) )
            else:
                new_state = cost
                cost += 8
                if d[u][new_state] > d[v][state] + cost:
                    d[u][new_state] = d[v][state] + cost
                    q.append( (u, new_state, cost - 1) )

    res = inf
    for i in range(17):
        res = min(res,d[t][i])
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )

# Liczba zaliczonych testów: 8/8
# Liczba testów z przekroczonym czasem: 0/8
# Liczba testów z błędnym wynikiem: 0/8
# Liczba testów zakończonych wyjątkiem: 0/8
# Orientacyjny łączny czas : 0.30 sek.
# Status testów: A A A A A A A A
