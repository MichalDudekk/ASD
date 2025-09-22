# egzamin 2024 termin 2 zadanie 2 - tory_amos
# Opis algorytmu - tory_amos( E, A, B ) - O(m):
# Funkcja edges_to_graph(E) zamienia listę krawędzi na graf w postać listy sąsiedztwa. Krawędzie
# wychodzące z wierzchołka v są zapisane jako krotki (u,d,line), gdzie d to waga krawędzi, a line to typ
# lini kolejowej - odpowiednio 0 oznacza linie indyjską a 1 oznacza linie przylądkową.
# Jako że wagi krawędzi to liczby naturalne ograniczone stałą 10 to możemy skorzystać z algorytmu
# delayed_bfs(G,s,t). Jest to zmodyfikowana wersja algorytmu bfs dla grafów ważonych.
# W kolejce przechowujemy nie tylko indeks wierzchołka, ale i delay. Za każdym razem kiedy wyciągamy
# wierzchołek z kolejki zmniejszamy delay o 1 i umieszczamy ponownie w kolejce, aż do momentu kiedy delay wynosi 0.
# Wierzchołek jest odwiedzany dopiero za (delay-1)-szym wyciągnięciem go z kolejki co symuluje rozchodzenie
# się fali bfs'a w grafie ważonym.
# Każdy wierzchołek ma dwa możliwe stany:
#  0 - oznacza, że przyjechaliśmy tam linią indyjską
#  1 - ozancza, że przyjechaliśmy tam linią przylądkową
# Przez to, że w kolejce przechowujemy state, czyli typ lini którym przyjechaliśmy do wierzchołka, to
# jesteśmy w stanie obliczyć ile zajmie nam przejechanie przez stacje.
# Wynikiem algorytmu jest najkrótsza ścieżka z A do B obliczona przez delayed_bfs(G,s,t).

from egz2btesty import runtests
from math import inf
from collections import deque

# O(m) - gdzie m to liczba linii kolejowych
def tory_amos( E, A, B ):
    I = 0
    P = 1

    def edges_to_graph(E):
        n = 0
        for v,u,d,t in E:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v, u, d, t in E:
            line = I if t == 'I' else P
            G[v].append( (u,d,line) )
            G[u].append( (v,d,line) )
        return G

    def delayed_bfs(G,s,t):
        n = len(G)
        visited = [[False for _ in range(2)] for i in range(n)]
        d = [[inf for _ in range(2)] for i in range(n)]
        q = deque()

        d[A][I] = 0
        d[A][P] = 0
        q.append( (A,I,0) )
        q.append( (A,P,0) )

        while q:
            v , state , delay = q.popleft()
            if visited[v][state]:
                continue
            if delay > 0:
                q.append( (v,state,delay-1) )
                continue
            visited[v][state] = True
            for u,weight,line in G[v]:
                cost = weight

                if v == s:
                    if d[u][line] > d[v][state] + cost:
                        d[u][line] = d[v][state] + cost
                        q.append( (u,line,cost-1) )

                if state != line:
                    cost += 20
                else:
                    if state == I:
                        cost += 5
                    else:
                        cost += 10
                if d[u][line] > d[v][state] + cost:
                    d[u][line] = d[v][state] + cost
                    q.append( (u,line,cost-1) )
        return d

    G = edges_to_graph(E)
    d = delayed_bfs(G,A,B)
    return min(d[B][I],d[B][P])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )

# Liczba zaliczonych testów: 11/11
# Liczba testów z przekroczonym czasem: 0/11
# Liczba testów z błędnym wynikiem: 0/11
# Liczba testów zakończonych wyjątkiem: 0/11
# Orientacyjny łączny czas : 0.19 sek.
# Status testów: A A A A A A A A A A A