# 54 - check and bishop - szach i goniec
# Algocja położona jest na wielkiej pustyni i składa się z miast i oaz połączonych drogami.
# Każde miasto otoczone jest murem i ma tylko dwie bramy.
# Z każdej bramy prowadzi dokładnie jedna droga do jednej oazy (ale dana oaza może mieć
# dowolną liczbę dróg do niej prowadzących, oazy mogą być również połączone ze sobą drogami).
# Prawo Algocji wymaga, aby jeśli ktoś wjeżdża do miasta jedną bramą, musiał opuścić je
# drugą. Szach Algocji postanowił wysłać gońca, który będzie czytał zakaz
# formułowania zadań "o szachownicy" (obraza majestatu) w każdym mieście. Szach chce,
# aby goniec odwiedził każde miasto dokładnie raz (ale nie ma limitu, ile razy goniec
# odwiedzi każdą oazę). Goniec wyrusza ze stolicy Algocji, miasta x, i po odwiedzeniu
# wszystkich miast ma wrócić do miasta x. Znajdź algorytm, który określi, czy istnieje
# odpowiednia trasa dla gońca.

def check_and_bishop(G,oasis):
    n = len(G)

    is_oasis = [False for _ in range(n)]
    for v in oasis:
        is_oasis[v] = True

    connected_oasis = []
    current = -1
    visited = [False]*n

    def dfs_visit(v):
        nonlocal current
        connected_oasis[current].append(v)
        visited[v] = True
        for u in G[v]:
            if visited[u]:
                continue
            if is_oasis[u]:
                dfs_visit(u)

    for v in oasis:
        if visited[v]:
            continue
        current += 1
        connected_oasis.append([])
        dfs_visit(v)

    m = len(connected_oasis)
    how_many_edges_to_cities = [0 for _ in range(m)]

    for i in range(m):
        for v in connected_oasis[i]:
            for u in G[v]:
                if is_oasis[u]:
                    continue
                how_many_edges_to_cities[i] += 1

    for i in range(m):
        if how_many_edges_to_cities[i] %2 != 0:
            return False
    return True

# Przykładowy test - oczekiwana wartość: False
G = [[2, 4], [2, 9], [0, 4, 3], [2, 5], [0, 2, 6], [3, 7, 8], [4, 7], [5, 6, 8], [5, 7], [1]]
oasis = [2, 4, 5, 7, 9]
print(check_and_bishop(G,oasis))
# Przykładowy test - oczekiwana wartość: True
G = [[1, 10], [0, 2], [1, 9, 14, 3], [2, 8, 4], [3, 7, 5], [4, 6], [7, 5, 14, 15], [8, 4, 14, 6], [3, 14, 7], [2, 14, 10, 12], [0, 9, 11], [10, 13], [9, 14], [11, 15], [2, 8, 9, 7, 6, 12], [13, 6]]
oasis = [0, 2, 3, 4, 6, 7, 8, 9, 10, 13, 14]
print(check_and_bishop(G,oasis))