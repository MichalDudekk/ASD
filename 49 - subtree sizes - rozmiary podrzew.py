# 49 - subtree sizes - rozmiary poddrzew
# Dana jest lista krawędzi drzewa (niekoniecznie binarnego) oraz wyróżniony wierzchołek - korzeń.
# Każdy wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka, znajdź liczbę
# wierzchołków w jego poddrzewie.

def subtree_sizes(E,s):
    def edges_to_graph(E):
        n = 0
        for v,u in E:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v,u in E:
            G[v].append(u)
            G[u].append(v)
        return G

    G = edges_to_graph(E)
    n = len(G)
    sizes = [0]*n
    visited = [False]*n

    def dfs_visit(v):
        visited[v] = True
        for u in G[v]:
            if visited[u]:
                continue
            sizes[v] += dfs_visit(u)
        sizes[v] += 1
        return sizes[v]

    dfs_visit(s)
    return sizes

# Przykładowy test - oczekiwana wartość: [22, 10, 11, 9, 2, 7, 1, 3, 2, 3, 1, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
E = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [5, 11], [5, 12], [7, 13],
         [7, 14], [8, 15], [9, 16], [9, 17], [11, 18], [11, 19], [11, 20], [12, 21]]
print(subtree_sizes(E,0))