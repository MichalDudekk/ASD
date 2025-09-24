# 55 - domino
# Mamy układ domino. Mamy go jako listę par [a, b]. Jeśli przewrócimy klocek a, klocek
# b również się przewróci. Znajdź minimalną liczbę klocków, które należy przewrócić ręcznie,
# tak aby wszystkie domino upadły.
# Opis algorytmu na dole.

from math import inf

def domino(E):
    def edges_to_graph(E):
        n = 0
        for v,u in E:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v,u in E:
            G[v].append(u)
        return G

    def dfs(G,order):
        n = len(G)
        visited = [False]*n
        res = []

        def dfs_visit(v):
            visited[v] = True
            for u in G[v]:
                if visited[u]:
                    continue
                dfs_visit(u)
            res.append(v)

        ctr = 0
        for i in order:
            if visited[i]:
                continue
            dfs_visit(i)
            ctr += 1

        res.reverse()
        return res, ctr

    G = edges_to_graph(E)
    n = len(G)
    new_order , _ = dfs(G,[i for i in range(n)])
    _ , ans = dfs(G,new_order)
    return ans

# Przykładowy test - oczekiwana wartość: 2
E = [[0, 1], [1, 2], [2, 3], [3, 1], [3, 5], [4, 2], [5, 6], [6, 7], [7, 8], [8, 9], [9, 6]]
print(domino(E))
# Przykładowy test - oczekiwana wartość: 3
E = [[0, 1], [1, 2], [3, 2], [2, 4], [4, 1], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 6],
     [4, 7], [4, 6], [5, 9], [10, 0], [15, 14], [15, 11], [15, 11], [11, 13], [14, 13], [5, 13],
     [16, 8], [0, 12], [12, 3]]
print(domino(E))

# Opis algorytmu - domino(E) - O(V+E)
# Odpalamy algorytm odpowiedzialny za znajdywanie silnie spójnych składowych.
# Funkcja zwróci nam tablice indeksów w odwrotnej kolejności co do przetworzenia wierzchołków.
# Wynik tej funkcji zapisujemy w tablicy order.
# Następnie wywołujemy algorytm dfs. Przechodząc pętlą w kolejności zapisanej w tablicy order (ta pętla na dole funkcji dfs).
# Ilość razy kiedy ręcznie wywołaliśmy dfs_visit to wynik naszego algorytmu - ctr.