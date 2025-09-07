# 89 - orders - zamówienia
# Dana jest lista zamówień. Każde zamówienie wymaga pewnego kapitału początkowego C[i],
# który będzie nam potrzebny do rozpoczęcia zamówienia, oraz zysku P[i], który zostanie
# dodany do naszego całkowitego kapitału po wykonaniu zamówienia.
# Otrzymujemy kapitał początkowy W i liczbę k. Wybierz co najwyżej k zamówień tak,
# aby zakończyć z maksymalnym możliwym kapitałem.
# Przykład: k = 2, P = [1, 2, 3], C = [0, 1, 1]. Rozwiązanie: na początku mamy kapitał 0,
# więc możemy wybrać tylko pierwsze zamówienie. Po jego ukończeniu mamy kapitał równy 1,
# więc możemy wybrać zamówienie 2 lub 3. Zamówienie 3 ma większy zysk, więc wybieramy
# zamówienie 3, ponieważ możemy wybrać tylko jedno zamówienie (k = 2). Kończymy z kapitałem 4.

from math import inf

def orders(P, C, k):
    n = len(P)
    all = []

    for i in range(n):
        all.append( (C[i],P[i]) )

    all.sort(reverse=True,key=lambda x:(x[0],-1*x[1]))

    capital = 0
    for i in range(k):
        for j in range(n):
            if all[j][1] <= capital:
                all[j] = (all[j][0],inf)
                capital += all[j][0]
                break
    return capital

# Przykładowy test - oczekiwana wartość: 20
k = 3
P = [2, 1, 3, 0, 1, 0, 4, 3, 1]
C = [7, 4, 0, 5, 8, 3, 2, 1, 3]
print(orders(P, C, k))