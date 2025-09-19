# egzamin 2023 termin 3 zadanie 2 - uncool
# wyżej w heapie - zostanie szybciej wyciągniety    np. jeśli w heapie jest 1 i 3 to 1 jest wyżej od 3
#
# Jeśli początek i koniec mają ten sam indeks to koniec jest wyżej w heapie
#
# Jeśli dwa początki mają ten sam indeks to ten o większej długości przedziału jest wyżej w heapie
# Jeśli dwa końce mają ten sam indeks to ten o mniejszej długości przedziału jest wyżej w heapie
#
# Dwa takie same przedziały:
# Jeśli dwa początki mają ten sam indeks i mają tą samą długość przedziału to ten o mniejszym (i) jest wyżej w heapie
# Jeśli dwa końce mają ten sam indeks i mają tą samą długość przedziału to ten o większym (i) jest wyżej w heapie

from egz3btesty import runtests
from queue import PriorityQueue

# O(n*log(n))
def uncool( P ):
    n = len(P)
    pq = PriorityQueue()
    for i in range(n):
        s,t = P[i]
        l = t - s
        pq.put( (s, 1, -l, i ,i) )
        pq.put( (t, 0, l, -i ,i) )
    stack = []
    while not pq.empty():
        v , type , _ , _ , i = pq.get()
        if type == 1:
            stack.append(i)
        else:
            j = stack.pop()
            if i != j:
                return i,j

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
