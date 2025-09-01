# 70 - traffic jams in cracow - krakowskie korki
# W Krakowie w godzinach szczytu są korki, dlatego kierowcom bardziej zależy na czasie niż na realnej odległości
# między dwoma punktami. Mamy mapę Krakowa, między skrzyżowaniami na ulicach są zaznaczone odległości i
# czasy przejazdu. W Krakowie (jak wszyscy wiemy ;)) są ulice jedno- i dwukierunkowe. Kierowcy potrzebują aplikacji,
# która pomoże im znajdować drogi, które pozwalają dotrzeć ze skrzyżowania A do B w jak najkrótszym czasie, a
# spośród tych o najmniejszym czasie wybiera i zwraca najkrótszą pod względem odległości.

from math import inf
from queue import PriorityQueue

def trafic_jams(E,s,r):
    def edges_to_graph(E):
        n = 0
        for v,u,time,weight in E:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v,u,time,weight in E:
            G[v].append( (u,weight,time) )
        return G

    def dijkstra(G,s,r):
        n = len(G)
        d = [inf]*n     # distance
        t = [inf]*n     # time
        visited = [False]*n
        pq = PriorityQueue()

        t[s] = 0
        d[s] = 0
        pq.put( (t[s],d[s],s) )

        while not pq.empty():
            _ , _ , v = pq.get()
            if visited[v]:
                continue
            visited[v] = True
            for u,weight,time in G[v]:
                if t[u] > t[v] + time:
                    t[u] = t[v] + time
                    d[u] = d[v] + weight
                    pq.put( (t[u],d[u],u) )
        return t[r],d[r]

    G = edges_to_graph(E)
    return dijkstra(G,s,r)

# Przykładowy test - oczekiwana wartość: (83, 62)
E = [(0, 7, 7, 12), (0, 1, 3, 5), (1, 0, 3, 5), (1, 2, 1, 2), (2, 1, 1, 2), (2, 3, 1, 2), (3, 2, 1, 2),
     (2, 4, 1, 2), (4, 2, 1, 2), (5, 0, 10, 7), (5, 7, 31, 21), (5, 15, 12, 10), (6, 9, 16, 6), (6, 5, 18, 12),
     (7, 5, 31, 21), (7, 6, 12, 6), (7, 8, 15, 13), (8, 7, 13, 15), (8, 9, 25, 12), (8, 24, 14, 10),
     (9, 13, 20, 5), (10, 29, 4, 2), (11, 29, 5, 3), (12, 29, 3, 2), (13, 29, 19, 2), (13, 9, 20, 5),
     (13, 20, 22, 9), (14, 13, 18, 2), (15, 13, 16, 3), (16, 14, 3, 4), (17, 18, 2, 4), (18, 17, 2, 4),
     (18, 16, 1, 1), (19, 28, 32, 20), (19, 18, 7, 5), (19, 15, 11, 16), (20, 19, 11, 12), (20, 13, 22, 9),
     (20, 25, 26, 15), (21, 22, 3, 3), (22, 21, 3, 3), (22, 23, 1, 2), (22, 24, 2, 4), (23, 22, 1, 2),
     (24, 22, 2, 4), (24, 20, 8, 4), (25, 20, 26, 15), (25, 28, 13, 8), (25, 8, 10, 21), (26, 27, 3, 5),
     (26, 28, 7, 5), (27, 26, 3, 5), (28, 26, 7, 5), (28, 20, 20, 14), (28, 19, 32, 20), (29, 10, 4, 2),
     (29, 11, 5, 3), (29, 12, 3, 2), (29, 13, 19, 2)]
s = 0
t = 28
print(trafic_jams(E,s,t))
# Przykładowy test - oczekiwana wartość: (79, 34)
s = 0
t = 11
print(trafic_jams(E,s,t))
# Przykładowy test - oczekiwana wartość: (48, 16)
s = 17
t = 11
print(trafic_jams(E,s,t))
