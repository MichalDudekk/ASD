# 58 - elevators in skyscraper - windy
# Wieżowiec ma 7 pięter i n wind, ale nie ma schodów. Każda winda ma listę pięter, na które
# jeździ, oraz prędkość w sekundach na piętro. Jesteśmy na piętrze i i chcemy dostać się
# na piętro j. Jaki jest minimalny czas w sekundach, który musimy spędzić w windach,
# aby tam dotrzeć?

from math import inf
from queue import PriorityQueue

def elevators(lifts,s,t):
    G = [[] for _ in range(7)]

    for lift in lifts:
        speed = lift[1]
        for i in range( len(lift[0]) - 1 ):
            floor1 = lift[0][i]
            floor2 = lift[0][i+1]
            G[floor1].append( (floor2 , (abs(floor2 - floor1) * speed) ) )
            G[floor2].append( (floor1 , (abs(floor2 - floor1) * speed) ) )

    def dijkstra(G,s):
        n = len(G)
        visited = [False]*n
        d = [inf]*n
        pq = PriorityQueue()

        d[s] = 0
        pq.put( (d[s],s) )

        while not pq.empty():
            _,v = pq.get()
            visited[v] = True
            for u,weight in G[v]:
                if visited[u]:
                    continue
                if d[u] > d[v] + weight:
                    d[u] = d[v] + weight
                    pq.put( (d[u],u) )
        return d

    d = dijkstra(G,s)
    return d[t]

# Przykładowy test - oczekiwana wartość: 12
lifts = [[[1, 2, 5], 3],
          [[3, 4, 5], 5],
          [[3, 6], 2],
          [[4], 3],
          [[5], 1],
          [[6], 4]]
print(elevators(lifts, 1, 5))
# Przykładowy test - oczekiwana wartość: 8
lifts = [([1, 2, 5], 1), ([0, 3, 5], 2), ([0, 3], 2), ([1, 2, 4], 3), ([3, 5], 1), ([0, 1, 2, 3, 4, 5], 5)]
print(elevators(lifts, 0, 5))
# Przykładowy test - oczekiwana wartość: 11
lifts = [([1, 2, 5], 1), ([0, 3, 5], 2), ([0, 3], 2), ([1, 2, 4], 3), ([3, 5], 1), ([0, 1, 2, 3, 4, 5], 5)]
print(elevators(lifts, 0, 4))
# Przykładowy test - oczekiwana wartość: 8
lifts = [([1, 2, 5], 1), ([0, 3, 5], 2), ([0, 3], 2), ([1, 2, 4], 3), ([3, 5], 1), ([0, 1, 2, 3, 4, 5], 5)]
print(elevators(lifts, 5, 0))