# 20 - knapsack problem number of possibilities - problem plecakowy ilość możliwości
# Złodziej włamuje się do sklepu z przedmiotami o danych wagach (tablica W)
# i cenach (tablica V). Obie tablice zawierają jedynie liczby naturalne.
# Przedmioty pakuje do plecaka o maksymalnej nośności max_weight. Tym razem nie chce ukraść przedmiotów
# o najwyższej możliwej wartości, lecz interesuje go na ile sposobów może wybrać przedmioty,
# aby ich łączna cena była nie mniejsza niż C, a łączna waga nie przekroczyła max_weight.
# Opis algorytmu na dole.

# bottom up - O( n^2 * ( sum(V) ) )
def another_knapsack(V,W,max_weight,C):
    n = len(V)
    sum_V = sum(V)

    F = [[[0 for h in range(sum_V + 1)] for k in range(n)] for w in range(max_weight+1)]
    # F[w][k][h] - na ile sposobów można wybrać przedmioty z przedziału <0,k> o łącznej wadze w i łącznej wartości h
    F[0][0][0] = 1
    if W[0] <= max_weight:
        F[ W[0] ][0][ V[0] ] = 1

    for k in range(n-1):
        for w in range(max_weight+1):
            for h in range(sum_V + 1):
                if F[w][k][h] == 0:
                    continue
                F[w][k+1][h] += F[w][k][h]      # nie bierzemy k+1-szego przedmiotu
                if W[k+1] + w > max_weight:
                    continue
                F[ W[k+1] + w ][ k+1 ][ h + V[k+1] ] += F[w][k][h]
                # bierzemy k+1-szy przedmiot

    res = 0
    for w in range(max_weight+1):
        for h in range(C,sum_V + 1):
            res += F[w][n-1][h]
    return res


# brute force O(2^n)
def another_knapsack_brute(V,W,max_weight,C):
    n = len(V)
    res = 0
    def recur(i,weight,profit):
        if i == n:
            if weight <= max_weight and profit >= C:
                nonlocal res
                res += 1
            return
        if weight > max_weight: return
        recur(i+1,weight+W[i],profit+V[i])
        recur(i+1,weight,profit)
    recur(0,0,0)
    return res

# Przykładowy test - oczekiwana wartość: 56
V = [4,3,1,2,4,2,2]
W = [2,1,2,2,4,1,3]
max_weight = 8
C = 6
print(another_knapsack(V,W,max_weight, C))
print(another_knapsack_brute(V,W,max_weight, C))
# Przykładowy test - oczekiwana wartość: 1
V = [4,3,1,2,4,2,2]
W = [2,1,2,2,4,1,3]
max_weight = 8
C = 13
print(another_knapsack(V,W,max_weight, C))
print(another_knapsack_brute(V,W,max_weight, C))

# Opis algorytmu - another_knapsack(V,W,max_weight,C) - O( n^2 * ( sum(V) ) )
# F[w][k][h] - na ile sposobów można wybrać przedmioty z przedziału <0,k> o łącznej wadze w i łącznej wartości h
# Dla każdego k-tego wywołania pętli, dla każdej komórki w tablicy F algorytm rozważa dwa przypadki:
# 1) nie bierze k+1-szego przedmiotu: F[w][k+1][h] += F[w][k][h]
# 2) bierze k+1-szy przedmiot (o ile to możliwe): F[ W[k+1] + w ][ k+1 ][ h + V[k+1] ] += F[w][k][h]
# W ten sposób algorytm oblicza wszystkie możliwości wyboru przedmiotów tak aby łączna waga wynosiła w
# a łączna wartość wynosiła h. Następnie wystarczy odczytać rozwiązanie sumując wartości z ostatniej kolumny (k == n-1),
# których sumaryczna wartość wynosi przynajmniej C.