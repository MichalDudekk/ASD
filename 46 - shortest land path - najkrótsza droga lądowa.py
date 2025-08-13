# 46 - shortest land path - najkrótsza droga lądowa
# Dana jest tablica 2D [N][N], w której każda komórka ma wartość "W" oznaczającą wodę
# lub "L" oznaczającą ląd. Jezioro to grupa komórek wodnych połączonych ze sobą brzegami.
# Zakładając, że tablica[0][0] i tablica[n-1][n-1] to ląd. Sprawdź, czy można przejść
# z [0][0] do [n-1][n-1] drogą lądową. Można poruszać się tylko w bok, nie po przekątnej.
# Znajdź również długość najkrótszej ścieżki między tymi komórkami.

from math import inf
from collections import deque

def land_path(G):
    n = len(G)
    d = [[inf for k in range(n)] for w in range(n)]
    visited = [[ (False if G[w][k] == "L" else True) for k in range(n)] for w in range(n)]
    q = deque()

    d[0][0] = 0
    visited[0][0] = True
    q.append( (0,0) )

    while q:
        w,k = q.popleft()

        if w+1 < n and not visited[w+1][k]:
            d[w+1][k] = d[w][k] + 1
            visited[w+1][k] = True
            q.append( (w+1,k) )
        if w-1 >= 0 and not visited[w-1][k]:
            d[w-1][k] = d[w][k] + 1
            visited[w-1][k] = True
            q.append( (w-1,k) )
        if k+1 < n and not visited[w][k+1]:
            d[w][k+1] = d[w][k] + 1
            visited[w][k+1] = True
            q.append( (w,k+1) )
        if k-1 >= 0 and not visited[w][k-1]:
            d[w][k-1] = d[w][k] + 1
            visited[w][k-1] = True
            q.append( (w,k-1) )

    return d[n-1][n-1]

# Przykładowy test - oczekiwana wartość: 20
G = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "W", "W", "W"],
     ["W", "W", "L", "W", "L", "L", "W", "L"],
     ["L", "L", "L", "L", "L", "L", "L", "L"]]
print(land_path(G))
