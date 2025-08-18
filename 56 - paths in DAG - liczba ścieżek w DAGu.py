# 56 - paths in DAG - liczba ścieżek w DAGu
# Otrzymujemy jako dane wejściowe skierowany graf acykliczny (DAG - Directed Acyclic Graph)
# w postaci listy krawędzi oraz parę wierzchołków s i t. Znajdź, ile jest możliwych ścieżek
# między s a t.

def paths_in_dag(E,s,t):
    def edges_to_graph(E):
        n = 0
        for v,u in E:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v,u in E:
            G[v].append(u)
        return G

    def dfs_visit(v,t):
        nonlocal res
        if v == t:
            res += 1
        for u in G[v]:
            dfs_visit(u,t)

    G = edges_to_graph(E)
    res = 0
    dfs_visit(s,t)
    return res

# Przykładowy test - oczekiwana wartość: 3
E = [[0, 1], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [3, 5], [4, 6], [6, 5]]
s = 1
t = 4
print(paths_in_dag(E, s, t))
# Przykładowy test - oczekiwana wartość: 9
E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (2, 6), (1, 6), (6, 3), (6, 9), (9, 10), (6, 7), (7, 10),
     (7, 8), (10, 11), (11, 8), (8, 4)]
s = 0
t = 5
print(paths_in_dag(E, s, t))