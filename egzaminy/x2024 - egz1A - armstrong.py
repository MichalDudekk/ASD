# egzamin 2024 termin 1 zadanie 1 - armstrong
# Opis algorytmu - armstrong( B, G, s, t) - O(E*log(V)):
# Funkcja edges_to_graph(E) zamienia listę krawędzi G na graf w postaci listy sąsiedztwa.
# Uruchamiam algorytm dijkstry z wierzchołka końcowego t i zapisuje wynik w d_finish.
# Dla każdego roweru (i,p,q) w B dodaje do i-tego wierzchołka krawędź do wierzchołka końcowego t.
# Waga tej krawędzi to (p/q) * d_finish[i], czyli (p/q) * najkrótsza ścieżka z wierzchołka i do wierzchołka t.
# Uruchamiam algorytm dijkstry z wierzchołka startowego s na grafie wzbogaconym o nowe krawędzie.
# Najkrótsza ścieżka z s do t zwrócona przez algorytm dijkstry (zaokrąglona do minut w dół) to wynik algorytmu.

from egz1atesty import runtests

from math import inf,floor
from queue import PriorityQueue

# O(V*E*log(V))
def armstrong_worse( B, G, s, t):
    def edges_to_graph(E):
        n = 0
        for v,u,w in E:
            n = max(n,v,u)
        n += 1
        graph = [[] for _ in range(n)]
        for v,u,w in E:
            graph[v].append( (u,w) )
            graph[u].append( (v,w) )
        return graph

    def dijkstra(graph,start):
        n = len(graph)
        d = [inf]*n
        visited = [False]*n
        pq = PriorityQueue()

        d[start] = 0
        pq.put( (d[start],start) )

        while not pq.empty():
            _ , v = pq.get()
            if visited[v]:
                continue
            visited[v] = True
            for u,weight in graph[v]:
                if d[u] > d[v] + weight:
                    d[u] = d[v] + weight
                    pq.put( (d[u],u) )
        return d

    graph = edges_to_graph(G)
    n = len(graph)

    add = []
    for i,p,q in B:
        d = dijkstra(graph,i)
        path = d[t]
        time = (p/q) * path
        add.append( (i,time) )

    for i,time in add:
        graph[i].append( (t,time) )

    d_start = dijkstra(graph,s)
    return floor(d_start[t])

# O(E*log(V))
def armstrong( B, G, s, t):
    def edges_to_graph(E):
        n = 0
        for v,u,w in E:
            n = max(n,v,u)
        n += 1
        graph = [[] for _ in range(n)]
        for v,u,w in E:
            graph[v].append( (u,w) )
            graph[u].append( (v,w) )
        return graph

    def dijkstra(graph,start):
        n = len(graph)
        d = [inf]*n
        visited = [False]*n
        pq = PriorityQueue()

        d[start] = 0
        pq.put( (d[start],start) )

        while not pq.empty():
            _ , v = pq.get()
            if visited[v]:
                continue
            visited[v] = True
            for u,weight in graph[v]:
                if d[u] > d[v] + weight:
                    d[u] = d[v] + weight
                    pq.put( (d[u],u) )
        return d

    graph = edges_to_graph(G)
    n = len(graph)
    d_finish = dijkstra(graph,t)

    for i,p,q in B:
        time = (p/q) * d_finish[i]
        graph[i].append( (t,time) )

    d_start = dijkstra(graph,s)
    return floor(d_start[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )

# Liczba zaliczonych testów: 14/14
# Liczba testów z przekroczonym czasem: 0/14
# Liczba testów z błędnym wynikiem: 0/14
# Liczba testów zakończonych wyjątkiem: 0/14
# Orientacyjny łączny czas : 0.44 sek.
# Status testów: A A A A A A A A A A A A A A