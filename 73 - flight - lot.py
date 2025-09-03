# 73 - flight - lot

from collections import deque

def flight(L,x,y,t):
    def edges_to_graph(L):
        n = 0
        for v,u,h in L:
            n = max(n,v,u)
        n += 1
        G = [[] for _ in range(n)]
        for v, u, h in L:
            G[v].append( (u,h) )
            G[u].append( (v,h) )
        return G

    def bfs_flight(G,s,y):
        n = len(G)
        visited = [{} for _ in range(n)]
        q = deque()

        for u,h in G[s]:
            q.append( (u,(h,h)) )
            visited[s][(h,h)] = True

        while q:
            v,h = q.popleft()
            mini, maxi = h
            if h in visited[v]:
                continue
            visited[v][h] = True
            for u,new_h in G[v]:
                new_mini = min(mini,new_h)
                new_maxi = max(maxi,new_h)
                size = new_maxi - new_mini
                if size > 2*t:
                    continue
                q.append( (u,(new_mini,new_maxi)) )
        print(visited)
        return visited[y]

    G = edges_to_graph(L)
    vis = bfs_flight(G,x,y)
    if len(vis) == 0:
        return False
    for mini,maxi in vis.keys():
        return (maxi+mini)//2

L = [(0,1,2000),(0,2,2100),(1,3,2050),(2,3,2300),
(2,5,2300),(3,4,2400),(3,5,1990),(4,6,2500),(5,6,2100)]
x = 0
y = 6
t = 60
print(flight(L,x,y,t))
