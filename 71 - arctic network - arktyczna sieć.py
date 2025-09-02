# 71 - arctic network - arktyczna sieć
# W Arktyce osady są oddalone od siebie na ogromne odległości. Otrzymujemy je jako pary współrzędnych (x, y).
# Niektóre z nich posiadają odbiorniki satelitarne - z takiej osady można bezpośrednio komunikować
# się z każdą inną osadą, która ma odbiornik satelitarny.
# Chcemy teraz w każdej osadzie umieścić radioodbiorniki o tym samym ograniczonym zasięgu D
# (liczba całkowita), aby można było się komunikować (pośrednio lub bezpośrednio) między każdą
# parą osad. Jakie jest minimalne D, które pozwoli osiągnąć ten cel?
# Uzasadnij poprawność rozwiązania.

from math import sqrt,ceil

def min_coverage_range(P, S):
    class Node:
        def __init__(self, value):
            self.val = value
            self.parent = self
            self.rank = 0
    def find(x):
        if x.parent != x:
            x.parent = find(x.parent)
        return x.parent
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1

    def create_graph(P):
        n = len(P)
        E = []
        for v in range(n):
            for u in range(v+1,n):
                x1,y1 = P[v]
                x2,y2 = P[u]
                dist = sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
                E.append( (v,u,dist) )
        return E

    def kruskal(E,S,P):
        n = len(P)
        nodes = [Node(i) for i in range(n)]

        for i in range(len(S)-1):
            union(nodes[S[i]],nodes[S[i+1]])

        E.sort(key = lambda x:x[2])
        result = 0

        for v,u,dist in E:
            if find(nodes[v]) == find(nodes[u]):
                continue
            result = dist
            union(nodes[v],nodes[u])

        return ceil(result)

    E = create_graph(P)
    return kruskal(E,S,P)


# Przykładowy test - oczekiwana wartość: 7
P = [(-10, 8), (-9, 3.5), (-11, -8), (-7, -7), (-5, -5), (-2, 1), (-4, 3.5), (-2, 8.3), (2.5, 7.5),
     (0, 0), (2, -4), (3, 3.5), (8, 7), (8, 3), (11, 2), (11, -8)]
S = [0, 6, 8, 9, 13, 15]
print(min_coverage_range(P, S))