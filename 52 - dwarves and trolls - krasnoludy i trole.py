# 52 - dwarves and trolls - krasnoludy i trolle
# Wyobraźmy sobie podziemny labirynt składający się z ogromnych jaskiń połączonych
# wąskimi korytarzami. W jednej z jaskiń krasnoludy zbudowały swoją osadę, a w każdej
# z pozostałych jaskiń żyje pewna liczba trolli. Krasnoludy chcą zaplanować swoją
# obronę na wypadek ataku trolli. Zamierzają zakraść się i podłożyć ładunek wybuchowy
# w jednym z korytarzy, tak aby trolle mieszkające za tym korytarzem nie miały
# ścieżki, żeby dotrzeć do osady krasnoludów. Który z korytarzy powinien zostać
# wysadzony w powietrze, żeby odciąć jak największej ilości trolli dostęp do osady krasnoludów.
# Podaj krawędź, która powinna zostać wysadzona i liczbę trolli, którą uda się wtedy odciąć.

from math import inf

def dwarves_and_trolls(G,T,village):
    def find_bridges(G,village):
        res = []

        n = len(G)
        visited = [False] * n
        parent = [None] * n
        discovered = [inf] * n
        low = [inf] * n
        time = 0

        def dfs_visit(v):
            nonlocal time
            time += 1
            visited[v] = True
            discovered[v] = time
            low[v] = discovered[v]

            for u in G[v]:
                if visited[u]:
                    if u != parent[v]:
                        low[v] = min(low[v], discovered[u])
                    continue
                parent[u] = v
                dfs_visit(u)
                low[v] = min(low[v], low[u])

            if discovered[v] == low[v] and parent[v] is not None:
                res.append((parent[v], v))

        dfs_visit(village)
        return res

    def how_many_trolls(s,parent):
        n = len(G)
        visited = [(True if i == parent else False) for i in range(n)]

        def dfs_visit(v):
            visited[v] = True
            res = T[v]
            for u in G[v]:
                if visited[u]:
                    continue
                res += dfs_visit(u)
            return res

        return dfs_visit(s)

    bridges = find_bridges(G, village)
    maxi = 0
    candidate = None

    for v,u in bridges:
        res = how_many_trolls(u,v)
        if res > maxi:
            maxi = res
            candidate = (v,u)

    return candidate, maxi


# Przykładowy test - oczekiwana wartość: ((0, 4), 32)
graph = [[1, 2, 3, 4], [0, 2, 5, 6], [0, 1, 3], [0, 2], [0, 9, 10], [1, 7, 8],
         [1], [5, 8], [5, 7], [4, 10], [4, 9, 11], [10]]
trolls = [0, 2, 8, 7, 17, 4, 13, 3, 12, 3, 1, 11]
village = 0
print(dwarves_and_trolls(graph, trolls, village))