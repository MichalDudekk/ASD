# 21 - knapsack 2D - problem plecakowy 2D
# Dana jest tablica P zawierająca przedmioty, gdzie każdy przedmiot P[i] ma trzy wartości:
# 1) P[i][0] - wartość przedmiotu
# 2) P[i][1] - waga przedmiotu
# 3) P[i][2] - wysokość przedmiotu
# Zaimplementuj algorytm, który zwraca maksymalną sumaryczną wartość przedmiotów,
# które razem nie przekraczają maksymalnej sumarycznej wagi plecaka (max_weight),
# ani nie przekraczają maksymalnej sumarycznej wysokości (max_height) - (Powiedzmy że przedmioty są ustawiane jednen na drugim).
# Opis algorytmu na dole.

# bottom up - O(n*max_weight*max_height)
def knapsack_2D(P,max_weight,max_height):
    n = len(P)
    F = [[[-1 for h in range(max_height+1)] for k in range(n)] for w in range(max_weight+1) ]
    # F[w][k][h] - maksywalna wartość przedmiotów z przedziału od 0 do k, wykorzystując dokłanie w wagi i h wysokości
    F[0][0][0] = 0      # przypisanie wartości początkowych
    if P[0][1] <= max_weight and P[0][2] <= max_height:     # edge case gdzyby nie dało się wziąć pierwszego przedmiotu
        F[ P[0][1] ][0][ P[0][2] ] = P[0][0]

    for k in range(n-1):
        for w in range(max_weight+1):
            for h in range(max_height+1):
                if F[w][k][h] == -1:
                    continue
                F[w][k+1][h] = max( F[w][k+1][h] , F[w][k][h] )     # nie bierzemy k+1-szego przedmiotu
                new_w = w + P[k+1][1]
                new_h = h + P[k+1][2]
                if new_w <= max_weight and new_h <= max_height:
                    F[new_w][k+1][new_h] = max( F[new_w][k+1][new_h] , F[w][k][h] + P[k+1][0] )
                    # bierzemy k+1-szy przedmiot
    res = 0
    for w in range(max_weight + 1):
        for h in range(max_height + 1):
            res = max(res,F[w][n-1][h])
    return res


# Przykładowy test - oczekiwana wartość: 25
P = [(10, 4, 2), (8, 5, 3), (4, 12, 1), (5, 9, 7), (3, 1, 4), (7, 13, 4)]
# (value, weight, height)
W = 24
H = 9
print(knapsack_2D(P, W, H))

# Opis algorytmu - knapsack_2D(P,max_weight,max_height) - O(n*max_weight*max_height)
# Problem zupełnie analogiczny do zwykłego problemu plecakowego, tym razem tablica F ma jeden dodatkowy wymiar na wysokość.
# F[w][k][h] - maksywalna wartość przedmiotów z przedziału od 0 do k, wykorzystując dokłanie w wagi i h wysokości.


