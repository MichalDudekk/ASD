# 84 - coverage by unit intervals - pokrycie przedziałami jednostokowymi
# Dany jest zbiór X punktów na prostej. Znajdź minimalną liczbę domkniętych przedziałów
# jednostkowych (długości 1), które są potrzebne do pokrycia wszystkich punktów ze zbioru X.

from math import ceil

def cover_points(X):
    res = 1
    X.sort()
    current = X[0] + 1
    for point in X:
        if point <= current:
            continue
        current = point + 1
        res += 1
    return res

# Przykładowy test - oczekiwana wartość: 4
X = [0.25, 0.5, 1.6, 1, 5, 2.3, 3.1, 4.5]
print(cover_points(X))
# Przykładowy test - oczekiwana wartość: 2
X = [0.1, 0.9, 5, 6]
print(cover_points(X))