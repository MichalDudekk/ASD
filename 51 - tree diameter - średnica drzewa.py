# 51 - tree diameter - średnica drzewa
# Średnica drzewa to odległość między jego wierzchołkami, które są od siebie najbardziej
# oddalone. Znajdź algorytm, który, mając drzewo (niekoniecznie binarne) przedstawione
# jako lista krawędzi, zwróci jego średnicę.

def diameter(E):
    def edges_to_graph(E):
        n = 0
        for v,u in E:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v, u in E:
            G[v].append(u)
            G[u].append(v)
        return G

    G = edges_to_graph(E)
    n = len(G)
    visited = [False]*n
    res = 0

    def dfs_visit(v):
        visited[v] = True
        max_dist_a = 0
        max_dist_b = 0
        for u in G[v]:
            if visited[u]:
                continue
            dist = dfs_visit(u)

            if dist > max_dist_b:
                if dist > max_dist_a:
                    max_dist_a, max_dist_b = dist, max_dist_a
                else:
                    max_dist_b = dist

        nonlocal res
        res = max(res, max_dist_a + max_dist_b )
        return max_dist_a + 1

    dfs_visit(0)
    return res

# Przykładowy test - oczekiwana wartość: 10
E = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [4, 9], [5, 10], [7, 11],
         [7, 12], [7, 13], [8, 14], [8, 15], [11, 16], [11, 17], [13, 18], [16, 19], [19, 20]]
print(diameter(E))

