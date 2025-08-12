# 43 - detect cycle - wykrywanie cyklu
# Sprawdź czy w grafie nieskierowanym istnieje cykl.

def detect_cycle(G):
    n = len(G)
    visited = [False]*n

    ans = False

    def dfs_visit(v,parent):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                dfs_visit(u,v)
            elif u != parent:
                nonlocal ans
                ans = True

    for v in range(n):
        if not visited[v]:
            dfs_visit(v,None)

    return ans

# graf ma cykl
G = [[1, 2, 3], [0, 7], [0, 5], [0, 5], [0, 6, 7], [2, 3, 6], [4, 5], [1, 4]]
print(detect_cycle(G))

# graf nie ma cyklu
G = [[1, 2, 5], [0, 3], [0, 4, 7, 8], [1], [2, 6], [0], [4], [2], [2]]
print(detect_cycle(G))