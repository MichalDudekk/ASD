# 68 - weird fees - dziwne opłaty
# Transport publiczny w pewnym mieście jest dość dziwnie zorganizowany. Za każdy odcinek
# między dwoma stacjami pobierana jest osobna opłata. Jednakże od tej kwoty odejmuje się
# całkowity koszt poniesiony od początku podróży (jeśli jest ujemny, po prostu nic nie
# płacisz). Mamy dany graf połączeń w dowolnej reprezentacji (nieskierowany, ważony).
# Znajdź minimalny koszt przejazdu między wierzchołkiem s a wierzchołkiem t.

from math import inf
from queue import PriorityQueue

def weird_fees(G,s,t):
    n = len(G)
    d = [inf]*n
    visited = [False]*n
    pq = PriorityQueue()

    d[s] = 0
    pq.put( (d[s],s,0) )

    while not pq.empty():
        _ , v , fee = pq.get()
        if visited[v]:
            continue
        visited[v] = True
        for u,weight in G[v]:
            cost = max(0,weight-fee)
            if d[u] > d[v] + cost:
                d[u] = d[v] + cost
                pq.put( (d[u], u, fee+cost) )
    return d[t]

# Przykładowy test - oczekiwana wartość: 80
G = [[(1, 60), (4, 120)], [(0, 60), (2, 80)], [(1, 80), (3, 70)], [(2, 70), (4, 150)], [(3, 150), (0, 120)]]
s = 0
t = 3
print(weird_fees(G,s,t))
# Przykładowy test - oczekiwana wartość: 120
s = 3
t = 4
print(weird_fees(G,s,t))