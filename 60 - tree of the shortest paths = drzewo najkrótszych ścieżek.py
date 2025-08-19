# 60 - tree of the shortest paths = drzewo najkrótszych ścieżek
# Mamy dany ważony graf G i drzewo rozpinające T, które zawiera wierzchołek s.
# Znajdź algorytm, który sprawdza, czy T jest drzewem najkrótszych ścieżek z wierzchołka s.
# Drzewo najkrótszych ścieżek to drzewo rozpinające, w którym ścieżka od pewnego wierzchołka
# źródłowego (s) do każdego innego wierzchołka w tym drzewie jest jednocześnie najkrótszą
# możliwą ścieżką między tymi wierzchołkami w oryginalnym grafie.

from math import inf
from queue import PriorityQueue

def tree_of_the_shortest_paths(G,T,s):
    def dijkstra(graph,s):
        n = len(graph)
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
            for u,weight in graph[v]:
                if d[u] > d[v] + weight:
                    d[u] = d[v] + weight
                    pq.put( (d[u],u) )
        return d

    d_graph = dijkstra(G,s)
    d_tree = dijkstra(T,s)

    return d_graph == d_tree

# Przykładowy test - oczekiwana wartość: True
G = [[(1, 6), (3, 1)], [(0, 6), (3, 7), (6, 11), (2, 1), (4, 3), (5, 2)], [(4, 5), (1, 1)],
     [(1, 7), (0, 1), (5, 2)], [(2, 5), (1, 3)], [(3, 2), (1, 2), (6, 3)], [(1, 11), (5, 3)]]
T = [[(3, 1)], [(2, 1), (4, 3), (5, 2)], [(1, 1)], [(0, 1), (5, 2)], [(1, 3)], [(3, 2), (1, 2), (6, 3)], [(5, 3)]]
print(tree_of_the_shortest_paths(G,T,0))
# Przykładowy test - oczekiwana wartość: False
G = [[(1, 5), (3, 1)], [(0, 5), (3, 7), (6, 11), (2, 1), (4, 3), (5, 3)], [(4, 5), (1, 1)],
     [(1, 7), (0, 1), (5, 2)], [(2, 5), (1, 3)], [(3, 2), (1, 3), (6, 3)], [(1, 11), (5, 3)]]
T = [[(3, 1)], [(2, 1), (4, 3), (5, 3)], [(1, 1)], [(0, 1), (5, 2)], [(1, 3)], [(3, 2), (1, 3), (6, 3)], [(5, 3)]]
print(tree_of_the_shortest_paths(G,T,0))