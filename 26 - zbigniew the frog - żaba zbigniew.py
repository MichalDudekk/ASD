# 26 - zbigniew the frog - żaba zbigniew
# Żaba Zbigniew skacze po osi liczbowej. Musi przejść od 0 do n-1, skacząc tylko w kierunku większych liczb.
# Skok z i do j (j > i) kosztuje Zbigniewa (j-i) jednostek energii, a jego energia nie może spaść poniżej 0.
# Na początku Zbigniew ma 0 jednostek energii, ale na niektórych liczbach (w tym na 0) znajdują się przekąski
# o określonej wartości energetycznej (wartość przekąski dodaje się do aktualnej energii Zbigniewa).
# Zaimplementuj funkcję zbigniew(A), która otrzymuje na wejściu tablicę A o długości len(A) = n, gdzie
# każde pole zawiera wartość energetyczną przekąski leżącej na odpowiadającej liczbie. Funkcja powinna
# zwrócić minimalną liczbę skoków potrzebnych Zbigniewowi do przejścia od 0 do n-1 lub zwrócić -1, jeśli to niemożliwe.
# Opis algorytmu na dole
from math import inf

def zbigniew(A):
    n = len(A)
    sum_A = sum(A)

    F = [[inf for k in range(n)] for w in range(sum_A+1)]
    # F[w][k] - minimalna ilość skoków, aby znaleźć się na k-tym polu mając dokładnie w energii.
    F[ A[0] ][0] = 0

    for k in range(n-1):
        for w in range(sum_A+1):
            if F[w][k] == inf:
                continue
            for i in range(1,w+1):
                new_k = k + i
                if new_k >= n:
                    break
                new_w = w - i + A[new_k]
                F[new_w][new_k] = min( F[new_w][new_k] , F[w][k] + 1 )
    res = inf
    for w in range(sum_A+1):
        res = min(res,F[w][n-1])
    return -1 if res==inf else res

# Przykładowy test - oczekiwana wartość: 3
A = [2,2,1,0,0,0]
print(zbigniew(A))
# Przykładowy test - oczekiwana wartość: 2
A = [4,5,2,4,1,2,1,0]
print(zbigniew(A))
# Przykładowy test - oczekiwana wartość: 2
A = [2, 3, 1, 1, 2, 0]
print(zbigniew(A))
# Przykładowy test - oczekiwana wartość: -1
A = [4,0,0,0,0,0]
print(zbigniew(A))

# Opis algorytmu - zbigniew(A) - O(n^2 * sum(A))
# F[w][k] - minimalna ilość skoków, aby znaleźć się na k-tym polu mając dokładnie w energii.
# Przechodzimy po każdym wierszu w w każdej kolumnie k. Jeśli F[w][k] == inf to nie da się
# dotrzeć na k-te pole mając dokładnie w energii, więc nie ma sensu rozważać potencjalnych
# skoków z tego miejsca.
# Jeśli F[w][k] != inf to rozważamy wszystkie możliwe skoki z pola k. Będzie to w możliwość
# o ile k+w < n inaczej mamy nawet więcej energii niż jest potrzebne aby dotrzeć na ostatnie pole.
# Rozwiązanie odczytujemy biorąc najniższą wartość z ostatniej kolumny tablicy F.
