# 03 - matrix-chain_multiplication - optymalne mnożenie macierzy
# Mamy ciąg (łańcuch) macierzy [A1, A2, ..., An], gdzie dla każdego
# i = (1, 2, ..., n), macierz Ai ma wymiary p[i-1] x p[i]. Należy w pełni
# nawiasować iloczyn A1*A2*...*An w taki sposób, aby zminimalizować liczbę
# mnożeń skalarnych.
# Opis algorytmu na dole.
from math import inf

# top down
def matrix_order(p):
    n = len(p)

    F = [[inf for k in range(n)] for w in range(n)]
    # F[w][k] - optymalne nawiasowanie przedziału <w,k>

    def recur(w,k):
        if F[w][k] != inf:
            return F[w][k]
        if k == w+1:
            F[w][k] = 0
            return F[w][k]
        for i in range(w+1,k):
            F[w][k] = min( F[w][k] , recur(w,i) + recur(i,k) + (p[w] * p[i] * p[k]) )
        return F[w][k]

    return recur(0,n-1)

# bottom up
def matrix_order_bottom_up(p):
    n = len(p)

    F = [[inf for k in range(n)] for w in range(n)]
    # F[w][k] - optymalne nawiasowanie przedziału <w,k>

    for i in range(n-1):
        F[i][i+1] = 0

    for r in range(3,n+1):
        for w in range(0,n-r+1):
            k = w + r - 1
            for i in range(w+1,k):
                F[w][k] = min( F[w][k] , F[w][i] + F[i][k] + (p[w] * p[i] * p[k]) )

    return F[0][n-1]

p = [30, 35, 15, 5, 10, 20, 25] # 15125
print(matrix_order(p))
print(matrix_order_bottom_up(p))

# Opis algorytmu - matrix_order(p) - O(n^3)
# recur(w,k) - optymalne nawiasowanie przedziału <w,k>
# Z powodu tego że macierze mają dwa wymiary p[i-1] × p[i], to podczas mnożenia oba przedziały będą zamknięte.
# Z danego przedziału <w,k> wybieramy punkt i z przedziału <w+1,k-1>, który dzieli <w,k> na dwa przedziały
# <w,i>, <i,k>. Wynikiem takiego nawiasowania jest: recur(w,i) + recur(i,k) + ( p[w] * p[i] * p[k] )
# Dla każdego przedziału <w,k> wybieramy takie i, które zapewnia najmniejszą ilość mnożeń.
# Liczba unikalnych podproblemów recur(w,k) wynosi O(n^2)
# Rozwiązanie każdego z nich wymaga sprawdzenia wszystkich możliwych punktów podziału i między w a k, co daje O(n) operacji
# Z tego wynika, że złożoność to O(n^3)