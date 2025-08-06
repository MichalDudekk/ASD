# 08 - staircase problem - schody
# Dana jest odległość n. Oblicz całkowitą liczbę sposobów pokonania tej odległości
# za pomocą kroków o długości 1, 2 lub 3.
# Opis algorytmu na dole.

# bottom up - O(n)
def staircase(n):
    steps = [1,2,3]

    F = [0 for i in range(n+1)]
    # F[i] - liczba sposobów pokonania odległości i
    F[0] = 1

    for i in range(1,n+1):
        for s in steps:
            if i - s < 0:
                continue
            F[i] += F[i-s]
    return F[n]

# Przykładowy test - oczekiwana wartość: 24
n = 6
print(staircase(n))
# Przykładowy test - oczekiwana wartość: 274
n = 10
print(staircase(n))
# Przykładowy test - oczekiwana wartość: 10562230626642
n = 50
print(staircase(n))

# Opis algorytmu - staircase(n) - O(n)
# F[i] - liczba sposobów pokonania odległości i
# Dla każdej wartości i algorytm sumuje F[i-1] , F[i-2] , F[i-3]
# Wyjaśnienie: F[i-3] oznacza, że bierzemy liczbę sposobów pokonania odległości (i-3) a następnie stawiamy krok długości 3
# F[i-1] , F[i-2] - zupełnie analogicznie
