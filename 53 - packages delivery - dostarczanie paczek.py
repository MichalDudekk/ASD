# 53 - packages delivery - dostarczanie paczek
# Bitlandia to kraina zawierająca N miast i N-1 dróg dwukierunkowych. System dróg tworzy spójny
# graf. Dana jest lista K miast, do których musimy dostarczyć paczki i mając możliwość
# rozpoczęcia i zakończenia trasy w dowolnym mieście, znajdź minimalną odległość, którą
# musimy pokonać, aby dostarczyć wszystkie paczki.
# Opis algorytmu na dole.

def diameter(G):
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

def delivery(G):
    n = len(G)
    visited = [False]*n
    to_visit = n
    res = 0

    def dfs_visit(v):
        nonlocal to_visit, res
        visited[v] = True
        to_visit -= 1

        for u in G[v]:
            if visited[u]:
                continue
            res += 1
            dfs_visit(u)
            res += 1

    dfs_visit(0)
    return res - diameter(G)

# Przykładowy test - oczekiwana wartość: 27
G = [[1], [0, 2], [1, 3, 4], [2, 6], [2, 5], [4], [3, 7, 8], [6], [6, 9, 10, 11],
         [8], [8], [8, 12, 16], [11, 13, 14], [12, 15], [12], [13], [11, 17, 18], [16], [16]]
print(delivery(G))

# Opis algorytmu - delivery(G) - O(V+E)
# Z polecenia wynika, że graf G jest drzewem. 
# Gdybyśmy mieli zacząć i zakończyć w tym samym wierzchołku, to zadanie byłoby banalne.
# Wystarczyłoby odpalić algorytm dfs i dodawać 1 do wyniku za każdym razem, gdy odwiedzamy
# nowy wierzchołek u oraz za każdym razem gdy z niego wracamy (dfs_visit(u) zakończy się).
# Jako, że mamy możliwość zacząć i zakończyć w dowolnych dwóch wierzchołkach to należy wybrać dwa najbardziej od siebie oddalone, w ten sposób zaoszczędzimy najwięcej drogi.
# Algorytm realizuje to przez odjęcie od wyniku średnicy grafu G, czyli długości ścieżki między dwoma najbardziej oddalonymi wierzchołkami.
