# egzamin 2023 termin 1 zadanie 1 - gold
from egz1Atesty import runtests
from math import inf
from queue import PriorityQueue

# O(V^2 * log(V))
def gold(G,V,s,t,r):
    n = len(G)
    visited = [[False for _ in range(2)] for i in range(n)]
    d = [[inf for _ in range(2)] for i in range(n)]
    pq = PriorityQueue()

    d[s][0] = 0
    pq.put( (0,d[s][0],s) )

    while not pq.empty():
        state , _ , v = pq.get()
        if visited[v][state]:
            continue
        visited[v][state] = True

        if state == 0:
            if d[v][1] > d[v][0] - V[v]:
                d[v][1] = d[v][0] - V[v]
                pq.put( (1,d[v][1],v) )

        for u,weight in G[v]:
            if state == 1:
                weight = (2*weight) + r

            if d[u][state] > d[v][state] + weight:
                d[u][state] = d[v][state] + weight
                pq.put( (state,d[u][state],u) )
    return d[t][1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )

# Liczba zaliczonych testów: 10/10
# Liczba testów z przekroczonym czasem: 0/10
# Liczba testów z błędnym wynikiem: 0/10
# Liczba testów zakończonych wyjątkiem: 0/10
# Orientacyjny łączny czas : 2.46 sek.
# Status testów: A A A A A A A A A A
