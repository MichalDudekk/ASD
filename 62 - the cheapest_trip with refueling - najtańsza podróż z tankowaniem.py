# 62 - the cheapest trip with refueling - najtańsza podróż z tankowaniem
# Dostajemy na wejściu graf, w którym wierzchołkami są miasta, a krawędziami drogi między nimi.
# Dla każdego miasta znamy cenę paliwa w złotych na litr (tablica C), a dla każdej drogi jej długość w
# kilometrach.
# Nasz samochód ma zbiornik pojemności 100 litrów i pali jeden litr na kilometr.
# Startujemy z miasta s z pustym zbiornikiem. Ile minimalnie musimy zapłacić za paliwo, aby dotrzeć
# do miasta t?

from math import inf
from queue import PriorityQueue

def fuel(G,C,s,t):
    n = len(G)
    d = [[inf for _ in range(101)] for _ in range(n)]
    visited = [[False for _ in range(101)] for _ in range(n)]
    pq = PriorityQueue()

    d[s][0] = 0
    pq.put( (d[s][0],s,0) )

    while not pq.empty():
        _ , v , state = pq.get()
        if visited[v][state]:
            continue
        visited[v][state] = True
        # driving
        for u,weight in G[v]:
            new_state = state - weight
            if new_state < 0:
                continue
            if d[u][new_state] > d[v][state]:
                d[u][new_state] = d[v][state]
                pq.put( (d[u][new_state],u,new_state) )
        # fueling
        for i in range(1, 101 - state):
            if d[v][state + i] > d[v][state] + ( i*C[v] ):
                d[v][state + i] = d[v][state] + ( i*C[v] )
                pq.put( (d[v][state + i],v, state+i ) )
    res = inf
    for i in range(101):
        res = min(res,d[t][i])
    return res

# Przykładowy test - oczekiwana wartość: 79
G = [[(1, 5), (2, 7)], [(0, 5), (2, 3)], [(1, 3), (0, 7), (3, 4)], [(2, 4), (4, 6)], [(3, 6)]]
C = [8, 5, 3, 2, 1]
s = 0
t = 4
print(fuel(G,C,s,t))








