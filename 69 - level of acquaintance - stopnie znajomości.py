# 69 - level of acquaintance - stopnie znajomości
# Zadanie 1: Stopnie znajomości
# Definiujemy relację znajomości między osobami jako symetryczną.
# Znajomość:
# - pierwszego stopnia to bezpośrednia znajomość osoby
# - drugiego stopnia to bycie "znajomym znajomego" osoby, ale nie bezpośrednim znajomym
#   osoby
# - trzeciego, czwartego, piątego stopnia, itd.
# - nieskończonego stopnia zachodzi wtedy gdy nie ma ciągu znajomości, który łączyłby dwie
#   osoby
# Mając na wejściu listę osób i znajomości pierwszego stopnia między nimi, chcemy znaleźć
# największy stopień znajomości wśród każdej z możliwych par.

from math import inf
from collections import deque

def acquaintance_degree(E):
    def edges_to_graph(E):
        n = 0
        for v,u in E:
            n = max(n,v,u)
        n+=1
        G = [[] for _ in range(n)]
        for v,u in E:
            G[v].append(u)
            G[u].append(v)
        return G

    def bfs(G,s):
        n = len(G)
        d = [inf]*n
        visited = [False]*n
        q = deque()

        d[s] = 0
        visited[s] = True
        q.append(s)

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
    n = len(G)
    res = 0
    for i in range(n):
        d = bfs(G,i)
        res = max(res,max(d))
    return res

# Przykładowy test - oczekiwana wartość: 5
P = [(0, 1), (1, 2), (1, 6), (1, 3), (2, 3), (2, 6), (0, 7), (7, 6), (3, 4), (6, 4), (4, 5), (6, 5),
     (5, 9), (8, 9), (8, 10), (9, 10)]
print(acquaintance_degree(P))
# Przykładowy test - oczekiwana wartość: inf
P = [(0, 1), (1, 2), (1, 6), (1, 3), (2, 3), (2, 6), (0, 7), (7, 6), (3, 4), (6, 4), (4, 5), (6, 5),
     (8, 9), (8, 10), (9, 10)]
print(acquaintance_degree(P))
