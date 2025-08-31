# 66 - edge reducing the distance - krawędź zmniejszająca dystans
# Dany jest ważony graf G z dodatnimi wagami. Dana jest również lista krawędzi E', które
# nie należą do grafu, ale są krawędziami między wierzchołkami w G. Podane są również
# dwa wierzchołki s i t. Określ, którą krawędź z E' należy dodać do grafu G, aby jak
# najbardziej zmniejszyć odległość między s i t. Jeśli żadna krawędź nie zmniejsza
# odległości między s i t, algorytm powinien zwrócić False.

from math import inf
from queue import PriorityQueue

# O(E' * E*log(V))
def reduce_distance(E,E2,s,t):
    def edges_to_graph(E):
        n = 0
        for v,u,w in E:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v, u, w in E:
            G[v].append((u,w))
            G[u].append((v,w))
        return G

    def dijkstra(G,s,t):
        n = len(G)
        d = [inf]*n
        visited = [False]*n
        pq = PriorityQueue()

        d[s] = 0
        pq.put( (d[s],s) )

        while not pq.empty():
            _ , v = pq.get()
            if visited[v]:
                continue
            visited[v] = True
            for u,weight in G[v]:
                if d[u] > d[v] + weight:
                    d[u] = d[v] + weight
                    pq.put( (d[u],u) )
        return d[t]

    res = dijkstra(edges_to_graph(E),s,t)
    ans = False

    for i in range(len(E2)):
        E.append(E2[i])
        d = dijkstra(edges_to_graph(E),s,t)
        if res > d:
            res = d
            ans = i
        E.pop()

    return E2[ans] if ans != False else False


# O( (E+E')*log(V) )
def better_reduce_distance(E,E2,s,t):
    def edges_to_graph(E,E2):
        n = 0
        for v,u,w in E:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v, u, w in E:
            G[v].append((u,w,-1))
            G[u].append((v,w,-1))

        for i in range(len(E2)):
            v, u, w = E2[i]
            G[v].append((u,w,i))
            G[u].append((v,w,i))

        return G

    def modified_dijkstra(G,s):
        n = len(G)
        d = [[inf,inf] for _ in range(n)]
        visited = [[False,False] for _ in range(n)]
        bonus_edge = [None]*n
        pq = PriorityQueue()

        d[s][0] = 0
        pq.put( (d[s][0],0,s) )

        while not pq.empty():
            _ , state , v = pq.get()
            if visited[v][state]:
                continue
            visited[v][state] = True
            for u,weight,edge in G[v]:
                if edge == -1:
                    if d[u][state] > d[v][state] + weight:
                        d[u][state] = d[v][state] + weight
                        if state == 1:
                            bonus_edge[u] = bonus_edge[v]
                        pq.put( (d[u][state],state,u) )
                    continue
                if state == 1:
                    continue
                if d[u][1] > d[v][0] + weight:
                    d[u][1] = d[v][0] + weight
                    bonus_edge[u] = edge
                    pq.put( (d[u][1],1,u) )
        return d,bonus_edge

    G = edges_to_graph(E,E2)
    d, bonus_edge = modified_dijkstra(G,s)
    return E2[bonus_edge[t]] if d[t][1] < d[t][0] else False


E  = [(0, 2, 5), (0, 4, 2), (2, 3, 6), (2, 5, 4), (1, 5, 5), (2, 6, 8), (5, 7, 6), (6, 7, 8),
      (6, 8, 4), (7, 8, 7)]
E2 = [(0, 1, 3), (1, 2, 4), (4, 3, 4),
      (3, 6, 5),
      (3, 8, 6),
      (5, 6, 3)]
# Przykładowy test - oczekiwana wartość: (5, 6, 3)
s = 0
t = 8
print(reduce_distance(E, E2, s, t))
print(better_reduce_distance(E, E2, s, t))
# Przykładowy test - oczekiwana wartość: (3, 8, 6)
s = 3
t = 8
print(reduce_distance(E, E2, s, t))
print(better_reduce_distance(E, E2, s, t))
# Przykładowy test - oczekiwana wartość: False
s = 0
t = 2
print(reduce_distance(E, E2, s, t))
print(better_reduce_distance(E, E2, s, t))







