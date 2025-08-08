# 22 - amazon's recursive stairs - rekurencyjne schody amazona
# Dana jest tablica A z liczbami naturalnymi ≥ 1. Zaczynamy na pozycji 0, a wartość A[i] określa
# maksymalną długość skoku do następnej pozycji. Przykład: [1, 3, 2, 1, 0] - z pozycji 0 można
# skoczyć na 1, z pozycji 1 można skoczyć na 2, 3 lub 4. Oblicz na ile sposobów można przejść
# z pozycji 0 na pozycję n-1, przestrzegając zasad określonych w tablicy.
# Opis algorytmu na dole.

# bottom up - O(n^2)
def amazon(A):
    n = len(A)
    F = [0 for _ in range(n)]       # F[i] - na ile sposobów można przejść z pozycji 0 na pozycję i
    F[0] = 1
    for i in range(n):
        for j in range(1,A[i]+1):
            if i + j >= n:
                break
            F[i+j] += F[i]
    return F[n-1]

# Przykładowy test - oczekiwana wartość: 4
T = [1, 3, 2, 1, 0]
print(amazon(T))
# Przykładowy test - oczekiwana wartość: 8
T = [2, 1, 3, 2, 1, 0]
print(amazon(T))
# Przykładowy test - oczekiwana wartość: 761
T = [10, 6, 4, 4, 9, 10, 2, 3, 3, 6, 7, 7]
print(amazon(T))

# Opis algorytmu - amazon(A) - O(n^2)
# F[i] - na ile sposobów można przejść z pozycji 0 na pozycję i
# Dla każdego i-tego wywołania pętli algorytm aktualizuje wartości w tablicy F z zakresu <i+1, i+A[i]>.
