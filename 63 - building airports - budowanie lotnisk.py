# 63 - building airports - budowanie lotnisk
# Mamy daną listę trójek (miasto_A, miasto_B, koszt). Każda z nich oznacza, że możemy zbudować
# drogę między miastem_A i miastem_B za podany koszt. Co więcej, w każdym mieście możemy
# zbudować lotnisko za koszt K, niezależnie od miasta. Na początku nie ma lotniska w żadnym
# mieście, ani nie ma zbudowanej drogi między żadnymi dwoma miastami. Naszym celem jest
# zbudowanie lotnisk i dróg za minimalny całkowity koszt tak, aby każde miasto miało dostęp
# do lotniska. Miasto ma dostęp do lotniska, jeśli:
#    1) ma lotnisko
#    2) możliwe jest podróżowanie do innego miasta, które ma lotnisko
# Jeśli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, wybierz to z największą
# liczbą lotnisk. Zwróć minimalny całkowity koszt oraz liczbę postawionych lotnisk.

class Node:
    def __init__(self,id):
        self.vertex = id
        self.parent = self
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
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

def build_airports(E,K):
    n = 0
    for v,u,weight in E: n = max(n,v,u)
    n += 1

    Nodes = []
    for i in range(n):
        Nodes.append(Node(i))

    E.sort(key = lambda x: x[2])

    how_many_airports = n
    res = how_many_airports * K

    for v,u,weight in E:
        if find(Nodes[v]) == find(Nodes[u]):
            continue
        if weight >= K:
            break
        union(Nodes[v],Nodes[u])
        how_many_airports -= 1
        res = res - K + weight

    return res, how_many_airports

# Przykładowy test - oczekiwane wartości: (27, 4)
E = [(0, 1, 2), (0, 2, 3), (0, 6, 4), (0, 7, 7), (2, 3, 1), (2, 5, 5), (3, 4, 3),
         (6, 7, 4), (6, 8, 6), (7, 8, 2)]
K = 4
print(build_airports(E, K))







