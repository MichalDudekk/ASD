# 12 - traveling salesman - problem komiwojażera (na grafie pełnym)
# Dany jest zbiór miast i odległości między każdą parą miast. Znajdź najkrótszą możliwą trasę,
# która odwiedza każde miasto dokładnie raz i wraca do miasta początkowego.
# Opis algorytmu na dole.
from math import inf

# O(n!)
def traveling_salesman(G):
    n = len(G)

    def recur(v, s, visited):
        ans = inf
        flag = True
        for i in range(n):
            if not visited[i]:
                flag = False
                new_visited = [visited[k] for k in range(n)]
                new_visited[i] = True
                ans = min(ans, recur(i,s,new_visited) + G[v][i])
        if flag:
            return G[v][s]
        return ans

    s = 0
    res = recur(s,s,[ (True if i == s else False) for i in range(n)])
    return res

# Przykładowy test - oczekiwana wartość: 45
distances = [
    [0, 10, 15],  # Odległości z miasta 0
    [10, 0, 20],   # Odległości z miasta 1
    [15, 20, 0]     # Odległości z miasta 2
]
print(traveling_salesman(distances))
# Przykładowy test - oczekiwana wartość: 26
distances = [
    [0, 5, 6, 8],
    [5, 0, 9, 7],
    [6, 9, 0, 8],
    [8, 7, 8, 0]
]
print(traveling_salesman(distances))

# Opis algorytmu - traveling_salesman(G) - O(n!)
# Dla każdego wywołania recur(v, s, visited) algorytm zapamiętuje, które miasta zostały już odwiedzone.
# Następnie sprawdza każdą ścieżke do miast, które nie zostały jeszcze odwiedzone.
# W wierzchołku startowym ma (n) możliwości, w następnym (n-1), w kolejnym (n-2) etc, dlatego złożoność to O(n!).

# Istnieje jeszcze rozwiązanie bitoniczne tego problemu, które ma złożoność O(n^2), jednak
# nie gwarantuje ono optymalnego wyniku, a jedynie przybliżony.
