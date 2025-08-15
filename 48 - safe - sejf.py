# 48 - safe - sejf
# Mamy sejf, który można odblokować czterocyfrowym kodem PIN (0000 - 9999). Na wyświetlaczu
# pokazana jest aktualna liczba z przedziału (0000 - 9999). Poniżej
# wyświetlacza znajdują się przyciski z liczbami od 1 do 9999 (na przykład: 13, 223,
# 782, 3902). Ten sejf działa inaczej niż zwykły. Naciśnięcie przycisku z liczbą dodaje
# tę liczbę do liczby na wyświetlaczu. Jeśli suma jest większa niż 9999, pierwsza cyfra
# jest obcinana. Znamy kod PIN i liczby, które są aktualnie wyświetlane. Znajdź
# najkrótszą sekwencję naciśnięć przycisków, która pozwoli odblokować sejf. Jeśli taka
# sekwencja nie istnieje, zwróć None.

from collections import deque
from math import inf

def safe(buttons, start, PIN):
    n = 10000
    G = [[] for _ in range(n)]

    for button in buttons:
        for i in range(n):
            v = button + i
            if v >= n:
                v -= n        # 15187 -> 5187
            G[i].append( (v,button) )

    def bfs(G,start):
        n = len(G)
        d = [inf]*n
        visited = [False]*n
        parent = [None]*n
        q = deque()

        d[start] = 0
        q.append(start)

        while q:
            v = q.popleft()
            for u,button in G[v]:
                if visited[u]:
                    continue
                visited[u] = True
                d[u] = d[v] + 1
                parent[u] = (v,button)
                q.append(u)

        return visited,parent

    visited,parent = bfs(G,start)
    if not visited[PIN]:
        return None
    res = []
    current = PIN
    while current != start:
        current,button = parent[current]
        res.append(button)
    res.reverse()
    return res

# Przykładowy test - oczekiwana wartość: [13, 13, 782, 782, 782, 782, 782, 782, 782, 782, 782, 782, 3902, 3902, 500]
display = 1234
PIN = 7384
buttons = [13, 223, 782, 3902, 500]
print(safe(buttons, display, PIN))

