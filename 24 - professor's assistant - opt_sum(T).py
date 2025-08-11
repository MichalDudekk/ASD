# 24 - professor's assistant - opt_sum(T)
# Asystent słynnego profesora otrzymał zadanie obliczenia sumy ciągu liczb (liczby mogą być dodatnie i ujemne).
# Aby zminimalizować błędy zaokrągleń, asystent postanowił wykonać dodawania w takiej kolejności,
# aby największa wartość bezwzględna wyniku pośredniego (wyniku każdej operacji dodawania; traktujemy też
# końcową sumę jako wynik pośredni) była jak najmniejsza. Aby uprościć zadanie, asystent nie zmienia
# kolejności liczb w sumie, a jedynie wybiera kolejność wykonywania operacji dodawania.
# Napisz funkcję opt_sum, która przyjmuje jako parametr tablicę liczb n1, n2, ..., nk (w kolejności,
# w jakiej występują w sumie; zakładamy, że tablica zawiera co najmniej dwie liczby) i zwraca
# największą wartość bezwzględną wyniku pośredniego przy optymalnej kolejności dodawania.
# Na przykład dla tablicy: [1, -5, 2] funkcja powinna zwrócić 3, co odpowiada dodaniu -5 i 2,
# a następnie dodaniu 1 do wyniku.
from math import inf

def opt_sum(T):
    n = len(T)
    F = [[inf for k in range(n)] for w in range(n)]
    # F[w][k] - minimalna, największa wartość bezwzględna wyniku pośredniego dodawań przedziału <w,k>

    S = [T[k] for k in range(n)]
    for k in range(1,n): S[k] += S[k-1]
    S.append(0)     # z tego wynika, że: S[-1] = 0

    def recur(w,k):
        if F[w][k] != inf:
            return F[w][k]
        if w==k:
            F[w][k] = 0
            return F[w][k]
        if k==w+1:
            F[w][k] = abs(T[w]+T[k])
            return F[w][k]
        for i in range(w+1,k+1):
            F[w][k] = min(
                F[w][k],
                max(
                    recur(w,i-1),
                    recur(i,k),
                    abs( (S[i-1] - S[w-1]) + (S[k] - S[i-1]) )
                )
            )
        return F[w][k]

    return recur(0,n-1)

# Przykładowy test - oczekiwana wartość: 3
T = [1, -5, 2]
print(opt_sum(T))
# Przykładowy test - oczekiwana wartość: 3
T = [1, -5, 8, -6, 2, 3]
print(opt_sum(T))
# Przykładowy test - oczekiwana wartość: 98
T = [1,1,-100,1,1]
print(opt_sum(T))
