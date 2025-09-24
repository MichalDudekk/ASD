# 57 - the sailor Henry - żeglarz Henryk
# Żeglarz Henryk mieszka na wyspie na pewnym archipelagu. Wszystkie wyspy, w tym archipelagu,
# są tak małe, że można je przedstawić jako punkty w przestrzeni R^2. Pozycje wszystkich
# wysp są podane jako sekwencja W = ((x1, y1), ..., (xn, yn)). Henryk mieszka na wyspie
# (x1, y1), ale chce przenieść się na wyspę (xn, yn). Normalnie każdego dnia może żeglować
# na wyspę oddaloną o co najwyżej Z odległości (w standardowej odległości euklidesowej).
# Może również żeglować na odległość do 2Z, pod warunkiem, że będzie odpoczywał przez cały
# następny dzień. Henryk zawsze musi nocować na jakiejś wyspie. Znajdź minimalną liczbę
# dni, której Henryk potrzebuje, aby dotrzeć do swojej docelowej wyspy (lub stwierdź,
# że jest to niemożliwe).
# Opis algorytmu na dole.

from math import sqrt, inf
from collections import deque

def sailor_henry(W,Z):
    n = len(W)
    G = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            x1,y1 = W[i]
            x2,y2 = W[j]
            dist = sqrt( (abs(x2-x1)**2) + (abs(y2-y1)**2) )

            if dist <= Z:
                G[i].append( (j,1) )
                G[j].append( (i,1) )
                continue
            if dist <= (2*Z):
                G[i].append( (j,2) )
                G[j].append( (i,2) )

    def delayed_bfs(G,s):
        n = len(G)
        d = [inf]*n
        visited = [False]*n
        q = deque()

        d[s] = 0
        q.append( (s, 0) )

        while q:
            v, delay = q.popleft()
            if visited[v]:
                continue
            if delay > 0:
                q.append( (v, delay-1) )
                continue
            visited[v] = True
            for u,weight in G[v]:
                if d[u] > d[v] + weight:
                    d[u] = d[v] + weight
                    q.append( (u, weight - 1) )
        return d

    d = delayed_bfs(G,0)
    return d[n-1]

# Przykładowy test - oczekiwana wartość: 10
W = [(0, 0), (0, 1), (2, 1), (1, 3), (2, 5), (3, 2), (5, 2), (4, 4), (3, 4), (4, 1), (2, 4), (5, 5)]
Z = 1
print(sailor_henry(W, Z))
# Przykładowy test - oczekiwana wartość: 4
W = [(-9.83, 7.32), (-7.12, 0.73), (-5.01, 6.81), (-2.35, 6.83), (0.23, 7.11), (-2.21, 5.12),
     (-6.03, 3.43), (-3.42, -1.21), (-1.96, 2.97), (2.58, 0.21), (4.12, 4.23), (10.12, 7.57), (8.02, 1.12)]
Z = 5
print(sailor_henry(W, Z))

# Opis algorytmu - sailor_henry(W, Z) - O(V+E)
# Cała trudność zadania polega na przygotowaniu grafu.
# Odległości między wierzchołkami to liczba dni potrzebna na przebycie dystansu:
#  1) 1 jeśli dist <= Z
#  2) 2 jeśli dist <= 2*Z
# W ten sposób jeśli Henryk chce przepłynąć odległość <= Z to zużywa jednen dzień, natomiast jeśli chce przepłynąć odległość <= 2*Z to zużywa dwa dni.
# Na przygotowanym grafie wystarczy odpalić algorytm delayed_bfs (bo wagi są liczbami naturalnymi ograniczonymi z góry przez 2) lub algorytm dijkstry, jednak wtedy złożoność jest gorsza O(E*log(V))
