# 29 - multiplicity - mnogość
# Dana jest tablica liczb całkowitych A [a1, a2, ..., an]. Tablica B nazywana jest podciągiem A, jeśli
# można usunąć niektóre elementy z A, aby otrzymać B. Tablica [b1, b2, ..., bk] nazywana jest dobrą,
# jeśli jest niepusta i dla każdego i (1 <= i <= k) bi jest podzielne przez i. Znajdź liczbę dobrych
# podciągów w A. Dwa podciągi są uważane za różne, jeśli różnią się zestawem indeksów
# elementów wziętych z oryginalnej tablicy. To znaczy, wartości elementów nie mają znaczenia przy
# porównywaniu podciągów. W szczególności, tablica A ma dokładnie 2^n - 1 różnych podciągów
# (z wyłączeniem pustego podciągu).

# bottom up - O(n^2)
def multiplicity(A):
    n = len(A)
    F = [[0 for k in range(n)] for w in range(n)]
    # F[w][k] - liczba dobrych podciągów z przedziału <a0,ak> o długości w

    F[0][0] = 1
    F[1][0] = 1

    for k in range(n-1):
        for w in range(n):
            F[w][k+1] += F[w][k]
            if A[k+1] % (w+1) == 0:
                F[w+1][k+1] += F[w][k]

    res = 0
    for w in range(1,n):
        res += F[w][n-1]
    return res

# Przykładowy test - oczekiwana wartość: 15
A = [0,1,2,3,4]
print(multiplicity(A))
# 0 , 1 , 2 , 3 , 4
# 02 , 12 , 04 , 14 , 24 , 34
# 023 , 123
# 0234 , 1234