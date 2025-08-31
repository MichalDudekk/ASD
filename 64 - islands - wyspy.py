# 64 - islands - wyspy
# Pewna kraina składa się z wysp, między którymi istnieją połączenia lotnicze, promowe i mostowe.
# Między dwiema wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
# na wyspę kosztuje 8, przeprawa promowa kosztuje 5, a za przejazd mostem trzeba zapłacić 1.
# Znajdź trasę z wyspy s do wyspy t, która na każdej kolejnej wyspie zmienia środek transportu
# na inny i minimalizuje koszt podróży. Dana jest tablica G, która określa koszt połączeń
# między wyspami. Wartość 0 oznacza, że nie ma bezpośredniego połączenia. Zaimplementuj funkcję
# islands(G, A, B), która zwraca minimalny koszt podróży z wyspy A do wyspy B. Jeśli taka
# trasa nie istnieje, funkcja powinna zwrócić None.

from math import inf
from queue import PriorityQueue
from collections import deque

# rozwiązanie z użyciem algorytmu dijkstry - O(E*log(V))
def islands_dijkstra(G,s,t):
    n = len(G)
    d = [[inf for _ in range(3)] for i in range(n)]
    visited = [[False for _ in range(3)] for i in range(n)]
    # 0 - przybyl samolotem ; 1 - przybyl promem ; 2 - przybyl mostem
    pq = PriorityQueue()

    for i in range(3):
        d[s][i] = 0
        pq.put( (d[s][i],s,i) )

    while not pq.empty():
        _ , v , state = pq.get()
        if visited[v][state]:
            continue
        visited[v][state] = True
        for u in range(n):
            if G[v][u] == 0:
                continue
            if G[v][u] == 8:
                new_state = 0
            elif G[v][u] == 5:
                new_state = 1
            else:
                new_state = 2

            if state == new_state:
                continue
            if d[u][new_state] > d[v][state] + G[v][u]:
                d[u][new_state] = d[v][state] + G[v][u]
                pq.put( (d[u][new_state],u,new_state) )

    res = min(d[t][0],d[t][1],d[t][2])
    return res if res != inf else None

# rozwiązanie z użyciem algorytmu delayed bfs - O(V + E)
def islands_delayed_bfs(G,s,t):
    n = len(G)
    d = [[inf for _ in range(3)] for i in range(n)]
    visited = [[False for _ in range(3)] for i in range(n)]
    # 0 - przybyl samolotem ; 1 - przybyl promem ; 2 - przybyl mostem
    q = deque()

    for i in range(3):
        d[s][i] = 0
        q.append( (s,i,0) )

    while q:
        v , state , delay = q.popleft()
        if visited[v][state]:
            continue
        if delay > 0:
            q.append( (v,state,delay-1) )
        visited[v][state] = True
        for u in range(n):
            if G[v][u] == 0:
                continue
            if G[v][u] == 8:
                new_state = 0
            elif G[v][u] == 5:
                new_state = 1
            else:
                new_state = 2

            if state == new_state:
                continue
            if d[u][new_state] > d[v][state] + G[v][u]:
                d[u][new_state] = d[v][state] + G[v][u]
                q.append( (u,new_state,G[v][u] - 1) )

    res = min(d[t][0],d[t][1],d[t][2])
    return res if res != inf else None

G = [[0,5,1,8,0,0,0],
     [5,0,0,1,0,8,0],
     [1,0,0,8,0,0,8],
     [8,1,8,0,5,0,1],
     [0,0,0,5,0,1,0],
     [0,8,0,0,1,0,5],
     [0,0,8,1,0,5,0]]
# Przykładowy test - oczekiwana wartość: 13
s = 5
t = 2
print(islands_dijkstra(G, s, t))
print(islands_delayed_bfs(G,s,t))
# Przykładowy test - oczekiwana wartość: 12
s = 5
t = 0
print(islands_dijkstra(G, s, t))
print(islands_delayed_bfs(G,s,t))