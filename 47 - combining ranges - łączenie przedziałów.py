# 47 - combining ranges - łączenie przedziałów
# Dany jest zbiór przedziałów [ai, bi]. Dwa przedziały mogą być połączone, jeśli mają
# dokładnie jeden wspólny punkt. Znajdź algorytm, który sprawdza, czy można uzyskać
# przedział [a, b] poprzez łączenie tych przedziałów.
# Opis algorytmu na dole

def ranges(T,a,b):
    n = max(t[1] for t in T) + 1
    G = [[] for _ in range(n)]
    for x,y in T:
        G[x].append(y)
        G[y].append(x)

    visited = [False]*n

    def dfs_visit(v):
        visited[v] = True
        for u in G[v]:
            if visited[u]:
                continue
            dfs_visit(u)

    dfs_visit(a)
    return visited[b]

# Przykładowy test - oczekiwana wartość: True
T = [[1, 3], [2, 3], [4, 5], [5, 7], [0, 6], [6, 7], [0, 2], [3, 4], [8, 9]]
a = 0
b = 1
print(ranges(T,a,b))
# Przykładowy test - oczekiwana wartość: False
T = [[1, 3], [2, 3], [4, 5], [5, 7], [0, 6], [6, 7], [0, 2], [3, 4], [8, 9]]
a = 5
b = 9
print(ranges(T,a,b))

# Opis algorytmu - ranges(T,a,b) - O(V+E)
# Tworzymy graf - wierzchołkami są początki i końce przedziałów, a krawędzie to przedziały łączące je.
# Interesuje nas czy istnieje ścieżka z a do b. W tym celu odpalamy dfs_visit() z wierzchołka a.
# Jeśli visited[b] == True to znaczy, że można uzyskać przedział [a,b].
