# 61 - super cool paths - superfajne ścieżki
# Mamy dany ważony graf G. Super fajna ścieżka to taka, która jest nie tylko najkrótszą
# ścieżką ważoną między v i u, ale także ma najmniej krawędzi (innymi słowy szukamy
# najkrótszych ścieżek pod względem liczby krawędzi spośród najkrótszych ścieżek w
# sensie wagowym). Znajdź algorytm, który dla danego wierzchołka początkowego s znajdzie
# super fajne ścieżki do innych wierzchołków.

from math import inf
from queue import PriorityQueue

def modified_dijkstra(G,s):
    n = len(G)
    d = [inf]*n
    visited = [False]*n
    parent = [None]*n
    pq = PriorityQueue()
    how_many_edges = [inf]*n

    d[s] = 0
    how_many_edges[s] = 0
    pq.put( (d[s],how_many_edges[s],s) )

    while not pq.empty():
        _ , _ , v = pq.get()
        if visited[v]:
            continue
        visited[v] = True
        for u,weight in G[v]:
            if d[u] > d[v] + weight:
                d[u] = d[v] + weight
                parent[u] = v
                how_many_edges[u] = how_many_edges[v] + 1
                pq.put( (d[u],how_many_edges[u],u) )
    return d,parent

def get_path(G,s,v):
    d,parent = modified_dijkstra(G,s)
    path = []
    current = v
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    print(d[v],path)

# Przykładowy test - oczekiwane wartości:   4 [0, 3, 4]
#                                           2 [0, 1, 2]
G = [[(4, 5), (3, 2), (1, 1)], [(0, 1), (2, 1)], [(1, 1), (4, 2)], [(0, 2), (4, 2)], [(0, 5), (2, 2), (3, 2)]]
s = 0
get_path(G,s,4)
get_path(G,s,2)
# Przykładowy test - oczekiwane wartości:   8 [0, 6, 4]
#                                           11 [0, 1, 2, 3]
G = [[(1, 2), (6, 2)], [(0, 2), (2, 5)], [(1, 5), (3, 4)], [(2, 4), (4, 3)], [(6, 6), (5, 2), (3, 3)], [(6, 4), (4, 2)], [(0, 2), (5, 4), (4, 6)]]
s = 0
get_path(G,s,4)
get_path(G,s,3)