# egzamin 2021 termin 0 zadanie 1 - tanagram

from zad1testy import runtests

def tanagram(x, y, t):
    n = len(x)
    letters = {}

    for i in range(n):
        if x[i] not in letters:
            letters[x[i]] = []
        letters[x[i]].append(i)

    # wszystkie odwracane listy mają sumaryczną długość równą n - sumarycznie O(n) operacji
    for letter in letters.keys():
        letters[letter].reverse()

    for i in range(n):
        j = letters[y[i]].pop()
        if abs(i-j) > t:
            return False
    return True

runtests(tanagram)
