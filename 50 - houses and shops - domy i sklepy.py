# 50 - houses and shops - domy i sklepy
# Mamy mapę miasta, na której znajdują się domy i sklepy. Są też drogi (każda o długości 1),
# które łączą dom z domem lub dom ze sklepem. Musimy znaleźć dla każdego domu odległość
# do najbliższego sklepu.

from math import inf
from collections import deque

def houses_and_shops(E,shops):
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

    def bfs(G,shops):
        n = len(G)
        d = [inf]*n
        visited = [False]*n
        q = deque()

        for shop in shops:
            visited[shop] = True
            d[shop] = 0
            q.append(shop)

        while q:
            v = q.popleft()
            for u in G[v]:
                if visited[u]:
                    continue
                visited[u] = True
                d[u] = d[v] + 1
                q.append(u)
        return d

    G = edges_to_graph(E)
    return bfs(G,shops)

# Przykładowy test - oczekiwana wartość: [1, 1, 0, 0, 2, 1, 1, 1, 1, 0, 1, 1, 2, 2]
roads = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [1, 5], [2, 5], [2, 6], [2, 7], [3, 6], [3, 8],
         [4, 8], [4, 5], [5, 7], [6, 7], [8, 9], [9, 10], [9, 11], [10, 13], [11, 12], [12, 13]]
shops = [2, 3, 9]
print(houses_and_shops(roads, shops))