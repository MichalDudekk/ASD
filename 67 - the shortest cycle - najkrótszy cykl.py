# 67 - the shortest cycle - najkrótszy cykl
# Mamy dany ważony graf z dodatnimi wagami. Znajdź długość najkrótszego cyklu w grafie.
# Algorytm powinien zwrócić False, jeśli cykl nie istnieje.

from math import inf

# O( V*(V+E) )
def the_shortest_cycle(G):
    def dfs_find_all_cycles(G):
        n = len(G)
        visited = [False]*n
        parent = [None]*n

        cycles = []
        cycle = [None]*n
        cycle_index = -1

        def dfs_visit(v):
            visited[v] = True
            for u,w in G[v]:
                if not visited[u]:
                    parent[u] = v
                    dfs_visit(u)
                    continue
                if parent[v] == u:
                    continue

                nonlocal cycle_index
                cycles.append([])
                cycle_index += 1

                left = []
                right = []

                current = u
                while current is not None:
                    cycle[current] = cycle_index
                    current = parent[current]
                current = v
                while cycle[current] != cycle_index:
                    right.append(current)
                    current = parent[current]
                crossing_point = current

                current = u
                while current != crossing_point:
                    left.append(current)
                    current = parent[current]

                left.append(crossing_point)
                right.reverse()
                right.append(u)
                cycles[cycle_index] = left + right

        for i in range(n):
            if visited[i]:
                continue
            dfs_visit(i)
        return cycles

    cycles = dfs_find_all_cycles(G)
    res = inf

    for cycle in cycles:
        m = len(cycle)
        cycle_weight = 0
        for i in range(m-1):
            idx = cycle[i]
            for u,weight in G[idx]:
                if u == cycle[i+1]:
                    cycle_weight += weight
                    break
        res = min(res,cycle_weight)
    return res if res != inf else False

# Przykładowy test - oczekiwana wartość: 7
G = [[(1, 2), (4, 1)], [(0, 2), (3, 1), (2, 4)], [(1, 4), (3, 5)], [(1, 1), (2, 5), (4, 3)], [(0, 1), (3, 3)]]
print(the_shortest_cycle(G))
# Przykładowy test - oczekiwana wartość: False
G = [[(3, 1)], [(2, 1), (4, 3), (5, 2)], [(1, 1)], [(0, 1), (5, 2)], [(1, 3)], [(3, 2), (1, 2), (6, 3)], [(5, 3)]]
print(the_shortest_cycle(G))