# 72 - meeting with the professor - spotkanie z profesorem
# Pewien znany profesor zaprosił Cię na spotkanie w Magicznym Mieście. W mieście tym niektóre
# drogi mogą być uczęszczane tylko przez ludzi poniżej 30 roku życia (w tym Ciebie), inne tylko przez
# ludzi w wieku od 30 lat (w tym profesora). Są też drogi, które mogą być uczęszczane przez
# każdego. Każda z dróg ma określoną długość, wyrażoną dodatnią liczbą naturalną, może być jedno-
# lub dwukierunkowa.
# Drogi te łączą możliwe lokalizacje spotkania. Wśród nich wyróżniamy mieszkanie Twoje i
# mieszkanie profesora.
# Profesor prosi Cię, byś wybrał takie miejsce na spotkanie, aby łączna droga, którą musicie pokonać
# Ty i profesor była jak najmniejsza. Jeżeli jest więcej niż jedno takie miejsce, podaj je wszystkie.
# Jeżeli takie miejsce nie istnieje, algorytm również powinien to stwierdzić.
# Algorytm powinien zwrócić łączną drogę i wierzchołek, w którym się spotkacie.

from math import inf
from queue import PriorityQueue

def meeting_with_the_professor(under_thirty, over_thirty, normal, student_house, professor_house):
    def create_graph():
        n = 0
        for v,u,w in under_thirty:
            n = max(n,v,u)
        for v,u,w in over_thirty:
            n = max(n,v,u)
        for v,u,w in normal:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v,u,w in under_thirty:
            G[v].append( (u,w,-30) )        # -30 znaczy że ścieżka dla osób poniżej trzydziestki
        for v, u, w in over_thirty:
            G[v].append( (u,w,30) )         # 30 znaczy że ścieżka dla osób od trzydziestki
        for v, u, w in normal:
            G[v].append( (u,w,0) )          # 0 znaczy że ścieżka dla wszystkich
        return G

    def dijkstra(G,s,age : '-30 znaczy że poniżej trzydziestki , 30 znaczy że ma przynajmniej trzydziestkę'):
        n = len(G)
        d = [inf]*n
        visited = [False]*n
        pq = PriorityQueue()

        d[s] = 0
        pq.put( (d[s],s) )

        while not pq.empty():
            _ , v = pq.get()
            if visited[v]:
                continue
            visited[v] = True
            for u,w,type in G[v]:
                if type == (age * -1):
                    continue
                if d[u] > d[v] + w:
                    d[u] = d[v] + w
                    pq.put( (d[u],u) )
        return d

    G = create_graph()
    d_under30 = dijkstra(G,student_house,-30)
    d_over30 = dijkstra(G,professor_house,30)
    res = inf
    ans = None
    for v in range(len(G)):
        if res > d_under30[v] + d_over30[v]:
            res = d_under30[v] + d_over30[v]
            ans = v
    return res, ans

# Przykładowy test - oczekiwana wartość: (42, 9)
under_thirty = [(0, 7, 12), (2, 3, 2), (3, 2, 2), (5, 15, 10), (8, 9, 12), (25, 28, 8), (28, 20, 14)]
over_thirty = [(5, 7, 21), (7, 5, 21), (9, 13, 5), (13, 9, 5), (10, 29, 2), (29, 10, 2), (13, 20, 9), (20, 13, 9), (18, 16, 1)]
normal = [(0, 1, 5), (1, 0, 5), (1, 2, 2), (2, 1, 2), (2, 4, 2), (4, 2, 2), (5, 0, 7), (6, 9, 6), (6, 5, 12), (7, 6, 6),
          (7, 8, 13), (8, 7, 13), (8, 24, 10), (11, 29, 3), (29, 11, 3), (12, 29, 2), (29, 12, 2), (13, 29, 2), (29, 13, 2),
          (14, 13, 2), (15, 13, 3), (16, 14, 4), (17, 18, 4), (18, 17, 4), (19, 28, 20), (28, 19, 20), (19, 18, 5),
          (19, 15, 16), (20, 19, 12), (20, 25, 15), (25, 20, 15), (21, 22, 3), (22, 21, 3), (22, 23, 2), (23, 22, 2),
          (22, 24, 4), (24, 22, 4), (24, 20, 4), (25, 8, 21), (26, 27, 5), (27, 26, 5), (26, 28, 5), (28, 26, 5)]
student_house = 3
professor_house = 10
print(meeting_with_the_professor(under_thirty, over_thirty, normal, student_house, professor_house))