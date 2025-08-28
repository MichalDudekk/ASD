# 48 - safe - sejf
# Mamy sejf, który można odblokować czterocyfrowym kodem PIN (0000 - 9999). Na wyświetlaczu
# pokazana jest aktualna liczba z przedziału (0000 - 9999). Poniżej
# wyświetlacza znajdują się przyciski z liczbami od 1 do 9999 (na przykład: 13, 223,
# 782, 3902). Ten sejf działa inaczej niż zwykły. Naciśnięcie przycisku z liczbą dodaje
# tę liczbę do liczby na wyświetlaczu. Jeśli suma jest większa niż 9999, pierwsza cyfra
# jest obcinana. Znamy kod PIN i liczby, które są aktualnie wyświetlane. Znajdź
# najkrótszą sekwencję naciśnięć przycisków, która pozwoli odblokować sejf. Jeśli taka
# sekwencja nie istnieje, zwróć None.
# Opis algorytmu na dole.

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

# Opis algorytmu - safe(buttons, display, PIN) - O(len(buttons))
# Na początku przygotowujemy graf. Wierzchołkami są wszystkie liczby z przedziału (0-9999). Każdy wierzchołek
# ma dokładnie tyle krawędzi ile jest przycisków w buttons. Dla każdego wierzchołka obliczamy do jakich innych
# wierzchołków dostaniemy się klikając w przyciski z tablicy buttons i dodajemy do nich krawędź.
# Po stworzeniu grafu wystarczy puścić zwykłego bfs-a z wierzchołka startowego display, który obliczy najkrótszą drogę do wierzchołka końcowego PIN.
# Na koniec, aby odtworzyć wynik, przechodzimy po "drzewie" stworzonym przez tablice patent, aż nie dojdziemy do wierzchołka startowego display.
# Złożoność obliczeniowa to O(len(buttons)), bo liczba wierzchołków jest ograniczona przez stałą 10000 co daje złożoność
# stałą O(1), jednak przez to, że liczba przycisków nie jest w żaden sposób ograniczona to złożoność jest zależna właśnie od niej O(len(buttons)).
# Gdyby liczba wierzchołków nie była ograniczona przez 10000 tylko przez n, to złożoność wynosiłaby O(n + n*len(buttons)) - złożoność algorytmu bfs.
